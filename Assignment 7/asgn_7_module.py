#################################
# File: asgn_7_module.py
# Name: Brady Peneton
# Assignment: 7
#################################

import datetime

now = datetime.datetime.now()

def payMe(): #requires two variables to return all info
    print("What's the most you are willing to pay me for my advice?")
    payment = input("The more you pay, the better the answer! (minimum price $975.46)\n")
    try:
        payment = float(payment)
    except:
        print("Terribly sorry. We cannot accept that type of payment. There was an error.")
    if float(payment) < 975.46:
        return False, payment;
    else:
        return True, payment;



def getTarget(question):
    who = "who"
    what = "what"
    where = "where"
    when = "when"
    why = "why"
    how = "how"
    question = question.lower()
    if who in question:
        return "who"
    elif what in question:
        return "what"
    elif where in question:
        return "where"
    elif when in question:
        return "when"
    elif why in question:
        return "why"
    elif how in question:
        return "how"
    else:
        return "unknown"


def createList(target):
    display_list = []
    filename = "A7_answers.txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                display_list.append(line)
        answersList = []
        for answer in display_list:
            if target.lower() in answer.lower():
                question, answer = answer.split('*',1)
                answersList.append(answer)
        return answersList
    except FileNotFoundError:
        print("Sorry, there was an error communicating with my crystal ball. Please check to be sure necessary files are available and try again.")


def spinTheWheel(crystalBall):
    listLength = len(crystalBall)
    if listLength == 0:
        remainder = 0
    elif listLength > 0:
        remainder = now.second % listLength
    input("Press Enter to Spin the Wheel")
    print("Spin...Spin...Spin...Spin......Spin......tick, tick, tick, stop")
    return crystalBall[remainder]



