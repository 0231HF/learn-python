import pymysql


# print("xasxsa")

def get_host_data():
    # print("xasxas")
    # 连接MySQL数据库

    #todo.. 改成从配置文件里面读取数据库相关信息
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='my-secret-pw',
        database='cmdb_test',
        charset='utf8mb4',
        # cursorclass=pymysql.cursors.DictCursor  # 以字典形式返回查询结果
    )

    try:
        with conn.cursor() as cursor:
            host_set = set()
            ip_set = set()
            # print("xsxas")
            # 执行查询语句
            sql = "select host ,ip_address from host"
            cursor.execute(sql)

            # 获取查询结果
            rows = cursor.fetchall()

            # 打印结果
            for row in rows:
                host_set.add(row[0])
                ip_set.add(row[1])
            # print(host_set)
            # print(ip_set)

    finally:
        # 关闭数据库连接
        conn.close()
    print(ip_set)
    return  ip_set

# get_host_data()