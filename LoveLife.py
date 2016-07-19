__author__ = 'zhangxp'
#LoveLife主程序
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import base64,uuid
import yaml
import controller.home
import sys


# 定义基本信息
from tornado.options import define,options
define('port', default=8002, help='give a port!', type=int)
define('host', default='127.0.0.1', help='localhost')
define('url', default=None, help='The Url Show HTML')
define('config', default = "./config.yaml", help="config file's full path")

tornado.options.parse_command_line()
if not tornado.options.options.url:
	tornado.options.options.url = "http://%s:%d" % (tornado.options.options.host, tornado.options.options.port)

handlers = [
        (r'/', controller.home.HomeHandler),
        ]
settings = {
    'base_url':options.url,
    'config_filename':options.config,
    'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    "xsrf_cookies": True,
    'template_path': 'templates',
    'static_path': 'static',
}
config = {}
try:
    with open(settings["config_filename"], "r") as fin:
        config = yaml.load(fin)
    for k, v in config["global"].items():
        settings[k] = v
    if "session" in config:
        settings["session"]["driver_settings"] = config["session"]
except:
	print ("cannot found config.yaml file")
	sys.exit(0)

# 应用程序基础类
class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
   app = Application();
   http_server = tornado.httpserver.HTTPServer(app)
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()








