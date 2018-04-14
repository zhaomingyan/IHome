# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis


app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #设置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
