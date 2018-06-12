from __future__ import unicode_literals

import requests


def get_news1():

    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['note']
    return contents, translation


if __name__ == "__main__":
    # print(get_news1()[0])
    # print(get_news1()[1][5:])
    # send_news()
    # send_self()
    text = get_news1()[0] + "\n" * 2 + get_news1()[1][:]
    print(text)

