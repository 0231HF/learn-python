'''


1. 根据需求写代码

   ```python
   dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

   # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
   # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
   # 请在k3对应的值中追加一个元素 44，输出修改后的字典
   # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
   ```

2. 根据需求写代码

   ```python
   dic1 = {
    'name':['alex',2,3,5],
    'job':'teacher',
    'oldboy':{'alex':['python1','python2',100]}
   }

   # 1，将name对应的列表追加⼀个元素’wusir’。
   # 2，将name对应的列表中的alex全变成大写。
   # 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
   # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
   ```

3. 循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）

   ```python
   例如：用户输入 x1|wupeiqi ,则需要再字典中添加键值对 {'x1':"wupeiqi"}
   ```

4. 判断以下值那个能做字典的key ？那个能做集合的元素？

   - 1
   - -1
   - ""
   - None
   - [1,2]
   - (1,)
   - {11,22,33,4}
   - {'name':'wupeiq','age':18}

5. 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：

   ```python
   key_list = []
   value_list = []
   info = {'k1':'v1','k2':'v2','k3':'v3'}
   ```

6. 字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

   ```python
   a. 请循环输出所有的key
   b. 请循环输出所有的value
   c. 请循环输出所有的key和value
   ```

7. 请循环打印k2对应的值中的每个元素。

   ```python
   info = {
       'k1':'v1',
       'k2':[('alex'),('wupeiqi'),('oldboy')],
   }
   ```

8. 有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....}

9. 写代码

   ```python
   """
   有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。

      result = {'k1':[],'k2':[]}
   """
   ```

10. 输出商品列表，用户输入序号，显示用户选中的商品

    ```python
    """
    商品列表：
      goods = [
    		{"name": "电脑", "price": 1999},
    		{"name": "鼠标", "price": 10},
    		{"name": "游艇", "price": 20},
    		{"name": "美女", "price": 998}
    	]
    要求:
    1：页面显示 序号 + 商品名称 + 商品价格，如：
          1 电脑 1999
          2 鼠标 10
    	  ...
    2：用户输入选择的商品序号，然后打印商品名称及商品价格
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入Q或者q，退出程序。
    """
    ```
'''

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic.setdefault("k4", "v4")
print(dic)
dic.update({"k1": "alex"})
print(dic)
dic.get("k3").append(44)
print(dic)
dic.get("k3").insert(0, 18)
print(dic)
print("".center(30, "-"))
dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}

# 1，将name对应的列表追加⼀个元素’wusir’。
# 2，将name对应的列表中的alex全变成大写。
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
dic1.get('name').append("wusir")
dic1.get('name')[0] = dic1.get('name')[0].upper()
print(dic1)
dic1.get('oldboy').setdefault("男孩", "linux")
dic1.get('oldboy').update({"男孩sxs": "linuxxasx"})

print(dic1)
dic1.get('oldboy').get("alex").remove("python2")
print(dic1)

# print(" 循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）")
# new_dict = {}
# while True:
#     contxt =input("请输入内容:")
#     if contxt.upper() == "N":
#         break
#     else:
#         new_dict.update({contxt.split("|")[0]:contxt.split("|")[1]})
#
# print(new_dict)

key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key,vakue in info.items():
        key_list.append(key)
        value_list.append(vakue)

print(key_list)
print(value_list)

'''
有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....}
'''
list1= "k: 1|k1:2|k2:3  |k3 :4"
dict33 ={}
for i in list1.split("|"):
     dict33.update({i.split(":")[0].strip():int(i.split(":")[1].strip())})

print(dict33)


"""
    商品列表：
      goods = [
    		{"name": "电脑", "price": 1999},
    		{"name": "鼠标", "price": 10},
    		{"name": "游艇", "price": 20},
    		{"name": "美女", "price": 998}
    	]
    要求:
    1：页面显示 序号 + 商品名称 + 商品价格，如：
          1 电脑 1999
          2 鼠标 10
    	  ...
    2：用户输入选择的商品序号，然后打印商品名称及商品价格
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入Q或者q，退出程序。
    """

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
index=0
for i in goods:
    print(f'{index+1}\t {i.get("name")} \t{i.get("price")}')
    index +=1
while True:
    num = input("请选择商品序号,如需退出请输入Q:")
    if num.upper() == "Q":
        break
    else:
        if int(num) <= len(goods):
            good=goods[int(num)-1]
            print(f'你的选择为{good.get("name")} 价格为{good.get("price")}')
        else:
            print("输入错误")