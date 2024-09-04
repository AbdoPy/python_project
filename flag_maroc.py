import turtle
a = turtle.Turtle()
a.getscreen().bgcolor('red')
a.penup()
a.goto(-50, 50)
a.pendown()
a.color('green', 'red')
a.speed(25)
def star(turtle, size):
    if size<=199:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
star(a, 200)
turtle.done()
#########################################################
