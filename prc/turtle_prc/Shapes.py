from turtle import Turtle, Screen
import random


def draw_shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


timmy = Turtle()
shape = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
color = ["slate blue", "magenta", "spring green", "dodger blue", "blue violet", "medium purple"]
timmy.penup()
timmy.sety(50)
timmy.setx(-50)
timmy.pendown()
for i in range(3, 11):
    timmy.shape(random.choice(shape))
    timmy.color(random.choice(color))
    draw_shapes(i)

screen = Screen()
screen.exitonclick()
