#Homework 3 Project 2
#Sept. 24 2020

'''Write a function count_frequency that takes a list of words 
as an argument, counts how many times each word appears in the 
list, and then returns this frequency listing as a Python dictionary '''

def count_frequency(list1):
    return {ele: list1.count(ele) for ele in list1}
    

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
