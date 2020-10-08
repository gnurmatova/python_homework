#Homework6.3
#Oct. 7 2020

#Prompt user to enter a start path and file name, 
#search recursively for the given file name starting at the given path, 
#when file is found, display the full path to the file. 
import os
import fnmatch

startPath = input("Enter starting path: ")
fileName = input("Enter name of file to search for: ")
found = False

for dirpath, dirs, files in os.walk(startPath):
    if found == True:
        break
    for single_file in files: #traverse recursively if looking for a file
        if fileName in single_file:
            print(os.path.join(dirpath,single_file))
            found = True
    found = False
            
    if found != True:
        for directory in dirs: #traverse recursively if looking for directory
            if found == True:
                break
            elif fileName in directory:
                print(os.path.join(dirpath,directory))
                found = True

#couldnt find good enough way with regex to get files within a directory to not print out as well
#used break statements for the solution instead
        










       