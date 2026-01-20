# Drawing and loop
# Author: Sarah
# Ict,14,2025

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")
# TMNT - turtles
mikey = turtle.Turtle()
mikey.turtlesize(10)
mikey.color("orange")
mikey.shape("turtle")
mikey.forward(500)
mikey.goto(0, 0)
# Snowman
mikey.color("lightblue")
mikey.pencolor("lightblue")
mikey.fillcolor("lightblue")
mikey.width(5)
mikey.begin_fill()
mikey.circle(100)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 200)
mikey.pd()
mikey.begin_fill()
mikey.circle(80)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 360)
mikey.pd()
mikey.begin_fill()
mikey.circle(60)
mikey.end_fill()0


# Make 100 cookies
def make_cookie(x: int, y: int):
    # Turtle poninting east
    mikey.turtlesize(1)
    mikey.shape("classic")
    mikey.setheading(0)
    # chang the cookie color
    mikey.color("brown")
    # draw a circle
    mikey.pu()
    mikey.goto(-5 + x, -30 + y)
    mikey.pd()
    mikey.circle(30)

    #
    mikey.pu()
    mikey.goto(-10 + x, 10 + y)
    mikey.stamp()

    #
    mikey.goto(-10 + x, -10 + y)
    mikey.stamp()

    #
    mikey.goto(0 + x, 0 + y)
    mikey.stamp()

    make_cookie(100, 100)


window.exitonclick()
