#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from time import sleep
from tornado.options import parse_config_file, options, define

define("demo_user")

parse_config_file("config.conf")

while 1:
    print('start')
    print options.demo_user
    sleep(5)

