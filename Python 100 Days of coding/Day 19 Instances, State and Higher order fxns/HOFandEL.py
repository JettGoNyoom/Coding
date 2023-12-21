# Higher order FXNs and Event Listeners

from turtle import Turtle, Screen
timmy = Turtle()

screen = Screen()

def move_forwards():
    timmy.forward(10)

screen.listen()
# When passing fxns as inputs, pass ONLY the name, without the parenthesis ()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()