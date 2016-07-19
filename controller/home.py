__author__ = 'zhangxp'
import tornado.web
class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #此处从后台数据库获取
        img_url = '/static/images/logo/header_logo.jpg'
        img_house = '/static/images/house.jpg'
        img_news = '/static/images/news.jpg'
        img_tour = '/static/images/Tourism.jpg'
        img_chat = '/static/images/Chat.jpg'
        img_hot = '/static/images/hot.jpg'
        self.render('main.html',imgurl = img_url,
                    imghouse = img_house,imgnews = img_news, imgtour = img_tour, imgchat = img_chat,
                    imghot = img_hot)
