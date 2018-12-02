# this program draws a design using repeated circles.

import turtle

# Named Constants
NUM_CIRCLES = 36    # Number of circles to draw
RADIUS = 100        # Radius of each circle
ANGLE = 10          # Angle to turn
ANIMATION_SPEED = 20 # Animation speed

# Set the animation speed
turtle.speed(ANIMATION_SPEED)

# Draw 3 circles, with turtle tilted by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()