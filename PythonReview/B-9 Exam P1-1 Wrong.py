# Exam Practice 1
# 输入三个整数a,b,c，由小到大输出【而且再次读题，发现理解错了！】

# 【问题出在列表的初始化】
num = [0, 0, 0]
cnt = 0
while cnt < 3:
    num[cnt] = int(input("Input a number: "))
    cnt += 1

max = num[0]
for i in num:
    if max < i:
        max = i
    else:
        continue

print(max)