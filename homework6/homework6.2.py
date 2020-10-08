#Homework6.2
#Oct 9 2020

#Modify the quote generator program (on this page) such that if there are multiple quotes for the given author,
#instead of writing them out into the same file, the program instead creates a new file for each quote, 
#hence if you have 3 quotes for an author, you would have 3 files in that author's folder, 
#named quote_1.txt, quote_2.txt, quote_3.txt. If the author has only 1 quote, then file can be named wither quote.txt or quote_1.txt


import json, os
import shutil


PARENT_DIR = "quotes_output"

with open("quotes.json", 'r') as quotes_file:
	data = json.load(quotes_file)

#if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
	shutil.rmtree(PARENT_DIR)#os.rmdir(PARENT_DIR)

os.mkdir(PARENT_DIR) #parent directory
os.chdir(PARENT_DIR) #change directory so that we are inside the parent directory
print("Created parent directory ", PARENT_DIR)
dir_dict = {} #create dictionary to help with file names

for node in data:
    corrected_author = node["author"] if node["author"] is not None else "Unknown"
    dir_name = corrected_author.replace(" ", "_")
    os.mkdir(dir_name) if not os.path.exists(dir_name) else print("{} already exists".format(dir_name))

    #update dictionary
    if dir_name not in dir_dict:
        dir_dict[str(dir_name)] = 1
    else:
        dir_dict[str(dir_name)] += 1
        
    os.chdir(dir_name) # go inside the newly created directory
    
    val = dir_dict.get(str(dir_name))
    fileName = "quote"+str(val)+".txt" #establish unique file name with dictionary values

    #out = open("quote.txt",val, "w")
    out = open(fileName, "w")
    out.write(node["text"])
    #out.write("\n\n")
    out.close()
    os.chdir("..") # go one level up in the directory tree