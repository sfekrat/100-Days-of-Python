from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.color("yellow")
        self.setheading(90)
        self.x_val = 10
        self.y_val = 10

    def up(self):
        new_y = self.y_val + self.ycor()
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.y_val * -1
        self.goto(self.xcor(), self.ycor() + new_y)

    def rt(self):
        new_x = self.x_val + self.xcor()
        self.goto(new_x, self.ycor())

    def lt(self):
        new_x = self.x_val * -1
        self.goto(new_x + self.xcor(), self.ycor())
