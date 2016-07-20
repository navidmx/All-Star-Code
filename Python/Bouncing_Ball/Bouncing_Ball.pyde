#Bouncing Ball Lab - Navid
from random import *

circleX=float(randrange(50,350))
circleY=float(randrange(50,350))
slopeX=3
slopeY=3
right=choice([True,False])
up=choice([True,False])

def setup():
    size(400,400)

def draw():
    global circleX
    global circleY
    global slopeX
    global slopeY
    i=0
    stroke(255,215,0)
    strokeWeight(20)
    rect(0,0,400,400)
    noStroke()
    fill(0)
    rect(10,10,380,380)
    ellipseMode(CENTER)
    fill(255)
    ellipse(circleX,circleY,50,50)
    circleX=circleX+slopeX
    circleY=circleY+slopeY
    if circleX<=35:
        slopeX=randrange(2,5)
    elif circleX>=365:
        slopeX=randrange(-5,-2)
    if circleY<=35:
        slopeY=randrange(2,5)
    elif circleY>=365:
        slopeY=randrange(-5,-2)