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
import controller.base
import controller.auth
import controller.admins
import controller.proanaly
import controller.status


# 定义基本信息
from tornado.options import define,options
define('port', default=8009, help='give a port!', type=int)
define('host', default='127.0.0.1', help='localhost')
define('url', default=None, help='The Url Show HTML')
define('config', default = "./config.yaml", help="config file's full path")

tornado.options.parse_command_line()
if not tornado.options.options.url:
	tornado.options.options.url = "http://%s:%d" % (tornado.options.options.host, tornado.options.options.port)

handlers = [
        (r'^/', controller.home.HomeHandler),
    (r'^/login',controller.auth.LoginHandler),
    (r'^/register',controller.auth.RegisterHandler),
    (r'^/admins',controller.admins.AdminsHandler),
    (r'^/proanaly',controller.proanaly.ProAnalyHandler),
    (r'^/show/(.*)',controller.proanaly.ShowHandler),
    (r'^/analy',controller.admins.AnalyHandler),
    (r'^/news',controller.admins.NewsHandler),
    (r'^/newsshow',controller.home.NewsShowHandler),
    (r'^/newsdetailshow/(.*)',controller.home.NewDetailShowHandler),
    (r'^/status',controller.status.StatusHandler)
        ]
settings = {
    'base_url':options.url,
    'config_filename':options.config,
    'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    "xsrf_cookies": False,
    'template_path': 'templates',
    'static_path': 'static',
    #session redis配置
    'session_secret':str(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)),
    'session_timeout':6000,
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
# for key, data in config["session"].items():
#     print('session')
#     settings[k] = v
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
        #初始化mongodbs
        self.db = settings["database"]





if __name__ == '__main__':
   app = Application();
   http_server = tornado.httpserver.HTTPServer(app)
   http_server.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()








