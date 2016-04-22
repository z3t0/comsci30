import turtle
import math

def drawPolygon(x, y, n, radius, heading):
    new_turtle = turtle.Turtle()
    new_turtle.setheading(heading)
    sideLen = 2 * radius * math.sin (math.pi / n)
    angle = 360.0 / n
    new_turtle.penup()
    new_turtle.goto (x, y)
    new_turtle.pendown()
    for iter in range (n):
    	new_turtle.forward (sideLen)
    	new_turtle.left (angle)
    new_turtle.ht()


turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Pattern 30")


for i in range(0, 6):
    drawPolygon(0, 0, 6, 100, 360 / 6.0 * i)


wn.exitonclick()


