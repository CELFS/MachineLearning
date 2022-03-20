# 多项式回归的实现

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

# Step 1
# 初始化参数 θ
theta = np.random.rand(3)

# 创建训练数据的矩阵 X【这个矩阵的格式是如何与数学公式对应的？其实我还没理解 vstack 的处理逻辑】
# 【解读 vstack 本质是将传入参数向右扩展】
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]), x, x ** 2]).T

X = to_matrix(train_z)

# 预测函数
def f(x):
    return np.dot(x, theta)

# Step 2
# 误差的差值
diff = 1

# 重复学习
error = E(X, train_y)
while diff > 1e-2:
    # 更新参数
    theta = theta - ETA * np.dot(f(X) - train_y, X)
    # 计算与上一次误差的差值
    current_error = E(X, train_y)
    diff = error - current_error
    error = current_error

x = np.linspace(-3, 3, 100)

plt.plot(train_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()