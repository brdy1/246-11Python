#################################
# File: assignment3.py
# Student: Brady Peneton
# Assignment: 3
#################################

#initialize variables
output = ""
guest = "guest"
guestlist = ""
guestcounter = 1

#enter name
print()
print("Assignment 3")
print()
print("What is your name?")
name = input()
print()

#enter best friends
print("Please enter the names of your three best friends.")
for ff in range(1, 4):
    friend = input("Enter friend name:")
    output = output + str(ff) + ". " + friend + "\n"

#output best friends
print()
print("Your three best friends are:")
print(output)
print()

#wedding guest input
print("Now enter the names of other people you are inviting to your wedding.")
while guest != "": #only ask if the last guest was not blank
    guest = input("Guest's name (or press Enter to quit):")
    if guest != "": #if the guest string is not blank, append it to the guest list
        guestlist = guestlist + str(guestcounter) + ". " + guest + "\n"
        guestcounter += 1   

#output the guest list
print()
print("The wedding attendees are:")
print(guestlist)
print()
print("END OF ASSIGNMENT 3")
