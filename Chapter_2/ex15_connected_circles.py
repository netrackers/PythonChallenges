# Draws the connected circles from Exercise 15
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

import turtle

# changing the background color
turtle.bgcolor('light sky blue')

# Setting the pen size
turtle.pensize(3)

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Drawing the circles
turtle.circle(40)
turtle.penup()
turtle.goto(40, 40)
turtle.pendown()
turtle.circle(-40)
turtle.penup()
turtle.goto(90, 0)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(140, 40)
turtle.pendown()
turtle.circle(-40)
turtle.penup()
turtle.goto(185,0)
turtle.pendown()
turtle.circle(40)

turtle.done()