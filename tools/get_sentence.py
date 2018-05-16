from __future__ import unicode_literals
from wxpy import *
import requests


# bot = Bot()
# bot = Bot(console_qr=2,cache_path="botoo.pkl")   　


def get_news1():

    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['note']
    return contents, translation


def send_news():
    try:
        # 你朋友的微信名称，不是备注，也不是微信帐号。 --亲爱的偏执狂
        my_friend = bot.friends().search(u'yx')[0]
        text = get_news1()[0] + "\n" * 2 + \
            get_news1()[1][:] + "\n" * 2 + "来自特哥的心灵鸡汤！"
        my_friend.send(text)
        # 每86400秒（1天），发送1次，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
        # t = Timer(86400, send_news)
        # t.start()
    except Exception:
        # 你的微信名称，不是微信帐号
        my_friend = bot.friends().search('monkeyQK')[0]
        my_friend.send(u"今天消息发送失败了")


def send_self():
    text = get_news1()[0] + "\n" * 2 + get_news1()[1][:] + \
        "\n" * 2 + "来自特哥的心灵鸡汤！"
    bot.file_helper.send(text)


if __name__ == "__main__":
    # print(get_news1()[0])
    # print(get_news1()[1][5:])
    # send_news()
    # send_self()
    text = get_news1()[0] + "\n" * 2 + get_news1()[1][:]
    print(text)

    # print(get_news1())
