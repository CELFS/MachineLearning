import numpy as np

cnt = 0
for i in dir(np):
    cnt += 1
    print(cnt, '---', i)

# 【613 个属性和方法，有点离谱啊...说明只能需要什么学什么，去查文档】