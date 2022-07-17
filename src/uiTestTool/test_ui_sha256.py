import hashlib
text='123'
sha256=hashlib.sha256()
sha256.update(text.encode('utf-8'))
res=sha256.hexdigest()
print(res)
