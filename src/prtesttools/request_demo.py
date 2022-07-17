#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/18 23:11
# @author: Mrwhite
# @File:request_demo.py
# @DESC:

import requests
import os
import configparser

def get_json_value():
    conf = configparser.ConfigParser()
    #路径中使用斜杠不要使用反斜杠
    path =  os.path.abspath("data.conf")
    #加载配置文件
    conf.read(path)
    #读取配置
    url = conf.get("interface","url")
    response=requests.post(url)
    data=response.json()["data"]["name"]
    return data

if __name__=="__main__":
    data=get_json_value()
    print(data)



