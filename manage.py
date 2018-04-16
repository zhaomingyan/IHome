# coding=utf-8
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    #设置SECRET_KEY
    SECRET_KEY = '9Cz8jQvxZINyp7hXX5YnUvlo2tztLTqg0tl4kbC20NBbvLzl7x5UpBY0xDgkhwCO'
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #设置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    #设置session存储到ridis中
    SESSION_TYPE = 'redis'
    #设置存储session的redis地址
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    #设置session的信息加密
    SESSION_USE_SIGNER = True
    #设置session 的过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

#csrf开启保护
CSRFProtect(app)

#session存储
Session(app)


@app.route('/')
def index():
    #测试session
    # session['name'] = 'zhao'
    return 'index'


if __name__ == '__main__':
    app.run()
