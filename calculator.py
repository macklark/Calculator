from add import *
from subtract import *
from multiply import *
from divide import *

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
