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


timmy.speed("fastest")
for _ in range(72):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)

screen = t.Screen()
screen.exitonclick()
