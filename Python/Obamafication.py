#Obamafication - Navid
from Myro import *

pic=makePicture("Batman.jpg")
pix=getPixels(pic)

ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)

for i in pix:
    if getGray(i)>180:
        setColor(i,ObamaYellow)
    elif getGray(i)>120 and getGray<=180:
        setColor(i,ObamaBlue)
    elif getGray(i)>60 and getGray(i)<=120:
        setColor(i,ObamaYellow)    
    else:
        setColor(i,ObamaDarkBlue)
show(pic)