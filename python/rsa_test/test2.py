#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64

import rsa

__author__ = 'f0x11'

with open('public.pem') as publickfile:
    p = publickfile.read().encode('utf-8')
    pubkey = rsa.PublicKey.load_pkcs1(p)

with open('licence.txt', 'r') as fp:
    licence = fp.read()

message, signature = base64.b64decode(licence.strip().encode('utf-8')).split(b'\n', 1)

rsa.verify(message, signature, pubkey)

endtime = base64.b64decode(message).decode('utf-8')
print(endtime)
