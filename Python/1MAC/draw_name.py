#Draw my initials, which are 'A', 'M', 'H, and 'Y'
import turtle

window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()

t.shape("turtle")
t.speed(3)
t.color("blue")

#draw "A"
t.ht()#hide
t.up()#up
t.setpos(-300,0)#start point
t.down()#down
t.st()#st
t.left(60)#left
t.forward(200)#forward
t.right(120)#right
t.forward(200)#forward
t.up()#up
t.ht()
t.backward(100)
t.right(120)
t.st()
t.down()
t.forward(100)

#draw "M"
t.ht()#hide
t.up()#up
t.setpos(-50,0)
t.down()
t.st()
t.right(90)
t.forward(170)
t.right(165)
t.forward(90)
t.left(150)
t.forward(90)
t.right(165)
t.forward(170)

#draw "H"
t.ht()#hide
t.up()#up
t.setpos(50,0)
t.down()
t.st()
t.right(180)
t.forward(170)
t.ht()#hide
t.up()#up
t.setpos(100,170)
t.down()
t.st()
t.right(180)
t.forward(170)
t.ht()#hide
t.up()#up
t.setpos(100,85)
t.down()
t.st()
t.right(90)
t.forward(50)

#draw "Y"
t.ht()#hide
t.up()#up
t.setpos(150,170)
t.down()
t.st()
t.left(120)
t.forward(90)
t.left(120)
t.forward(90)
t.ht()#hide
t.up()#up
t.backward(90)
t.left(30)
t.down()
t.st()
t.backward(100)

window.exitonclick()