# coding:utf-8
import json
# str = '{"key": "wwww", "word": "qqqq"}'
# j = json.loads(str)
# data = json.dumps(j,sort_keys=False, indent=2, separators=(',', ': '),ensure_ascii=False)
# print(data)
# print(type(data))


def json_Data_Conversion(source_str):
    j = json.loads(source_str)
    data = json.dumps( j, sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False )
    return data
str = '{"key": "wwww", "word": "qqqq"}'
print(json_Data_Conversion(str))