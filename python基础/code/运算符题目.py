"""

1. 实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）。

2. 猜年龄游戏
   要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。

3. 猜年龄游戏升级版
   要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
"""
print("第一道题目".center(20, "*"))
#
print("xxx用户登录系统")
# count = 0
# user = "feifeifei"
# password = "123de"
# while count < 3:
#     name_input = input("请输入用户名:")
#     passwd_input = input("请输入密码:")
#     if name_input == user and passwd_input == password:
#         print(f"登录成功，欢迎{name_input}登录")
#         break
#     else:
#         print("登录失败")
#         count += 1
#         print(f"剩余{3 - count}次机会")


print("第二道题目".center(20, "*"))
# print("猜年龄游戏")
# count = 0
# age = 20
# while count < 3:
#     age_input= int(input("请输入你猜的年纪:"))
#     if age_input == age:
#         print("恭喜你猜对了")
#         break
#     else:
#         count +=1

# print("第三道题目".center(20, "*"))
# print(
#     "要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。")
# #
# print("猜年龄游戏升级版")
# count = 0
# age = 20
# while count < 3:
#     age_input = int(input("请输入你猜的年纪:"))
#     if age_input == age:
#         print("恭喜你猜对了")
#         break
#     else:
#         count += 1
#         if count > 2:
#             next_input = input("是否需要继续如果要继续输入y")
#             if next_input == "Y":
#                 print("xxx")
#                 count = 0

print("猜年龄游戏升级版版本2")
count = 0
age = 22
while count < 3:
    count += 1
    age_input = int(input("请输入你猜的年纪:"))
    if age_input == age:
        print("恭喜你猜对了")
        break
    else:
        print("猜错了")
    if count == 3:
        choice = input("是否需要继续(y/n)")
        if choice == "N":
            break
        elif choice == "y":
            count = 0
        else:
            print("内容输入错误")
            break
