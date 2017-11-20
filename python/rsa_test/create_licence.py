#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import time
from datetime import datetime, timedelta
import rsa

LIMIT_DAYS = 30

with open('private.pem') as privatefile:
    p = privatefile.read().encode('utf-8')
    privkey = rsa.PrivateKey.load_pkcs1(p)


def generate_licence():
    message = str(int((datetime.now() + timedelta(LIMIT_DAYS)).timestamp()))
    message = base64.b64encode(message.encode('utf-8'))

    signature = rsa.sign(message, privkey, 'SHA-1')

    licence = message + b'\n' + signature

    licence_file = 'licence{0}.txt'.format(str(int(time.time())))
    with open(licence_file, 'w') as fp:
        fp.write(base64.b64encode(licence).decode('utf-8'))


if __name__ == '__main__':
    generate_licence()
