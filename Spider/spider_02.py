# -*- coding：utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

"""
下载网络小说《大主宰》
"""


class downloader(object):
    """docstring for downloader"""

    def __init__(self):
        # 爬取的根目录
        self.server = "http://www.biqukan.com/"
        # 爬取小说的目录页
        self.target = "http://www.biqukan.com/0_910/"
        # 存放章节名
        self.names = []
        # 存放章节链接
        self.urls = []
        # 存放章节数
        self.nums = 0


    def get_contents(self, target):
        # 发送get请求
        req = requests.get(url=target)
        # 返回html内容
        html = req.text
        #
        bf = BeautifulSoup(html, "html.parser")
        # 查找div标签 属性为showtxt的
        texts = bf.find_all('div', class_='showtxt')
        #替换8个空格为换行
        texts_finnal = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts_finnal

    # 获取下载地址


    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all('a')
        #设置需要下载的章节
        #self.nums = len(a[13:])#从第13章开始
        self.nums = len(a[13:24])
        for each in a[13:24]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get("href"))


    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print("《大主宰》开始下载：")
    for i in range(dl.nums):
        dl.writer(dl.names[i], "大主宰.txt", dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.2f%%" % float(i/dl.nums*100) + '\r')
        sys.stdout.flush()
print("《大主宰》下载完成！")
