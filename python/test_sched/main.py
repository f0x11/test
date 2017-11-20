#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sched

__author__ = 'f0x11'

schedule = sched.scheduler(time.time, time.sleep)


def func(string1, float1):
    print("now is", time.time(), " | output=", string1, float1)


print(time.time())
schedule.enter(2, 0, func, ("test1", time.time()))
schedule.enter(2, 0, func, ("test1", time.time()))
schedule.enter(3, 0, func, ("test1", time.time()))
schedule.enter(4, 0, func, ("test1", time.time()))
schedule.run()
print(time.time())
