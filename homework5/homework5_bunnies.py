#Homework 5.2
#Sept. 30, 2020

# We have bunnies standing in a line, numbered 1, 2, ... 
# The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, 
# because they each have a raised foot. 
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication). 



def bunnyEars(num_bunnies:int)->int:
    if(num_bunnies)==0:
        return 0
    if (num_bunnies) % 2 == 0:
        return bunnyEars(num_bunnies-1)+3
    elif (num_bunnies) % 2 != 0:
        return bunnyEars(num_bunnies-1)+2

#result = bunnyEars(2)
#print(result)