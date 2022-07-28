from turtle import Turtle, Screen
import random

color = ["red", "green", "blue", "yellow", "purple"]

screen = Screen()
screen.setup(width=1280, height=720)

tim = Turtle()
rim = Turtle()
gim = Turtle()
sim = Turtle()
pim = Turtle()

turtles = {"Red": tim, "Green": rim, "Blue": gim, "Yellow": sim, "Purple": pim}
speeds = ["fastest", "fast", "normal", "slow", "slowest"]

for i in turtles:
    turtles[i].shapesize(2)
    turtles[i].penup()
    turtles[i].shape("turtle")
    turtles[i].color(i)
    # turtles[i].setx(-350)

tim.setposition(-600, 200)
rim.setposition(-600, 100)
gim.setposition(-600, 0)
sim.setposition(-600, -100)
pim.setposition(-600, -200)

text = screen.textinput("Enter your bet", "Which Turtle will win the race? Enter the color: ").capitalize()

for i in range(50):
    tim.forward(random.randint(10, 30))
    rim.forward(random.randint(10, 30))
    gim.forward(random.randint(10, 30))
    sim.forward(random.randint(10, 30))
    pim.forward(random.randint(10, 30))

max_pos = turtles["Red"]
won = "Red"
for i in turtles:
    if turtles[i].xcor() > max_pos.xcor():
        max_pos = turtles[i]
        won = i

if turtles[text].xcor() == max_pos.xcor():
    print(True)
    print(f"{won} Won")
else:
    print(False)
    print(f"{won} Won")

screen.exitonclick()
