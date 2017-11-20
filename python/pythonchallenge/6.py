# -*- coding: utf-8 -*-
import zipfile
import StringIO
import requests

__author__ = 'f0x11'

def get_challenge(url):
    return requests.get("http://www.pythonchallenge.com/pc/def/" + url).content


z = zipfile.ZipFile(StringIO.StringIO(get_challenge('channel.zip')))

index = "90052"
z_list = []
try:
    while True:
        print int(index)
        content1 = z.read(index + '.txt')
        index = content1.rsplit(" ", 1)[1]
        z_list.append(index)
except:
    pass


print ''.join([z.getinfo('%s.txt' % p).comment for p in z_list])
