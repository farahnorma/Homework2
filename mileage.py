#Norma
#mileage.py

#Write a program that will compute MPG for a
# car.
# Prompt the user to enter the number of
# miles driven and the number of gallons
# used.
#Print a nice message with the answer.

miles = float(input("Number of miles driven: "))
gal = float(input("Number of gallons used: "))

def mileage(miles, gal):
    result = miles/gal
    return result

answer = mileage(miles, gal)
print("You're mileage is ", answer, " mpg")