"""
1. 计算整型50乘以10再除以5的商并使用print输出。

2. 判断整型8是否大于10的结果并使用print输出。

3. 计算整型30除以2得到的余数并使用print输出。

4. 使用字符串乘法实现 把字符串”我爱我的祖国”创建三遍并拼接起来最终使用print输出。

5. 判断 字符串”wupeiqi”和”alex”是否相等的结果并使用print输出。

6. 判断 整型666和整型666是否相等的结果并使用print输出。

7. 判断 字符串”666”和整型666是否相等的结果并使用print输出。

8. 看代码写结果（禁止运行代码）：

   ```python
   print( int("100")*3 )
   print( int("123") + int("88") )
   print( str(111) + str(222) )
   print( str(111)*3 )
   print( int("8") > 7 )
   print( str(111) == 111 )
   print( bool(-1) )
   print( bool(0) )
   print( bool("") )
   print( bool("你好") )
   print( True == True)
   print( True == False)
   print( bool("") == bool(0) )
   ```

注意：类型转换不是改变原来值，实际在底层是新创建了一个值。例如有整数 6 ，然后使用 str(6) 转化了一下得到 “6”,实际上这个字符串”6”是依据整数6新创建的。
"""

print(50 * 10 / 5)
print(8 > 10)
print(30 % 2)
print("我爱我的祖国" * 3)
print("xxx" == "yyy")
print(666 == 666)
print(666 == "666")

print("xs------")
print(int("100") * 3)  # 300
print(int("123") + int("88"))  # 211
print(str(111) + str(222))  # 111222
print(str(111) * 3)  # 111111111
print(int("8") > 7)  # True
print(str(111) == 111)  # False
print(bool(-1))  # True
print(bool(0))  # False
print(bool(""))  # Falseß
print(bool("你好"))  # True
print(True == True)  # True
print(True == False)  # False
print(bool("") == bool(0))  # True
