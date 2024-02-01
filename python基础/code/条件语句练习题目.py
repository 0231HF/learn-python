"""
1. 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

2. 提示⽤户输入 "feifeifei" ，判断⽤户输入的对不对。如果对, 提示真聪明, 如果不对, 提示你是傻逼么。

3. 写程序，成绩有ABCDE5个等级，与分数的对应关系如下.

   ```python
   A    90-100
   B    80-89
   C    60-79
   D    40-59
   E    0-39
   ```

   要求用户输入0-100的数字后，你能正确打印他的对应成绩等级.

"""
# print(
#     "设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。")
#
# number = int(input("请输入一个数字:"))
# ideal_data = 66
# if number == ideal_data:
#     print("猜测正确")
# elif number > ideal_data:
#     print("猜测大了")
# else:
#     print("猜测小了")

# print("2. 提示⽤户输入'feifeifei' ，判断⽤户输入的对不对。如果对, 提示真聪明, 如果不对, 提示输入错误。")
# input_data = input("请输入:")
#
# if input_data == "feifeifei":
#     print("真聪明")
# else:
#     print("输入错误")

int_score = input("请输入你的分数:")
score = int(int_score)
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("E")
