#Space Invaders - Navid, Richard, and Michel

from random import *
shipX=300 #Default shipX
bulletX=0
alienBulletX=0
bulletY=-10
alienBulletY=610
tempX=0
alienTempX=0
alienX=100
alienY=150
score=0
lives=3
bulletOnScreen=False
alienBulletOnScreen=False
activateBullet=False
alienActivateBullet=False
gameOver=False
gameStart=False
gameWin=False
aliens=[[3,3,3,3,3],[2,2,2,2,2],[1,1,1,1,1]] #Grid of aliens
alienRight=True #Aliens start moving right

#Sets up Window
def setup():
    size(600,600)

#Bullet fired event
def bullet():
    global bulletOnScreen
    global activateBullet
    global tempX
    global bulletY
    if keyPressed==True and key==' ' and bulletOnScreen==False:
        tempX=shipX #Stores the current shipX, therefore not moving with bullet
        bulletY=470
        bulletOnScreen=True #Check if bullet is currently on screen
        activateBullet=True #Checks if bullet is shot
    return tempX
    return bulletY

#Create the bullet
def createBullet():
    global bulletX
    global bulletY
    global tempX
    fill(255)
    bulletX=tempX
    rect(bulletX,bulletY,3,15)
    bulletY=bulletY-10
    
#Alien bullet fired event
def alienBullet():
    global alienBulletOnScreen
    global alienActivateBullet
    global alienTempX
    global alienBulletY
    aX=randrange(5)
    aY=randrange(3)
    if alienActivateBullet==False and aliens[aY][aX]!=0:
        alienBulletY=610
        alienTempX=(alienX+aX*100) #Stores the current shipX, therefore not moving with bullet
        alienBulletY=(alienY+aY*50)
        alienBulletOnScreen=True #Check if bullet is currently on screen
        alienActivateBullet=True #Checks if bullet is shot
        return alienTempX
        return alienBulletY

#Create the alien bullet
def alienCreateBullet():
    global alienBulletX
    global alienBulletY
    global alienTempX
    fill(255,0,0)
    alienBulletX=alienTempX
    rect(alienBulletX,alienBulletY,3,15)
    alienBulletY=alienBulletY+7
    
#Create each row of aliens
def alienRow():
    global alienX
    global alienY
    global bulletX
    global bulletY
    global score
    for x in range(len(aliens)): #Checks through grid of aliens to draw
        for i in range(len(aliens[x])):
            if aliens[x][i]==1: #Default value of alien, draws it
                fill(255)
                rect(alienX+(i*100),alienY+(x*50),40,20) #Alien main body
                rect((alienX-10)+(i*100),(alienY-10)+(x*50),10,10) #"Ears"
                rect((alienX+10)+(i*100),(alienY-10)+(x*50),10,10)
                fill(0)
                rect((alienX-10)+(i*100),alienY+(x*50),8,5) #"Eyes"
                rect((alienX+10)+(i*100),alienY+(x*50),8,5)
            if aliens[x][i]==2: #Default value of alien, draws it
                fill(255)
                rect(alienX+(i*100),alienY+(x*50),40,20) #Alien main body
                rect((alienX-10)+(i*100),(alienY-10)+(x*50),10,10) #"Ears"
                rect((alienX+10)+(i*100),(alienY-10)+(x*50),10,10)
                rect((alienX-20)+(i*100),(alienY-18)+(x*50),10,5)
                rect((alienX+20)+(i*100),(alienY-18)+(x*50),10,5)
                fill(0)
                rect((alienX)+(i*100),alienY+5+(x*50),8,5) #"Eyes"
                rect((alienX-10)+(i*100),alienY+(x*50),8,5)
                rect((alienX+10)+(i*100),alienY+(x*50),8,5)
            if aliens[x][i]==3: #Default value of alien, draws it
                fill(255)
                rect(alienX+(i*100),alienY+(x*50),40,20) #Alien main body
                rect((alienX-10)+(i*100),(alienY-10)+(x*50),10,10) #"Ears"
                rect((alienX+10)+(i*100),(alienY-10)+(x*50),10,10)
                rect((alienX-15)+(i*100),(alienY-17)+(x*50),20,5)
                rect((alienX+15)+(i*100),(alienY-17)+(x*50),20,5)
                fill(0)
                rect((alienX)+(i*100),alienY+(x*50),20,5) #"Eyes"
            if bulletX>=((alienX-20)+(i*100)) and bulletX<=((alienX+20)+(i*100)) and bulletY==(alienY+(x*50)+10) and aliens[x][i]==1:
                aliens[x][i]=0 #Sets alien value to 0, therefore not drawing it
                score+=10
                bulletX=0 #Makes bullet disappear after alien shot
                bulletY=-10
            if bulletX>=((alienX-20)+(i*100)) and bulletX<=((alienX+20)+(i*100)) and bulletY==(alienY+(x*50)+10) and aliens[x][i]==2:
                aliens[x][i]=0 #Sets alien value to 1, therefore not drawing it
                score+=20
                bulletX=0 #Makes bullet disappear after alien shot
                bulletY=-10
            if bulletX>=((alienX-20)+(i*100)) and bulletX<=((alienX+20)+(i*100)) and bulletY==(alienY+(x*50)+10) and aliens[x][i]==3:
                aliens[x][i]=0 #Sets alien value to 1, therefore not drawing it
                score+=30
                bulletX=0 #Makes bullet disappear after alien shot
                bulletY=-10
                
