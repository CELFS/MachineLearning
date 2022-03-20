# 创建列表【末位可逗号 “,” 表示动态数组（列表）】
a = [1, 2, 3, 4, 5, 6]

# 访问列表元素
print(a[0])
print(a[1])

# 在索引上加入负号，可以从后面访问元素
print(a[-1])
print(a[-2])

# 有一种使用 “:” 的被称为切片的方便写法
# 获取指定范围的值【左闭右开。实际访问索引 1、2 的元素。为什么不设置与相似范围取值语法，如 range 的区间封闭性保持一致？】
# 获取范围：第一个元素的索引 ~ 最后一个元素的索引加一
print(a[1:3])

# 获取从第 1/2 个值开始到最后的所有值
print(a[1:])
print(a[2:])

# 获取从开始到第 3 个值的所有值
print(a[:3])

# 获取全部元素
print(a[:])
print(a)

# 步长
print(a[::2])
print(a[:4:2])