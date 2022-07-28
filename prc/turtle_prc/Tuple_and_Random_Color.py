import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(500):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
