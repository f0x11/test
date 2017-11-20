#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'f0x11'


def db_session_scope():
    """Provide a transactional scope around a series of operations."""
    print '11111'
    try:
        print '22222'
        raise
    except:
        print '33333'
        raise
    finally:
        print '44444'


if __name__ == '__main__':
    db_session_scope()