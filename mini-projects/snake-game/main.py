import time
import turtle
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen, Turtle
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Nokia 3310 Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Draw A Wall To Collide

wall = Turtle()
wall.color("white")
wall.penup()
wall.goto(-290, -290)
wall.pendown()
for _ in range(4):
    wall.forward(580)
    wall.left(90)
wall.hideturtle()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        snake.add_segment()
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    segments = snake.segments[1:]
    for segment in segments:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

# scoreboard.game_over()

screen.exitonclick()
