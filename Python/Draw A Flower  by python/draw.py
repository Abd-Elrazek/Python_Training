import turtle
import random

loadWindow = turtle.Screen()
loadWindow.bgcolor("yellow")

#create turtles
dodo = turtle.Pen()
soso = turtle.Pen()
toto = turtle.Pen()
nono = turtle.Pen()


#change turtle shapes
dodo.shape("turtle")
soso.shape("turtle")
toto.shape("turtle")
nono.shape("turtle")

#change turtle colors
dodo.color('red')
soso.color('blue')
toto.color('#FF00FF')
nono.color('brown')

#turtels starting positions

dodo.left(90)
soso.forward(-50)
soso.left(90)
toto.forward(50)
toto.left(90)
nono.forward(100)
nono.left(90)


#turtels begin race
for x in range(25):
	d = random.randint(-5,20)
	s = random.randint(-5,20)
	t = random.randint(-5,20)
	n = random.randint(-5,20)

	dodo.forward(d)
	soso.forward(s)
	toto.forward(t)
	nono.forward(n)


turtle.exitonclick()