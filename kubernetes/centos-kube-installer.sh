#/bin/bash

FIND_IP=http://checkip.amazonaws.com/
sudo yum update -y
#sudo yum remove docker docker-common docker-selinux docker-engine -y
echo "Installing Docker"
sudo yum -y install ftp://fr2.rpmfind.net/linux/centos/7.3.1611/extras/x86_64/Packages/container-selinux-2.9-4.el7.noarch.rpm
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum makecache fast
sudo yum install -y docker-ce
sudo systemctl enable docker.service
sudo systemctl start docker.service
echo "Docker Installation Successfull!"
echo ""
echo "Setup will start Kubernetes installation in 3 seconds.(Press Ctrl+c to exit!)"
sleep 3
sudo tee /etc/yum.repos.d/kubernetes.repo > /dev/null <<EOF
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

sudo tee /etc/docker/daemon.json > /dev/null <<EOF
{
   "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF
sudo systemctl restart docker
sudo setenforce 0
sudo yum install -y kubelet kubeadm
sudo systemctl enable kubelet && sudo systemctl start kubelet
PUBLIC_IP=`curl -s "$FIND_IP"`
if [[ -n "$PUBLIC_IP" ]]; then
  echo "Your Public IP: $PUBLIC_IP"
  sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=$PUBLIC_IP --skip-preflight-checks
else:
  echo "Not able to find your public IP"
  sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --skip-preflight-checks
fi
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
sudo kubectl taint nodes --all node-role.kubernetes.io/master-
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
sudo kubectl create -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel-rbac.yml
sudo kubectl create -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl create clusterrolebinding anonymous-cluster-admin-binding --clusterrole=cluster-admin --user=system:anonymous
kubectl get pods --all-namespaces
echo ""
kubectl cluster-info
