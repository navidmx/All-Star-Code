#Battleship - Navid and Ike

from random import *
grid=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
j=0
gameOver=False
amount=0
missed=0
#0 = water, 1 = missed, 2 = ship, 3 = hit

def createShip():
    shipX=randrange(0,5)
    shipY=randrange(0,5)
    grid[shipX][shipY]=2
    direction=randrange(0,3)
    if direction==0 and shipX+1<=5 and (grid[shipX+1][shipY])!=2:
        grid[shipX+1][shipY]=2
    elif direction==1 and shipX-1>=0 and (grid[shipX-1][shipY])!=2:
        grid[shipX-1][shipY]=2
    elif direction==2 and shipY+1<=5 and (grid[shipX][shipY+1])!=2:
        grid[shipX][shipY+1]=2
    elif direction==3 and shipY-1>=0 and (grid[shipX][shipY-1])!=2:
        grid[shipX][shipY-1]=2

def setup():
    for i in range(randrange(2,4)):
        createShip()
    size(610,670)

def refresh():
    global amount
    global missed
    background(0,154,205)
    amount=0
    missed=0
    for x in range(len(grid)):
        for i in range(len(grid[x])):
            if grid[x][i]==0: #Water
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
            if grid[x][i]==1: #Missed
                missed+=1
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
                stroke(209,238,238)
                strokeWeight(5)
                ellipseMode(CENTER)
                ellipse((i*100+55),(x*100+55),70,70)
                ellipse((i*100+55),(x*100+55),30,30)
                noStroke()
            if grid[x][i]==2: #Hidden Ship
                amount+=1
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
            if grid[x][i]==3: #Hit Ship
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
                stroke(255,0,0)
                strokeWeight(5)
                ellipseMode(CENTER)
                ellipse((i*100+55),(x*100+55),70,70)
                ellipse((i*100+55),(x*100+55),30,30)
                noStroke()
            
def mouseClicked():
     for x in range(len(grid)):
            for i in range(len(grid[x])):
                if mouseX>=(i*100+10) and mouseX<=(i*100+100) and mouseY>=(x*100+10) and mouseY<=(x*100+100):
                    if grid[x][i]==0:
                        grid[x][i]=1
                    elif grid[x][i]==1:
                        grid[x][i]==1
                    elif grid[x][i]==2:
                        grid[x][i]=3

def draw():
    global gameOver
    if gameOver==False:
        global j
        noStroke()
        refresh()
        fill(0)
        textSize(36)
        textAlign(CENTER)
        text("Ships="+str(amount),500,645)
        text("Missed="+str(missed),115,645)
        if mouseX and mouseY:
            fill(255)
            ellipse(mouseX,mouseY,15,15)
            fill(255,0,0)
            ellipse(mouseX,mouseY,5,5)
        if amount==0:
            fill(0)
            text("You WIN!",305,310)
            gameOver=True