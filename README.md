# OpsMx Automated Scripts

#### AWS Credentials Validator
Get the script ->  `wget -qO aws_credentials_check.py https://goo.gl/WKPu97`
```
$ python aws_credentials_check.py -a XXXXXXXXXXX -s YYYYYYYYY
Failed
$ python aws_credentials_check.py -a XXXXXXXXXXA -s YYYYYYYYY
Success
```
