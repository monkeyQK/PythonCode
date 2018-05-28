import pymysql.cursors

conn = pymysql.connect(host='192.168.3.11', port=3306, user='root',
                       password='12345678', db='ITIL', charset='utf8mb4')


def insert_data():
    cursor = conn.cursor()
    sql = "insert into user (id,user_name) values('002','李四')"
    cursor.execute(sql)
    conn.commit()


def del_data():
    try:
        cursor = conn.cursor()
        sql = "delete from  user where id='002'"
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)


def query_data():
    try:
        cursor = conn.cursor()
        sql = "select * from  user"
        cursor.execute(sql)
        result = cursor.fetchall()
        # result = cursor.fetchone()
        # print(result)
        for i in result:
            print(i)
        conn.commit()
        # conn.close()
    except Exception as e:
        print(e)


def create_table():
    try:
        cursor = conn.cursor()
        sql = """create table user(id varchar(50),user_name varchar(50),
        password varchar(50),phone varchar(50))"""
        cursor.execute(sql)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def update_data():
    try:
        cursor = conn.cursor()
        sql = "update user set phone='123456' where id='002'"
        # print(sql)
        cursor.execute(sql)
        conn.commit()
        # conn.close()
    except Exception as e:
        print(e)


def main():
    insert_data()
    # query_data()
    # update_data()
    # del_data()
    query_data()
    conn.close()


if __name__ == '__main__':
    main()
