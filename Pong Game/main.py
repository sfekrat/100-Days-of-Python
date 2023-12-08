from turtle import Screen, Turtle
import time
from players import Player
from ball import Ball

POSITIONS = [(-350, 0), (350, 0)]
SCOREBOARD = [(-40, 240), (40, 240)]

screen = Screen()
screen.title('Pong Game')
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

t = Turtle()
t.color('white')
t.shape('square')
t.shapesize(stretch_len=0.2, stretch_wid=0.2)
t.penup()
t.hideturtle()
for i in range(-300, 300, 15):
    t.goto(0, i)
    t.stamp()

player_1 = Player(POSITIONS[0], "Player_1", SCOREBOARD[0])
player_2 = Player(POSITIONS[1], "Player_2", SCOREBOARD[1])
game_ball = Ball()

screen.listen()

screen.onkeypress(player_2.up, "Up")
screen.onkeypress(player_2.down, "Down")
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(game_ball.move_speed)
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    if player_1.distance(game_ball) < 50 and game_ball.xcor() < -320 or player_2.distance(
            game_ball) < 50 and game_ball.xcor() > 320:
        game_ball.bounce_x()
    if game_ball.xcor() > 380:
        player_1.s.increase_score()
        game_ball.reset_position()
    if game_ball.xcor() < -380:
        player_2.s.increase_score()
        game_ball.reset_position()
    if player_1.s.score >= 5:
        player_1.s.game_over()
        is_game_on = False
    elif player_2.s.score >= 5:
        player_1.s.game_over()
        is_game_on = False

screen.exitonclick()
