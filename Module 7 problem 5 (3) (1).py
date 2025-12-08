# Jessica Kusmierz
# 11/6/2025
# Problem 5

import turtle

def draw_square(t,sz):
    """Draw a square of given size with turtle t."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")    
wn.title("multiple turtles")

# Make a turtle
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

# List of square sizes
sizes = [20, 40, 60, 80, 100]

# Move turtle to a starting position
alex.penup()
alex.backward(50)
alex.right(90)
alex.forward(50)
alex.left(90)
alex.pendown()

# Draw squares of different sizes
for size in sizes:
    draw_square(alex, size)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

# Hide the turtle and wait for click to exit
alex.hideturtle()
wn.exitonclick()
