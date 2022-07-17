#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/29 0:29
# @author: Mrwhite
# @File:flask_post_demo.py
# @DESC:

from flask import Flask, request, jsonify
import json
import logging

my_logging = logging.getLogger('bktest')#创建日志收集器
my_logging.setLevel('DEBUG')#设置日志收集级别
ch =logging.StreamHandler()#输出到控制台
my_logging.setLevel('DEBUG')#设置日志输出级别
my_logging.addHandler(ch)#对接，添加渠道

#指定输出的格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息-%(message)s')
#规定日志输出的时候按照formatter格式来打印
ch.setFormatter(formatter)

my_logging.debug("这是一个debug的信息")
my_logging.info("这是一个info的信息")
my_logging.warning("这是一个warning的信息")
my_logging.error("这是一个error的信息")
my_logging.critical("这是一个critical的信息")

app = Flask(__name__)
app.debug = True
@app.route('/add/test',methods=['post'])
def add_stu():
    if  not request.data:   #检测是否有数据
        return ('fail')
    student = request.data.decode('utf-8')
    #获取到POST过来的数据，因为我这⾥传过来的数据需要转换⼀下编码。根据晶具体情况⽽定
    student_json = json.loads(student)
    a=student_json["key"]
    #调用数据处理的核心方法
    res=getData(a)
    my_logging.debug(f"调用getData方法获取")
    student_json["key"]=res
    #把区获取到的数据转为JSON格式。
    return jsonify(student_json)
    #返回JSON数据。

def getData(parameter):
    response = f"hello {parameter} world"
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8800)
