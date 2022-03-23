import random
import time
import turtle

t = turtle.Turtle()

# 场地初始位置
x0 = -300
y0 = 300
t.penup()
t.goto(x0, y0)
t.pendown()

# 绘制初始方向、速度
t.right(90)
t.speed(100)

# 场地绘制，总长度 19 * 50
for i in range(20):
    x0 += 50
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.write(i)
    t.forward(500)

# 移走绘图箭头【可能可以 shape 成看不见的点？】
t.penup()
t.goto(1000, 1000)
t.pendown()

# 比赛选手初始化
mike = turtle.Turtle()
bob = turtle.Turtle()
lani = turtle.Turtle()

# 将对应变量存为列表，便于统一初始化【后面可以用类来初始化】
players = [mike, bob, lani]
colors = ['red', 'green', 'blue']
turtle_names = ['Mike', 'Bob', 'Lani']
# 设置三只龟龟的初始化起点，距离线的起点 50，走完全程 1000
x = -300
y = 200
# 初始化三只龟龟的属性【有个问题，即原点会出现箭头，原因是执行顺序】
# 【但是，如果把龟对象放到循环里面初始化，就会出现 players 的元素未定义，若字符串，则类型错误】
for i, turtle_color, turtle_name in zip(range(3), colors, turtle_names):
    players[i].speed(10000) # 用来减少画笔滞留时间的速度
    players[i].shape("turtle")
    players[i].color(turtle_color)
    players[i].penup()
    players[i].goto(x, y)
    players[i].pendown()
    y -= 150
    players[i].write('%s' % turtle_name, font=('SimHei', 20, 'normal'))
    players[i].speed(random.randrange(1,3)) # 把龟龟速度正常化，随机化

# 开始比赛【但龟龟如何同时开跑？】
# 对比了成果，这里应该放死循环，甚至可以在死循环里利用随机数控制执行哪个分支，控制随机移动【这个思路太复杂了，对比了课程的代码，发现只需要一点小技巧】
# 实现乌龟 “同时” 出发，相继到达终点:
start_time = time.time()
mike_time = 0
bob_time = 0
lani_time = 0
# 买定离手（滑稽）
time.sleep(5)

# 比赛开始
for step in range(110): # 10~20 的速度，最少走 50 步，最多走 100 步，多留 10 步，确保到达终点
    if mike_time and bob_time and lani_time:
        break
    if mike.xcor() < 710: # 这个距离，应以原点为依据 不能是 1000，经测试为700
        mike.forward(random.randrange(10,20))
    else:
        if mike_time == 0:
            mike_time = time.time()
    if bob.xcor() < 710:
        bob.forward(random.randrange(10,20))
    else:
        if bob_time == 0:
            bob_time = time.time()
    if lani.xcor() < 710:
        lani.forward(random.randrange(10,20))
    else:
        if lani_time == 0:
            lani_time = time.time()
    time.sleep(0.1) # 给 for 循环一个短暂停止时间，相当于把三只乌龟的出发时刻进行一次 “同步”（至少肉眼认为同步）

# 排名【xcor 未使用】【已用】
# 通过 xcor方法，获取三只龟的 x 距离，判断谁先到达终点
#       (1) 到达终点，乌龟暂停
#       (2) 到达终点，显示排名文字
# 使用时间模块，计算龟龟排名
#       (1) 查找最大值，返回下标
mike_time = mike_time - start_time
bob_time = bob_time - start_time
lani_time = lani_time - start_time
rank = {'Mike': mike_time, 'Bob': bob_time, 'Lani': lani_time}
champion = min(rank, key=rank.get)
for i in rank:
    print('%4s' % i, 'time is: %.2f' % rank[i])

print('冠军是: %s !' % champion)

t.penup()
t.goto(0, 0)
t.pendown()
t.write('冠军是: %s!' % champion, font=('SimHei', 30, 'normal'))

turtle.exitonclick()

# 【后记】花了点时间去考虑如何通过字典检索用时最少的龟龟
#       两层循环得不到结果，因为最终得到的是最后一个元素
#       查阅发现，字典检索有 min() 和 max() 方法，但还是要解决前面碰到的问题，这里只是当做字典学习