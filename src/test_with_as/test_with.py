#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback

__author__ = 'f0x11'

class SessionCM(object):
    val = 1

    def __enter__(self):
        return self.val

    def __exit__(self, exc_type, exc_val, exc_tb):
        # try:
        #     self.session.rollback()
        # except:
        #     log.e('session rollback error')
        if exc_tb is not None:
            log.i(traceback.format_exc())
            print '[Exit %s]: Exited with exception raised.' % self.tag

        self.session.close()


def test():
    with SessionCM() as b:
        raise


if __name__ == '__main__':
    test()
