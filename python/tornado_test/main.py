# -*- coding: utf-8 -*-
from flask import json

__author__ = 'f0x11'

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("cok1", 'f0x11')
        self.render("hello.html")

    def post(self):
        self.write(json.dumps({"status": 'ok', 'call': 111}))
        self.finish()



class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print(self)
        file = self.request.files['file'][0]

        file_name = file['filename']
        content_type = file['content_type']
        body = file['body']
        return


class NewNoteHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('web/note_post.html')

    def post(self):
        file_list = []
        for i in range(len(self.request.files)):
            tmp_file = self.request.files[("file[%s]" % i)][0]
            file_list.append(tmp_file['filename'])

            with open(os.path.join('images', tmp_file['filename']), 'w+') as fp:
                fp.write(tmp_file['body'])

        print(file_list)
        self.finish()
        return


class ManageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('cms2/message_system.html')

    def post(self):
        self.write(json.dumps({"status": 'ok', 'call': 111}))
        self.finish()


if __name__ == "__main__":
    print(__file__)
    settings = {
        "static_path": './static',
        'template_path': './templates',
        'debug': True,
    }

    application = tornado.web.Application([
        (r"/api/v2/auth", MainHandler),
    ], **settings)

    application.listen(9999, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
