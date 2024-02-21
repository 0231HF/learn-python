"""
1、从获取prometheus里面的所有的targets相关信息
2、解析mysql数据库信息


"""

import requests
from get_data_from_mysql import get_host_data

def print_targets(targets,ups,downs,all1):
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
            all1.add(labels.get("instance"))
        else:
            up_type = "异常"
            downs.add(labels.get("instance").split(":")[0])
            all1.add(labels.get("instance").split(":")[0])
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
    return  all1


def get_targets(prometheus_address):
    f_data = {}
    try:
        uri = 'http://{}/api/v1/targets'.format(prometheus_address)
        res = requests.get(uri)
        # print(res.json())
        data = res.json().get("data")
        activeTargets = data.get("activeTargets")
        droppedTargets = data.get("droppedTargets")

        ups = set()
        downs = set()
        all = set()
        c = print_targets(activeTargets,ups,downs,all)
        d =print_targets(droppedTargets,ups,downs,all)



    except Exception as e:
        print(e)
    return c


def generate_file(targets):
    # 构建文件内容
    content = f"- targets: ['{targets}:9100']\n  labels:\n    group: lxc-node"

    # 文件名，这里假设文件名为 targets.txt
    filename = f"{targets}.yaml"

    # 写入文件
    with open(filename, 'w') as file:
        file.write(content)


def generate_file_list(targets,group_name):
    # 构建文件内容
    content = "- targets:\n"
    for target in targets:
        content += f"    - ['{target}:9100']\n"
    content +=f"  labels:\n    group: {group_name}"
    # 文件名，这里假设文件名为 targets.txt
    filename = f"{group_name}.yaml"

    # 写入文件
    with open(filename, 'w') as file:
        file.write(content)


prometheu_host = get_targets("127.0.0.1:9090")
cmdb_host = get_host_data()
print(cmdb_host)

## 集合取差集
new=cmdb_host - prometheu_host
print(f'未被cmdb采集的机器有{new}')

"""
从集合中查询信息 生成prometheus配置文件
"""
#### todo..
# for i in new:
#     generate_file(i)

generate_file_list(list(new),"lxc_node")