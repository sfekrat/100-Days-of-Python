import random
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
usr_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtles():
    turtles = []
    y = -70
    for i in colors:
        t = Turtle(shape="turtle")
        t.color(i)
        t.penup()
        t.goto(x=-230, y=y)
        y += 30
        turtles.append(t)
    return turtles


def lets_race(all_turtles):
    is_race_started = False
    if usr_bet:
        is_race_started = True
    while is_race_started:
        rand_dist = randint(0, 10)
        any_turtle = random.choice(all_turtles)
        any_turtle.fd(rand_dist)
        if any_turtle.xcor() > 230:
            if any_turtle.pencolor() == usr_bet:
                print(f"You've won the race! The {usr_bet} turtle is the winner!")
            else:
                print(f"You've lost! The {any_turtle.pencolor()} turtle won the race!")
            is_race_started = False


racers = create_turtles()
lets_race(racers)

screen.exitonclick()
