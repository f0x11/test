# -*- coding: utf-8 -*-
import requests

__author__ = 'f0x11'

# 16044 66831

index = "16"
url_prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while True:
    res = requests.get(url_prefix + index)
    index = res.content.rsplit(" ", 1)[1]
    print int(index)
