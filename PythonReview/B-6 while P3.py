# 计算水仙花数

n = 100
while n <= 999:
    # 赋值给临时变量，不破坏 n
    ans = n

    # 这部分不写不知道，一写吓一跳，忘了 90% 的逻辑，实现都是乱来的，心态浮躁
    # 我为自己觉得一道题简单想逃避的心理而羞耻
    n0 = ans % 10
    ans = (ans - n0) / 10
    n1 = ans % 10
    ans = (ans - n1) / 10
    n2 = ans

    if n0 ** 3 + n1 ** 3 + n2 ** 3 == n:
        print(n)

    n += 1