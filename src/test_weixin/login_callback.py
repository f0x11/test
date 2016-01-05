# -*- coding: utf-8 -*-
__author__ = 'f0x11'


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.escape
import tornado.httpserver


class WebCallbackHandler(tornado.web.RequestHandler):
    def post(self):
        print self.request.body


class Application(tornado.web.Application):

    def __init__( self ) :
        handlers = [
            (r"/weixin/web/callback", WebCallbackHandler),
        ]

        tornado.web.Application.__init__(self, handlers)

def main( p_port ) :
    if p_port == 0 :
        print 'port could not be set as 0'
        exit( 1 )
    app = Application()
    app.listen( p_port )
    tornado.ioloop.IOLoop.instance().start()


#define("port", default=8888, help="run on the given port", type=int)
port = 0
try :
    port = int( sys.argv[1].split('=')[1] )
except :
    print 'need port params'
    exit( 1 )


if __name__ == "__main__" :
    main( port )