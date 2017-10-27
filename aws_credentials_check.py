#!/usr/bin/env python
'''
Author: OpsMx
Description: Validates AWS ACCESS KEY and SECRET KEY.
'''
import argparse
try:
    from boto.s3.connection import S3Connection
    from boto.exception import S3ResponseError
except ImportError:
    print "[!] 'boto' client is not installed. Please install-> sudo pip install boto"


def check_cred(access_key, secret_key):
    conn = S3Connection(access_key, secret_key)
    try:
        conn.get_all_buckets()
    except S3ResponseError:
        print "Failed"
        exit(1)
    print "Success"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks AWS ACCESS KEY and SECRET KEY are valid or not. \
                                                NOTE: Please install boto client->sudo pip install boto")
    parser.add_argument("-a", action="store", dest="access_key", help="AWS Access Key")
    parser.add_argument("-s", action="store", dest="secret_key", help="AWS Secret Key")
    options = parser.parse_args()
    if options.access_key and options.secret_key:
        check_cred(options.access_key, options.secret_key)
    else:
        print "[!] Please AWS access key and secret key. For help -> python aws_credential_check.py -h"
        exit(1)
