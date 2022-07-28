import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def moves_forward():
    timmy.forward(10)


def moves_back():
    timmy.backward(10)


def rotate_counterclockwise():
    timmy.setheading(timmy.heading() + 10)


def rotate_clockwise():
    timmy.setheading(timmy.heading() - 10)


def clear_the_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    # or turtle.resetscreen()


# timmy.setheading(90)
screen.listen()
screen.onkey(key="w", fun=moves_forward)
screen.onkey(key="s", fun=moves_back)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_the_screen)

screen.exitonclick()
