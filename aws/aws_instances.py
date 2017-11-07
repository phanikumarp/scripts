#!/usr/bin/env python
'''
Author: OpsMx
Description: Retrieves auto scaling groups info from AWS
'''
import argparse
import json
from datetime import datetime

try:
    import boto.ec2.autoscale
    from boto.ec2.autoscale import LaunchConfiguration
    from boto.ec2.autoscale import AutoScalingGroup
except ImportError:
    print "[!] 'boto' client is not installed. Please install-> sudo pip2 install boto"
    exit(1)


class AwsInstances:
    def __init__(self, region, access_key, secret_key, check=True):
        self.region = region
        self.access_key = access_key
        self.secret_key = secret_key
        try:
            autoscale_conn = boto.ec2.autoscale.connect_to_region(region_name=self.region,
                                                                  aws_access_key_id=self.access_key,
                                                                  aws_secret_access_key=self.secret_key)
            groups_list = autoscale_conn.get_all_groups()
            if check:
                print "Success"
                exit(0)
            else:
                self.group_list = groups_list
        except boto.exception.BotoServerError:
            print "Failed to fetch"
            exit(1)
        except AttributeError:
            print "Failed to fetch"
            exit(1)

    def get_instance_details(self, instance_id):
        conn = boto.ec2.connect_to_region(region_name=self.region, aws_access_key_id=self.access_key,
                                          aws_secret_access_key=self.secret_key)
        reservations = conn.get_all_reservations(instance_ids=[instance_id])
        info = reservations[0].instances[0]
        instance_details = {
            "instanceId": instance_id, "launchTime": info.launch_time,
            "privateIp": info.private_ip_address, "publicIp": info.ip_address
        }
        return instance_details

    def display_as_details(self, as_group):
        instances_list = list()
        for group in self.group_list:
            if as_group == group.name:
                for instances in group.instances:
                    instances_list.append(self.get_instance_details(instances.instance_id))
                info = {
                    "name": group.name, "instances": instances_list,
                    "createdTime": group.created_time
                }
                print json.dumps(info)
                exit(0)

    def as_by_appname(self, appname):
        autoscale = dict()
        instances_list = list()
        for group in self.group_list:
            if appname in group.name:
                autoscale.setdefault(datetime.strptime(group.created_time, '%Y-%m-%dT%H:%M:%S.%fZ'), group)
        if not autoscale:
            print "[!] Auto scale groups not found."
            exit(1)
        latest_autoscale = autoscale[max(autoscale)]
        for instances in latest_autoscale.instances:
            instances_list.append(self.get_instance_details(instances.instance_id))
        info = {
            "name": latest_autoscale.name, "instances": instances_list,
            "createdTime": latest_autoscale.created_time
        }
        print json.dumps(info)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Retrieves auto scaling groups info from AWS \
                                                ****NOTE: Please install boto client->sudo pip2 install boto")
    parser.add_argument("-a", action="store", dest="access_key", help="AWS Access Key")
    parser.add_argument("-s", action="store", dest="secret_key", help="AWS Secret Key")
    parser.add_argument("-r", action="store", dest="region", help="AWS region")
    parser.add_argument("-A", action="store", dest="auto_scaling_group", help="Auto scaling group name")
    parser.add_argument("-p", action="store", dest="application_name", help="Spinnaker application name")
    options = parser.parse_args()
    if options.access_key and options.secret_key and options.region and options.auto_scaling_group:
        # Get info with "Auto Scaling Groups"/"Server Group Name"
        inst = AwsInstances(options.region, options.access_key, options.secret_key, check=False)
        inst.display_as_details(options.auto_scaling_group)
    elif options.access_key and options.secret_key and options.region and options.application_name:
        # Get info with Application Name in Spinnaker
        inst = AwsInstances(options.region, options.access_key, options.secret_key, check=False)
        inst.as_by_appname(options.application_name+"-")
    elif options.access_key and options.secret_key and options.region:
        # Check the keys are working or not
        AwsInstances(options.region, options.access_key, options.secret_key)
    else:
        print "[!] Please specify AWS region name, access key and secret key. For help -> python2 aws_instance.py -h\n"
        exit(1)
