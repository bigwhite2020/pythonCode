#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/28 10:57
# @author: Mrwhite
# @File:flask_demo.py
# @DESC:

from flask import Flask, request, jsonify
import json
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
    student_json["key"]=res
    #把区获取到的数据转为JSON格式。
    return jsonify(student_json)
    #返回JSON数据。

def getData(parameter):
    response = f"hello {parameter} world"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8800)