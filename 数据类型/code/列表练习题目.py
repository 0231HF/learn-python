print('''
1. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
   ```

   - 计算列表的长度并输出
   - 列表中追加元素"seven",并输出添加后的列表
   - 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表
   - 请修改列表第2个索引位置的元素为"Kelly",并输出修改后的列表
   - 请将列表的第3个位置的值改成 "妖怪"，并输出修改后的列表
   - 请将列表 `data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li` 中，并输出添加后的列表
   - 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。
   - 请删除列表中的元素"barry",并输出添加后的列表
   - 请删除列表中的第2个元素，并输出删除元素后的列表
   - 请删除列表中的第2至第4个元素，并输出删除元素后的列表

2. 写代码，有如下列表，利用切片实现每一个功能

   ```python
   li = [1, 3, 2, "a", 4, "b", 5,"c"]
   ```

   - 通过对li列表的切片形成新的列表 [1,3,2]
   - 通过对li列表的切片形成新的列表 ["a",4,"b"] 
   - 通过对li列表的切片形成新的列表  [1,2,4,5]
   - 通过对li列表的切片形成新的列表 [3,"a","b"]
   - 通过对li列表的切片形成新的列表 [3,"a","b","c"]
   - 通过对li列表的切片形成新的列表  ["c"]
   - 通过对li列表的切片形成新的列表 ["b","a",3]

3. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
   ```

   - 将列表lis中的第2个索引位置的值变成大写，并打印列表。
   - 将列表中的数字3变成字符串"100"
   - 将列表中的字符串"tt"变成数字 101
   - 在 "qwe"前面插入字符串："火车头"

4. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   0 武沛齐
   1 景女神
   2 肖大侠
   ```

5. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   1 武沛齐
   2 景女神
   3 肖大侠
   ```

6. 写代码实现以下功能

   - 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：

     ```python
     0,汽车
     1,飞机
     2,火箭
     ```

   - 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。

7. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。

8. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：

   ```python
   [48,45,42...]
   ```

9. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

   ```python
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   ```

10. 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。

    ```python
    data = ["京1231", "冀8899", "京166631", "晋989"]
    ```
''')

print('''
写代码，有如下列表，按照要求实现每一个功能。

   ```python
   li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
   ```

   - 计算列表的长度并输出
   - 列表中追加元素"seven",并输出添加后的列表
   - 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表
   - 请修改列表第2个索引位置的元素为"Kelly",并输出修改后的列表
   - 请将列表的第3个位置的值改成 "妖怪"，并输出修改后的列表
   - 请将列表 `data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li` 中，并输出添加后的列表
   - 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。
   - 请删除列表中的元素"barry",并输出添加后的列表
   - 请删除列表中的第2个元素，并输出删除元素后的列表
   - 请删除列表中的第2至第4个元素，并输出删除元素后的列表
''')
li = ["alex", "WuSir", "ritian", "barry"]
print(len(li))
li.append("seven")
print(li)
li.insert(1, "Tony")
print(li)
li[2] = "kelly"
print(li)
li[3] = "妖怪"

print(li)
data = [1, "a", 3, 4, "heart"]
li.extend(data)
print(li)
s = "qwert"
s_li = str(s)
li.extend(s_li)
print(li)
li.extend(s)
print(li)
li.remove("barry")
print(li)
c = li.pop(1)
print(c)
print(li)
del li[2:4]
print(li)

print("".center(30, "-"))
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
'''

   - 将列表lis中的第2个索引位置的值变成大写，并打印列表。
   - 将列表中的数字3变成字符串"100"
   - 将列表中的字符串"tt"变成数字 101
   - 在 "qwe"前面插入字符串："火车头"
'''
lis[2] = lis[2].upper()
print(lis)
index = lis.index(3)
lis[index] = 100
print(lis)
print(3 in lis[3][2][1])
lis[3].insert(0, "火车头")
print(lis)

users = ["武沛齐", "景女神", "肖大侠"]
for i in range(len(users)):
    print(f"{i + 1} {users[i]}")

'''
6. 写代码实现以下功能

   - 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：

     ```python
     0,汽车
     1,飞机
     2,火箭
     ```

   - 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
'''

goods = ['汽车', '飞机', '火箭']
print("您可选择的商品为")
for i in range(len(goods)):
    print(f"{i} {goods[i]}")

user_index = int(input("请输入你呀呀哦选择的商品编号:"))
print(f"你选择的商品为{goods[user_index]}")
goods.pop(user_index)
print("剩余商品信息如下:")
for i in range(len(goods)):
    print(f"{i} {goods[i]}")

'''
7. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
'''
l = []
for i in range(51):
    if i % 3 == 0:
        l.append(i)

print(l)

'''
8. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：

   ```python
   [48,45,42...]
   ```
'''
l = []
for i in range(51):
    if i % 3 == 0:
        l.insert(0,i)

print(l)

'''
9. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

   ```python
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   ```

10. 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。

    ```python
    data = ["京1231", "冀8899", "京166631", "晋989"]
    ```
'''
data = ["京1231", "冀8899", "京166631", "晋989"]
count =0
for i in data:
    if "京" in i:
        count +=1
print(f"京牌车辆的数量为{count}")

li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
new_l=[]
for i in li:
    if i.strip().startswith("a"):
        new_l.append(i.strip())

print(new_l)