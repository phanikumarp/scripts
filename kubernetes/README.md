# Kubernetes
Check [wiki](https://github.com/OpsMx/scripts/wiki/Kubernetes) for info 

### Latest PODs finder from `cluster name` or `application name` (kube-pod-finder.py)
  * ##### Help
  ```
  python kube-pod-finder.py -h
  usage: kube-pod-finder.py [-h] [-c CLUSTER_NAME]

  Latest pods finder in K8s cluster. NOTE: Please specify 'K8s_IP' in script

  optional arguments:
    -h, --help       show this help message and exit
    -c CLUSTER_NAME  cluster name or cluster name with version
  ```

  * ##### Get PODs from `cluster name with VERSION`
  ```
  python kube-pod-finder.py -c datadogtest1-sg1-v012
  [{"applicationName": "datadogtest1", "creationTimestamp": "2017-10-17 09:13:44", "podName": "datadogtest1-sg1-v012-bpsm2"}]
  ```
  * ##### Get latest/current PODs in the `cluster`
  ```
  python kube-pod-finder.py -c datadogtest1-sg1-current
  [{"applicationName": "datadogtest1", "creationTimestamp": "2017-10-17 09:13:44", "podName": "datadogtest1-sg1-v012-bpsm2"}]
  ```
  * Please specify `K8s_IP` in the script. If needed specify `NAMESPACE` also.
  * Get the script ---> `wget -qO kube-pod-finder.py https://goo.gl/62Gu11`
