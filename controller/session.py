__author__ = 'zhangxp'
import uuid
import hmac
import ujson
import hashlib
import redis

# session异常处理类
class InvalidSessionException(BaseException):
    pass

# session数据
class SessionData(dict):
    def __init__(self, session_id, hmac_key):
        self.session_id = session_id
        self.hmac_key = hmac_key

# session主类
# 成员变量
# session_manager 通过redis存取session数据的.
# request_handler tornado的ReuqestHandler类
# session_id session_id
# hmac_key hmac_key
# Session[key] = data 获取session数据的方法
# 方法
# save保存session更改到redis
class Session(SessionData):
    def __init__(self, session_manager, request_handler):
        self.session_manager = session_manager
        self.request_handler = request_handler
        try:
            current_session = session_manager.get(request_handler)
        except InvalidSessionException:
            current_session = session_manager.get()
        for key,data in current_session.items():
            self[key] = data
        self.session_id = current_session.session_id
        self.hmac_key = current_session.hmac_key
    def save(self):
        self.session_manager.set(self.request_handler, self)

# session管理器
class SessionManager(object):
    def __init__(self, secret, store_options, session_timeout):
        self.secret = secret
        self.session_timeout = session_timeout
        try:
            if store_options['redis_pass']:
                self.redis = redis.StrictRedis(host=store_options['redis_host'], port=store_options['redis_port'], password=store_options['redis_pass'])
            else:
                self.redis = redis.StrictRedis(host=store_options['redis_host'], port=store_options['redis_port'])
        except Exception as e:
            print (e)
    def _fetch(self, session_id):
        try:
            session_data = raw_data = self.redis.get(session_id)
            if raw_data != None:
                self.redis.setex(session_id, self.session_timeout, raw_data)
                session_data = ujson.loads(raw_data)
            if type(session_data) == type({}):
                return session_data
            else:
                return {}
        except IOError:
            return {}
    # 获取一个session
    def get(self, request_handler = None):
        print('get')
        # 如果tornado request_handler不存在,置session数据为空;否则,通过request_handler的get_secure_cookie方法
        # 获取cookie中设置的session_id, 认证key
        if (request_handler == None):
            session_id = None
            hmac_key = None
        else:
            session_id = request_handler.get_secure_cookie("session_id")
            hmac_key = request_handler.get_secure_cookie("verification")
        # 如果session_id不存在,产生一个新的session_id,hmac_key
        if session_id == None:
            print('session_id none')
            session_exists = False
            session_id = self._generate_id()
            hmac_key = self._generate_hmac(session_id)
            print('error')
        else:
            session_exists = True
        check_hmac = self._generate_hmac(session_id)
        # 校验hmac_key,校验出错抛出异常
        if hmac_key != check_hmac:
            raise InvalidSessionException()
        session = SessionData(session_id, hmac_key)
        # 对于存在的session_id,从redis获取session数据
        if session_exists:
            print('session_exists')
            session_data = self._fetch(session_id)
            for key, data in session_data.iteritems():
                session[key] = data
        return session

    # 设置一个session,存入redis数据库
    def set(self, request_handler, session):
        request_handler.set_secure_cookie("session_id", session.session_id)
        request_handler.set_secure_cookie("verification", session.hmac_key)
        session_data = ujson.dumps(dict(session.items()))
        self.redis.setex(session.session_id, self.session_timeout, session_data)

    # session_id产生算法
    def _generate_id(self):
        print('gener id')
        new_id = hashlib.sha256((self.secret + str(uuid.uuid4())).encode('utf8'))
        print('new_id')
        return new_id.hexdigest()
    # session_hmac产生算法
    def _generate_hmac(self, session_id):
        print('new hmac')
        return hmac.new(b'session_id', b'self.secret', hashlib.sha256).hexdigest()





