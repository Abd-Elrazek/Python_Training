# A Nautilus figure drawn using repeated rotated and rescaled
# squares
# By jxxcarlson
# Modified from http://square-the-circle.com/tag/turtle-graphics/

import turtle

# Set the background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turle
daisy = turtle.Turtle()
daisy.width(2)
daisy.speed(0.5)
daisy.color("red")


# Draws a square with the given side length
def drawSquare(t, length):
  for i in range(4):
    t.forward(length)
    t.left(90)

# Draws a spiral of the given number of squares, offset by the
# given angle, starting with a square of the given length, and
# scaling the squares by the given scale factor
def drawSquareSpiral(t, num, angle, length, scale):
  for i in range(num):
    drawSquare(t, length)
    t.left(angle)
    length = scale * length

# Get drawing!
# daisy.penup()
daisy.goto(-5, -53)
daisy.pendown()
drawSquareSpiral(daisy, 90, 10, 200, 0.97)
