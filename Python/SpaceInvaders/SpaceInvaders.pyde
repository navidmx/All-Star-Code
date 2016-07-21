#Space Invaders - Navid, Richard, and Michael

shipX=300
bulletX=0
bulletY=470
isBulletReady=True
bulletOnScreen=False
aliens=[[0,0,0,0,0],[0,0,0,0,0]]

def setup():
    size(600,600)

def bullet():
    if keyPressed==True and key==' ':
        fill(255)
        bulletX=shipX
        rect(bulletX,bulletY,3,15)
        bulletOnScreen=True

def draw():
    global shipX
    global bulletY
    noStroke()
    rectMode(CENTER)
    background(0)
    fill(124,252,0) #Neon Green
    rect(shipX,500,60,20) #Main ship body
    rect(shipX,490,10,20) #Ship cannon
    for x in range(len(aliens)):
        for i in range(len(aliens[x])):
            if aliens[x][i]==0:
                fill(255)
                rect(90+(i*100),90,10,10)
                rect(110+(i*100),90,10,10)
                rect(100+(i*100),100,40,20)
                fill(0)
                rect(90+(i*100),100,8,5)
                rect(110+(i*100),100,8,5)
    if keyPressed==True:
        if key=="a": #Move left
            shipX-=5
        elif key=="d": #Move right
            shipX+=5
    bullet()
    if bulletOnScreen==True:
        bulletY+=5