# 花色列表
color_list = ["红桃", "黑桃", "方片", "梅花"]

# 牌值
num_list = []
for num in range(1, 14):
    num_list.append(num)

result = []
for i in color_list:
    for j in num_list:
        result.append((i, j))

print(result)
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
