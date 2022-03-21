import turtle

t = turtle.Turtle()

# heading() 返回海龟前进的角度（相对初始方向）
print(t.heading())

t.forward(100)
t.left(70)
print(t.heading())

t.forward(100)
t.right(90)
print(t.heading())

t.forward(100)
# seth() 是绝对的角度，不管前面转了多少，都直接设为 180
t.seth(180)
print(t.heading())

t.forward(100)

turtle.exitonclick()