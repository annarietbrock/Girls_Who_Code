from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
t.penup()
setup(500,300)


### Write your code below:

#SQUARE
def square():
    t.pendown()
    for sides in range(4):
        t.forward(50)
        t.right(90)

#TRIANGLE
def triangle():
    t.pendown()
    for sides in range(3):
        t.forward(50)
        t.right(120)

#RANDOM
def random():
    n = input('Number of Sides')
    t.pendown()
    for sides in range(n):
        t.forward(50)
        t.right(360/n)

Size = 150
def triangles():
    t.begin_fill()
    for sides in range(3):
        t.forward(Size)
        t.right(120)
    for sides in range(3):
        t.backward(Size)
        t.left(120)
    for sides in range(3):
        t.forward(Size)
        t.left(120)
    for sides in range(3):
        t.backward(Size)
        t.right(120)
    for sides in range(3):
        t.left(120)
        t.forward(Size)
        t.left(120)
    for sides in range(3):
        t.left(120)
        t.backward(Size)
        t.left(120)
    t.end_fill()


Color = input('Pick your fill color')
Pen = input('Pick your stroke color')


t.fillcolor(Color)
t.pencolor(Pen)
width = Size
t.goto(-450,0)

for hexagons in range(7):
    t.pendown()
    triangles()
    t.goto(-450+width,0)
    width+=Size









# Close window on click.
exitonclick()
