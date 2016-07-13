from Myro import *
from Graphics import *
import math
sides=int(input("How many sides in your shape?"))
length=int(input("What is the length of each side?"))
angle=360/sides
print(angle)
sim = Simulation("My World", 600, 600, Color("white"))
sim.setup()
makeRobot("SimScribbler", sim)
penDown("blue")
while sides>0:
    forward(1,length)
    turnBy(angle)
    sides=sides-1
penUp()