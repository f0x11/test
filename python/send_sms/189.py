#!/usr/bin/env python
# encoding: utf-8
import requests

res = requests.post('http://yunpian.com/v1/sms/send.json', {
    'apikey': '',
    'mobile': 'xxxxxx',
    'text': '【xxxx】您的验证码是1234',
})

print(res)