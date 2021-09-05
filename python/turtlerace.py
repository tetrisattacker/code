from turtle import *
from random import randint
speed()
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ruby = Turtle()
ruby.color('red')
ruby.shape('turtle')

ruby.penup()
ruby.goto(-160, 100)
ruby.pendown()
for turn in range(10):
    ruby.right(36)

lily = Turtle()
lily.color('blue')
lily.shape('turtle')

lily.penup()
lily.goto(-160, 70)
lily.pendown()

for turn in range(72):
    lily.left(5)

tooga = Turtle()
tooga.shape('turtle')
tooga.color('green')

tooga.penup()
tooga.goto(-160, 40)
tooga.pendown()

for turn in range(60):
    tooga.right(6)

juju = Turtle()
juju.shape('turtle')
juju.color('orange')

juju.penup()
juju.goto(-160, 10)
juju.pendown()

for turn in range(30):
    juju.left(12)

for turn in range(100):
    ruby.forward(randint(1,5))
    lily.forward(randint(1,5))
    tooga.forward(randint(1,5))
    juju.forward(randint(1,5))
if ruby.xcor() > lily.xcor() and ruby.xcor() > tooga.xcor() and ruby.xcor() > juju.xcor():
    print("Ruby wins!")
elif lily.xcor() > ruby.xcor() and lily.xcor() > tooga.xcor() and lily.xcor() > juju.xcor():
    print("Lily wins!")
elif tooga.xcor() > ruby.xcor() and tooga.xcor() > lily.xcor() and tooga.xcor() > juju.xcor():
    print("Tooga wins!")
elif juju.xcor() > ruby.xcor() and juju.xcor() > lily.xcor() and juju.xcor() > tooga.xcor():
    print("Juju wins!")
print("That was an awesome race!")