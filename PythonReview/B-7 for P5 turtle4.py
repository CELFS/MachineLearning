import turtle

n = int(input("Please input the edges: \n"))

t = turtle.Turtle()

for i in range(n):
    t.forward(50)
    # t.left(180 - 180 * (n - 2) / n)
    # 通分也可得到下式
    t.left(360 / n)

turtle.exitonclick()