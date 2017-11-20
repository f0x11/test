#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import hashlib

__author__ = 'f0x11'

print(base64.b64encode(bytes("cmingxu:dmJAh69uV}@RRe".encode())))

print('{{"auths": {{"{0}": {{"auth": "{1}", "email": "{2}@xxx.com"}}}}}}'.format("2", "3", "4"))


def auth_config(user_id):
    user_string = str(user_id)
    print(bytes((user_string + ":" + hashlib.md5(user_string.encode()).hexdigest()).encode()))
    config = {
        "auths": {
            '22222': {
                "auth": base64.b64encode((
                    (user_string + ":" + hashlib.md5(user_string.encode()).hexdigest()).encode()
                )).decode(),
                "email": "{0}@xxx.com".format(user_string)
            }
        }
    }
    return config

# print(auth_config(111))
