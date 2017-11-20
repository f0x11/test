#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta
import base64

import rsa

__author__ = 'f0x11'

with open('public.pem') as publickfile:
    p = publickfile.read().encode('utf-8')
    pubkey = rsa.PublicKey.load_pkcs1(p)

with open('private.pem') as privatefile:
    p = privatefile.read().encode('utf-8')
    privkey = rsa.PrivateKey.load_pkcs1(p)


message = str(int((datetime.now() + timedelta(30)).timestamp()))
print(message)
message = base64.b64encode(message.encode('utf-8'))

signature = rsa.sign(message, privkey, 'SHA-1')

print(signature)

licence = message + b'\n' + signature

with open('licence.txt', 'w') as fp:
    fp.write(base64.b64encode(licence).decode('utf-8'))




