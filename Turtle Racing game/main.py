from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_back():
    tim.back(10)


def change_counter():
    tim.left(10)


def change_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=change_counter)
screen.onkey(key="d", fun=change_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
