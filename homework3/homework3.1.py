#Homework 3 Project 1
#Sept. 24 2020

#Write a function that converts temperature from 
#Fahrenheit to Celsius using formula

def tempConvert(tempF):
   return ((5/9) * (tempF - 32))



#Test converter

tempC = tempConvert(68)
print(tempC, "C")
