#################################
# File: assignment4.py
# 
# Assignment: 4
#################################

import asgn4_module as test #import asgn4_module

def main():
    print("Assignment 4")
    print()
    print()
    firstname = get_firstname() #run the get_firstname function
    print()
    lastname = get_lastname() #run the get_lastname function
    print()
    age = get_age() #run the get_age function and convert the age from a string to a number variable
    print()
    age = float(age)
    if age > 40:
        print("Well, " + str(firstname) + " " + str(lastname) + ", it looks like you are over the hill.")
    else:
        print("It looks like you have many programming years ahead of you, " + str(firstname) + " " + str(lastname) + ".")
    print()
    print("END OF ASSIGNMENT 4")

    
def get_firstname():

    firstname = ""
    firstblank = test.is_field_blank(firstname)
    print("firstblank " + str(firstblank))
    while firstblank:
        firstname = input("Please enter your first name: ")
        firstblank = test.is_field_blank(firstname)
        if firstblank:
            print("You must enter a first name.")
            print()
    return firstname

def get_lastname():

    lastname = ""
    lastblank = test.is_field_blank(lastname)
    print("lastblank " + str(lastblank))
    while lastblank:
        lastname = input("Please enter your last name: ")
        lastblank = test.is_field_blank(lastname)
        if lastblank:
            print("You must enter a last name.")
            print()
    return lastname
    
def get_age():

    age = ""
    ageblank = test.is_field_blank(age)
    agetest = test.is_field_a_number(age)
    print("ageblank " + str(ageblank))
    print("agetest " + str(agetest))
    while ageblank == True or agetest == False:
        age = input("Please enter your age: ")
        ageblank = test.is_field_blank(age)
        agetest = test.is_field_a_number(age)
        
        if ageblank == True:
            print("You must enter an age.")
            print()
        if agetest == False:
            print("You must enter a numeric age.")
            print()
    return age

if __name__ == "__main__":
    main()
