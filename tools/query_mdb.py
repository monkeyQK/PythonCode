import win32com.client
import os
import shutil


def connent_mdb():
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    PROVIDER = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;'
    DATA_SOURCE = r'DATA SOURCE = E:/work/data/SpirometryResult.mdb'
    DSN = PROVIDER + DATA_SOURCE
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    return conn, rs


def read_mdb(conn, rs):
    rs_name = 'Person'
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()  # 光标移到首条记录
    count = 0
    while True:
        if rs.EOF:
            break
        else:
            # print("第%s条记录" % count)
            for i in range(rs.Fields.Count):
                # 字段名：字段内容
                # if rs.Fields[i].Name.strip() == 'Created' and str(rs.Fields[i].Value)[:11] > '2018-06-01':
                if rs.Fields[i].Name.strip() == 'LastName' and str(rs.Fields[i].Value) == '张顺华':
                    print(rs.Fields[i].Name, "：",
                          rs.Fields[i].Value, type(rs.Fields[i].Value))

                    count += 1
        rs.MoveNext()
    print("共有%s条记录" % count)


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def main():
    # srcfile = 'E:/work/data/SpirometryResult.mdb'
    # dstfile = 'E:/work/data/SpirometryResult_cold.mdb'
    # mycopyfile(srcfile, dstfile)
    read_mdb()


def add_data(conn, table_name):
    # 增
    # sql语句
    sql = "Insert Into " + table_name + \
        " (id, innerserial, mid) Values ('002133800088980002', 2, '21338')"
    conn.Execute(sql)  # 执行sql语句


def del_data(conn, rs, table_name):
    # 删
    # help(pywintypes.datetime)
    # end_time = pywintypes.datetime("2018-01-01")
    start_time = "'2015-10-09'"
    end_time = "'2015-10-10'"
    # rs.Open('[' + table_name + ']', conn, 1, 3)
    sql = "DELETE FROM {} where Created>DateValue({}) and Created<DateValue({})".format(
        table_name, start_time, end_time)
    print(sql)
    conn.Execute(sql)


def update_data(conn, table_name):
    # 改
    sql = "Update " + table_name + " Set mid = 2016 where innerserial = 3"
    conn.Execute(sql)


if __name__ == '__main__':
    conn, rs = connent_mdb()
    table_name = 'Person'
    del_data(conn, rs, table_name)
    # read_mdb(conn, rs)
