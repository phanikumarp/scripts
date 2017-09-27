#!/bin/env python
'''
Simple script that exports tsdb data and uploads to S3 bucket
'''
import argparse
import os
import subprocess
import traceback
import logging
import time
from logging.handlers import RotatingFileHandler
try:
    import tinys3
except ImportError:
    print "[!] `tinys3 module is not installed. Please install->'pip install tinys3'"
    exit(1)

LOG_LOCATION = '/var/log/s3_uploader.log'
MAX_SIZE_LOG=20 #Mega Bytes
BACKUP_COUNT=0
S3_ACCESS_KEY = ""
S3_SECRET_KEY = ""
BUCKET_NAME = "tsdb"
HBASE_DIR_LOCATION = "/root/extraspace/sendbox/hbase-0.94.19"
TABLES = ["tsdb", "tsdb-meta",
    "tsdb-tree", "tsdb-uid"]


def log_it(level,message):
    log.setLevel(levels[level])
    log.addHandler(handler)
    handler.setLevel(levels[level])
    if level=="info":
        log.info(message)
    elif level=="debug":
        log.debug(message)
    elif level=="warning":
        log.warning(message)
    elif level=="error":
        log.error(message)
    elif level=="critical":
        log.critical(message)


def daemonize():
    if os.fork():
        os._exit(0)
    os.chdir("/")
    os.umask(022)
    os.setsid()
    os.umask(0)
    if os.fork():
        os._exit(0)
    stdin = open(os.devnull)
    stdout = open(os.devnull, 'w')
    os.dup2(stdin.fileno(), 0)
    os.dup2(stdout.fileno(), 1)
    os.dup2(stdout.fileno(), 2)
    stdin.close()
    stdout.close()
    os.umask(022)
    for fd in xrange(3, 1024):
        try:
            os.close(fd)
        except OSError:
            pass


def export_tables(dir_location):
    exported_files = list()
    habase_bin_file = os.path.join(dir_location, "bin/hbase")
    if not os.path.exists(habase_bin_file):
        print "[!] hbase binary file {} not found".format(habase_bin_file)
        log_it("error", "hbase binary file {} not found".format(habase_bin_file))
        exit(1)
    for table in TABLES:
        try:
            cmd = habase_bin_file + " org.apache.hadoop.hbase.mapreduce.Driver export "+table+" /tmp/"+table
            print "[+] Running Command {}\n  [+] Trying to export table -> {}".format(cmd, table)
            log_it("info", "Running Command {}".format(cmd))
            #subprocess.check_output(cmd, shell=True)
            log_it("info", "Exported the table {}".format(table))
            exported_files.append("/tmp/"+table)
        except:
            print "[!] Unable to perform operation"
            print traceback.print_exc()
            log_it("error", str(traceback.print_exc()))
    return exported_files


def get_file_paths(dir_list):
    files_list=list()
    def goto_tail(directory):
        for item in os.listdir(directory):
            total_path=os.path.join(directory, item)
            if not os.path.isdir(total_path):
                print item
                files_list.append(total_path)
            else:
                goto_tail(total_path)
    for dirs in dir_list:
        goto_tail(dirs)
    print files_list

def upload(location, bucket):
    global S3_ACCESS_KEY, S3_SECRET_KEY
    for file_name in location:
        if not os.path.exit(file_name):
            print "[!] {} not found".format(file_name)
            log_it("error", "{} not found".format(file_name))
            continue
        try:
            conn = tinys3.Connection(S3_ACCESS_KEY, S3_SECRET_KEY, tls=True)
            f = open(file_name,'rb')
            print "[*] Uploading {}...".format(file_name)
            log_it("info", "Uploading {}".format(file_name))
            conn.upload(file_name,f,bucket)
            log_it("info", "Uploaded {}".format(file_name))
        except:
            print "[!] Unable tp perform operation"
            print traceback.print_exc()
            log_it("error", str(traceback.print_exc()))

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Simple script that exports tsdb data and uploads files to S3 bucket [OpsMx]")
    parse.add_argument("-b", dest="bucket", action="store", help="Bucket Name. Default tsdb")
    parse.add_argument("-l", dest="location", action="store", help="hbase directory location")
    parse.add_argument("-d", dest="daemon", action="store_true", default=False, help="Run task as daemon")
    results = parse.parse_args()
    if results.bucket:
        BUCKET_NAME = results.bucket
    if not S3_ACCESS_KEY or not S3_SECRET_KEY:
        print "[!] Please specify 'S3_ACCESS_KEY' and 'S3_SECRET_KEY' in the script"
        exit(1)
    if not results.location:
        if os.path.exists(HBASE_DIR_LOCATION):
            location = HBASE_DIR_LOCATION
        else:
            location = raw_input("Please enter hbase directory location> ").strip()
            if not location or not os.path.exists(location):
                print "[!] Please enter corrent location"
                exit(1)
    else:
        if not os.path.exists(results.location):
            print "[!] {} not found".format(results.location)
            exit(1)
        location = results.location
    if results.daemon:
        print "[*] Running task in background. You can check the PID with 'pgrep s3_uploader.py'"
        daemonize()
    handler=RotatingFileHandler(LOG_LOCATION, mode='a', maxBytes=MAX_SIZE_LOG*1024*1024, backupCount=BACKUP_COUNT, encoding=None, delay=0)
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)s[%(process)d] %(levelname)s: %(message)s'))
    log=logging.getLogger('S3-Uploader')
    levels={"debug":logging.DEBUG, "info":logging.INFO,
            "warning":logging.WARNING, "error":logging.ERROR,
            "critical":logging.CRITICAL}
    #start_time=int(time.time())
    file_location=export_tables(location)
    #upload(file_location, BUCKET_NAME)
    #total_time=(int(time.time())-start_time)/60
    #log_it("info", "Task Completed in {} minutes".format(total_time))
    get_file_paths(file_location)
