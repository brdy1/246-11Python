#################################
# File: assignment4.py
# Name: Brady Peneton
# Assignment: 4
#################################

import asgn4_module as test #import asgn4_module

def main():
    print("Assignment 4")
    print()
    print()
    firstname = get_firstname() #retrieve first name input from user
    print()
    lastname = get_lastname() #retrieve last name input from user
    print()
    age = get_age() #retrieve numeric age input from user
    print()
    age = float(age) #convert age to float
    if age > 40: #split messages
        print("Well, " + str(firstname) + " " + str(lastname) + ", it looks like you are over the hill.")
    else:
        print("It looks like you have many programming years ahead of you, " + str(firstname) + " " + str(lastname) + ".")
    print()
    print("END OF ASSIGNMENT 4")


def get_firstname():

    firstname = ""
    firstblank = test.is_field_blank(firstname)
    while firstblank: #repeat this loop until we get a first name
        firstname = input("Please enter your first name: ")
        firstblank = test.is_field_blank(firstname)
        if firstblank:
            print("You must enter a first name.")
            print()
    return firstname #send verified first name input back to main

def get_lastname():

    lastname = ""
    lastblank = test.is_field_blank(lastname)
    while lastblank: #repeat this loop until we get a last name
        lastname = input("Please enter your last name: ")
        lastblank = test.is_field_blank(lastname)
        if lastblank:
            print("You must enter a last name.")
            print()
    return lastname #send verified last name input back to main

def get_age():

    age = ""
    ageblank = test.is_field_blank(age)
    agetest = test.is_field_a_number(age)
    while ageblank == True or agetest == False: #repeat this loop until we get a non-blank numeric input
        age = input("Please enter your age: ")
        ageblank = test.is_field_blank(age)
        agetest = test.is_field_a_number(age)
        if ageblank == True:
            print("You must enter an age.")
            print()
        elif agetest == False:
            print("You must enter a numeric age.")
            print()
    return age #send verified age value back to main

if __name__ == "__main__":
    main()
