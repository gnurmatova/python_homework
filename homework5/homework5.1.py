#Homework 5.1
#Sept. 30 2020

#Use generator functions to create your own version of range function, call it my_range.
#Do not use the python's range function in the code.


def my_range(start, end):
	x = start
	while x < end:
		yield x
		x=x + 1

for i in my_range(0,10):
	print(i)