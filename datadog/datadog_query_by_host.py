from datadog import initialize, api
import time

options = {
    'api_key': '',
    'app_key': ''
}

initialize(**options)

now = int(time.time())
query = 'system.cpu.idle{*}by{*}'
print api.Metric.query(start=now - 3600, end=now, query=query)