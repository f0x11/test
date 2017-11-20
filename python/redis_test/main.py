#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis
import tornadoredis
import tornado.ioloop
from tornado import gen

__author__ = 'f0x11'

# Use the synchronous redis client to publish messages to a channel
redis_client = redis.Redis(host="127.0.0.1", port=6379)
# Create the tornadoredis.Client instance
# and use it for redis channel subscriptions

client = tornadoredis.Client()


def a(b):
    print(b)


@gen.engine
def main():
    def handle_message(msg):
        print(msg)
        if msg.kind == 'message':
            print(msg.body)
        elif msg.kind == 'disconnect':
            # Disconnected from the redis server
            pass

    yield gen.Task(client.psubscribe, "*")
    client.listen(handle_message)


if __name__ == '__main__':
    main()
    tornado.ioloop.IOLoop.instance().start()




