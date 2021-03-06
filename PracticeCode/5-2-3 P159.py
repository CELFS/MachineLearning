# Step 1
import numpy as np
import matplotlib.pyplot as plt

# 读入训练数据
train = np.loadtxt('click.csv', delimiter=',', skiprows=1)
train_x = train[:,0]
train_y = train[:,1]

# 绘图
plt.plot(train_x, train_y, 'o')
plt.show()

# Step 2
# 参数初始化
theta0 = np.random.rand()
theta1 = np.random.rand()

# 预测函数
def f(x):
    return theta0 + theta1 * x

# 目标函数
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)

# Step 3
# 标准化
mu = train_x.mean()
sigma = train_x.std()
def standardize(x):
    return (x - mu) / sigma

train_z = standardize(train_x)

# Step 4
plt.plot(train_z, train_y, 'o')
plt.show()

