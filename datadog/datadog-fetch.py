#!/usr/bin/env python
'''
Description: Datadata metrics data fetcher
'''

import time
import json
import argparse
import csv
import warnings
try:
    from datadog import initialize, api
except ImportError:
    print "[!] Please install datadog python module. Run 'pip install datadog'"
    exit(1)

warnings.filterwarnings("ignore")
options = {
    'api_key': 'KEY',
    'app_key': 'KEY'
}
initialize(**options)
metrics_list = [
    "apache.conns_async_closing",
    "apache.conns_async_keep_alive",
    "apache.conns_async_writing",
    "apache.conns_total",
    "apache.net.bytes",
    "apache.net.bytes_per_s",
    "apache.net.hits",
    "apache.net.request_per_s",
    "apache.performance.busy_workers",
    "apache.performance.cpu_load",
    "apache.performance.idle_workers",
    "apache.performance.uptime",
    "jvm.gc.cms.count",
    "jvm.gc.parnew.time",
    "jvm.heap_memory",
    "jvm.heap_memory_committed",
    "jvm.heap_memory_init",
    "jvm.heap_memory_max",
    "jvm.non_heap_memory",
    "jvm.non_heap_memory_committed",
    "jvm.non_heap_memory_init",
    "jvm.non_heap_memory_max",
    "jvm.thread_count",
    "postgresql.archiver.archived_count",
    "postgresql.archiver.failed_count",
    "postgresql.bgwriter.buffers_alloc",
    "postgresql.bgwriter.buffers_backend",
    "postgresql.bgwriter.buffers_backend_fsync",
    "postgresql.bgwriter.buffers_checkpoint",
    "postgresql.bgwriter.buffers_clean",
    "postgresql.bgwriter.checkpoints_requested",
    "postgresql.bgwriter.checkpoints_timed",
    "postgresql.bgwriter.maxwritten_clean",
    "postgresql.bgwriter.sync_time",
    "postgresql.bgwriter.write_time",
    "postgresql.buffer_hit",
    "postgresql.commits",
    "postgresql.connections",
    "postgresql.database_size",
    "postgresql.db.count",
    "postgresql.deadlocks",
    "postgresql.disk_read",
    "postgresql.max_connections",
    "postgresql.percent_usage_connections",
    "postgresql.rollbacks",
    "postgresql.rows_deleted",
    "postgresql.rows_fetched",
    "postgresql.rows_inserted",
    "postgresql.rows_returned",
    "postgresql.rows_updated",
    "postgresql.table.count",
    "postgresql.temp_bytes",
    "postgresql.temp_files",
    "redis.aof.last_rewrite_time",
    "redis.aof.rewrite",
    "redis.clients.biggest_input_buf",
    "redis.clients.blocked",
    "redis.clients.longest_output_list",
    "redis.cpu.sys",
    "redis.cpu.sys_children",
    "redis.cpu.user",
    "redis.cpu.user_children",
    "redis.expires",
    "redis.expires.percent",
    "redis.info.latency_ms",
    "redis.key.length",
    "redis.keys",
    "redis.keys.evicted",
    "redis.keys.expired",
    "redis.mem.fragmentation_ratio",
    "redis.mem.lua",
    "redis.mem.maxmemory",
    "redis.mem.peak",
    "redis.mem.rss",
    "redis.mem.used",
    "redis.net.clients",
    "redis.net.commands",
    "redis.net.instantaneous_ops_per_sec",
    "redis.net.rejected",
    "redis.net.slaves",
    "redis.perf.latest_fork_usec",
    "redis.persist",
    "redis.persist.percent",
    "redis.pubsub.channels",
    "redis.pubsub.patterns",
    "redis.rdb.bgsave",
    "redis.rdb.changes_since_last",
    "redis.rdb.last_bgsave_time",
    "redis.replication.backlog_histlen",
    "redis.replication.master_repl_offset",
    "redis.stats.keyspace_hits",
    "redis.stats.keyspace_misses",
    "system.cpu.guest",
    "system.cpu.idle",
    "system.cpu.iowait",
    "system.cpu.stolen",
    "system.cpu.system",
    "system.cpu.user",
    "system.disk.free",
    "system.disk.in_use",
    "system.disk.total",
    "system.disk.used",
    "system.fs.file_handles.in_use",
    "system.fs.inodes.free",
    "system.fs.inodes.in_use",
    "system.fs.inodes.total",
    "system.fs.inodes.used",
    "system.io.avg_q_sz",
    "system.io.avg_rq_sz",
    "system.io.await",
    "system.io.r_await",
    "system.io.r_s",
    "system.io.rkb_s",
    "system.io.rrqm_s",
    "system.io.svctm",
    "system.io.util",
    "system.io.w_await",
    "system.io.w_s",
    "system.io.wkb_s",
    "system.io.wrqm_s",
    "system.load.1",
    "system.load.15",
    "system.load.5",
    "system.load.norm.1",
    "system.load.norm.15",
    "system.load.norm.5",
    "system.mem.buffered",
    "system.mem.cached",
    "system.mem.free",
    "system.mem.page_tables",
    "system.mem.pct_usable",
    "system.mem.shared",
    "system.mem.slab",
    "system.mem.total",
    "system.mem.usable",
    "system.mem.used",
    "system.net.bytes_rcvd",
    "system.net.bytes_sent",
    "system.net.packets_in.count",
    "system.net.packets_in.error",
    "system.net.packets_out.count",
    "system.net.packets_out.error",
    "system.net.tcp.backlog_drops",
    "system.net.tcp.in_segs",
    "system.net.tcp.listen_drops",
    "system.net.tcp.listen_overflows",
    "system.net.tcp.out_segs",
    "system.net.tcp.retrans_segs",
    "system.net.udp.in_csum_errors",
    "system.net.udp.in_datagrams",
    "system.net.udp.in_errors",
    "system.net.udp.no_ports",
    "system.net.udp.out_datagrams",
    "system.net.udp.rcv_buf_errors",
    "system.net.udp.snd_buf_errors",
    "system.swap.cached",
    "system.swap.free",
    "system.swap.total",
    "system.swap.used",
    "system.uptime",
    "tomcat.bytes_rcvd",
    "tomcat.bytes_sent",
    "tomcat.cache.access_count",
    "tomcat.error_count",
    "tomcat.jsp.count",
    "tomcat.jsp.reload_count",
    "tomcat.max_time",
    "tomcat.processing_time",
    "tomcat.request_count",
    "tomcat.servlet.error_count",
    "tomcat.servlet.processing_time",
    "tomcat.servlet.request_count",
    "tomcat.threads.busy",
    "tomcat.threads.count",
    "tomcat.threads.max"
]


