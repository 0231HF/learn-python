"""
1. 写代码实现判断用户输入的值否以 "al"开头,如果是则输出 "是的" 否则 输出 "不是的"

2. 写代码实现判断用户输入的值否以"Nb"结尾,如果是则输出 "是的" 否则 输出 "不是的"

3. 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果

4. 写代码实现对用户输入的值判断，是否为整数，如果是则转换为整型并输出，否则直接输出"请输入数字"

5. 对用户输入的数据使用"+"切割，判断输入的值是否都是数字？
   提示：用户输入的格式必须是以下+连接的格式，如 5+9 、alex+999

6. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）

7. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5 +9或5+ 9或5 + 9，计算出两个值的和（提示：先分割再去除空白、再转换为整型，再相加）

"""
print('写代码实现判断用户输入的值否以 "al"开头,如果是则输出 "是的" 否则 输出 "不是的"')
# input_data=input("请输入值:")
# if input_data.startswith("al"):
#     print("是的")
# else:
#     print("不是的")

print('2. 写代码实现判断用户输入的值否以"Nb"结尾,如果是则输出 "是的" 否则 输出 "不是的"')
# input_data=input("请输入值:")
# if input_data.endswith("No"):
#     print("是的")
# else:
#     print("不是的")

print('3. 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果')
name = "xsaxsdflaxldxalsxsa;a"
print(name.replace("l", "p"))

print('4. 写代码实现对用户输入的值判断，是否为整数，如果是则转换为整型并输出，否则直接输出"请输入数字"')
# input_data=input("请输入值:")
# if input_data.isdecimal():
#     print(int(input_data))
# else:
#     print("请输入数字")


print('''
对用户输入的数据使用"+"切割，判断输入的值是否都是数字？
   提示：用户输入的格式必须是以下+连接的格式，如 5+9 、alex+999
''')
#
# input_data=input("请按照规定输入:")
# list_data=input_data.split("+")
# for i in range(0,len(list_data)):
#
#     if list_data[i].isdecimal():
#         continue
#     else:
#         print("输入不都是数字")
#         break

print('''
6. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）
''')
print("整数加法计算器")
# str_data=input("请输入要计算的式子")
# list_data=str_data.split("+")
# count=0
# for i in range(0,len(list_data)):
#     count+=int(list_data[i])
#
# print(f"计算的结果为{count}")


print('''

7. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5 +9或5+ 9或5 + 9，计算出两个值的和（提示：先分割再去除空白、再转换为整型，再相加）
''')
print("计算器升级版")
#
# str_data=input("请输入要计算的式子")
# list_data=str_data.split("+")
# count=0
# for i in range(0,len(list_data)):
#     count+=int(list_data[i].strip())
#
# print(f"计算的结果为{count}")
# # """
# 补充代码实现用户认证。
# 需求：提示用户输入手机号、验证码，全都验证通过之后才算登录成功（验证码大小写不敏感）
# """
import random

# code = random.randrange(1000, 9999)  # 生成动态验证码
# msg = "欢迎登录PythonAV系统，您的验证码为：{},手机号为：{}".format(code, "15131266666")
# print(msg)
# # 请补充代码
# mobile_phone_number =input("请输入你的手机号码:")
# code_in = input("请输入你的验证码:")
#
# if code==int(code_in) and mobile_phone_number == "15131266666":
#     print("登录 chengg")
# else:
#     print("登录失败 请重新登录")
"""
补充代码实现数据拼接
"""
data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby)
    # 将所有的爱好通过符号 "、"拼接起来并输出
hobby_str='、'.join(data_list)
print("爱好是"+hobby_str)