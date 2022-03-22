# Exam Practice 1

def swap(x, y):
    # 了解异或的效果
    x ^= y
    y ^= x
    x ^= y
    return x, y

# 输入三个整数a,b,c，由小到大输出【读错题，重做！】
# a = int(input("Input a number a: "))
# b = int(input("Input a number b: "))
# c = int(input("Input a number c: "))

# target = [a, b, c]
target = [99, 1, 20]
# test = [0, 0, 0]
print('start: ', target)
# target = [99, 1, 88, 67, 22, 3, 10]
for i in range(3):
    for j in range(3): # 【起始点如果是 0，下面要写成小于号，非常不直观】
        print('t[i]: ', target[i], 't[j]: ', target[j])
        if target[i] > target[j]:
            (target[i], target[j]) = swap(target[i], target[j])
        else:
            continue
    # test[i] = target # 触发了浅拷贝，因此 test 的每个元素指向同一对象
    # print(test)
    # print(target)
    print('*' * 20)
# 最后可以来一个全体重新赋值，以改变 a、b、c 变量的值
# print(a, b, c)
# print('*'*20)
print('end: ', target)
# print('*'*20)
# print(test)