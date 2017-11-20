#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fnmatch as m

__author__ = 'f0x11'


print(m.__doc__.splitlines()[0])  # Filename matching with shell patterns.
print(m.__name__)  # fnmatch
print(m.__file__)  # /usr/lib/python2.6/fnmatch.pyc
print(m.__dict__.items()[0])  # ('fnmatchcase', <function>)</function>
