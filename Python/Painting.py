from Processing import *

window(800,500)
fill(255)
rect(100,0,600,500)

#Left side controls - WEIGHT/ERASE
stroke(150)
strokeWeight(5)
ellipseMode(CENTER)
fill(0)
ellipse(48,50,30,30) #Width 1
fill(0)
ellipse(48,150,40,40) #Width 2
fill(0)
ellipse(48,250,50,50) #Width 3
fill(255,192,203)
rect(23,325,50,50) #Erase
stroke(255,0,0)
strokeWeight(8)
line(23,425,73,475) #Reset
line(23,475,73,425)
stroke(255,0,0)

#Right side controls - COLORS
stroke(150)
strokeWeight(5)
ellipseMode(CENTER)
fill(255,0,0)
ellipse(752,50,60,60) #Red
fill(0,0,255)
ellipse(752,150,60,60) #Blue
fill(255,255,0)
ellipse(752,250,60,60) #Yellow
fill(0,255,0)
ellipse(752,350,60,60) #Green
fill(0)
ellipse(752,450,60,60) #Black
fill(0)

#Borders
strokeWeight(5)
stroke(150)
line(100,0,100,500)
line(700,0,700,500)

bold=10
fill(0)

def draw():
    while(True):
        global bold
        strokeWeight(bold)
        if isMousePressed()==True and mouseX()>722 and mouseX()<782 and mouseY()>20 and mouseY()<80:
            stroke(255,0,0)
        if isMousePressed()==True and mouseX()>722 and mouseX()<782 and mouseY()>120 and mouseY()<180:
            stroke(0,0,255)
        if isMousePressed()==True and mouseX()>722 and mouseX()<782 and mouseY()>220 and mouseY()<280:
            stroke(255,255,0)
        if isMousePressed()==True and mouseX()>722 and mouseX()<782 and mouseY()>320 and mouseY()<380:
            stroke(0,255,0)
        if isMousePressed()==True and mouseX()>722 and mouseX()<782 and mouseY()>420 and mouseY()<480:
            stroke(0)
        if isMousePressed()==True and mouseX()>33 and mouseX()<63 and mouseY()>35 and mouseY()<65:
            bold=10
        if isMousePressed()==True and mouseX()>23 and mouseX()<73 and mouseY()>125 and mouseY()<175:
            bold=15
        if isMousePressed()==True and mouseX()>13 and mouseX()<83 and mouseY()>215 and mouseY()<285:
            bold=20
        if isMousePressed()==True and mouseX()>23 and mouseX()<73 and mouseY()>325 and mouseY()<375:
            fill(255)
        if isMousePressed()==True and mouseX()>23 and mouseX()<73 and mouseY()>425 and mouseY()<475:
            noStroke()
            fill(255)
            rect(103,0,597,500)
            fill(0)
            stroke(15)
        if isMousePressed()==True and mouseX()>103 and mouseX()<697:
            line(pmouseX(),pmouseY(),mouseX(),mouseY())
draw()