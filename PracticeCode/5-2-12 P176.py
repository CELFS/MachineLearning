# 随机梯度下降法的实现

import numpy as np
import matplotlib.pyplot as plt

# 读入训练数据
train = np.loadtxt('click.csv', delimiter=',', skiprows=1)
train_x = train[:,0]
train_y = train[:,1]

# 参数初始化
theta0 = np.random.rand()
theta1 = np.random.rand()

# 目标函数
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)

# 标准化
mu = train_x.mean()
sigma = train_x.std()
def standardize(x):
    return (x - mu) / sigma

train_z = standardize(train_x)

# 学习率
ETA = 1e-3

# 创建训练数据的矩阵 X【这个矩阵的格式是如何与数学公式对应的？其实我还没理解 vstack 的处理逻辑】
# 【解读 vstack 本质是将传入参数向右扩展】
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]), x, x ** 2]).T

X = to_matrix(train_z)

# 均方误差
def MSE(x, y):
    return (1 / x.shape[0]) * np.sum((y - f(x)) ** 2)

# 初始化参数 θ
theta = np.random.rand(3)

# 均方误差的历史记录
errors = []

# 预测函数
def f(x):
    return np.dot(x, theta)

# 误差的差值
diff = 1

# 重复学习
errors.append(MSE(X, train_y))
while diff > 1e-2:
    # 为了调整训练数据的顺序，准备随机的序列
    p = np.random.permutation(X.shape[0])
    # 随机取出训练数据，使用随机梯度下降法更新参数
    for x, y in zip(X[p,:], train_y[p]):
        theta = theta - ETA * (f(x) - y) * x
    # 计算与上一次误差的差值
    errors.append(MSE(X, train_y))
    diff = errors[-2] - errors[-1]

# 绘制误差变化图
x = np.linspace(-3, 3, 100)

plt.plot(train_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()

