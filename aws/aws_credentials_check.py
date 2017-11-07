#!/usr/bin/env python
'''
Author: OpsMx
Description: Validates AWS ACCESS KEY and SECRET KEY. Also retrieves auto scaling groups info
'''
import argparse
import json
try:
    import boto.ec2.autoscale
    from boto.ec2.autoscale import LaunchConfiguration
    from boto.ec2.autoscale import AutoScalingGroup
except ImportError:
    print "[!] 'boto' client is not installed. Please install-> sudo pip2 install boto"
    exit(1)


def check_cred(region, access_key, secret_key):
    autoscale = list()
    try:
        autoscale_conn = boto.ec2.autoscale.connect_to_region(region_name=region, aws_access_key_id=access_key,
                                                              aws_secret_access_key=secret_key)
        ag = autoscale_conn.get_all_groups()
        for group in ag:
            info = dict()
            info.setdefault("name", group.name)
            info.setdefault("configuration", group.launch_config_name)
            info.setdefault("loadBalancer", group.load_balancers)
            autoscale.append(info)
        print json.dumps(autoscale)
    except boto.exception.BotoServerError:
        print "Failed"
        exit(1)
    except AttributeError:
        print "Failed"
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks AWS ACCESS KEY and SECRET KEY are valid or not. \
            Also retrieves auto scaling groups info. NOTE: Please install boto client->sudo pip2 install boto")
    parser.add_argument("-a", action="store", dest="access_key", help="AWS Access Key")
    parser.add_argument("-s", action="store", dest="secret_key", help="AWS Secret Key")
    parser.add_argument("-r", action="store", dest="region", help="AWS region")
    options = parser.parse_args()
    if options.access_key and options.secret_key and options.region:
        check_cred(options.region, options.access_key, options.secret_key)
    else:
        print "[!] Please specify AWS region name, access key, secret key. For help -> python2 aws_credential_check.py -h"
        exit(1)
