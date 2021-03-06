import numpy as np

# 创建 3 × 3 的多维数组（矩阵）
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

# 访问第 1 行第 1 列的元素
print(a[0][0])

# 访问第 2 行第 2 列的元素
print(a[1][1])

# 取出第 1 列【语法即：单个[:]定位到每行首地址，逗号后跟列索引值，本质是一位数组的单元素操作，拓展到多维数组相同属性/位置的操作】
print(a[:, 0])

# 取出第 1 行
print(a[0])
print(a[0, :])

# 取出第 2 列和第 3 列
print(a[:, 1:3])

# 取出第 2 行和第 3 行
print(a[1:3, :])

# 取出第 1 行，并赋值给变量
b = a[0]
print('b = ', b)

for i in a[0]:
    print(i)

# 也可以使用数组访问元素
# 依次取出数组 b 的第 3 个和第 1 个元素【没想到还能这样，这个太有用了，而且思想传达到本质：关于传参的形式】
c = [2, 0]
print(b[c])