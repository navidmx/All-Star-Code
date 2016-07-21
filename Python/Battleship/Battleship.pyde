#Battleship - Navid and Ike

from random import *
grid=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] #Board
gameOver=False #Decides whether or not gameOver is true
amount=0 #Amount of ships
missed=0 #Missed shots
#0 = water, 1 = missed, 2 = ship, 3 = hit

def createShip():
    shipX=randrange(0,5) #Randomly decide on an X coord for the ship
    shipY=randrange(0,5) #Randomly decide on a Y coord for the ship
    grid[shipX][shipY]=2 #Set the value of a ship in the board to "2" (ship)
    direction=randrange(0,3) #Randomly decide on a direction for second piece of the ship to go
    if direction==0 and shipX+1<=5:
        grid[shipX+1][shipY]=2
    elif direction==1 and shipX-1>=0:
        grid[shipX-1][shipY]=2
    elif direction==2 and shipY+1<=5:
        grid[shipX][shipY+1]=2
    elif direction==3 and shipY-1>=0:
        grid[shipX][shipY-1]=2

def setup():
    for i in range(randrange(2,4)): #Randomly decide amount of ships
        createShip()
    size(610,670) #Window size

def refresh():
    global amount
    global missed
    background(0,154,205)
    amount=0
    missed=0
    for x in range(len(grid)): #Check through the grid for values
        for i in range(len(grid[x])):
            if grid[x][i]==0: #If value is 0, create water
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
            if grid[x][i]==1: #If value is 1, create ripples (missed)
                missed+=1
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
                stroke(209,238,238)
                strokeWeight(5)
                ellipseMode(CENTER)
                ellipse((i*100+55),(x*100+55),70,70)
                ellipse((i*100+55),(x*100+55),30,30)
                noStroke()
            if grid[x][i]==2: #If value is 2, create hidden ship (looks like water)
                amount+=1
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
            if grid[x][i]==3: #If value is 3, create red target (hit)
                fill(135,206,250)
                rect((i*100+10),(x*100+10),90,90)
                stroke(255,0,0)
                strokeWeight(5)
                ellipseMode(CENTER)
                ellipse((i*100+55),(x*100+55),70,70)
                ellipse((i*100+55),(x*100+55),30,30)
                noStroke()
            
def mouseClicked():
     for x in range(len(grid)): #Check which element the mouse is in
            for i in range(len(grid[x])):
                if mouseX>=(i*100+10) and mouseX<=(i*100+100) and mouseY>=(x*100+10) and mouseY<=(x*100+100):
                    if grid[x][i]==0: #If water clicked, create missed ripples
                        grid[x][i]=1
                    elif grid[x][i]==2: #If hidden ship clicked, create red target
                        grid[x][i]=3

def draw():
    global gameOver
    if gameOver==False: #Loop will only run while gameOver is False (from beginning of game)
        noStroke()
        refresh() #Refresh board each loop, checking for new values
        fill(0)
        textSize(36)
        textAlign(CENTER)
        text("Ships="+str(amount),500,645) #Text for "Ships"
        text("Missed="+str(missed),115,645) #Text for "Missed"
        fill(255) #Cursor
        ellipse(mouseX,mouseY,15,15)
        fill(255,0,0)
        ellipse(mouseX,mouseY,5,5)
        if amount==0:
            fill(0)
            text("You WIN!",305,310)
            gameOver=True #Set gameOver to true, therefore closing the loop