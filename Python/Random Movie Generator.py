#Random Movie Generator - Navid
from random import *

List1=["Screams of a", "In love with a", "Understanding a", "Finding the", "Discovering a", "Adventures of a", "Protecting the", "Saving a", "Defeating the", "Fighting for a"]
List2=["glorious", "disgusting", "smelly", "beautiful", "horrible", "fierce", "mysterious", "dark", "bright", "happy"]
List3=["hyena", "Batman", "Godzilla", "Guardian", "cat", "serpent", "fossil", "city", "bird", "girl"]
NewList1=[]
NewList2=[]
NewList3=[]

i=0
while i<10:
    num=randrange(len(List1))
    element1=List1[num]
    NewList1.append(element1)
    List1.remove(element1)
    num=randrange(len(List2))
    element2=List2[num]
    NewList2.append(element2)
    List2.remove(element2)
    num=randrange(len(List3))
    element3=List3[num]
    NewList3.append(element3)
    List3.remove(element3)
    i=i+1
    print(element1,element2,element3)