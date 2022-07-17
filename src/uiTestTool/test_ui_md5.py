import hashlib
#加密
#m = hashlib.md5()
data='123'
#m.update(b'123')
m1=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
print(m1)
#解密


#202cb962ac59075b964b07152d234b70