#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/25 23:38
# @author: Mrwhite
# @File:mysql_demo.py
# @DESC:
import configparser
import os

#读取配置
#conf=configparser.ConfigParser()
conf=configparser.RawConfigParser()

# 路径中使用斜杠不要使用反斜杠
path=os.path.abspath( "data.conf" )
# 加载配置文件
conf.read( path)
# 读取配置
host=conf.get( "mysql", "host" )
user=conf.get( "mysql", "user" )
password=conf.get( "mysql", "password" )
database=conf.get( "mysql", "database" )

print(password)