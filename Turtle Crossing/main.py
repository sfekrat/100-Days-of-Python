from turtle import Screen
from player import Player
from swarm import Swarm
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

p1 = Player()
game_score = Scoreboard()

screen.onkeypress(p1.up, 'Up')
screen.onkeypress(p1.down, 'Down')
screen.onkeypress(p1.lt, 'Left')
screen.onkeypress(p1.rt, 'Right')
my_swarm = Swarm()
is_game_on = True
while is_game_on:
    my_swarm.create_swarm()
    time.sleep(0.1)
    screen.update()
    my_swarm.move()
    # Detect Collision
    for car in my_swarm.swarms:
        if p1.distance(car) < 22:
            game_score.game_over()
            is_game_on = False
            break
    if p1.ycor() > 280:
        # Level Up
        game_score.increase_level()
        # Go to initial position
        p1.goto(0, -280)
        # Speed up the game
        my_swarm.level_up()

screen.exitonclick()
