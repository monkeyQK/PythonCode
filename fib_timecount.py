# -*- coding:utf-8 -*-
dict_num = {}


def f(n):  # 找规律
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n > 2:
        return f(n - 1) * 2


def func(num):  # 生成规律字典
    count = 0
    for i in range(1, num + 1):
        dict_num[i] = f(i)
        count = count + dict_num[i]
        if count >= num:
            return i


while True:
    num = int(input("输入一个数："))
    print(func(num))
