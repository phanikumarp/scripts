# Datadog

### Enabling services
#### NOTE: 
  * For Tomcat, make sure that JMX Remote is enabled on the server. Check [here](https://github.com/OpsMx/scripts/wiki/Tomcat) to know how to enable
  * For Hbase, please enable JMX remote and place the JMX port in yaml file. Check [here](https://hbase.apache.org/metrics.html) to know how to enable
1. Copy service `.yaml` file to `/etc/dd-agent/conf.d/`
2. Restart data-agent: `sudo service datadog-agent restart`
3. Check the service is properly enabled or not: `sudo service datadog-agent info` (You should see service instance as `[OK]`)

#### Get `yaml` files
   * apache.yaml -> `wget -qO /etc/dd-agent/conf.d/apache.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/apache.yaml`
   * haproxy.yaml -> `wget -qO /etc/dd-agent/conf.d/haproxy.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/haproxy.yaml`
   * master_hbase.yaml -> `wget -qO /etc/dd-agent/conf.d/master_hbase.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/hbase_master.yaml`
   * postgres.yaml -> `wget -qO /etc/dd-agent/conf.d/postgres.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/postgres.yaml`
   * redis.yaml -> `wget -qO /etc/dd-agent/conf.d/redis.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/redisdb.yaml`
   * tomcat.yaml -> `wget -qO /etc/dd-agent/conf.d/tomcat.yaml https://raw.githubusercontent.com/OpsMx/scripts/master/datadog/tomcat.yaml`


### Info

* Create trail Account -> https://www.datadoghq.com/
* List of metrics there are currently active -> https://app.datadoghq.com/metric/summary
* API settings page -> https://app.datadoghq.com/account/settings#api
* API documentation -> https://docs.datadoghq.com/api/
* Datadog dashboard -> https://app.datadoghq.com

### Tril Accounts
<table>
  <tr>
  <th>No.</th><th>Account Name</td><th>Status</th>
  </tr>
 <tr>
 <tr>
  <td>1</td><td>caped@storj99.com</td><td>Expired</td>
  </tr>
 <tr>
  <td>2</td><td>vipobocif@crusthost.com</td><td>Expired</td>
  </tr>
 <tr>
  <td>3</td><td>pohisafe@morsin.com</td><td>Expired</td>
  </tr>
 <tr>
  <td>4</td><td>wiko@zhorachu.com</td><td>Active on 24-Oct-2017/ Expire in 5 Days</td>
  </tr>
 </table>
