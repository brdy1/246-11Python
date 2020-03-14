#################################
# File: assignment6.py
# Name: Brady Peneton
# Assignment: 6
#################################

import os
import sys


#blank lists
itemsList = [] #used for the items, pulled from items.txt if the filename is entered and the file exists
costList = [] #used for costs
removalList = [] #used to remove inputs that generated errors

def main():
    if os.path.exists("costlist.txt"):
        os.remove("costlist.txt")
    print("Assignment 6")
    print()
    filename = "filename" #placeholder value for filename
    while filename != "end":
        filename = input("Enter the filename (enter 'end' to stop): ")
        if filename != "end":
            success = openFile(filename)
            if success:
                itemsList.sort()
                getCosts()
                writeCosts()
                displayCosts()
                exit
                endProgram()
        else:
            endProgram()

def openFile(filename): #attempt to open the file using the given filename. prints error and gives false if the file doesn't exist
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                itemsList.append(line)
        return True
    except FileNotFoundError:
        print("The file " + filename + " was not found. Please try again.")
        print()
        return False

def getCosts(): #prompt user for cost for each item in file
    for item in itemsList:
        print()
        cost = input("How much should " + item + " cost? ")
        try:
            float(cost)
            costList.append(cost)
        except ValueError:
            print("You entered an invalid number that could not be converted to a float (" + cost + "). Skipping to next item.")
            removalList.append(item)
    for item in removalList: #remove all items from itemsList that were assigned errored values
        itemsList.remove(item)
            
            
        
def writeCosts(): #write items and costs together, 1 per line in file called "costlist.txt"
    x = 0
    with open("costlist.txt", "w+") as file:
        for cost in costList:
            file.write(itemsList[x] + " have a cost of " + cost + " dollars\n")
            x +=1

def displayCosts(): #display costs in print statement
    print()
    print("Cost List:")
    print()
    with open("costlist.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            print(line)
        
def endProgram():
    print()
    print("Program ended.")
    sys.exit()

if __name__ == "__main__":
    main()
        
           
            
