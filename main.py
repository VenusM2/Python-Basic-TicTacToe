'''
KNOWN BUGS TO FIX AND FEATURES
------------------
* AI...?
------------------
--GENERAL NOTICE--
------------------
X's number value here is usually 1, while 0's number value is usually 2

if you find any place that takes X as 2 or O as 1 in any variable report it to me I will fix that

'''

import turtle
import random

# previous winner to choose who will be the next first player
rng = random.randint(1, 2)

# setup screen and play
scrn = turtle.Screen()
scrn.bgcolor("red")
scrn.title("TicTacToe")

scrn.addshape('x.gif')
scrn.addshape('o.gif')

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
# score variable setup
xwinstat = 0
owinstat = 0

xstatplayer = turtle.Turtle()
ostatplayer = turtle.Turtle()
xstatplayer.penup()
ostatplayer.penup()
xstatplayer.goto(40, -175)
ostatplayer.goto(40, -200)
xstatplayer.hideturtle()
ostatplayer.hideturtle()
# Winner announcer
wina = turtle.Turtle()
wina.hideturtle()
wina.penup()
wina.setpos(40, 200)
# Helps wina turtle declare the winner, 1 is X and 2 is O
whowon = 0
# prevents duplicate announcements
wasWon = False

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
# Replay button
scrn.addshape('retry.gif')
replay = turtle.Turtle()
replay.penup()
replay.shape('retry.gif')
replay.shapesize(0.2)
replayable = False
# checks for win after every click on the board
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

    global xwinstat
    global owinstat
    global rng
    global whowon
    global wasWon
    global replayable
    if whowon == 0:
        # checks if X won in any way
        # horizontal line check for x
        if xo1C == 1 and xo2C == 1 and xo3C == 1:
            whowon = 1
        elif xo4C == 1 and xo5C == 1 and xo6C == 1:
            whowon = 1
        elif xo7C == 1 and xo8C == 1 and xo9C == 1:
            whowon = 1
        # curved lines check for x
        elif xo1C == 1 and xo5C == 1 and xo9C == 1:
            whowon = 1
        elif xo7C == 1 and xo5C == 1 and xo3C == 1:
            whowon = 1
        # vertical lines check for x
        elif xo1C == 1 and xo4C == 1 and xo7C == 1:
            whowon = 1
        elif xo2C == 1 and xo5C == 1 and xo8C == 1:
            whowon = 1
        elif xo3C == 1 and xo6C == 1 and xo9C == 1:
            whowon = 1
        # checks if O won in any way
        # horizontal lines check for o
        elif xo1C == 2 and xo2C == 2 and xo3C == 2:
            whowon = 2
        elif xo4C == 2 and xo5C == 2 and xo6C == 2:
            whowon = 2
        # curved lines check for o
        elif xo7C == 2 and xo8C == 2 and xo9C == 2:
            whowon = 2
        elif xo1C == 2 and xo5C == 2 and xo9C == 2:
            whowon = 2
        elif xo7C == 2 and xo5C == 2 and xo3C == 2:
            whowon = 2
        # vertical lines check for o
        elif xo1C == 2 and xo4C == 2 and xo7C == 2:
            whowon = 2
        elif xo2C == 2 and xo5C == 2 and xo8C == 2:
            whowon = 2
        elif xo3C == 2 and xo6C == 2 and xo9C == 2:
            whowon = 2


    if whowon != 0 and wasWon == False:
        xo1C = 3
        xo2C = 3
        xo3C = 3
        xo4C = 3
        xo5C = 3
        xo6C = 3
        xo7C = 3
        xo8C = 3
        xo9C = 3
        if rng == 1:
            rng = 2
        elif rng == 2:
            rng = 1
        if whowon == 1:
            print("X won")
            wasWon = True
            wina.clear()
            wina.write("X is the WINNER", align='center',font=('arial',40,'normal'))
            replay.write('Replay', align='center', font=('arial', 10, 'normal'))
            replay.showturtle()
            replay.goto(35, 135)
            replayable = True
            xwinstat += 1
        elif whowon == 2:
            print("O won")
            wasWon = True
            wina.clear()
            wina.write("O is the WINNER", align='center', font=('arial', 40, 'normal'))
            replay.write('Replay', align='center')
            replay.showturtle()
            replay.goto(35, 135)
            replayable = True
            owinstat += 1

    if xo1C != 0 and xo2C != 0 and xo3C != 0 and xo4C != 0 and xo5C != 0 and xo6C != 0 and xo7C != 0 and xo8C != 0 and xo9C != 0 and replayable == False:
        print("DRAW")
        wasWon = True
        wina.clear()
        wina.write("DRAW", align='center', font=('arial', 40, 'normal'))
        replay.write('Replay', align='center', font=('arial', 10, 'normal'))
        replay.showturtle()
        replay.goto(35, 135)
        replayable = True

