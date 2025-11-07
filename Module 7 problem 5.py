# Jessica Kusmierz
# 11/6/2025
# Problem 5

import turtle

def draw_square(t,sz):
    """Get turtle t to draw a square of sz size."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")    
wn.title("multiple turtles")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

sizes = [20, 40, 60, 80, 100]

alex.penup()
alex.backward(10)
alex.right(90)
alex.forward(10)
alex.left(90)
alex.pendown()

alex.hideturtle()
wn.exitonclick()
