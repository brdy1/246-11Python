#################################
# File: asgn_7_main.py
# Name: Brady Peneton
# Assignment: 7
#################################


from asgn_7_module import payMe
from asgn_7_module import getTarget
from asgn_7_module import createList
from asgn_7_module import spinTheWheel
import datetime

def main():
    print("* * The Wizard * *")
    print("The Wizard will see you now...")
    print()
    checkPayment, payment = payMe()
    payment = '${:,.2f}'.format(payment) #format the payment amount as money
    if checkPayment:
        print()
        print("I guess " + str(payment) + " seems like a fair price.")
        print("Okay, let's get started!")
        username = ""
        while username == "": #wait for nonblank username
            print()
            username = input("What is your name?\n")
        another = "y"
        while another.lower() == "y": #wait for N to break out of loop
            question = ""
            print()
            while question == "":
                print()
                question = input("What is your question?\n")
            print()
            question = question.strip()
            target = getTarget(question)
            crystalBall = createList(target)
            answer = spinTheWheel(crystalBall)
            print()
            print("Attention, " + username + "! The Wizard declares: " + answer)
            print()
            another = input("Do you have another question? Y/N\n").strip()
        print()
        weekday = datetime.date.today().strftime("%A")
        date = datetime.date.today().strftime("%d")
        #series of if statements to format the date correctly
        if int(date) == 1:
            date = "1st"
        elif int(date) == 2:
            date = "2nd"
        elif int(date) == 3:
            date = "3rd"
        elif int(date) < 10:
            zero, date = date
            date += "th"
        elif int(date) > 9:
            date += "th"
        month = datetime.date.today().strftime("%B")
        year = datetime.date.today().strftime("%Y")
        print("On this day, " + weekday + ", the " + date + " in the month of " + month + " in the year of " + year + "\nThe Wizard wants you to go away now!")
    else:
        print("What an insult! Go away!")

if __name__ == "__main__":
    main()