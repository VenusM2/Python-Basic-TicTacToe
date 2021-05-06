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
import winsound
import asyncio
# previous winner to choose who will be the next first player
rng = random.randint(1, 2)
# list for the X or O variables
xnum = ['xo1','xo2','xo3','xo4','xo5','xo6','xo7','xo8','xo9']
b1color = ['orange','yellow','green','blue']
b2color = ['yellow','green','blue','orange']
b3color = ['green','blue','orange','yellow']
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
for i in range(0, 9, 1):
    xnum[i] = turtle.Turtle()
    xnum[i].shape('square')
    xnum[i].shapesize(2)
    xnum[i].speed(0)
    xnum[i].penup()
# score variable setup
xwinstat = 0
owinstat = 0

xstatplayer = turtle.Turtle()
ostatplayer = turtle.Turtle()
xstatplayer.speed(0)
ostatplayer.speed(0)
xstatplayer.penup()
ostatplayer.penup()
xstatplayer.goto(40, -180)
ostatplayer.goto(40, -225)
xstatplayer.hideturtle()
ostatplayer.hideturtle()
# Winner announcer
wina = turtle.Turtle()
wina.speed(0)
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

def RainbowColor(b1,b2,b3):
    print('WIP not ready yet')
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
            RainbowColor(0,1,2)
        elif xo4C == 1 and xo5C == 1 and xo6C == 1:
            whowon = 1
            RainbowColor(3,4,5)
        elif xo7C == 1 and xo8C == 1 and xo9C == 1:
            whowon = 1
            RainbowColor(6,7,8)
        # curved lines check for x
        elif xo1C == 1 and xo5C == 1 and xo9C == 1:
            whowon = 1
            RainbowColor(0,4,8)
        elif xo7C == 1 and xo5C == 1 and xo3C == 1:
            whowon = 1
            RainbowColor(6,4,2)
        # vertical lines check for x
        elif xo1C == 1 and xo4C == 1 and xo7C == 1:
            whowon = 1
            RainbowColor(0,3,6)
        elif xo2C == 1 and xo5C == 1 and xo8C == 1:
            whowon = 1
            RainbowColor(1,4,7)
        elif xo3C == 1 and xo6C == 1 and xo9C == 1:
            whowon = 1
            RainbowColor(2,5,8)
        # checks if O won in any way
        # horizontal lines check for o
        elif xo1C == 2 and xo2C == 2 and xo3C == 2:
            whowon = 2
            RainbowColor(0,1,2)
        elif xo4C == 2 and xo5C == 2 and xo6C == 2:
            whowon = 2
            RainbowColor(3,4,5)
        # curved lines check for o
        elif xo7C == 2 and xo8C == 2 and xo9C == 2:
            whowon = 2
            RainbowColor(6,7,8)
        elif xo1C == 2 and xo5C == 2 and xo9C == 2:
            whowon = 2
            RainbowColor(0,4,8)
        elif xo7C == 2 and xo5C == 2 and xo3C == 2:
            whowon = 2
            RainbowColor(6,4,2)
        # vertical lines check for o
        elif xo1C == 2 and xo4C == 2 and xo7C == 2:
            whowon = 2
            RainbowColor(0,3,6)
        elif xo2C == 2 and xo5C == 2 and xo8C == 2:
            whowon = 2
            RainbowColor(1,4,7)
        elif xo3C == 2 and xo6C == 2 and xo9C == 2:
            whowon = 2
            RainbowColor(2,5,8)


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
            wina.write("X is the WINNER", align='center',font=('Comic Sans MS Bold', 40,'normal'))
            replay.write('Replay', align='center', font=('arial', 10, 'normal'))
            replay.showturtle()
            replay.goto(35, 135)
            replayable = True
            xwinstat += 1
            xstatplayer.clear()
            xstatplayer.write('X wins : ' + str(xwinstat), align='center', font=('Comic Sans MS Bold', 20, 'normal'))
        elif whowon == 2:
            print("O won")
            wasWon = True
            wina.clear()
            wina.write("O is the WINNER", align='center', font=('Comic Sans MS Bold', 40, 'normal'))
            replay.write('Replay', align='center')
            replay.showturtle()
            replay.goto(35, 135)
            replayable = True
            owinstat += 1
            ostatplayer.clear()
            ostatplayer.write('O wins : ' + str(owinstat), align='center', font=('Comic Sans MS Bold', 20, 'normal'))

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
ostatplayer.write('O wins : ' + str(owinstat), align='center', font=('Comic Sans MS Bold', 20, 'normal'))
xstatplayer.write('X wins : ' + str(owinstat), align='center', font=('Comic Sans MS Bold', 20, 'normal'))
for item in range(3):
    playerbox.sety(ystart)
    playerbox.setx(-70)
    for item in range(3):
        for item in range(4):
            playerbox.forward(70)
            playerbox.right(90)
        playerbox.forward(70)
    ystart = ystart - 70
