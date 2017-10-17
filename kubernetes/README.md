# Kubernetes
Check [wiki](https://github.com/OpsMx/scripts/wiki/Kubernetes) for info 

### Latest PODs finder from `cluster name` or `application name` (kube-pod-finder.py)

```
veeru@ultron:~/$ python kube-pod-finder.py -h
usage: kube-pod-finder.py [-h] [-c CLUSTER_NAME] [-a APP_NAME]

Latest pods finder in K8s cluster. NOTE: Please specify 'K8s_IP' in script

optional arguments:
  -h, --help       show this help message and exit
  -c CLUSTER_NAME  Cluster name
  -a APP_NAME      Application name
```
  * ##### Get PODs from `cluster name`
  ```
  python kube-pod-finder.py -c datadogtest1-sg1
  datadogtest1-sg1-v011-zkcrg - 2017-10-17 06:18:06  <==== Later POD
  datadogtest1-sg1-v010-hqp3s - 2017-10-16 19:58:13
  datadogtest1-sg1-v009-996s5 - 2017-10-16 19:02:44
  ```
  * ##### Get PODs from `application name`
  ```
  python kube-pod-finder.py -a datadogtest1
  datadogtest1-sg1-v011-zkcrg - 2017-10-17 06:18:06  <==== Later POD
  datadogtest1-sg1-v010-hqp3s - 2017-10-16 19:58:13
  datadogtest1-sg1-v009-996s5 - 2017-10-16 19:02:44
  ```
  * Please specify `K8s_IP` in the script. If needed specify `NAMESPACE` also.
  * Get the script ---> `wget -qO kube-pod-finder.py https://goo.gl/62Gu11`
