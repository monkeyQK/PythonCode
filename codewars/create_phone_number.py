def create_phone_number(n): # str.join(list)  列表转字符串，列表中元素为字符串时
    return ("(%s) %s-%s") % ("".join(map(str, n[: 3])),
                             "".join(map(str, n[3: 6])), "".join(map(str, n[6:])))


def create_phone_number_god(n): # 使用{}.format格式 使用*n 解包传入参数
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
