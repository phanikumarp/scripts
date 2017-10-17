'''
Author : OpsMx
Description :  Latest pods finder in K8s cluster
'''

import requests
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings("ignore")
K8s_IP = "localhost"
NAMESPACE = "default"
NAMESPACE_API_ENDPOINT = "http://{}:8001/api/v1/namespaces/"
ALL_PODS_API_ENDPOINT = "http://{}:8001/api/v1/namespaces/{}/pods"


def get_latest_pod(obj_name):
    response = requests.get(ALL_PODS_API_ENDPOINT.format(K8s_IP, NAMESPACE), verify=False)
    all_pods = response.json()
    pod_time_obj = dict()
    app_name = None
    cluster_name = None
    for items in all_pods["items"]:
        try:
            app_name = items["metadata"]["labels"]["app"]
        except KeyError:
            pass
        try:
            cluster_name = items["metadata"]["labels"]["cluster"]
        except KeyError:
            pass
        if app_name == obj_name or cluster_name == obj_name:
            times = items["metadata"]["creationTimestamp"].replace("T", " ").replace("Z", "")
            name = items["metadata"]["name"]
            pod_time_obj.setdefault(datetime.strptime(times, '%Y-%m-%d %H:%M:%S'), name)
    for x in reversed(pod_time_obj.keys()):
        print pod_time_obj[x], "- "+str(x)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Latest pods finder in K8s cluster. \
                                                    NOTE: Please specify 'K8s_IP' in script")
    parser.add_argument("-c", action="store", dest="cluster_name", help="Cluster name")
    parser.add_argument("-a", action="store", dest="app_name", help="Application name")
    options = parser.parse_args()
    if options.cluster_name and options.app_name:
        print "[!] Please specify any one, 'application name' or 'cluster name'"
    if options.app_name:
        get_latest_pod(options.app_name)
    elif options.cluster_name:
        get_latest_pod(options.cluster_name)
    else:
        print "[!] Please specify 'application name' or 'cluster name'. Help-> python kube-pod-finder.py -h"
