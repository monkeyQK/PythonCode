import pymssql as mssql
from xlwt import Workbook
import csv
import os
import pandas as pd


def database_config(host_i, user_i, password_i, database_i):  # 数据库配置
    try:
        conn = mssql.connect(host=host_i, user=user_i,
                             password=password_i, database=database_i,
                             charset="GBK")
        cur = conn.cursor()
    except Exception as e:
        return "0", "数据库连接失败!", "数据库连接失败!"
    if cur:
        return "1", conn, cur
    else:
        return "0", "数据库连接失败!", "数据库连接失败!"


def read_dbconfig():
    with open(r"E:/work/py_sql/dataset.ini") as f:
        config = f.readline()
        d = eval(config)
        return d["host"], d["user"], d["password"], d["database"]


def query_data(cur, sql):  # 查询数据
    # print("执行的语句为：{}".format(sql))
    print("正在查询数据>>")
    cur.execute(sql)
    cols_name = cur.description
    cols_name = list(i[0] for i in cols_name)
    # print(cols_name, type(cols_name))
    result = cur.fetchall()
    # print(type(result), type(result[0]))
    # print('总行数：' + str(cur.rowcount))
    new_result = result[::]
    # for i in new_result:
    #     print("{}".format(i))
    new_result.insert(0, tuple(cols_name))
    print("返回数据>>")
    return new_result
    # cur.close()


def read_sql(sql_file):  # 读取sql文件
    with open(sql_file, encoding='GBK', mode='r') as f:
        text = f.read()
        return text


def is_num(number):  # 判断字符是否是数字
    try:
        float(number)
        return True
    except Exception as e:
        return False


def csv_to_xlsx(input_file, xls_name):  # csv 文件转为 xls
    print("写入数据中>>")
    with open(input_file, 'r', encoding='GBK') as f:
        read = csv.reader(f)
        workbook = Workbook()
        sheet = workbook.add_sheet('sheet1')  # 创建一个sheet表格
        li = 0
        for line in read:
            # print(line)
            r = 0
            for i in line:
                # print(i)
                if is_num(i):
                    i = float(i)
                sheet.write(li, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            li = li + 1
        workbook.save(
            r'E:/work/py_sql/data/{}.xls'.format(xls_name))  # 传入文件名保存Excel
        print("写入完成>>")


def write_csv(input_file, result):  # list类型数据写入csv文件
    with open(input_file, encoding='GBK', mode='w') as f:
        for info in result:
            temp = ""
            for i in info:
                temp += str(i) + ","
            content = temp[:-1]
            f.write(content + "\n")


def del_csv(my_file):  # 删除文件
    if os.path.exists(my_file):
        # 删除文件，可使用以下两种方法。
        os.remove(my_file)
        # os.unlink(my_file)
    else:
        print('no such file:%s' % my_file)


def pd_write_xls():  # 通过pandas写入xls
    writer = pd.ExcelWriter(r'E:/work/py_sql/data/test.xls')
    df1 = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df1.to_excel(writer, 'Sheet1', index=False)
    writer.save()


def fetch_filename():  # 遍历文件
    for filename in os.listdir(r'F:/'):
        print(filename)


def fetch_sqlname():  # 遍历SQL文件
    file_dir = r'E:/work/py_sql/'
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.sql':
                file_info = (os.path.join(root, file), file)
                L.append(file_info)

    return L


def list2xls(sql_file, cur):  # list类型数据转为xls文件
    sql = read_sql(sql_file[0])
    sql = sql.format("'2018-4-1'", "'2018-5-1'")
    result = query_data(cur, sql)
    xls_name = str(sql_file[1]).replace(".sql", "")
    print("写入数据中>>")
    workbook = Workbook()
    sheet = workbook.add_sheet('sheet1')
    row = 0
    for line in result:
        cols = 0
        for i in line:
            sheet.write(row, cols, i)
            cols += 1
        row += 1
    workbook.save(
        r'E:/work/py_sql/data/{}.xls'.format(xls_name))  # 传入文件名保存Excel
    print("写入完成>>")


def main():
    host, user, password, database = read_dbconfig()
    state, conn, cur = database_config(host, user, password, database)
    if state == "1":
        print("数据库连接成功>>")
        sql_file_list = fetch_sqlname()
        for sql_file in sql_file_list:
            # list2csv2xls(sql_file, cur)
            list2xls(sql_file, cur)
        print("全部写入完毕！")
        conn.close()
    else:
        print(database_config(host, user, password, database)[1])


def list2csv2xls(sql_file, cur):
    sql = read_sql(sql_file[0])
    sql = sql.format("'2018-4-1'", "'2018-5-1'")
    result = query_data(cur, sql)
    input_file = r"E:/work/py_sql/temp.csv"
    write_csv(input_file, result)
    csv_to_xlsx(input_file, str(sql_file[1]).replace(".sql", ""))
    del_csv(input_file)


if __name__ == '__main__':
    main()
