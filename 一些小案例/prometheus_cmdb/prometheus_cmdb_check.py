"""
定时采集cmdb 和 promethsu里的监控主机信息 如果有异常就实现告警

"""
import pymysql
import requests
import socket

"""
print_targets
打印输出prometheus targets信息
"""


def print_targets(targets, ups, downs, all_host_ip):
    index = 1
    all = len(targets)
    for i in targets:
        scrapeUrl = i.get("scrapeUrl")
        state = i.get("health")
        labels = i.get("labels")
        lastScrape = i.get("lastScrape")
        lastScrapeDuration = i.get("lastScrapeDuration")
        lastError = i.get("lastError")
        if state == "up":
            up_type = "正常"
            ups.add(labels.get("instance"))
            all_host_ip.add(labels.get("instance"))
        else:
            up_type = "异常"
            downs.add(labels.get("instance").split(":")[0])
            all_host_ip.add(labels.get("instance").split(":")[0])
        msg = "状态:{} num:{}/{} endpoint:{} state:{} labels:{} lastScrape:{} lastScrapeDuration:{} lastError:{}".format(

            up_type,
            index,
            all,
            scrapeUrl,
            state,
            str(labels),
            lastScrape,
            lastScrapeDuration,
            lastError,

        )
        # print(msg)
        index += 1
    # print(f'查询正常的的tag有{ups}')
    # print(f'查询失败的tag有{downs}')
    return all_host_ip


"""
从prometheus总获取targets数据 
"""


def get_targets(prometheus_address):
    f_data = {}
    try:
        uri = 'http://{}/api/v1/targets'.format(prometheus_address)
        res = requests.get(uri)
        data = res.json().get("data")
        activeTargets = data.get("activeTargets")
        droppedTargets = data.get("droppedTargets")

        ups = set()
        downs = set()
        all_host_ip = set()
        active_ip = print_targets(activeTargets, ups, downs, all_host_ip)
        dropped_ip = print_targets(droppedTargets, ups, downs, all_host_ip)



    except Exception as e:
        print(e)
    return active_ip


def get_host_data_from_mysql():
    # print("xasxas")
    # 连接MySQL数据库

    # todo.. 改成从配置文件里面读取数据库相关信息
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
    return ip_set


"""
生成配置文件
"""


def generate_file(targets):
    # 构建文件内容
    content = f"- targets: ['{targets}:9100']\n  labels:\n    group: lxc-node"

    # 文件名，这里假设文件名为 targets.txt
    filename = f"{targets}.yaml"

    # 写入文件
    with open(filename, 'w') as file:
        file.write(content)


"""
生成配置文件2
"""


def generate_file_list(targets, group_name):
    # 构建文件内容
    content = "- targets:\n"
    for target in targets:
        content += f"    ['{target}:9100']\n"
    content += f"  labels:\n    group: {group_name}"
    # 文件名，这里假设文件名为 targets.txt
    filename = f"{group_name}.yaml"

    # 写入文件
    with open(filename, 'w') as file:
        file.write(content)


"""
将主机列表中的主机名解析为对应的IP地址，并返回一个包含所有IP地址的集合
"""
def resolve_hostnames_to_ips(hosts):
    ip_set = set()
    for host in hosts:
        try:
            ip = socket.gethostbyname(host)
            ip_set.add(ip)
        except socket.error as e:
            print(f"Error resolving hostname {host}: {str(e)}")
    return ip_set

"""
开始执行监控程序
"""
prometheu_host = get_targets("127.0.0.1:9090")
# cmdb_host = get_host_data_from_mysql()
# print(cmdb_host)
ips = resolve_hostnames_to_ips(prometheu_host)


## 集合取差集
# new=cmdb_host - prometheu_host
print(f'prometheus监控的主机数据有{ips}')
