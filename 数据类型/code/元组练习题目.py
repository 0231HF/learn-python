print('''
练习题1：判断是否可以实现，如果可以请写代码实现。

```python
li = ["alex", [11,22,(88,99,100,),33],  "WuSir",  ("ritian", "barry",),  "wenzhou"]
#        0               1                 2                3                4

# 1.请将 "WuSir" 修改成 "武沛齐"
li[2] = "武沛齐"
index = li.index("Wusir")
li[index] = "武沛齐"

# 2.请将 ("ritian", "barry",) 修改为 ['日天','日地']
li[3] = ['日天','日地']

# 3.请将 88 修改为 87
li[1][2][0] = 87 # (报错，)

# 4.请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "周周"
# li.remove("wenzhou")
# del li[-1]
li.insert(0,"周周")
```

练习题2：记住一句话：《"我儿子永远不能换成是别人，但我儿子可以长大"》

```python
data = ("123",666,[11,22,33], ("alex","李杰",[999,666,(5,6,7)]) )

# 1.将 “123” 替换成 9   报错

# 2.将 [11,22,33] 换成 "武沛齐"    报错

# 3.将 11 换成 99
data[2][0] = 99
print(data)  # ("123",666,[99,22,33], ("alex","李杰",[999,666,(5,6,7)]) )

# 4.在列表 [11,22,33] 追加一个44
data[2].append(44)
print(data) # ("123",666,[11,22,33,44], ("alex","李杰",[999,666,(5,6,7)]) )
```

练习题3：动态的创建用户并添加到用户列表中。

```python
# 创建用户 5个
# user_list = [] # 用户信息
user_list = [ ("alex","132"),("admin","123"),("eric","123") ]

while True:
    user = input("请输入用户名：")
    if user == "Q":
        brek
    pwd = input("请输入密码：")
    item = (user,pwd,)
    user_list.append(item)
    
# 实现：用户登录案例
print("登录程序")
username = input("请输入用户名：")
password = input("请输入密码：")

is_success = False

for item in user_list:
    # item = ("alex","132")   ("admin","123")    ("eric","123")
    if username == item[0] and password == item[1]:
        is_success = True
        break

if is_success:
    print("登录成功")
else:
    print("登录失败")
```

''')
