__author__ = 'zhangxp'
#LoveLife主程序
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import controller.home


from tornado.options import define,options
define('port', default=8002, help='give a port!', type=int)
define('host', default='127.0.01', help='localhost')
define('url', default=None, help='The Url Show HTML')

tornado.options.parse_command_line()
if not tornado.options.options.url:
	tornado.options.options.url = "http://%s:%d" % (tornado.options.options.host, tornado.options.options.port)

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r'/', controller.home.HomeHandler),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': 'static',
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
   app = Application();
   http_server = tornado.httpserver.HTTPServer(app)
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()








