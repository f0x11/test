# -*- coding: utf-8 -*-
__author__ = 'f0x11'

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("cms/topic_gallery.html")

    def post(self):
        print self


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print self
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
        for i in xrange(len(self.request.files)):
            tmp_file = self.request.files[("file[%s]" % i)][0]
            file_list.append(tmp_file['filename'])

            with open(os.path.join('images', tmp_file['filename']), 'w+') as fp:
                fp.write(tmp_file['body'])

        print file_list
        self.finish()
        return


class ManageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('cms2/message_system.html')


if __name__ == "__main__":
    print __file__
    settings = {
        "static_path": '/Users/lhfu/source/git_res_work/shitouren-qmap-server/app/static',
        'template_path': '/Users/lhfu/source/git_res_work/shitouren-qmap-server/app/templates',
        'debug': True,
    }

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/upload', UploadHandler),
        (r'/post', NewNoteHandler),
        (r'/api/note/post', NewNoteHandler),
        (r'/manage', ManageHandler),
    ], **settings)

    application.listen(9999, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
