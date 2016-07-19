#Bouncing Ball Lab - Navid
from Processing import *
from random import *

window(400,400)
noStroke()
stroke(255,215,0)
strokeWeight(20)
rect(0,0,400,400)
noStroke()

circleX=200
circleY=200
randX=randrange(-1,1)
randY=randrange(-1,1)



def draw():
    while True:
        global circleX
        global circleY
        ellipseMode(CENTER)
        fill(255)
        delay(1)
    
draw()