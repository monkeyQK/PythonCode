# -*- coding:utf-8 -*-


url_list = []


def read_big_txt(n):
    path = 'D:\\work\\test.txt'
    with open(path, 'r') as f:
        f.read(2)
        for i in range(1,2000001):
            #读取50个字符
            ret = f.read(50)
            #url_list.append(ret)
            if i == 2000000:
                print(ret)
        #print(url_list)
            
  
read_big_txt(99)     


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