# after clicking the replay button or when you open the program the board "prepares" itself
def prboard():
    global ystart
    global xo1C
    global xo2C
    global xo3C
    global xo4C
    global xo5C
    global xo6C
    global xo7C
    global xo8C
    global xo9C
    global replayable
    global xstart
    global playerbox
    global whowon
    global wasWon
    global xwinstat
    global owinstat
    global isX
    global rng

    xstatplayer.clear()
    ostatplayer.clear()
    xstatplayer.write('X wins : ' + str(xwinstat), align='center', font=('arial',15,'normal'))
    ostatplayer.write('O wins : ' + str(owinstat), align='center', font=('arial',15,'normal'))

    wasWon = False
    whowon = 0
    ystart = 70
    xstart = -70

    # Is it X's turn or O's turn
    isX = False
    if rng == 2:
        isX = False
    if rng == 1:
        isX = True

    replayable = False
    playerbox.clear()
    wina.clear()
    replay.clear()
    replay.hideturtle()
    replay.goto(35, 170)
    for item in range(3):
        playerbox.sety(ystart)
        playerbox.setx(-70)
        for item in range(3):
            for item in range(4):
                playerbox.forward(70)
                playerbox.right(90)
            playerbox.forward(70)
        ystart = ystart - 70

    xo1.shape("square")
    xo2.shape("square")
    xo3.shape("square")
    xo4.shape("square")
    xo5.shape("square")
    xo6.shape("square")
    xo7.shape("square")
    xo8.shape("square")
    xo9.shape("square")
    xo1.setpos(-35,35)
    xo2.setpos(35, 35)
    xo3.setpos(105, 35)
    xo4.setpos(-35, -35)
    xo5.setpos(35, -35)
    xo6.setpos(105, -35)
    xo7.setpos(-35, -105)
    xo8.setpos(35, -105)
    xo9.setpos(105, -105)
    xo1C = 0
    xo2C = 0
    xo3C = 0
    xo4C = 0
    xo5C = 0
    xo6C = 0
    xo7C = 0
    xo8C = 0
    xo9C = 0



    if isX == True:
        wina.write("X is the first", align='center',font=('arial',40,'normal'))
    if isX == False:
        wina.write("O is the first", align='center',font=('arial',40,'normal'))

# everytime you click the screen this method is called
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
                xo1.shape("x.gif")
                isX = False
                xo1C = 1
            else:
                xo1.shape("o.gif")
                isX = True
                xo1C = 2
    elif x < 65 and x > 5 and y > 5 and y < 65:
        if xo2C == 0:
            if isX == True:
                xo2.shape("x.gif")
                isX = False
                xo2C = 1
            else:
                xo2.shape("o.gif")
                isX = True
                xo2C = 2
    elif x < 135 and x > 75 and y > 5 and y < 65:
        if xo3C == 0:
            if isX == True:
                xo3.shape("x.gif")
                isX = False
                xo3C = 1
            else:
                xo3.shape("o.gif")
                isX = True
                xo3C = 2
    elif x < -5 and x > -65 and y > -65 and y < -5:
        if xo4C == 0:
            if isX == True:
                xo4.shape("x.gif")
                isX = False
                xo4C = 1
            else:
                xo4.shape("o.gif")
                isX = True
                xo4C = 2
    elif x < 65 and x > 5 and y > -65 and y < -5:
        if xo5C == 0:
            if isX == True:
                xo5.shape("x.gif")
                isX = False
                xo5C = 1
            else:
                xo5.shape("o.gif")
                isX = True
                xo5C = 2
    elif x < 135 and x > 75 and y > -65 and y < -5:
        if xo6C == 0:
            if isX == True:
                xo6.shape("x.gif")
                isX = False
                xo6C = 1
            else:
                xo6.shape("o.gif")
                isX = True
                xo6C = 2
    elif x < -5 and x > -65 and y > -135 and y < -75:
        if xo7C == 0:
            if isX == True:
                xo7.shape("x.gif")
                isX = False
                xo7C = 1
            else:
                xo7.shape("o.gif")
                isX = True
                xo7C = 2
    elif x < 65 and x > 5 and y > -135 and y < -75:
        if xo8C == 0:
            if isX == True:
                xo8.shape("x.gif")
                isX = False
                xo8C = 1
            else:
                xo8.shape("o.gif")
                isX = True
                xo8C = 2
    elif x < 135 and x > 75 and y > -135 and y < -75:
        if xo9C == 0:
            if isX == True:
                xo9.shape("x.gif")
                isX = False
                xo9C = 1
            else:
                xo9.shape("o.gif")
                isX = True
                xo9C = 2

    # checks if clicked on replay button
    elif x < 61 and x > 8 and y > 108 and y < 169:
        if replayable == True:
            prboard()
            print("game restart")

    WinCheck()

# board preperation on first start
prboard()

# on click function

scrn.onclick(onclickSquare)

# mainloop to keep the app running
turtle.mainloop()
