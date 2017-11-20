#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'f0x11'

import random
import skip32

# key = ''.join(chr(random.randint(0, 255)) for _ in xrange(10))
key = "NHkbgvLTxO"

encrypted = skip32.encrypt(key, 12345)

print encrypted

print skip32.decrypt(key, encrypted)
