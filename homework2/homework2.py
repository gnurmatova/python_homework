#Homework 2
# Sept. 8, 2020

name = input("Enter your name:  ")

print("Hello, ", name, "! Let's play a game!")
print("Think of a random number from 1 to 100, and I'll try to guess it!" \
    "Ready? Let's start!")

keep_going = True
correct = False
tries = 0
list1 = [x for x in range(0,101)]

while keep_going == True:
    while correct == False:
        val = len(list1)//2

        print("Is it ", list1[val],"?")
        answer = input("yes or no:  ")
        tries += 1

        if answer == "yes":
            print("Yay! I guess it with this many tries:    ", tries) 
            correct = True
        else:
            print("Is the number larger than ", list1[val], "?")
            update = input("yes or no:  ")

            if update == "yes":
                list1 = list1[val:]
            else:
                list1 = list1[:val]
    go = input("Would you like to play again? (yes/no)  ")
    if go == "yes":
        correct = False
    else:
        keep_going = False
        print("Goodbye!!")

#---------------------------------------------------------------------------------------------
#Part 2

s = input("Enter a scrambled word:    ")

s = list(s)
indices = []

print("Now you will enter the corresponding indices to unscramble the word.")
for x in range(len(s)):
    index = int(input("Enter index value:   "))
    indices.append(index)

print("For your reference...")
print("Scrambled Word:  ", s)
print("Corresponding Indices:   ", indices)

print("Now to unscramble your word....")

unscrambled = [0]*len(s)
print(unscrambled)

for i in range(0,len(s)):
    letter = s[i]
    pos = indices[i]
    
    unscrambled.pop(pos)
    unscrambled.insert(pos, letter)

print("Your unscrambled word is...","".join(unscrambled), "!")