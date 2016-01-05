# -*- coding: utf-8 -*-
import urllib
import requests

__author__ = 'f0x11'

WX_APPID = 'wx333dc23de3c8e46d'
WX_SECRET = '2680d85ef00c515fd7a266a811c924e6'

WX_SIGNIN_REDIRECT = 'https://open.weixin.qq.com/connect/oauth2/authorize' \
                     + '?appid=' + WX_APPID \
                     + '&redirect_uri=http%3A%2F%2Ftest.shitouren.com%2Fweixin%2Fweb%2Fcallback' \
                     + '&response_type=code' \
                     + '&scope=snsapi_userinfo' \
                     + '&state=krHVypmrn5#wechat_redirect'

print WX_SIGNIN_REDIRECT

# requests.get()
