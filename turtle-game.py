################################################################################

# Turtle Game
# Author Brayan Cordova - #BLC

################################################################################

# library import.
import turtle
import random

s = turtle.Screen()  # show screen.
s.title("Turtle Game by Brayan Cordova - #BLC")  # title of window.

################################################################################

# definition of the number of players.
player_1 = turtle.Turtle()  # player 1.
player_2 = turtle.Turtle()  # player 2.

################################################################################
################################################################################# Start Creating Players

# attributes for player 1.
player_1.shape("turtle")  # i assign the figure of the turtle.
player_1.color("black", "black")  # i assign the the color the turtle and line.


# attributes for player 2
player_2.shape("turtle")
player_2.color("green", "green")

# End Creating Players
################################################################################
################################################################################

# Start Drawing the Goals

# drawing the goal for player 1.
player_1.penup()  # i give him the instruction not to draw.
player_1.goto(200, 200)
player_1.pendown()  # i give him the instruction to draw a line.
player_1.circle(40)  # draw a circle with 40px of radius.

# point where the race starts player 1.
player_1.penup()
player_1.goto(-250, 225)

# drawing the goal for player 2.
player_2.penup()
player_2.goto(200, -200)
player_2.pendown()
player_2.circle(40)

# point where the race starts player 2.
player_2.penup()
player_2.goto(-250, -170)

# End Drawing the Goals
################################################################################
################################################################################

# Start 
# End 

turtle.done()  # keep the windows open.
