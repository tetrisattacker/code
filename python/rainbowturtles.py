import turtle
turtle = turtle.Turtle()
turtle.turtlesize(2, 2, 2)
turtle.shape('turtle')
turtle.penup()

for i in range(7):
    turtle.forward(50)
    if i == 0:
        turtle.color('red')
    elif i == 1:
        turtle.color('orange')
    elif i == 2:
        turtle.color('yellow')
    elif i == 3:
        turtle.color('green')
    elif i == 4:
        turtle.color('blue')
    elif i == 5:
        turtle.color('indigo')
    elif i == 6:
        turtle.color('violet')
    turtle.stamp()