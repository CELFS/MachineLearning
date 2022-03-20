a = int(input())

# 根据变量值能否被 3 或 5 整除，打印不同的消息
if a % 3 == 0:
    print('能被 3 整除的数')
elif a % 5 == 0:
    print('能被 5 整除的数')
else :
    print('既不能被 3， 也不能被 5 整除的数')