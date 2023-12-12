import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Fahima is a Cutie")


snakes = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()

screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()
    if snakes.head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        scoreboard.increase_score()

    if snakes.head.xcor() > 290 or snakes.head.xcor() < -290 or snakes.head.ycor() > 290 or snakes.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snakes.reset()

    for segment in snakes.snakes[1:]:
        if snakes.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snakes.reset()
screen.exitonclick()
