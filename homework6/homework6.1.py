#Homework6.1
#Oct. 9 2020

#write a program that will take a command line argument of full path 
#and prints True if the file/directory at the provided location is present 
#and False if it doesn't

import sys, os

exists = os.path.exists(str(sys.argv[1]))

'''if exists:
    print("True")
else:
    print("False")'''


#Change program such that it runs indefinitely, monitoring a file/directory at a certain location
#and if the file disappears, then the program should print "Alert"
while exists:
    exists = os.path.exists(str(sys.argv[1]))
    continue
print("ALERT!!")