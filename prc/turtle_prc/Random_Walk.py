from turtle import Turtle, Screen
import random

color = ["slate blue", "magenta", "spring green", "dodger blue", "blue violet", "medium purple"]
direction = [0, 90, 180, 270]
timmy = Turtle()
timmy.pensize(5)
timmy.speed("fastest")
for _ in range(500):
    timmy.color(random.choice(color))
    timmy.forward(20)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
