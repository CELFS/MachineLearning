# print Prime

# 1
# range(101, 1, -1) 翻转，从大到小进行循环
for i in range(2, 101): # 直接改范围也行
    # cnt 标记是否出现合数
    cnt = 0
    for j in range(2, i): # 【我使用 (i - 1)，是避免除自身算进去了，但实际不会，因为 range 的取值不包括右区间】
        if i % j == 0:
            cnt += 1
            break
        else:
            continue
    # cnt 为 0，说明没有除自身以外的因素
    if cnt == 0:
        print(i)
    else:
        continue


# 2【思路是一样的，只是形式不同，这种形式更简练，而且输出的顺序是从小到大】
for N in range(2, 101):
    f = True
    for i in range(2, N):
        if N % i == 0:
            f = False
            break
    if f:
        print(N, 'is a Prime')