'''
Author : OpsMx
Description :  Latest pods finder in K8s cluster
'''

import requests
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings("ignore")
K8s_MASTER_IP = ""
NAMESPACE = "default"
NAMESPACE_API_ENDPOINT = "https://{}:6443/api/v1/namespaces/"
ALL_PODS_API_ENDPOINT = "https://{}:6443/api/v1/namespaces/{}/pods"


def get_latest_pod(app_name):
    response = requests.get(ALL_PODS_API_ENDPOINT.format(K8s_MASTER_IP, NAMESPACE), verify=False)
    all_pods = response.json()
    pod_time_obj = dict()
    for items in all_pods["items"]:
        try:
            name = items["metadata"]["labels"]["app"]
        except: continue
        if name == app_name:
            times = items["metadata"]["creationTimestamp"].replace("T", " ").replace("Z", "")
            name = items["metadata"]["name"]
            pod_time_obj.setdefault(datetime.strptime(times, '%Y-%m-%d %H:%M:%S'), name)
    print pod_time_obj[max(pod_time_obj)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Latest pods finder in K8s cluster")
    #parser.add_argument("-H", action="store", dest="host", help="K8s cluster master node IP")
    #parser.add_argument("-n", action="store", dest="namespace", help="Namespace to look latest pod")
    #parser.add_argument("-p", action="store", dest="base_pod", help="Base POD name")
    parser.add_argument("-a", action="store", dest="app_name", help="Application name")
    options = parser.parse_args()
    if options.app_name:
        get_latest_pod(options.app_name)
    else:
        print "[!] Please specify application name"
        exit(1)
