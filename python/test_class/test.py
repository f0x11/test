#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'f0x11'


class a(object):
    b = 1


if __name__ == '__main__':
    getattr(a, 'b')
    try:
        getattr(a, 'c')
    except AttributeError as e:
        print(e)