#Controls alien animation
def alienDance():
    global alienX
    global alienY
    global alienRight
    if alienRight==True: #Decides if alien is moving right
        alienX+=1
    else:
        alienX-=1
    if alienX+440==600: #If alien hits right side, move left
        alienRight=False
        for i in range(10):
            alienY+=1
    elif alienX==40: #If alien hits left side, move right
        alienRight=True
        for i in range(10):
            alienY+=1
            
#Creates ship, ship bullets, and starts alienDance animation
def draw():
    global shipX
    global bulletY
    global bulletOnScreen
    global activateBullet
    global alienActivateBullet
    global alienX
    global alienBulletX
    global alienBulletY
    global lives
    global gameOver
    global gameStart
    global gameWin
    font=loadFont("SpaceInvaders.vlw")
    if gameStart==False:
        background(0)
        textAlign(CENTER)
        textFont(font,32)
        fill(124,252,0)
        text("SPACE INVADERS", 300, 300)
        fill(255)
        textFont(font,16)
        text("Press space to start", 300, 340)
        textFont(font,14)
        text("Developed by Navid, Richard, and Michel", 300, 575)
        if keyPressed==True and key==' ':
            gameStart=True
    if gameStart==True:
        if gameOver==False and gameWin==False:
            noStroke()
            rectMode(CENTER)
            background(0)
            textFont(font,16)
            textAlign(LEFT)
            fill(255)
            text("Lives",465,50)
            text("Score",50,50)
            fill(124,252,0) #Neon Green
            text(str(lives),535,50)
            text(str(score),120,50)
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
            bullet() #Repeats bullet functions
            alienBullet()
            alienRow() #Rows of aliens
            if bulletY>=50:
                bulletOnScreen=True  
            elif bulletY<0:
                bulletOnScreen=False
                activateBullet=False
            if activateBullet==True:
                createBullet()
            if alienBulletY<=550:
                alienBulletOnScreen=True  
            if alienBulletY>600:
                alienBulletOnScreen=False
                alienActivateBullet=False
            if alienActivateBullet==True:
                alienCreateBullet()
            if alienBulletX>shipX-25 and alienBulletX<shipX+25 and alienBulletY>480:
                lives-=1
                alienBulletX=0
                alienBulletY=610
            if lives==0:
                gameOver=True
            if score==300:
                gameWin=True
            alienDance()
        if gameOver==True:
            rectMode(CORNER)
            textFont(font,16)
            fill(0)
            rect(0,0,600,400)
            rectMode(CENTER)
            fill(255)
            text("Lives",465,50)
            text("Score",50,50)
            fill(124,252,0) #Neon Green
            text(str(lives),535,50)
            text(str(score),120,50)
            fill(255,0,0)
            textFont(font,32)
            text("GAME OVER",200,300)
        if gameWin==True:
            rectMode(CORNER)
            textFont(font,16)
            fill(0)
            rect(0,0,600,400)
            rectMode(CENTER)
            fill(255)
            text("Lives",465,50)
            text("Score",50,50)
            fill(124,252,0) #Neon Green
            text(str(lives),535,50)
            text(str(score),120,50) 
            textFont(font,32)
            text("YOU WIN!",230,300)