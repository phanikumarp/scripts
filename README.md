# OpsMx Automated Scripts

## AWS Credentials Validator
##### *Dependency -> Install `boto` Client `sudo pip2 install boto`
Get the script ->  `wget -qO aws_credentials_check.py https://goo.gl/WKPu97`
```
$ python2 aws_credentials_check.py -a <ACESS-KEY>- -s <SECRET-KEY>
Failed
$ python2 aws_credentials_check.py -a <ACESS KEY> -s <SECRET-KEY>
Success
```
