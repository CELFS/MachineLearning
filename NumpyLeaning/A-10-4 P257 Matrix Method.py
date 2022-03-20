import numpy as np

# 创建 3 × 3 的多维数组（矩阵）
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# a 的维度。由于是矩阵，所以二维 dimension
print(a.ndim)

# a 的形状。由于是 3 × 3 矩阵，所以为 (3, 3) 【这个方法可以获取多维数据的尺寸】
print(a.shape)

# a 的元素。由于是 3 × 3，所以元素为 9 【可获取数据量】
print(a.size)