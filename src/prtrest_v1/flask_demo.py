#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/28 10:57
# @author: Mrwhite
# @File:flask_demo.py
# @DESC:

import flask,json
from flask import request

#创建一个服务，将当前这个python文件作为一个服务
server = flask.Flask(__name__)
#使用装饰器@server.route()可以将普通的函数转换为服务登录的路径、请求方法
@server.route('/login',methods=['get','post'])
def login():
    #获取url请求传递的数据
    username = request.values.get('username')
    #获取url请求传递密码、明文
    pwd = request.values.get('pwd')
    #判断用户名、密码都不能为空
    if username and pwd:
        if username=='xiaoming' and pwd =='111':
            resu={'code':200,'message':'登录成功'}
            return json.dumps(resu,ensure_ascii=False) #将字典转换为json
        else:
            resu = {'code':-1,'message':'账户密码错误'}
            return json.dumps(resu,ensure_ascii=False)
    else:
        resu={'code': 1001, 'message': '登录成功'}
        return json.dumps( resu, ensure_ascii=False )

if __name__ == '__main__':
    server.run(debug=True,port=8888,host='0.0.0.0')#指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问