# -*- coding: utf-8 -*-
import requests

__author__ = 'f0x11'

appid = 'wxdb0487324499420e'
appsecret = 'd50ebb499a76e8b886ac057c40b28fd6'

url = 'https://api.weixin.qq.com/sns/oauth2/access_token?' + \
      'appid=' + appid + \
      '&secret=' + appsecret + \
      '&code=031678f087f40c13f9c87344595b2c1W' + \
      '&grant_type=authorization_code'

print url

res = requests.get(url)


print res
