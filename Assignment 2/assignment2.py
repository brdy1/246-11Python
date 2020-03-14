#################################
# File: assignment2.py
# Student: Brady Peneton
# Assignment: 2
#################################


#Step 1
print("Assignment 2")

print()

#Step 2
print("What is your name?")
name = input()

#Step 3
if name == "":
    print("Please enter your name.")
    print()
    name = input()
    #Step 4
    if name == "":
        print("Name is missing, exiting program...")
        print()
        print()
        exit()
#Step 5
if name.lower() == "steve":
    #Step 6
    print ("You are the instructor")
else:
    print ("Hi " + name + " You are a student")

#Step 7
print("What year were you born?")
birthyear = input()
print()


#Step 8
if not birthyear.isnumeric():
    print("Please enter your birth year with all numbers")
    birthyear = input()
    print()
#Step 9
else:
    print("What city do you live in?")
    city = input()
    print()
    if city.lower() == "fresno" or city.lower() == "bakersfield":
        print("I'm sorry it's so hot where you live")
    else:
        print("Hope you like it in " + city)

#Step 10
if birthyear == "":
    print("You never told me when you were born!")
else:
    print("It must be a good life for people born in " + birthyear)

#Step 11
print()
print("END OF ASSIGNMENT 2")
