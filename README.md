# OpsMx Automated Scripts

## AWS Credentials Validator
##### *Dependency -> Install `boto` Client `sudo pip2 install boto`
Get the script ->  `wget -qO aws_credentials_check.py https://goo.gl/WKPu97`
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
