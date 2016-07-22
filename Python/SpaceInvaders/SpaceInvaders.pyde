#Space Invaders - Navid, Richard, and Michael

shipX=300
bulletX=0
bulletY=-10
tempX=0
alienX=100
alienY=100
bulletOnScreen=False
activateBullet=False
aliens=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
alienRight=True

def setup():
    size(600,600)

def bullet(): #One bullet
    global bulletOnScreen
    global activateBullet
    global tempX
    global bulletY
    if keyPressed==True and key==' ' and bulletOnScreen==False:
        tempX=shipX
        bulletY=470
        bulletOnScreen=True
        activateBullet=True
    return tempX
    return bulletY

def createBullet():
    global bulletX
    global bulletY
    global tempX
    fill(255)
    bulletX=tempX
    rect(bulletX,bulletY,3,15)
    bulletY=bulletY-15

def alienRow(): #One row of aliens
    global alienX
    global alienY
    global bulletX
    global bulletY
    for x in range(len(aliens)):
        for i in range(len(aliens[x])):
            if aliens[x][i]==0:
                fill(255)
                rect((alienX-10)+(i*100),(alienY-10)+(x*50),10,10)
                rect((alienX+10)+(i*100),(alienY-10)+(x*50),10,10)
                rect(alienX+(i*100),alienY+(x*50),40,20)
                fill(0)
                rect((alienX-10)+(i*100),alienY+(x*50),8,5)
                rect((alienX+10)+(i*100),alienY+(x*50),8,5)
            if aliens[x][i]==1:
                fill(255,0,0)
                rect((alienX-10)+(i*100),(alienY-10)+(x*50),10,10)
                rect((alienX+10)+(i*100),(alienY-10)+(x*50),10,10)
                rect(alienX+(i*100),alienY+(x*50),40,20)
                fill(0)
                rect((alienX-10)+(i*100),alienY+(x*50),8,5)
                rect((alienX+10)+(i*100),alienY+(x*50),8,5)
            if bulletX>=((alienX-20)+(i*100)) and bulletX<=((alienX+20)+(i*100)) and bulletY<=alienY+10 and aliens[x][i]==0:
                aliens[x][i]=1
                bulletX=0
                bulletY=-10
            if bulletX>=((alienX-20)+(i*100)) and bulletX<=((alienX+20)+(i*100)) and bulletY<=alienY+10 and aliens[x][i]==1:
                aliens[x][i]=2

def alienDance():
    global alienX
    global alienY
    global alienRight
    if alienRight==True:
        alienX+=1
    else:
        alienX-=1
    if alienX+440==600:
        alienRight=False
        for i in range(10):
            alienY+=1
    elif alienX==40:
        alienRight=True
        for i in range(10):
            alienY+=1

def draw():
    global shipX
    global bulletY
    global bulletOnScreen
    global activateBullet
    global alienX
    noStroke()
    rectMode(CENTER)
    background(0)
    fill(124,252,0) #Neon Green
    rect(shipX,500,60,20) #Main ship body
    rect(shipX,490,10,20) #Ship cannon
    if keyPressed==True and shipX>30 and shipX<570:
        if key=="a" or key=="A" or keyCode==LEFT: #Move left
            shipX-=5
        elif key=="d" or key=="D" or keyCode==RIGHT: #Move right
            shipX+=5
    if shipX<40:
        shipX=40
    if shipX>560:
        shipX=560
    bullet()
    alienRow()
    if bulletY>=50:
        bulletOnScreen=True
    elif bulletY<0:
        bulletOnScreen=False
        activateBullet==False
    if activateBullet==True:
        createBullet()
    alienDance()