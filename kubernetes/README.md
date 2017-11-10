# Kubernetes
Check [wiki](https://github.com/OpsMx/scripts/wiki/Kubernetes) for more info 

* Automated K8s installer script - `wget -qO kube-install.sh https://goo.gl/j6LAzU && sh kube-install.sh`

### Latest PODs finder from `cluster name` or `cluster name with version` (kube-pod-finder.py)
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
  python kube-pod-finder.py -c datadogtest1-sg1-v010
[{"applicationName": "datadogtest1", "creationTimestamp": "2017-10-16 19:58:13", "sgName": "datadogtest1-sg1-v010", "podName": "datadogtest1-sg1-v010-hqp3s"}]
  ```
  * ##### Get latest/current PODs in the `cluster`
  ```
 python kube-pod-finder.py -c datadogtest1-sg1-current
[{"applicationName": "datadogtest1", "creationTimestamp": "2017-10-17 09:13:44", "sgName": "datadogtest1-sg1-v012", "podName": "datadogtest1-sg1-v012-bpsm2"}]
  ```
  * Please specify `K8s_IP` in the script. If needed specify `NAMESPACE` also.
  * Get the script ---> `wget -qO kube-pod-finder.py https://goo.gl/62Gu11`

### Retrives PODs in the `cluster` (pods-finder.py)
* ##### Dowload -> `wget -qO pods-finder.py https://goo.gl/jqs2GV`
* ##### Help
```
root@ultron:/home/veeru/Desktop# python kube.py -h
usage: kube.py [-h] [-c CLS_NAME] [-C CURRENT_CLS_NAME]

Latest pods finder in K8s cluster. NOTE: Please specify 'K8s_IP' in script

optional arguments:
  -h, --help           show this help message and exit
  -c CLS_NAME          Gets the pods in this cluster
  -C CURRENT_CLS_NAME  Gets the pods in 'current' cluster
```
* ##### Gets all pods in `current deployed` cluster
```
root@ultron:/# python2 pods-finder.py -C radium-prod-current
[
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T10:10:53Z",
      "sgName":"radium-prod-v003",
      "podName":"radium-prod-v003-779wx"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T10:10:53Z",
      "sgName":"radium-prod-v003",
      "podName":"radium-prod-v003-b46lr"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T10:10:53Z",
      "sgName":"radium-prod-v003",
      "podName":"radium-prod-v003-dd88f"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T10:10:53Z",
      "sgName":"radium-prod-v003",
      "podName":"radium-prod-v003-h5cxt"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T10:10:53Z",
      "sgName":"radium-prod-v003",
      "podName":"radium-prod-v003-kw4wc"
   }
]
```
* ##### Gets all pods in `specified` cluster
```
root@ultron:/# python2 pods-finder.py -c radium-prod-v001
[
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T08:13:59Z",
      "sgName":"radium-prod-v001",
      "podName":"radium-prod-v001-bpfqt"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T08:13:59Z",
      "sgName":"radium-prod-v001",
      "podName":"radium-prod-v001-dz8d6"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T08:13:59Z",
      "sgName":"radium-prod-v001",
      "podName":"radium-prod-v001-fcpf2"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T08:13:59Z",
      "sgName":"radium-prod-v001",
      "podName":"radium-prod-v001-fgt4r"
   },
   {
      "applicationName":"radium",
      "creationTimestamp":"2017-11-10T08:13:59Z",
      "sgName":"radium-prod-v001",
      "podName":"radium-prod-v001-mhl9f"
   }
]
```
