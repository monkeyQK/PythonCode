#如果有pip，直接pip install request.
#如果没有，先下载源码包，解压到python目录下后进入，找到setup.py，然后python setup.py install

import requests

url = 'http://www.zhidaow.com'

# 发送get请求
r = requests.get(url)
# 请求返回值
print(r.status_code)
# 文件头
print(r.headers['content-type'])
# 字符编码
print(r.encoding)
# 返回html内容
print(r.text)
