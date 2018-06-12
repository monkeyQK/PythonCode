import requests
from bs4 import BeautifulSoup
import re


url = "http://py4e-data.dr-chuck.net/known_by_Anayah.html"
# 发送get请求
# req = requests.get(url)
# # 设置字符编码
# req.encoding = 'utf-8'
# # 存储返回内容
# ss = req.text

ss = url

print(ss)

pattern = re.compile(r"<?name>[\S]+Anayah")

res1 = re.split(r"[_.]", ss)

res0 = pattern.findall(ss)

res2 = ss[ss.rfind("Anayah"):len("Anayah") + ss.rfind("Anayah")]

res3 = ss[ss.rindex("_") + 1:ss.rindex("_") + len("Anayah") + 1]

print(res1, res2, res3)

print(res0)
