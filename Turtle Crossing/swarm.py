from turtle import Turtle, colormode
import random

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
          (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
          (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
          (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
          (168, 99, 102)]

colormode(255)
MOVE_DISTANCE = 5


class Swarm:
    def __init__(self):
        self.swarms = []
        self.swarm_speed = MOVE_DISTANCE

    def create_swarm(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            t = Turtle("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.penup()
            t.goto(400, random.randint(-260, 260))
            t.color(random.choice(colors))
            self.swarms.append(t)

    def move(self):
        for t in self.swarms:
            t.backward(self.swarm_speed)

    def level_up(self):
        self.swarm_speed += 5

