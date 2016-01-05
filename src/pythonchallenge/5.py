# -*- coding: utf-8 -*-
import pickle
import requests

__author__ = 'f0x11'

content = requests.get("http://www.pythonchallenge.com/pc/def/channel.jpg").content
banner = pickle.dumps(content)

print banner

for line in banner:
    print(''.join(map(lambda x: x[0] * x[1], line)))
