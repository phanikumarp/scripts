# OpsMx Automated Scripts

#### AWS Credentials Validator
Get the script ->  `wget -qO aws_credentials_check.py https://goo.gl/WKPu97`
```
$ python aws_credentials_check.py -a <ACESS-KEY>- -s <SECRET-KEY>
Failed
$ python aws_credentials_check.py -a <ACESS KEY> -s <SECRET-KEY>
Success
```
