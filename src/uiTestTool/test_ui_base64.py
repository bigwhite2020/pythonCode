import base64
#加密
url = "https://www.cnblogs.com/songzhixue/"
bytes_url = url.encode("utf-8")
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
print(str_url)
print(type(str_url))
#byte转string
print(bytes.decode(str_url))

#解密
# 将base64解码成字符串
url = "aHR0cHM6Ly93d3cuY25ibG9ncy5jb20vc29uZ3poaXh1ZS8="
str_url = base64.b64decode(url).decode("utf-8")
print(str_url)

#'https://www.cnblogs.com/songzhixue/'