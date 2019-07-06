import math
import turtle

def iterc(c):
    iters = 0
    z = 0 + 0j

    while iters < 16 and math.hypot(z.real, z.imag) < 2:
        z = z * z + c
        iters += 1

    return iters

def getcolour(pos):
    x = iterc(pos)
    colournum = int(x * 6.25)
    return 'gray{}'.format(colournum)

def drawpixel(x, y, colour):
    turtle.goto(x, y)
    turtle.dot(1, colour)

def main():
    screen = turtle.Screen()
    screen.title('Mandelbrot Set')
    screen.bgcolor('#22ccaa')

    width = int(screen.numinput('Screen size', 'What width?', 600, 100, 20000))
    height = int(screen.numinput('Screen size', 'What height?', 600, 100, 10000))
    screen.setworldcoordinates(-width // 2, -height // 2, width // 2, height // 2)
    screen.tracer(0, 0)

    radius = 2

    turtle.penup()
    turtle.hideturtle()
    turtle.speed('fastest')

    x, y = -width // 2, -height // 2
    turtle.goto(x, y)

    while y < (height // 2):

        while x < (width // 2):

            newx = x / (width // 2) * radius
            newy = y / (width // 2) * radius
            mpos = newx + newy * 1j
            drawpixel(x, y, getcolour(mpos))
            x += 1

        x, y = -width // 2, y + 1
        screen.update()



main();