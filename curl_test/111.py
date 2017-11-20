#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

__author__ = 'f0x11'


headers = {
    'Authorization': '2114fa2177c97205b2bd0ea4355c76ea'
}


res = requests.get("http://123.59.56.132/api/v1/nodes/eg5t232h234w61i9cuut4r/info", headers=headers)

print(res)