def write_csv(host="ip-10-0-0-131.us-west-1.compute.internal"):
    start = int(time.time()) - 3600
    end = start + 3600
    #datapoints
    with open('names.csv', 'w') as csvfile:
        for metric_name in metrics_list:
            writer = csv.DictWriter(csvfile, fieldnames=metrics_list, dialect='excel')
            writer.writeheader()
            query = metric_name + '{*}by{' + host + '}'
            results = api.Metric.query(start=start - 3600, end=end, query=query)
            for datapoints in results["series"][0]["pointlist"]:
                #print datapoints[1]
                writer.writerow({metric_name: datapoints[1]})


        #f = open('out.txt', 'w')
        #print >> f, json.dumps(results)
        #f.close()


if __name__ == '__main__':
    frm, to = 0, 0
    parser = argparse.ArgumentParser(description="Datadog metrics data fetcher")
    parser.add_argument("-f", action="store", dest="from_time", help="Specify past time/from-time in seconds")
    parser.add_argument("-t", action="store", dest="to_time", help="Specify to-time in seconds. Default will be NOW")
    options = parser.parse_args()
    write_csv()
    '''
    if options.to_time:
        to = options.to_time
    else:
        to = int(time.time())
    if not options.from_time:
        print "[!] Please specify past time/from-time."
    else:
        try:
            frm = int(options.from_time)

        except:
            print "[!] Invalid from-time"
            exit(1)
    '''
