"""
实现一个用户登陆系统
需要用户反复输入用户名和密码 直到正确

2、输出 1-100 内所有的奇数 偶数
3、 求1-100所有的整数和
4、输出10 -1所有数
5、循环输出10以内除以7 为整数的数 1234568910
6.循环输出 1-100所有数
"""
print("实现一个用户登陆系统")
set_username = "feifeifei"
set_password = "123"
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == set_username and password == set_password:
        print("登录成功")
        break
    else:
        continue

print("2、输出 1-100 内所有的奇数 偶数")
i = 0
print("100以内的qi数有")
while i < 100:
    i += 1
    if i % 2:
        print(i)
    else:
        pass

i = 0
print("100以内的偶数有")
while i < 100:
    i += 1
    if i % 2:
        continue
    else:
        print(i)
print("3、 求1-100所有的整数和")
i = 1
num = 0
while i < 101:
    num += i
    i += 1
print("1到 100的和为:" + str(num))

print("4、输出10 -1所有数")
i = 10
while i > 0:
    print(i)
    i -= 1
print("5、循环输出10以内除以7 为整数的数 1234568910")
i = 1
while i < 11:
    if i % 7:
        print(i)
        i += 1
    else:
        i += 1
        continue
print("6.循环输出 1-100所有数")

i = 1

while i < 101:
    print(i)
    i += 1
