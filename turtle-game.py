################################################################################

# Turtle Game
# Author Brayan Cordova - #BLC

################################################################################


# library import.
import turtle
import random

###### Start Customizing the game #####

s = turtle.Screen()  # show screen.
s.title("Turtle Game by Brayan Cordova - #BLC")  # title of window.
s.bgcolor("light gray")  # background color.

##### End Customizing the game #####


###### definition of the number of players #####
player_1 = turtle.Turtle()  # player 1.
player_2 = turtle.Turtle()  # player 2.


##### Start Creating Players #####

# attributes for player 1.
player_1.hideturtle()  # hide the turtle.
player_1.shape("turtle")  # i assign the figure of the turtle.
player_1.color("black", "black")  # i assign the the color the turtle and line.
player_1.shapesize(2, 2, 2)  # size of turtle.
player_1.pensize(3)  # pen size.

# attributes for player 2
player_2.hideturtle()  # hide the turtle.
player_2.shape("turtle")
player_2.color("green", "green")
player_2.shapesize(2, 2, 2)  # size of turtle.
player_2.pensize(3)  # pen size.

##### End Creating Players #####


##### Start Drawing the Goals #####

# drawing the goal for player 1.
player_1.penup()  # i give him the instruction not to draw.
player_1.goto(200, 200)
player_1.pendown()  # i give him the instruction to draw a line.
player_1.circle(40)  # draw a circle with 40px of radius.

# point where the race starts player 1.
player_1.penup()
player_1.goto(-250, 225)
player_1.showturtle()  # show the turtle.

# drawing the goal for player 2.
player_2.penup()
player_2.goto(200, -200)
player_2.pendown()
player_2.circle(40)

# point where the race starts player 2.
player_2.penup()
player_2.goto(-250, -170)
player_2.showturtle()  # show the turtle.

##### End Drawing the Goals #####


###### Start pos method #####

# dice to play.
dice = [1, 2, 3, 4, 5, 6]


for i in range(20):
    if player_1.pos() >= (200, 200):
        print("Player 1 Won 🥳")
        break
    elif player_2.pos() >= (200, -200):
        print("Player 2 Won 🥳")
        break
    else:
        turn_1 = input("Press the enter key to advance player 1")
        turn_1 = random.choice(dice)
        print("Your number is: ", turn_1, "\nYou advance: ", turn_1 * 20)
        player_1.pendown()
        player_1.forward(20 * turn_1)

        turn_2 = input("Press the enter key to advance player 2")
        turn_2 = random.choice()
        print("Your number is: ", turn_2, "\nYou advance: ", turn_2 * 20)
        player_2.pendown()
        player_2.forward(20 * turn_2)

##### End pos method #####

turtle.done()  # keep the windows open.
