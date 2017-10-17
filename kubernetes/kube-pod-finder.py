'''
Author : OpsMx
Description :  Latest pods finder in K8s cluster
'''

import requests
import argparse
import warnings
from datetime import datetime
import json

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
            cluster_name = items["metadata"]["labels"]["cluster"]
        except KeyError:
            pass
        try:
            replication_con = items["metadata"]["labels"]["replication-controller"]
        except KeyError:
            pass
        if cluster_name == obj_name or replication_con == obj_name:
            times = items["metadata"]["creationTimestamp"].replace("T", " ").replace("Z", "")
            name = items["metadata"]["name"]
            app_name = items["metadata"]["labels"]["app"]
            replication_con = items["metadata"]["labels"]["replication-controller"]
            pod_time_obj.setdefault(datetime.strptime(times, '%Y-%m-%d %H:%M:%S'), [name, replication_con])
    try:
        latest_pod = pod_time_obj[max(pod_time_obj)]
    except ValueError:
        exit(0)
    data = [
        {
            "applicationName": app_name,
            "podName": latest_pod[0],
            "sgName":latest_pod[1],
            "creationTimestamp": str(max(pod_time_obj))
        }
    ]
    print json.dumps(data)
    #for x in reversed(pod_time_obj.keys()):
        #print pod_time_obj[x]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Latest pods finder in K8s cluster. \
                                                    NOTE: Please specify 'K8s_IP' in script")
    parser.add_argument("-c", action="store", dest="cluster_name", help="cluster name or cluster name with version")
    options = parser.parse_args()
    if options.cluster_name:
        if "-current" in options.cluster_name:
            name = options.cluster_name.strip("-current")
        else:
            name = options.cluster_name
        get_latest_pod(name)
    else:
        print "[!] Please specify 'cluster name'. Help-> python kube-pod-finder.py -h"
