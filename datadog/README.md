# Datadog

### Enabling services

1. Copy service `yml` file to `/etc/dd-agent/conf.d/`
2. Restart data-agent: `sudo service datadog-agent restart`
3. Check the service is properly enabled or not: `sudo service datadog-agent info` (You should see service instance as `[OK]`)

### Info

* Create trail Account -> https://www.datadoghq.com/
* List of metrics there are currently active -> https://app.datadoghq.com/metric/summary
* API settings page -> https://app.datadoghq.com/account/settings#api
* API documentation -> https://docs.datadoghq.com/api/
* Datadog dashboard -> https://app.datadoghq.com
