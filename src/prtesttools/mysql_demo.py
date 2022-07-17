#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/25 23:38
# @author: Mrwhite
# @File:mysql_demo.py
# @DESC:

import pymysql

#liunx开mysql服务： service mysqld start
conn = pymysql.connect(host='192.168.37.8', user='root',password='Mrwhite@2021',database='testdb',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql1 =' select * from game ;'
cursor.execute(sql1)
data=cursor.fetchall()
print('查询结果',data)