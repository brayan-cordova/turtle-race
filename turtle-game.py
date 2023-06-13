# Turtle Game
# Author Brayan Cordova - #BLC

import turtle
import random

s = turtle.Screen()  # show screen
s.title("Turtle Game by Brayan Cordova - #BLC")

player_1 = turtle.Turtle()  # player 1
player_2 = turtle.Turtle()  # player 2

# attributes for player 1
player_1.shape("turtle")  # i assign the figure of the turtle
player_1.color("black", "black")  # i assign the the color the turtle and line

# attributes for player 2
player_2.shape("turtle")
player_2.color("green", "green")

# i send the turtle to the point x and y
player_1.goto(-300, 100)
player_2.goto(-300, -100)

turtle.done()  # keep the windows open.
