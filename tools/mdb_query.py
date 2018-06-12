# -*- coding:utf-8 -*-

# 导入模块
import pypyodbc

# 定义conn


def mdb_conn(db_name, password=""):
    """
    功能：创建数据库连接
    :param db_name: 数据库名称6
    :param db_name: 数据库密码，默认为空
    :return: 返回数据库连接
    """
    str = 'Driver={Microsoft Access Driver (*.mdb)};PWD' + \
        password + ";DBQ=" + db_name
    conn = pypyodbc.win_connect_mdb(str)

    return conn

# 增加记录


def mdb_add(conn, cur, sql):
    """
    功能：向数据库插入数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        return False

# 删除记录


def mdb_del(conn, cur, sql):
    """
    功能：向数据库删除数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(e)

# 修改记录


def mdb_modi(conn, cur, sql):
    """
    功能：向数据库修改数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        return False

# 查询记录


def mdb_sel(cur, sql):
    """
    功能：向数据库查询数据
    :param cur: 游标
    :param sql: sql语句
    :return: 查询结果集
    """
    try:
        cur.execute(sql)
        # print("有%s条记录" % len(cur.fetchall()))
        return cur.fetchall()
        # return cur.fetchall()
    except Exception as e:
        print(e)


#     # 增
#     sql = "Insert Into " + tablename + " Values (33, 12, '天津', 0)"
#     if mdb_add(conn, cur, sql):
#         print("插入成功！")
#     else:
#         print("插入失败！")


#     # 改
#     sql = "Update " + tablename + " Set IsFullName = 1 where ID = 33"
#     if mdb_modi(conn, cur, sql):
#         print("修改成功！")
#     else:
#         print("修改失败！")


if __name__ == '__main__':
    # 需要读取的mdb路径
    pathfile = 'E:/work/data/SpirometryResult.mdb'
    # 需要读取的表
    tablename = 'Person'
    # 创建连接
    conn = mdb_conn(pathfile)
    # 打开游标
    cur = conn.cursor()

    # 定义变量
    start_time = "#2018/01/01#"
    end_time = "#2019/01/01#"
    PersonId_list = []
    SessionId_list = []
    SignalId_list = []
    PersonId_info = []
    SignalId_info = []

    # 根据时间段获取PersonId
    # sql = """SELECT PersonId FROM  Person
    # where Created>DateValue({})
    # and Created<DateValue({});
    # """.format(start_time, end_time)

    sql = """SELECT PersonId FROM  Person
    where Created>{}
    and Created<{};
    """.format(start_time, end_time)

    # sql = """SELECT Person.PersonId FROM  Person INNER JOIN Session
    # ON Session.PersonId = Person.PersonId
    # where Person.Created>DateValue({})
    # and Person.Created<DateValue({})
    # """.format(start_time, end_time)

    # print(sql)
    PersonId_info = mdb_sel(cur, sql)
    print(len(PersonId_info))

    # # 根据PersonId获取SignalId
    # for i in PersonId_info:
    #     sql = """
    #     SELECT Signal.SignalId FROM [Session] INNER JOIN Signal
    #     ON Session.SessionId = Signal.SessionId
    #     WHERE  Session.PersonId = {};""".format(i[0])
    #     # print(sql)
    #     # SignalId = mdb_sel(cur, sql)
    #     temp = mdb_sel(cur, sql)
    #     # print("temp=%s" % temp)
    #     for i in temp:
    #         SignalId_info.append(i[0])
    #     # print(len(SignalId))
    # for i in SignalId_info:
    #     sql = """SELECT Result.SignalId FROM Signal INNER JOIN Result
    #     ON Signal.SignalId = Result.SignalId
    #     WHERE Signal.SignalId ={};""".format(i)
    #     # print(sql)
    #     temp = mdb_sel(cur, sql)
    #     for i in temp:
    #         SignalId_list.append(i[0])

    PersonId_list = [PersonId[0] for PersonId in PersonId_info]
    # for i in PersonId_list:
    #     print(i)
    # SignalId_list = set(SignalId_list)

    # list2xls(sel_data, "test2")
    # 删

    # for i in SignalId_list:
    #     sql = "DELETE FROM Result where [SignalId]={}".format(i)
    #     if mdb_del(conn, cur, sql):
    #         # print("删除成功！")
    #         pass
    #     else:
    #         print("删除失败！")
    # print("删除成功！")

    # for i in SignalId_list:
    #     sql = "DELETE FROM Signal where [SignalId]={}".format(i)
    #     if mdb_del(conn, cur, sql):
    #         # print("删除成功！")
    #         pass
    #     else:
    #         print("删除失败！")
    # print("删除成功！")

    # for i in SignalId_list:
    #     sql = "DELETE FROM Session where [PersonId]={}".format(i)
    #     if mdb_del(conn, cur, sql):
    #         # print("删除成功！")
    #         pass
    #     else:
    #         print("删除失败！")
    # print("删除成功！")

    for i in PersonId_list:
        sql = "DELETE FROM Person where [PersonId]={}".format(i)
        # print(sql)
        if mdb_del(conn, cur, sql):
            # print("删除成功！")
            pass
        else:
            print("删除失败！")
    print("删除成功！")

    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
    # #     # 改
    # sql = "Update {} SET  LastName ='张三' where Created>DateValue({})".format(tablename,filed_vlaue )
    # print(sql)
    # if mdb_modi(conn, cur, sql):
    #     print("修改成功！")
    # else:
    #     print("修改失败！")
