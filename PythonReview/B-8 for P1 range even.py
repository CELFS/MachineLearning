# print Even

# 1【我的思路并不好，是假设已知答案范围而做的，不能很好运用题目给定的 20 来控制】
# for i in range(1, 41):
#     if i % 2 == 0:
#         print(i)

# 2【这是一种生成的思想】
for i in range(20):
    print((i + 1) * 2)

# 不使用 range 就要写列表 [0, 1, 2, ..., 40]