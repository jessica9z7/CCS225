import turtle

#Setup
sides = int(input("Enter the number of sides:"))
length = float(input("Enter the length of a side:"))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

Jessica = turtle.Turtle()

Jessica.color(line_color, fill_color)

Jessica.begin_fill()
degree = 360 /sides
for _ in range(5):
    Jessica.forward(length)
    Jessica.right(degree)

Jessica.end_fill()
Jessica.done
turtle.exitonclick()

