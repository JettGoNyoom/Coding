#from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
# Set shape
timmy.shape("turtle")
# Set color (purple best color)
#timmy.color("mediumpurple")
t.colormode(255)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# Challenge 1: Get Timmy the Turtle to draw a Square!
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Challenge 2: Draw a dashed line
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Challenge 3: Draw different shapes with random color, each side 100 in terms of length
    # Angles in each shape: 360 / # sides (Square: 360/4 = 90, Pentagon: 360/5 = 72, etc)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Challenge 4: Random walk
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
timmy.speed("fastest")

# for i in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
    
# Challenge 5: Use random RGB values and draw spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(rand_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

    
# All this has to happen at the bottom of the code
screen = t.Screen()
screen.exitonclick()