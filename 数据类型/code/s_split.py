print("s_split案例")
#判断用户密码是否正确
info ="feifeifei,root" # info字符串中存储了用户名和密码用“,”分割
user_list = info.split(",") # 得到一个包含了 2 个元素的列表 ["feifeifei","root"]
user =input("请输入用户名:")
pwd=input("请输入密码:")
if user == user_list[0] and pwd == user_list[1]:
    print("登录成功")
else:
    print("登录失败")
