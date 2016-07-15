from random import *

houseVar=rawInput("What kind of house do you want to live in?")
childrenVar=rawInput("How many children would you like?")
spouseVar=rawInput("Who is your ideal spouse?")
locationVar=rawInput("Where do you want to live?")
jobVar=rawInput("What would you like to be your job?")
salaryVar=rawInput("How much money do you want to make a year?")

House=["Mansion", "Apartment", "Shack", "House", "Shoe", houseVar]
Children=["one", "two", "fifty", "no", "negative", childrenVar]
Spouse=["Kate Upton", "Jack Black", "Leo DiCaprio", "Bill Gates", "a hobo", spouseVar]
Location=["New York", "Russia", "Antarctica", "Space", locationVar]
Job=["Janitor", "Doctor", "Hobo", "Coder", "Uber Driver", "President", jobVar]
Salary=["$0", "$10", "$10,000", "$100,000", "$1,000,000", "a dollop of lotion", salaryVar]