from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(x=x, y=y)

    def go_up(self):
        if self.ycor() <= 230:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self):
        if self.ycor() >= -220:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
