# -*- coding: utf-8 -*-
import requests

__author__ = 'f0x11'

appid = 'xxx'
appsecret = 'xxxxx'
code = 'xxx'

url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' + \
      'appid=' + appid + \
      '&secret=' + appsecret + \
      '&code=' + code + \
      '&grant_type=authorization_code'

print(url)

res = requests.get(url)


print(res)
