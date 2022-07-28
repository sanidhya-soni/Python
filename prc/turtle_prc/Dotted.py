from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape('circle')
timmy.shapesize(0.2)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()
