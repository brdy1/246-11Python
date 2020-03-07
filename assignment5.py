#################################
# File: assignment5.py
# Name: Brady Peneton
# Assignment: 5
#################################

import random

courselist = ["Python", "JavaScript", "PHP"]

def main():
    print("Assignment 5")
    displayMyClasses()
    selection = "blank"
    while selection != "": #make sure we get a nonblank answer before continuing the loop
        print()
        selection = input("Do you need to [A]DD or [R]EMOVE a class?")
        if selection.lower() == "a":
            print()
            add = input("Enter the name of the class you wish to add:") #ask for input for course appending
            courselist.append(add) #add the course
        elif selection.lower() == "r":
            print()
            remove = input("Enter the name of the class you wish to remove:") #ask for input for course removal
            for course in courselist:
                if course == remove:
                    courselist.remove(course) #remove the course
        else: #if selection is anything but A or R, ask user to enter one of these and repeat the loop
            print()
            print("You must choose 'A' to ADD or 'R' to REMOVE a class.")

    displayMyClasses()
    guessNext()
    print()
    print("END OF ASSIGNMENT 5")

def displayMyClasses():
    courselist.sort() #sort courses in alpha order
    print()
    print("List of Classes I Teach:")
    print()
    for x in range(len(courselist)):
        coursenumber = x + 1
        print (str(coursenumber) + ". " + courselist[x])

def guessNext():
    nextcourse = random.choice(courselist)
    print()
    print("The next class you should teach is: " + str(nextcourse))

if __name__ == "__main__":
    main()