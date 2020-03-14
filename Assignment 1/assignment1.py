#################################
# File: assignment1.py
# Student: Brady Peneton
# Assignment: 1
#################################

print("Assignment 1")

print()

print("What is your name?")
name = input()

print("What is your age?")
age = input()
#convert age to float
age = float(age)

print("How many hours per night do you sleep on average?")
sleep = input()
#convert sleep to float
sleep = float(sleep)

#calculate number of years unconscious
wasted_years = (sleep/24) * age
wasted = round(wasted_years, 2)

#establish complex string for final message
finalmessage = "Hello " + name + ".\n" \
               "You have been unconscious for " + str(wasted) + " years!"

print(finalmessage)

