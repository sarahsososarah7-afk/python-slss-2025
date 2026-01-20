# Turtle Artist
# Author:Sarah AL-Rihaymee
# 28 October
# drawing a house
import turtle

screen = turtle.Screen()
screen.title(" basic House")
screen.bgcolor("lightblue")


# Create a turtle named "builder"

builder = turtle.Turtle()

builder.color("black")


# Draw the house


def draw_square(size: float):
    for _ in range(4):
        builder.forward(size)

        builder.left(90)


def draw_triangle(size: float):
    builder.forward(size)

    builder.left(135)

    builder.forward(size / (2**0.5))

    builder.left(90)

    builder.forward(size / (2**0.5))

    builder.left(135)


# Draw the main house

builder.fillcolor("pink")

builder.begin_fill()

draw_square(200)

builder.end_fill()


# Draw the roof

builder.fillcolor("black")

builder.begin_fill()

builder.left(90)

builder.forward(200)

builder.right(90)

draw_triangle(200)

builder.end_fill()


# Draw the door

# builder.fillcolor("red")

# builder.penup()

# builder.goto(75, -200)

# builder.pendown()

# builder.begin_fill()

# builder.setheading(0)

# Draw the window

builder.fillcolor("lightblue")

builder.right(90)
builder.begin_fill()
builder.forward(50)
builder.left(90)
builder.forward(50)
builder.left(90)
builder.forward(50)
builder.end_fill()

# builder.left(90)

# builder.forward(100)

# builder.right(90)

# draw_square(5)

# Hide the turtle and finish

# builder.hideturtle()


# Keep the window open

screen.exitonclick()
