#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import htonl


def get_result_id(id):
    id = htonl(id)
    id = id ^ 0x3f91b217

    print '%010d' % id


if __name__ == '__main__':
    get_result_id(1)
    get_result_id(4)

