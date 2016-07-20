#Back in Black
from Myro import *
i=0
x=0

def riff1():
    forward(2,.4)
    wait(.5)
    x=0
    while x<2:
        forward(2,.05)
        wait(.001)
        forward(2,.05)
        wait(.6)
        x=x+1
    motors(3,-3,1.4)
    
def riff2():
    forward(2,.4)
    wait(.5)
    x=0
    while x<2:
        forward(2,.05)
        wait(.001)
        forward(2,.05)
        wait(.001)
        forward(2,.05)
        wait(.2)
        x=x+1
    x=0
    while x<4:
        backward(4,.12)
        forward(1,.06)
        x=x+1
    
beep(1,999)
wait(4.01)
    
while i<4: #Verse
    riff1()
    riff2()
    i=i+1
#    while i<6:
#        forward(2, 1.9)
#        motors(-10, 10, .5)
#        i=i+1
    
stop()