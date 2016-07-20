#Paddle Ball Lab - Navid
from random import *

circleX=float(randrange(50,100))
circleY=float(randrange(50,350))
slopeX=3
slopeY=3
paddle1=160
paddle2=160
right=True

def setup():
    size(600,400)

def draw():
    global circleX
    global circleY
    global slopeX
    global slopeY
    global paddle1
    global paddle2
    global right
    textAlign(CENTER)
    stroke(255,215,0)
    strokeWeight(20)
    rect(-100,0,800,400) #Gold Border
    noStroke()
    fill(0) #Background
    rect(0,10,600,380)
    fill(255,0,0) #Paddle 1
    rect(30,paddle1,20,80)
    fill(0,0,255) #Paddle 2
    rect(550,paddle2,20,80)
    if keyPressed==True: #Key controls
        if right==False:
            if key=='w':
                paddle1-=8
            if key=='s':
                paddle1+=8
        if right==True:
            if keyCode==UP:
                paddle2-=8
            if keyCode==DOWN:
                paddle2+=8
    ellipseMode(CENTER)
    fill(255)
    ellipse(circleX,circleY,30,30) #Ball
    circleX=circleX+slopeX
    circleY=circleY+slopeY
    if circleY<=30:
        slopeY=randrange(2,4)
    elif circleY>=370:
        slopeY=randrange(-4,-2)
    if circleY>=paddle1 and circleY<=(paddle1+80) and circleX<70 and circleX>50: #Paddle 1
        slopeX=randrange(2,4)
        right=True
    if circleY>=paddle2 and circleY<=(paddle2+80) and circleX>530 and circleX<550: #Paddle 2
        slopeX=randrange(-4,-2)
        right=False
    textSize(30)
    if circleX>650:
        fill(255,0,0)
        text("RED wins", 300, 200)
    if circleX<-50:
        fill(0,0,255)
        text("BLUE wins", 300, 200)