import numpy as np

# 创建 3 × 3 的多维数组（矩阵）
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

# 运算是针对每个元素的，而非针对矩阵【逐元素运算 与 矩阵乘法运算不同】
# 把 a 的所有元素加 10【内部实现，实际上把 10 当作 3 × 3 矩阵处理】
print(a + 10)

# 把 a 的所有元素乘 3【内部实现，实际上把 3 当作 3 × 3 矩阵处理】
print(a * 3)