import pandas as pd


def get_colsName(file):  # 取出标准列顺序
    name_li = []
    with open(file.encode("utf-8"), "r") as f:
        for line in f.readlines():
            name_li.append(line.strip())
            if len(name_li) == 1:
                break
    name_str = str(name_li[0]).strip(",")
    name_list = name_str.split(",")
    return name_list


def read_csv(file, columns):  # 按标准列顺序生成新的数据
    df = pd.read_csv(file)
    print(df)
    out_file = r"E:\work\1234.csv"
    # 按list列名称重新生成数据
    df.to_csv(out_file, encoding="utf-8", index=False, columns=columns)
    df_new = pd.read_csv(out_file)
    print(df_new)


def main():
    r_file = r"E:\work\right.csv"
    print("corret：{}".format(get_colsName(r_file)))
    w_file = r"E:\work\wrong.csv"
    print("incorret：{}".format(get_colsName(w_file)))
    read_csv(w_file, get_colsName(r_file))


if __name__ == '__main__':
    main()
