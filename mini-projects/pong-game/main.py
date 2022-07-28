import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.setposition(x=380, y=0)
#
#
# def go_up():
#     if paddle.ycor() <= 240:
#         paddle.goto(x=paddle.xcor(), y=paddle.ycor() + 10)
#
#
# def go_down():
#     if paddle.ycor() >= -230:
#         paddle.goto(x=paddle.xcor(), y=paddle.ycor() - 10)

l_paddle = Paddle(x=-380)
r_paddle = Paddle(x=375)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 350 or ball.distance(l_paddle) < 40 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect R Paddle Miss
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(0.5)

    # Detect L Paddle Miss
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(0.5)

screen.exitonclick()
