#Author: Gary Patricelli
#Date: 07/24/13
#Description: A simple script that calculates voltage, current, or resistance, using Ohm's law.

import sys

prompt = "> "
def checkChoice(choice):
    if (choice != 'V' and choice != 'I' and choice != 'R' \
        and choice != 'v' and choice != 'i' and choice !='r'):
        return False
    else: 
        return True  
#Check to see if arg entered is a valid float and is >0
def checkNum(entered):
    try:
        entered = float(entered)
    except ValueError:
        print(entered + " is not a valid input for this field. Exiting program.")
        sys.exit()
    if entered <= 0:
        print("Value must be a positive number. Exiting program.")
        sys.exit()

def calcV():
    print("Please enter the current in amps.")
    amps = input(prompt)
    checkNum(amps)
    amps = float(amps)
    print("Please enter the resistance in ohms.")
    resi = input(prompt)
    checkNum(resi)
    resi = float(resi)
    volt = amps * resi
    print("The voltage is equal to " +  str(volt) + "V")

def calcI():
    print("Please enter the voltage.")
    volt = input(prompt)
    checkNum(volt)
    volt = float(volt)
    print("Please enter the resistance in ohms.")
    resi = input(prompt)
    checkNum(resi)
    resi = float(resi)
    amps = volt / resi
    print("The current is equal to " +  str(amps) + "A")

def calcR():
    print("Please enter the voltage.")
    volt = input(prompt)
    checkNum(volt)
    volt = float(volt)
    print("Please enter the current in amps.")
    amps = input(prompt)
    checkNum(amps)
    amps = float(amps)
    resi = volt / amps 
    print("The resistance is equal to " +  str(resi) + " ohms")

def whichCalc(choice):
    if (choice == 'V' or choice == 'v'):
        calcV()
    if (choice == 'I' or choice == 'i'):
        calcI()
    if (choice == 'R' or choice == 'r'):
        calcR()

print("What would you like to find?")
print("Enter 'V' 'I' 'R'")
choice = input(prompt)
valid = checkChoice(choice)
if valid:
    whichCalc(choice)
else:
    print("Improper input, exiting program.")
