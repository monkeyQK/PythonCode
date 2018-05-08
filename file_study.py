# -*- coding:utf-8 -*-


def read_txt(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            print(line.strip())


def write_txt(path):
    with open(path, "w") as f:
        f.write("写入测试123123123123!")


def append_txt(path):
    with open(path, "a") as f:
        f.write("追加测试ABCDDE!")


path = 'e:/work/test.txt'
print("正在写入...")
write_txt(path)
print("正在读取...")
read_txt(path)
print("追加写入...")
append_txt(path)
print("正在读取...")
read_txt(path)
