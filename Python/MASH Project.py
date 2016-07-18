from random import *

houseVar=raw_input("What kind of house do you want to live in?")
childrenVar=raw_input("How many children would you like?")
spouseVar=raw_input("Who is your ideal spouse?")
locationVar=raw_input("Where do you want to live?")
jobVar=raw_input("What would you like to be your job?")
salaryVar=raw_input("How much money do you want to make a year?")

House=["Mansion", "Apartment", "Shack", "House", "Shoe", houseVar]
Children=["one", "two", "fifty", "no", "negative", childrenVar]
Spouse=["Kate Upton", "Jack Black", "Leo DiCaprio", "Bill Gates", "a hobo", spouseVar]
Location=["New York", "Russia", "Antarctica", "Space", locationVar]
Job=["Janitor", "Doctor", "Hobo", "Coder", "Uber Driver", "President", jobVar]
Salary=["$0", "$10", "$10,000", "$100,000", "$1,000,000", "a dollop of lotion", salaryVar]

numHouse=randrange(69)
finalHouse=House[numHouse]
numChildren=randrange(6)
finalChildren=Children[numChildren]
numSpouse=randrange(6)
finalSpouse=Spouse[numSpouse]
numLocation=randrange(6)
finalLocation=Location[numLocation]
numJob=randrange(6)
finalJob=Job[numJob]
numSalary=randrange(6)
finalSalary=Salary[numSalary]
print("You will live in a "+finalHouse+" in "+finalLocation+" with "+finalChildren+" kids, making "+finalSalary+" as a "+finalJob+" while married to "+finalSpouse)