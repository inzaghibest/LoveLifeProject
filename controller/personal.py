# 个人主页功能
__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

class PublishHandler(BaseHandler):
    def get(self, *args, **kwargs):
        cursor = yield self.db.post_category.find()
        if(cursor != None):

        self.render("Publish.html",Message="欢迎发帖")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_current_user()
        print(username)
        articleTitle = self.get_body_argument("articleName")
        print(articleTitle)
        articleText = self.get_body_argument("editor")
        print(articleText)
        # "username":发表用户姓名
        # "ArticleTitle":文章标题
        # "ArticleText":文章内容
        # "ZambisCount":赞次数
        # "CollectionCount":收藏次数
        # "Comment":[{"name":"","text":""}]
        yield self.db.user_publish.insert({"username":username,
                                           "ArticleTile":articleTitle,
                                           "ArticleText":articleText,
                                           "ZambisCount":0,
                                           "CollectionCount":0,
                                           "Comment":[{}],
                                           "PublshTime":self.get_current_time()})
        self.render("Publish.html",Message = "发表成功!")



