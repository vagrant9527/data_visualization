#absolute_import:解决搜索路径的问题，引入标准模块
#division：解决2×版本和3×版本中除法不同的问题
#print_function：解决2×版本和3×版本中print不同的问题
#unicode_literals：python库中有些接口参数要求是str类型，有些是unicode类型。这里是将模块中显式出现的所有字符串转为unicode类型
#https://zhuanlan.zhihu.com/p/32756176

#urllib方法下载文件
from __future__ import  (absolute_import,division,print_function,unicode_literals)
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import json
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response=urlopen(json_url)
# #读取数据
# req=response.read()#byte格式
# #将数据写入文件
# with open('btc_close_urllib.json','wb') as f: #写入二进制文件
#     f.write(req)
# #加载json格式
# file_urllib = json.loads(req.decode('utf8'))#这里将文件内容转换为python能够处理的格式。file_urllib是一个list
# print(type(file_urllib))
# print(file_urllib)


#request方法下载文件
#req.text属性能够直接读取文件内容，返回的格式是字符串。
#req.json能转换成python列表
req=requests.get(json_url)
with open('btc_close_2017_request.json','w') as f:
    f.write(req.text)
file_requests=req.json()
print(type(req))
print(type(file_requests))

