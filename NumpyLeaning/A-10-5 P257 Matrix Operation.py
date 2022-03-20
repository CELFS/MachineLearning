import numpy as np

# 与 3 × 1 的数组横向合并【要注意的是，矩阵的维度与运算的关系，维度不同，不可运算（因为数量对不上）】
a = [[1], [2], [3]]
b = [[4], [5], [6]]

# 【以数组传参的语法？或者只是首地址索引值，多参数传参的语法（参考A-10-4）】
h = np.hstack([a, b])
print(h)

# 与 1 × 3 的数组纵向合并
a2 = [1, 2, 3]
b2 = [4, 5, 6]
v = np.vstack([a2, b2])
print(v)