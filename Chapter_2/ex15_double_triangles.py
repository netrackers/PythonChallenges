# Draws the double triangles figure 1 from Exercise 15
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

import turtle

# changing the background color
turtle.bgcolor('light sky blue')

# Seeting the fill color
turtle.fillcolor('white')

# Setting the pen size
turtle.pensize(3)

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Begin drawing
turtle.begin_fill()
turtle.left(50)
turtle.forward(125)
turtle.right(100)
turtle.forward(125)
turtle.goto(0,0)
turtle.end_fill()
turtle.left(115)
turtle.forward(200)
turtle.goto(160.50,0)
turtle.done()