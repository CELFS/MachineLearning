import numpy as np
import matplotlib.pyplot as plt

# 读入训练数据
train = np.loadtxt('images1.csv', delimiter=',', skiprows=1)
train_x = train[:,0:2] # 获取所有行。每一行读两个，索引 0 号到索引 1 号
train_y = train[:,2] # 获取所有行。每行读索引 2 号
# print(train_x)
# print(train_y)

# 绘图
plt.plot(train_x[train_y == 1, 0], train_x[train_y == 1, 1], 'o')
plt.plot(train_x[train_y == -1, 0], train_x[train_y == -1, 1], 'x')
plt.axis('scaled')
plt.show()
