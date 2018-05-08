# -*- coding:utf-8 -*-


def word_count(arry):  # 词频统计
    word_num = {}
    for i in arry:
        if i in word_num:
            word_num[i] += 1
        else:
            word_num[i] = 1

    word_num = sorted(word_num.items(), key=lambda x: x[1], reverse=True)
    # return word_num  # 排序后返回的是tuple
    return(dict(word_num))  # 转换为字典


def read_txt(file_path):  # 读取文本
    word_arry = []
    with open(file_path.encode("utf-8"), mode='r') as f:
        for line in f.readlines():
            # print(line.strip())
            word_arry.append(line.strip())
    return word_arry


def write_txt(content):  # 写入文本
    import os
    while True:
        file_name = input('input file_name:')
        file_path = "E:\\work\\" + file_name + ".txt"
        if os.path.exists(file_path):
            print("Error:%s.txt already exists" % file_name)
        else:
            break
    file_obj = open(file_path.encode("utf-8"), 'w')
    # 分行写入
    for k, v in content.items():
        s = k + ":" + str(v)
        # print(type(s), s)
        file_obj.write("%s\n" % s)
    file_obj.close()


def main():
    file_path = "E:\\work\\test.txt"
    print("Reading txt")
    print("*" * 30)
    word_arry = read_txt(file_path)
    print("The content of txt is %s" % word_arry)
    print("Words counting")
    print("*" * 30)
    content = word_count(word_arry)
    print("Words count result is %s" % content)
    print("Write a new txt")
    print("*" * 30)
    write_txt(content)
    print("Write done!")


if __name__ == '__main__':
    main()
