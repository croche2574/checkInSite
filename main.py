import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
import pymysql



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/index.html')

class DashHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/dashboard.html')

class Application(tornado.web.Application): 
    def __init__(self):

        

        handlers = [
            (r'/dashboard', DashHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "static"}),
            
            (r'/', IndexHandler),
        ]
        settings = {
            "debug": True,
            
        }
        tornado.web.Application.__init__(self, handlers, **settings)



if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()