def prboard():
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
    global playerbox
    global whowon
    global wasWon
    global xwinstat
    global owinstat
    global isX
    global rng
    wasWon = False
    whowon = 0
    # Is it X's turn or O's turn
    isX = False
    if rng == 2:
        isX = False
    if rng == 1:
        isX = True
    replayable = False
    wina.clear()
    replay.clear()
    replay.hideturtle()
    replay.goto(35, 170)


    for i in range(0, 9, 1):
        xnum[i].shape('square')
    xnum[0].setpos(-35,35)
    xnum[1].setpos(35, 35)
    xnum[2].setpos(105, 35)
    xnum[3].setpos(-35, -35)
    xnum[4].setpos(35, -35)
    xnum[5].setpos(105, -35)
    xnum[6].setpos(-35, -105)
    xnum[7].setpos(35, -105)
    xnum[8].setpos(105, -105)
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
        wina.write("X is the first", align='center',font=('Comic Sans MS Bold', 40,'normal'))
    if isX == False:
        wina.write("O is the first", align='center',font=('Comic Sans MS Bold', 40,'normal'))

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
    winsound.PlaySound('ClickingSound.wav', winsound.SND_ASYNC)
    # x or o placement
    if x < -5 and x > -65 and y > 5 and y < 65:
        if xo1C == 0:
            if isX == True:
                xnum[0].shape("x.gif")
                isX = False
                xo1C = 1
            else:
                xnum[0].shape("o.gif")
                isX = True
                xo1C = 2
    elif x < 65 and x > 5 and y > 5 and y < 65:
        if xo2C == 0:
            if isX == True:
                xnum[1].shape("x.gif")
                isX = False
                xo2C = 1
            else:
                xnum[1].shape("o.gif")
                isX = True
                xo2C = 2
    elif x < 135 and x > 75 and y > 5 and y < 65:
        if xo3C == 0:
            if isX == True:
                xnum[2].shape("x.gif")
                isX = False
                xo3C = 1
            else:
                xnum[2].shape("o.gif")
                isX = True
                xo3C = 2
    elif x < -5 and x > -65 and y > -65 and y < -5:
        if xo4C == 0:
            if isX == True:
                xnum[3].shape("x.gif")
                isX = False
                xo4C = 1
            else:
                xnum[3].shape("o.gif")
                isX = True
                xo4C = 2
    elif x < 65 and x > 5 and y > -65 and y < -5:
        if xo5C == 0:
            if isX == True:
                xnum[4].shape("x.gif")
                isX = False
                xo5C = 1
            else:
                xnum[4].shape("o.gif")
                isX = True
                xo5C = 2
    elif x < 135 and x > 75 and y > -65 and y < -5:
        if xo6C == 0:
            if isX == True:
                xnum[5].shape("x.gif")
                isX = False
                xo6C = 1
            else:
                xnum[5].shape("o.gif")
                isX = True
                xo6C = 2
    elif x < -5 and x > -65 and y > -135 and y < -75:
        if xo7C == 0:
            if isX == True:
                xnum[6].shape("x.gif")
                isX = False
                xo7C = 1
            else:
                xnum[6].shape("o.gif")
                isX = True
                xo7C = 2
    elif x < 65 and x > 5 and y > -135 and y < -75:
        if xo8C == 0:
            if isX == True:
                xnum[7].shape("x.gif")
                isX = False
                xo8C = 1
            else:
                xnum[7].shape("o.gif")
                isX = True
                xo8C = 2
    elif x < 135 and x > 75 and y > -135 and y < -75:
        if xo9C == 0:
            if isX == True:
                xnum[8].shape("x.gif")
                isX = False
                xo9C = 1
            else:
                xnum[8].shape("o.gif")
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
