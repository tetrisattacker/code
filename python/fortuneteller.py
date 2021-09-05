import random
import turtle

pointer = turtle.Turtle()
pointer.turtlesize(3, 3, 2)
pen = turtle.Turtle()
spin_amount = random.randint(1,630)
pen.penup()

pen.goto(200, 0)
pen.pendown()
pen.write('Yes!', font=('Open Sans', 30))
pen.penup()

pen.goto(-400, 0)
pen.pendown()
pen.write('Absolutely Not!', font=('Open Sans', 30))
pen.penup()

pen.goto(-100, 300)
pen.pendown()
pen.write('Uhh, Maybe?', font=('Open Sans', 30))
pen.penup()

pen.goto(0, -200)
pen.pendown()
pen.write('Yes, but after 50 years!', font=('Open Sans', 30))
pen.ht()
pointer.right(spin_amount)