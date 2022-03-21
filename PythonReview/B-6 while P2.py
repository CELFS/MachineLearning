# 整体结构要优化，比如 restart 的循环放在最外层，精简代码结构
import random

target = random.randrange(0, 101)
print(target)
cnt = 0
while True:
    cnt += 1
    guess = int(input('In put a num to guess the target num'))
    if guess == target:
        print('You are right! You have guessed %d times' % cnt)
        again = input('Would you like to restart the game ? Press r, if not press q to quit.')
        # 可加入异常处理，判断输入的类型是否与要求的一致【可考虑功能结构拆分，封装函数】
        # print('Something wrong ! Please press the right key.')
        if again == 'r':
            # 初始化目标值，初始化计算次数
            target = random.randrange(0, 100)
            print(target)
            cnt = 0
            continue
        if again == 'q':
            print('You have quit the game.')
            break
    elif guess > target:
        print('Your number is bigger')
        continue
    else :
        print('Your number is smaller')
        continue