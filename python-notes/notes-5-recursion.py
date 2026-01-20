# recursion
# Author:Sarah Al-Rihaymee
# Oct,20,2025

import turtle

# Drawing trees
wn = turtle.Screen()
t = turtle.Turtle()

t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()

#  Dictionary to hold colors
LEAF_COLORS = {
    "spring": "c28cae",
    "summer": "a8d4ad",
    "autumn": "92b9bd",
    "winter": "e57a44",
}


def draw_complicated_tree(level: int, branch_length: float):
    """A recrusive function to draw trees
    level - the levels of branches
    branch_length - length of brunch to draw
    """
    t.pendown()

    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("LEAF_COLORS['summer]")
        t.stamp()
        t.color("brown")
        # For all the levels
    else:
        #   1.Go forward
        t.forward(branch_length)
        #   2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        #   3.Turn to the right and
        t.right(74)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        #   4. Go back where we started
        t.left(37)
        t.backward(branch_length)


def factorial(num: int) -> int:
    """Returns the factorical of a given num
    calculated recursively"""
    # if the number is less than or equal to 1, return 1
    # otherwise, return the number multiplied by the factorial of the number minus 1
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


# def fibonacci(num: int) -> int:
#      """Returns the nth fibonacci number and
#      calculated recursively"""

t.speed(100)
# t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, 100)
t.pendown()

draw_complicated_tree(12, 128)
print(factorial(3))
print(factorial(4))
print(factorial(3))
print(factorial(4))
print(factorial(100))

wn.exitonclick()
