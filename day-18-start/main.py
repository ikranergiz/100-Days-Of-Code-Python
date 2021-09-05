import turtle
from turtle import Turtle, Screen
from turtle import *
import random

tim = Turtle()
turtle.colormode(255)


#Draw a Random walk with random colors

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]
#tim.pensize(15)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(i * 5 + 100)
        tim.circle(50)

draw_spirograph(5)

    #Second solution (mine)
    # tim.circle(100)
    # tim.setheading(tim.heading() + 10)




# for i in range(100):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#
#




#Drawing different shapes
# colors = ["red", "blue", "purple", "orange", "brown", "green", "black", "grey", "yellow"]
#
# edge = 3
# for i in range(edge, 10):
#     tim.color(random.choice(colors))
#     for j in range(0, edge):
#         tim.forward(100)
#         tim.right(360 / edge)
#
#     edge += 1




# Drawing a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup ()
#     tim.forward(10)
#     tim.pendown()

#Draw a red square
# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


screen = Screen()
screen.exitonclick() #hold the screen

#Some notes about importing
# import turtle
#
# tim = turtle.Turtle()
#
# import turtle as t
#
# tim = t.Turtle()


# import heroes
# print(heroes.gen())



