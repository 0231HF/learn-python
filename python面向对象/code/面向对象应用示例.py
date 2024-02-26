"""

将数据封装刀对象中，在类的相关方法对原始数据进行加工处理 功能展示

"""

# #原来的方案
user_list = ["用户-{}".format(i) for i in range(1000)]


# #分页显示
# while True:
#     page=int(input("请输入页码:"))
#     start_index =(page-1)*10
#     end_index = page*10
#
#     page_list=user_list[start_index:end_index]
#     for item in page_list:
#         print(item)
#
class Pagination:
    def __init__(self, current_page, per_page_num=10):
        pass

    def start(self):
        pass

    def end(self):
        pass


# 分页显示
while True:
    page = int(input("请输入页码:"))
    # page 当前访问的页码
    # 10 每页显示10条数据
    # 内部执行init方法
    pg_object = Pagination(page, 10)
    pass
