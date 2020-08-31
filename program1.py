#Additional Program
#Aug. 30, 2020
#Create a variable and assign a number to it in a range from 80 to 100
#For the given number, calculate the letter grade

#--------------------------------------------------------------------------
import random

x = random.randint(80, 100)

print("Numerical Grade:\t\t", x)

if (x >= 95 or x == 100):
    print("Letter Grade:\t\tA+")
elif (x >= 90 and x < 95):
    print("Letter Grade:\t\tA")
elif (x >= 85 and x < 90):
    print("Letter Grade:\t\tA-")
else:
    print("Letter Grade:\t\tB+")

