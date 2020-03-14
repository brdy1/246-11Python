#################################
# File: assignment8.py
# Name: Brady Peneton
# Assignment: 8
#################################


dictionary = {}
namesList = []

def main():
    processFile()
    createList()
    displayList()
    nameLookupLoop()
    print("End of Program")

def processFile():
    try:
        with open("A8_names.txt", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                names = line.split("*") #split the lines into a names array
                dictionary[names[0]] = names[1] #use the names array to assign and append each to key-value dictionary pairs
    except FileNotFoundError:
        print("The file was not found.")

def createList():
    for code in dictionary:
        namesList.append(code) #put each key from the dictionary into the list
    namesList.sort() #sort the created list in alphabetical order

def displayList():
    print()
    for name in namesList: #loop through entire list in alpha order
        lastName = dictionary.get(name) #store the value for each key as lastName
        print(name + " " + lastName) #print the name

def nameLookupLoop():
    print()
    while True: #wait for blank input
        selection = input("What is the first name you are looking for? (Enter blank to end)\n")
        selection = selection.capitalize() #capitalize first letter to correct for lowercase inputs
        print()
        if selection in dictionary:
            lastname = dictionary[selection]
            print("Your full name is: " + selection + " " + lastname)
            print()
        elif selection == "":
            break
        else:
            print("I was unable to find " + selection + " in the list.")
            print()

if __name__ == "__main__":
    main()