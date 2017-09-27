from datadog import initialize, api
import time
import json

options = {
    'api_key': '<KEY>', #Your API_KEY and APP_KEY, see https://app.datadoghq.com/account/settings#api
    'app_key': '<KEY>'
}

initialize(**options)

start = int(time.time()) - 3600 #Here you can specify the time period over which you want to fetch the data, it's in seconds so here we fetch one hour
end = start + 3600

query = 'system.cpu.idle{*}' #Select the metric you want to get, see your list here: https://app.datadoghq.com/metric/summary . Select the host from which you want the data, see here: https://app.datadoghq.com/infrastructure

results = api.Metric.query(start=start - 3600, end=end, query=query)

f = open('out.txt', 'w') #this will create a file name out.txt in the folder you are in
print >> f, json.dumps(results)
f.close()
#print results #That should display the results in the terminal
