# AWS related scripts
1. ### `aws_instances.py` [Retrives Auto Scaling Groups Info]
#### Dependencey Install `boto` python module: `sudo pip2 install boto`
Download -> wget -qO aws_instances.py https://raw.githubusercontent.com/OpsMx/scripts/master/aws/aws_instances.py

* Help
```
python2 aws_instances.py -h
usage: aws_instances.py [-h] [-a ACCESS_KEY] [-s SECRET_KEY] [-r REGION]
              [-A AUTO_SCALING_GROUP] [-p APPLICATION_NAME]

Retrieves auto scaling groups info from AWS ****NOTE: Please install boto
client->sudo pip2 install boto

optional arguments:
  -h, --help            show this help message and exit
  -a ACCESS_KEY         AWS Access Key
  -s SECRET_KEY         AWS Secret Key
  -r REGION             AWS region
  -A AUTO_SCALING_GROUP
                        Auto scaling group name
  -p APPLICATION_NAME   Spinnaker application name

```
* AWS Keys validation
  * If Keys are valid, it will display `Scucces`
  * If keys are invalid, it will display `Failed to fetch`
```
python2 aws.py -a <AWS_ACCESS_KEY> -s <AWS_SECRET_KEY> -r <AWS_REGION>
Success
```
* ##### Get Auto Scaling Group's instances by `Application Name`. [Gets latest server group]
```
python2 aws.py -a XXXXXXXXXXXXXX -s YYYYYYYYYYYY -r us-west-32 -p test54
{
   "createdTime":"20X7-XX-07TXX:35:12.328Z",
   "instances":[
      {
         "instanceId":"i-asdsdfsdfsdfsdf",
         "publicIp":"AA.XX.YY.YY",
         "launchTime":"20X7-XX-07TXX:35:15.000Z",
         "privateIp":"10.0.0.5"
      }
   ],
   "name":"canaryapp-XX-dev-XX-v001"
}
```
* #####  Get Auto Scaling Group's instances by `Server Group Name` 
```

python2 aws.py -a XXXXXXXXXXXXXX -s YYYYYYYYYYYY -r us-west-23 -A test54
{
   "createdTime":"20X7-XX-07TXX:35:12.328Z",
   "instances":[
      {
         "instanceId":"i-asdsdfsdfsdfsdf",
         "publicIp":"AA.XX.YY.YY",
         "launchTime":"20X7-XX-07TXX:35:15.000Z",
         "privateIp":"10.0.0.5"
      }
   ],
   "name":"canaryapp-XX-dev-XX-v001"
}
```
2. ### `aws_credentials_check.py` [AWS Credentials Validator]
##### *Dependency -> Install `boto` Client `sudo pip2 install boto`
Get the script ->  `wget -qO aws_credentials_check.py https://raw.githubusercontent.com/OpsMx/scripts/master/aws/aws_credentials_check.py`
* On success it will display `Autoscaling` group info in `json` formate
* On failure it will display `Failed`
```
$ python2 aws_credentials_check.py -r <REGION> -a <ACESS-KEY>- -s <SECRET-KEY>
[
   {
      "configuration":"aaaa-evt-v006-1010051455",
      "name":"aaaaa-evt-v006",
      "loadBalancer":[
         "aaaaa-evtreg"
      ]
   },
   {
      "configuration":"bbbb-evt-v007-101717062405",
      "name":"bbbb-evt-v007",
      "loadBalancer":[
         "bbbb-evtreg"
      ]
   }
]
$ python2 aws_credentials_check.py -r <REGION> -a <ACESS KEY> -s <SECRET-KEY>
Failed
```
