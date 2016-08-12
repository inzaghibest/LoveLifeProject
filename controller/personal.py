# 个人主页功能
__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

# 发帖子
class PublishHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        cursor = self.db.post_category.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
                coll = cursor.next_object()
                colls.append({})
                for k,v in coll.items():
                    colls[i][k]=v
                print(colls)
                i+=1
        self.render("Publish.html",Message="欢迎发帖",colls = colls)
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_current_user()
        print(username)
        articleTitle = self.get_body_argument("articleName")
        print(articleTitle)
        articleText = self.get_body_argument("editor")
        print(articleText)
        articleCategory = self.get_body_argument("articleCategory")
        print(articleCategory)
        # "sername":发表用户姓名
        # "ArticleTitle":文章标题
        # "ArticleText":文章内容
        # "ZambisCount":赞次数
        # "CollectionCount":收藏次数
        # "Comment":[{"name":"","text":""}]
        yield self.db.user_publish.insert({"username":username,
                                           "ArticleTile":articleTitle,
                                           "ArticleText":articleText,
                                           "ArticleCategory":articleCategory,
                                           "ZambisCount":0,
                                           "CollectionCount":0,
                                           "Comment":[{}],
                                           "PublishTime":self.get_current_time()})
        self.render("Publish.html",Message = "发表成功!",colls = self.category_colls)



