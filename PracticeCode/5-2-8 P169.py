import numpy as np

# 初始化参数 θ
theta = np.random.rand(3)

# 创建训练数据的矩阵 X【这个矩阵的格式是如何与数学公式对应的？其实我还没理解 vstack 的处理逻辑】
# 【解读 vstack 本质是将传入参数向右扩展】
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0])], x, x ** 2).T

X = to_matrix(train_z)

# 预测函数
def f(x):
    return np.dot(x, theta)