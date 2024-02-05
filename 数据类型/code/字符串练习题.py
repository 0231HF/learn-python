"""
1. 请用代码实现如下进制的转换。

   ```python
   v1 = 675          # 请将v1转换为二进制（字符串类型）。

   v2 = "0b11000101" # 请将二进制v2转换为十进制（整型）

   v3 = "11000101"   # 请将二进制v3转换为十进制（整型）
   ```

2. 按要求实现

   > 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，然后将两个二进制拼接起来，最终再转换为整型（十进制）。
   >
   > 例如：
   >
   > ​		123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011"
   >
   > ​		456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"
   >
   > ​		将两个二进制拼接起来的值为："1111011111001000"，再将此值转换为整型为：63432

3. 按要求实现

   > 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，再补足为2个字节（16位），然后将两个二进制拼接起来，最终再转换为整型（十进制）。
   >
   > 例如：
   >
   > ​		123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011" ，补足16位为  "00000000 01111011"
   >
   > ​		456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"，，补足16位为  "00000001 11001000"
   >
   > ​		将两个二进制拼接起来的值为："00000000 0111101100000001 11001000"，再将此值转换为整型为：8061384

4. 列举你了解的那些数据类型的值转换为布尔值为False。

5. 看代码写结果：

   ```python
   if "":
       print(123)
   else:
       print(456)
   ```

   ```python
   if 0:
       print(999)
   else:
       print(666)
   ```

   ```python
   if "武沛齐":
       print(345)
   else:
       print(110)
   ```

6. 让用户输入一段文本，请实现将文本中的敏感词 `物理老师`、`化学老师`替换为 `***`，最后并输入替换后的文本。

7. 有变量name = "aleX leNb " 完成如下操作：

   - 移除 name 变量对应的值两边的空格,并输出处理结果
   - 判断 name 变量是否以 "al" 开头,并输出结果（用切片 或 startswith实现）
   - 判断name变量是否以"Nb"结尾,并输出结果（用切片 或 endswith实现）
   - 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
   - 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
   - 将name变量对应的值根据第一个"l"分割,并输出结果
   - 将 name 变量对应的值变大写,并输出结果
   - 将 name 变量对应的值变小写,并输出结果

8. 如何实现字符串的翻转？

9. 有字符串s = "123a4b5c"

   - 通过对s切片形成新的字符串 "123"
   - 通过对s切片形成新的字符串 "a4b"
   - 通过对s切片形成字符串 "c"
   - 通过对s切片形成字符串 "ba2"

10. 使用while循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。

11. 使用for循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。

12. 使用for循环和range实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行倒叙输出。

13. 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。

14. 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。

"""




name = "aleX leNb "
print(name.strip())
print(name.startswith("al"))

print(name.endswith("Nb"))
print(name.replace("l","p"))
print(name.split("l"))
print(name.split("l",1))
print(name.upper())
print(name.lower())



print('''
9. 有字符串s = "123a4b5c"

   - 通过对s切片形成新的字符串 "123"
   - 通过对s切片形成新的字符串 "a4b"
   - 通过对s切片形成字符串 "c"
   - 通过对s切片形成字符串 "ba2"
''')
s = "123a4b5c"

print(s[0:3])
print(s[3:6])
print(s[-1])
print(s[-3::-2])
print(s[::-1])

message = "伤情最是晚凉天，憔悴厮人不堪言"



print("10")
count =0
while count < len(message):
    print(message[count])
    count+=1
print('''
11
''')

for i  in message:
    print(i)


print('''
12. 使用for循环和range实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行倒叙输出。
''')
# message = "伤情最是晚凉天，憔悴厮人不堪言"
for i in range(len(message)-1,-1, -1):
    print(message[i])

print('''
13. 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
''')
for i in range(3, 0, -1):
    print(f"倒计时{i}秒")

print("计算用户输入文件中浪 出现的次数")
# context_data=input("请输入文本:")
# print(f"这个文本中出现的浪的次数为{context_data.count('浪')}")
#
# print("".center(20,"-"))


"""
15. 获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）：
要求：
将num1中的的所有数字找到并拼接起来：1232312
将num1中的的所有数字找到并拼接起来：1218323
然后将两个数字进行相加。

"""
# num1 = input("请输入：") # asdfd123sf2312
# num2 = input("请输入：") # a12dfd183sf23
# # 请补充代码
# num1_list =[]
# num2_list =[]
# for i in range(len(num1)):
#     if num1[i].isdecimal():
#         num1_list.append(num1[i])
#     else:
#         pass
# for i in range(len(num2)):
#     if num2[i].isdecimal():
#         num2_list.append(num2[i])
#     else:
#         pass
#
# print(f'{int("".join(num1_list))+ int("".join(num2_list))}')
