# 不使用 list 改写以下代码
numlist = list()
# numlist = []
while True :
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)

# 步骤如下
# 1. 原算法目的是求所有元素的平均值
# 2. 因此，只需考虑输入个数、数值的和两个量即可
cnt = 0
sumup = 0

while True :
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    value = float(inp)
    sumup += value
    cnt += 1

average = sumup / cnt
print('Average: ', average)

# 【推广】不使用 list 实现 list 的存储逻辑
# 1. 从 list 的结构定义入手:
#       (1) 一格对应一个存储元素
#       (2) 可通过索引进行随机访问

# 实现一格存储
# value = 0
# index = 0

