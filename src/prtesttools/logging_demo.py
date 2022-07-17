#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/27 0:36
# @author: Mrwhite
# @File:logging_demo.py
# @DESC:


import logging
import os
import time

root_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir=os.path.join(root_dir,"logs")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)


my_logging = logging.getLogger('bktest')#创建日志收集器
my_logging.setLevel('DEBUG')#设置日志收集级别
ch =logging.StreamHandler()#输出到控制台
my_logging.setLevel('INFO')#设置日志输出级别
my_logging.addHandler(ch)#对接，添加渠道

#创建文件处理器fh，log_file为日志存放的文件夹
log_file=os.path.join(log_dir,"{}_log".format(time.strftime("%Y-%m-%d",time.localtime())))
fh = logging.FileHandler(log_file,encoding="UTF-8")
my_logging.addHandler(fh)#对接，添加渠道

#指定输出的格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息-%(message)s')
#规定日志输出的时候按照formatter格式来打印
ch.setFormatter(formatter)
fh.setFormatter(formatter)


my_logging.debug("这是一个debug的信息")
my_logging.info("这是一个info的信息")
my_logging.warning("这是一个warning的信息")
my_logging.error("这是一个error的信息")
my_logging.critical("这是一个critical的信息")
