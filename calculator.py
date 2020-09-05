from add import *
from subtract import *
from multiply import *
from divide import *

decision = True

while decision:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    operator = input("Enter + or - or * or / : ")

    if operator == "+":
        addition(a, b)
    elif operator == "-":
        subtraction(a, b)
    elif operator == "*":
        multiplication(a, b)
    elif operator == "/":
        division(a, b)

    user_inp = input("Would you like to continue [Y/N] : ")
    if user_inp == "Y":
        decision
    else:
        break
