__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime
from tornado import gen
import time
# 职业数据生成接口
from extends.scrapy_tutorials.tutorials.displays import picinterfaces

#向js发送get数据,用于页面动态刷新的场景
class StatusHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        print("接受到get请求")
        requesttype = self.get_argument("requesttype")
        print(requesttype)
        if(requesttype == "checkname"):
            username = self.get_argument("username")
            print(username)
            doc_coll = yield self.db.userinfo.find_one({"username":username})
            print(doc_coll)
            msg = ""
            if(doc_coll == None):
                print("None")
                msg = ""
            else:
                print("have")
                msg = "该用户已经注册了,请换个名字吧"
            print(msg)
            self.write({"msg":msg})
        elif(requesttype == "occupation"):
            #模拟声称图片
            occupation = self.get_argument("occupation");
            print(occupation)
            #time.sleep(5)
            picinterfaces.zp_show_oneZw_gzddCounts_Bar(occupation, 'static/images/OccupationPic/%sForArea.png'%occupation)
            # 生成此职业不同经验的需求程度
            picinterfaces.zp_show_oneZw_gzjyCounts_Bar(occupation,'static/images/OccupationPic/%sForExperience.png'%occupation)
            # 生成此职业不同学历的需求程度
            picinterfaces.zp_show_oneZw_xlCounts_Bar(occupation,'static/images/OccupationPic/%sForEducation.png'%occupation)
            self.write({"msg":"success"})




