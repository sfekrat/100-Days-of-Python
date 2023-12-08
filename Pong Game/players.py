from turtle import Turtle
from scoreboard import Scoreboard


class Player(Turtle):
    def __init__(self, pos, name, score_pos):
        super().__init__()
        self.name = name
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.speed('fastest')
        self.s = Scoreboard(score_pos, self.name)

    def move(self):
        if 260 > self.ycor() > -260:
            self.fd(20)

    def up(self):
        new_y = 20
        self.goto(self.xcor(), self.ycor() + new_y)

    def down(self):
        new_y = 20
        self.goto(self.xcor(), self.ycor() - new_y)
