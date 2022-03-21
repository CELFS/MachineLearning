import random
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

# 场地绘制
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

# 设置三只龟龟的初始化起点
x = -350
y = 200
# 初始化三只龟龟的属性【有个问题，即原点会出现箭头，原因是执行顺序】
# 【但是，如果把龟对象放到循环里面初始化，就会出现 players 的元素未定义，若字符串，则类型错误】
for i, turtle_color in zip(range(3), colors):
    players[i].speed(10000) # 用来减少画笔滞留时间的速度
    players[i].shape("turtle")
    players[i].color(turtle_color)
    players[i].penup()
    players[i].goto(x, y)
    players[i].pendown()
    y -= 150
    players[i].speed(random.randrange(1,3)) # 把龟龟速度正常化，随机化

# 开始比赛【但龟龟如何同时开跑？】
# 对比了成果，这里应该放死循环，甚至可以在死循环里利用随机数控制执行哪个分支，控制随机移动
mike.forward(1100)
bob.forward(1100)
lani.forward(1100)

# 排名【xcor 未使用】

turtle.exitonclick()