#Homework6.4
#Oct. 7 2020

#Use decorator function you created for the previous homework
#estimate how much operation on a dictionary is faster(or slower)
#than operation on a shelve
import time, shelve

def dec_function(passedFunction):
    def inner():
        start = time.time()
        passedFunction()
        end = time.time()
        return (end-start)
    return inner #return decorator function

########################################################
@dec_function
def shelf():
    sh = shelve.open("my_items")
    sh["list"]=[1,2,3,4,5]
    #print(sh["list"])
    return "\n"


@dec_function
def dictionary():
    thisdict = {
        "val1": 1,
        "val2": 2,
        "val3": 3,
        "val4": 4,
        "val5": 5
        }
    #print(thisdict)
    return "\n"
#########################################################################
shelfTime = shelf()
dictTime = dictionary()

print("Shelf Time: ",shelfTime)
print("Dictionary Time: ", dictTime)
print("Total Time Difference between Functions: ", float(shelfTime-dictTime))
