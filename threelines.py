#Norma
#threelines.py

import turtle

def draw(m, h):
    m.pendown()
    m.forward(h)
    m.penup()
    m.backward(h)
    m.penup()

def draw3(m, h, g):
    m.penup()
    m.forward(g*2)
    m.left(90)
    draw(m, h)

    for count in range(2):
        m.left(90)
        m.forward(g)
        m.right(90)
        draw(m, h)

def main():

    wn = turtle.Screen()
    m = turtle.Turtle()
    m.pensize(3)
    m.stamp()
    #m.speed(0)
    m.left(90)
    h = 200
    g = 30
    draw3(m, h, g)
    wn.exitonclick()

main()

# m.width(3)
# m.stamp()
# m.penup()
# m.left(90)
# m.forward(60)
# m.left(90)
# m.forward(200)
# m.pendown()
# m.right(180)
# m.forward(200)

# m.penup()
# m.right(90)
# m.forward(30)
# m.pendown()
# m.right(90)
# m.forward(200)
#
# m.penup()
# m.left(90)
# m.forward(30)
# m.pendown()
# m.left(90)
# m.forward(200)

#wn.exitonclick()