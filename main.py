'''
KNOWN BUGS TO FIX
-----------------
* Replay button would be nice
-----------------
'''

import turtle

# setup screen and play
scrn = turtle.Screen()
scrn.bgcolor("red")

playerbox = turtle.Turtle()
playerbox.hideturtle()
playerbox.speed(0)

playerbox.color("white")
playerbox.pensize(10)
# setup related variables
ystart = 70
xstart = -70

# set x and o turtles
xo1 = turtle.Turtle()
xo2 = turtle.Turtle()
xo3 = turtle.Turtle()
xo4 = turtle.Turtle()
xo5 = turtle.Turtle()
xo6 = turtle.Turtle()
xo7 = turtle.Turtle()
xo8 = turtle.Turtle()
xo9 = turtle.Turtle()
xo1.shape("square")
xo2.shape("square")
xo3.shape("square")
xo4.shape("square")
xo5.shape("square")
xo6.shape("square")
xo7.shape("square")
xo8.shape("square")
xo9.shape("square")
xo1.shapesize(2)
xo2.shapesize(2)
xo3.shapesize(2)
xo4.shapesize(2)
xo5.shapesize(2)
xo6.shapesize(2)
xo7.shapesize(2)
xo8.shapesize(2)
xo9.shapesize(2)
xo1.penup()
xo2.penup()
xo3.penup()
xo4.penup()
xo5.penup()
xo6.penup()
xo7.penup()
xo8.penup()
xo9.penup()
# Winner announcer
wina = turtle.Turtle()
wina.hideturtle()
wina.penup()
wina.setpos(40, 200)
# Helps wina turtle declare the winner, 1 is X and 2 is O
whowon = 0
# prevents duplicate announcements
wasWon = False

# Replay button(W.I.P)
def WinCheck():
    global xo1C
    global xo2C
    global xo3C
    global xo4C
    global xo5C
    global xo6C
    global xo7C
    global xo8C
    global xo9C

    global whowon

    global wasWon
    if whowon == 0:
        # checks if X won in any way
        # horizontal line check for x
        if xo1C == 1 and xo2C == 1 and xo3C == 1:
            whowon = 1
        if xo4C == 1 and xo5C == 1 and xo6C == 1:
            whowon = 1
        if xo7C == 1 and xo8C == 1 and xo9C == 1:
            whowon = 1
        # curved lines check for x
        if xo1C == 1 and xo5C == 1 and xo9C == 1:
            whowon = 1
        if xo7C == 1 and xo5C == 1 and xo3C == 1:
            whowon = 1
        # vertical lines check for x
        if xo1C == 1 and xo4C == 1 and xo7C == 1:
            whowon = 1
        if xo2C == 1 and xo5C == 1 and xo8C == 1:
            whowon = 1
        if xo3C == 1 and xo6C == 1 and xo9C == 1:
            whowon = 1
        # checks if O won in any way
        # horizontal lines check for o
        if xo1C == 2 and xo2C == 2 and xo3C == 2:
            whowon = 2
        if xo4C == 2 and xo5C == 2 and xo6C == 2:
            whowon = 2
        # curved lines check for o
        if xo7C == 2 and xo8C == 2 and xo9C == 2:
            whowon = 2
        if xo1C == 2 and xo5C == 2 and xo9C == 2:
            whowon = 2
        if xo7C == 2 and xo5C == 2 and xo3C == 2:
            whowon = 2
        # vertical lines check for o
        if xo1C == 2 and xo4C == 2 and xo7C == 2:
            whowon = 2
        if xo2C == 2 and xo5C == 2 and xo8C == 2:
            whowon = 2
        if xo3C == 2 and xo6C == 2 and xo9C == 2:
            whowon = 2

    if whowon != 0 and wasWon == False:
        if whowon == 1:
            print("X won")
            wasWon = True
            wina.write("X is the WINNER", align='center',font=('arial',40,'normal'))
        if whowon == 2:
            print("O won")
            wasWon = True
            wina.write("O is the WINNER", align='center', font=('arial', 40, 'normal'))




def prboard():
    global ystart
    for item in range(3):
        playerbox.sety(ystart)
        playerbox.setx(-70)
        for item in range(3):
            for item in range(4):
                playerbox.forward(70)
                playerbox.right(90)
            playerbox.forward(70)
        ystart = ystart - 70

    xo1.setpos(-35,35)
    xo2.setpos(35, 35)
    xo3.setpos(105, 35)
    xo4.setpos(-35, -35)
    xo5.setpos(35, -35)
    xo6.setpos(105, -35)
    xo7.setpos(-35, -105)
    xo8.setpos(35, -105)
    xo9.setpos(105, -105)

isX = False

# 0 means the button is unused, 1 for X, 2 for O
xo1C = 0
xo2C = 0
xo3C = 0
xo4C = 0
xo5C = 0
xo6C = 0
xo7C = 0
xo8C = 0
xo9C = 0

def onclickSquare(x, y):
    global isX


    global xo1C
    global xo2C
    global xo3C
    global xo4C
    global xo5C
    global xo6C
    global xo7C
    global xo8C
    global xo9C
    # x or o placement
    if x < -5 and x > -65 and y > 5 and y < 65:
        if xo1C == 0:
            if isX == True:
                xo1.shape("turtle")
                isX = False
                xo1C = 1
            else:
                xo1.shape("circle")
                isX = True
                xo1C = 2
    if x < 65 and x > 5 and y > 5 and y < 65:
        if xo2C == 0:
            if isX == True:
                xo2.shape("turtle")
                isX = False
                xo2C = 1
            else:
                xo2.shape("circle")
                isX = True
                xo2C = 2
    if x < 135 and x > 75 and y > 5 and y < 65:
        if xo3C == 0:
            if isX == True:
                xo3.shape("turtle")
                isX = False
                xo3C = 1
            else:
                xo3.shape("circle")
                isX = True
                xo3C = 2
    if x < -5 and x > -65 and y > -65 and y < -5:
        if xo4C == 0:
            if isX == True:
                xo4.shape("turtle")
                isX = False
                xo4C = 1
            else:
                xo4.shape("circle")
                isX = True
                xo4C = 2
    if x < 65 and x > 5 and y > -65 and y < -5:
        if xo5C == 0:
            if isX == True:
                xo5.shape("turtle")
                isX = False
                xo5C = 1
            else:
                xo5.shape("circle")
                isX = True
                xo5C = 2
    if x < 135 and x > 75 and y > -65 and y < -5:
        if xo6C == 0:
            if isX == True:
                xo6.shape("turtle")
                isX = False
                xo6C = 1
            else:
                xo6.shape("circle")
                isX = True
                xo6C = 2
    if x < -5 and x > -65 and y > -135 and y < -75:
        if xo7C == 0:
            if isX == True:
                xo7.shape("turtle")
                isX = False
                xo7C = 1
            else:
                xo7.shape("circle")
                isX = True
                xo7C = 2
    if x < 65 and x > 5 and y > -135 and y < -75:
        if xo8C == 0:
            if isX == True:
                xo8.shape("turtle")
                isX = False
                xo8C = 1
            else:
                xo8.shape("circle")
                isX = True
                XO8C = 2
    if x < 135 and x > 75 and y > -135 and y < -75:
        if xo9C == 0:
            if isX == True:
                xo9.shape("turtle")
                isX = False
                xo9C = 1
            else:
                xo9.shape("circle")
                isX = True
                xo9C = 2
    WinCheck()


prboard()
scrn.onclick(onclickSquare)

turtle.mainloop()
