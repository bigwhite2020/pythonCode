import  time
#当前时间戳格式
# t = str(round(time.time() * 1000))
# print(t)

#当前日期格斯
# date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(date,type(date))

#时间戳转日期格式
# 时间戳转日期格式
# def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
#     time_array = time.localtime( time_stamp / 1000 )
#     str_date = time.strftime( format_string, time_array )
#     return str_date
# a = 1622392855001
# print(a,type(a))
# print(timestamp_to_date(a))

# 字符类型的时间
#将时间字符串转换为10位时间戳，时间字符串默认为2017-10-01 13:37:04格式
# def date_to_timestamp(date, format_string="%Y-%m-%d %H:%M:%S"):
#     time_array = time.strptime(date, format_string)
#     time_stamp = int(time.mktime(time_array))
#     return time_stamp
# print(date_to_timestamp("2017-10-01 13:37:04"))

#测试长度
print(len("12312343"))