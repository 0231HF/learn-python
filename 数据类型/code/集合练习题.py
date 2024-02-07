'''

1. 写代码实现

   ```python
   v1 = {'alex','武sir','肖大'}
   v2 = []

   # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
   while True:
       name = input("请输入姓名(N/n退出)：")
       if name.upper() == "Q":
           break
       if name in v1:
           v2.append(name)
   	else:
           v1.add(name)
   ```

2. 下面那些值不能做集合的元素

   ```python
   ""
   0
   [11,22,33]   # 不能
   []           # 不能
   (123)
   {1,2,3}      # 不能
   ```
   可以hash的才能做集合的元素 不可hash的不能和做集合的元素

3. 模拟用户信息录入程序，已录入则不再创建。

   ```python
   user_info_set = set()

   while True:
       name = input("请输入姓名：")
       age = input("请输入年龄：")
   	item = (name,age,)
       if item in user_info_set:
           print("该用户已录入")
   	else:
       	user_info_set.add(item)
   ```

4. 给你个列表去重。
'''
v = [11, 22, 11, 22, 44455]
data = set(v)
result = list(data)
print(result)