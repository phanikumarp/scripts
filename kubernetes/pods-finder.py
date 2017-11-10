'''
Author : OpsMx
Description :  Retrives all pods in cluster/Replicasets
'''

import requests
import argparse
import warnings
from datetime import datetime
import json

warnings.filterwarnings("ignore")
K8s_IP = "localhost"
NAMESPACE = "default"
NAMESPACE_API_ENDPOINT = "https://{}:6443/api/v1/namespaces/"
ALL_PODS_API_ENDPOINT = "https://{}:6443/api/v1/namespaces/{}/pods"


class K8s_API:
    def __init__(self):
        try:
            response = requests.get(ALL_PODS_API_ENDPOINT.format(K8s_IP, NAMESPACE), verify=False)
        except:
            print "[!] Not able to connect to K8s cluster. Please check API"
            exit(1)
        self.all_pods = response.json()

    def get_latest_cluster(self, application):
        versions=dict()
        cluster_name = None
        for items in self.all_pods["items"]:
            try:
                cluster_name = items["metadata"]["labels"]["cluster"]
            except: continue
            if  cluster_name == application:
                versions.setdefault(int(items["metadata"]["labels"]["version"]), items["metadata"]["labels"]["replication-controller"])
        try:
            return versions[max(versions)]
        except:
            print "[!] Not able to get the latest cluster"
            exit(1)

    def get_latest_pod(self, cluster_name):
        data = list()
        for items in self.all_pods["items"]:
            try:
                replication_con = items["metadata"]["labels"]["replication-controller"]
            except: continue
            if replication_con == cluster_name:
                info = {
                    "applicationName": items["metadata"]["labels"]["app"],
                    "podName": items["metadata"]["name"],
                    "sgName":items["metadata"]["labels"]["replication-controller"],
                    "creationTimestamp": items["metadata"]["creationTimestamp"]
                    }
                data.append(info)
        print json.dumps(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrives all pods in cluster/Replicasets. \
                                                    NOTE: Please specify 'K8s_IP' in script")
    parser.add_argument("-c", action="store", dest="cls_name", help="Gets the pods in this cluster")
    parser.add_argument("-C", action="store", dest="current_cls_name", help="Gets the pods in 'current' cluster")
    options = parser.parse_args()
    if options.cls_name:
        k8s = K8s_API()
        k8s.get_latest_pod(options.cls_name)
    elif options.current_cls_name:
        k8s = K8s_API()
        latest_cluster = k8s.get_latest_cluster(options.current_cls_name.replace("-current",""))
        if latest_cluster:
            k8s.get_latest_pod(latest_cluster)
    else:
        print "[!] Please specify 'cluster name'. Help-> python kube-pod-finder.py -h"
