from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self, pos, name):
        super().__init__()
        self.name = name
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(pos)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over, {self.name} Won!", align=ALIGNMENT, font=('Courier', 20, 'normal'))
