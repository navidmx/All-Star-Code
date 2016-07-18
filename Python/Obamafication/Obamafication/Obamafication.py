#Obamafication - Navid
from Myro import *

image=input("Pick a superhero!") #User's input

pic=makePicture(image+".jpg") #Scan picture
pix=getPixels(pic) #Get pixels of picture

ObamaDarkBlue = makeColor(0,51,76) #Dark Blue value
ObamaRed = makeColor(217, 26, 33) #Red Value
ObamaBlue = makeColor(112,150,158) #Blue Value
ObamaYellow = makeColor(252, 227, 166)

show(pic) #Show the original picture
wait(1) #Wait before changing pixels

for i in pix: #Conditionals per value
    if getGray(i)>180:
        setColor(i,ObamaYellow)
    elif getGray(i)>120 and getGray<=180:
        setColor(i,ObamaBlue)
    elif getGray(i)>60 and getGray(i)<=120:
        setColor(i,ObamaRed)    
    else:
        setColor(i,ObamaDarkBlue)
        
show(pic) #Show the new picture