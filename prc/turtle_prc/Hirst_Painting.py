# import colorgram
#
# colors = colorgram.extract('painting.jpg', 30)
#
# color_list = []
#
# for i in colors:
#     color_list.append((i.rgb.r, i.rgb.g, i.rgb.b))
#
# print(color_list)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

color_list = [(219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98),
              (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102),
              (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174),
              (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53),
              (232, 209, 16), (74, 79, 40)]

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.sety(-250)
timmy.setx(-250)

for i in range(0, 10):
    for j in range(0, 10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setx(-250)
    timmy.sety(50 * (i + 1) - 250)

screen = Screen()
screen.exitonclick()
