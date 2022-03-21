import turtle

t = turtle.Turtle()

# 改成乌龟图标
t.shape('turtle')

# for i in range(4) 等价于 [0, 1, 2, 3]
for i in range(0,4):
    t.forward(50)
    t.left(90)

turtle.exitonclick()