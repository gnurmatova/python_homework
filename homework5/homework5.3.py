#Homework5.3
#Sept. 30, 2020

#The program below gives elapsed execution time in seconds of the print statement 
#Create a decorator function that will take any function, with any number of arguments and print the time it takes to execute it

import time

def dec_function(passedFunction):
    def inner():
        start = time.time()
        passedFunction()
        end = time.time()
        print(end - start)
    return inner #return decorator function

########################################################
@dec_function
def my_range(start=0, end=500):
    x = start
    while x < end:
        yield x
        x=x + 1
    
############################################################
#print(bunnyEars(4))
print(my_range())