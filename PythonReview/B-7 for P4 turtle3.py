import turtle

# 画一个五角星
t = turtle.Turtle()
# t.shape('turtle')

for i in range(5):
    t.forward(300)
    t.left(144)

turtle.exitonclick()