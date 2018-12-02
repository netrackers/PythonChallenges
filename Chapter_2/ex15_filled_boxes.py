# Draw figure 1 from Exercise 15
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

import turtle

# changing the background color
turtle.bgcolor('light sky blue')

# Seeting the fill color
turtle.fillcolor('white')

# Setting the pen size
turtle.pensize(5)

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Begin drawing
turtle.begin_fill()
turtle.left(45)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()
turtle.done()