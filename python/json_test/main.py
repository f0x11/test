#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'f0x11'

import json

# ios_str = u'{"idx":1,"ver":"2.2.1","params":{"content1":"不要\\js","content2":"在一起是不是","content3":"我想我是真的有点大"}}'
# print repr(ios_str)
#
# print '--------'
# print json.loads(ios_str)

# print '2--------------------'
# str1 = u'{1: "\\"}'
# str1r = json.loads(str1)
# print str1r
# print repr(str1r)

def print_4():
    str2 = u'{"2": "\\\\"}'
    str2r = json.loads(str2)
    print str2r
    print repr(str2r)


if __name__ == "__main__":
    print_4()
