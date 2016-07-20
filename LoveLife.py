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
import motor
import controller.session


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
    #session redis配置
    'session_secret':"3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
    'session_timeout':60,
    'store_options':{
            'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': ''
        }
}

# 从config.yaml中读取配置信息
config = {}
try:
    with open(settings["config_filename"], "r") as fin:
        config = yaml.load(fin)
    for k, v in config["global"].items():
        settings[k] = v
    if "session" in config:
        for key, data in config["session"].items():
            settings[k] = v
        #settings["session"]["driver_settings"] = config["session"]
except:
	print ("cannot found config.yaml file")
	sys.exit(0)

# mongodb connection
# format: mongodb://user:pass@host:port/
# database name: minos

try:
	client = motor.MotorClient(config["database"]["config"])
	database = client[config["database"]["db"]]
	settings["database"] = database
except:
	print ("cannot connect mongodb, check the config.yaml")
	sys.exit(0)



# 应用程序基础类
class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)
        # 初始化session_manager
        self.session_manager = controller.session.SessionManager(settings['session_secret'],
                                                                 settings['store_options'],
                                                                 settings['session_timeout'])


if __name__ == '__main__':
   app = Application();
   http_server = tornado.httpserver.HTTPServer(app)
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()








