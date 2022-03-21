import turtle

# Draw a circle with turtle
c = turtle.Turtle()
c.shape('turtle')

c.color('red')
c.penup()
c.goto(-100, 0)
c.pendown()
c.circle(100)

turtle.exitonclick()