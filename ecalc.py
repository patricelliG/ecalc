#Author: Gary Patricelli
#Date: 07/24/13
#Description: A simple script that calculates voltage, current, or resistance, using Ohm's law.
#Note: Missing verification of proper entry of values for voltage, current, resistance. 

prompt = "> "
def checkChoice(choice):
    if (choice != 'V' and choice != 'I' and choice != 'R' \
        and choice != 'v' and choice != 'i' and choice !='r'):
        return False
    else: 
        return True  

def calcV():
    print("Please enter the current in amps.")
    amps = input(prompt)
#check if num
    amps = float(amps)
    print("Please enter the resistance in ohms.")
    resi = input(prompt)
#check if num
    resi = float(resi)
    volt = amps * resi
    print("The voltage is equal to " +  str(volt) + "V")

def calcI():
    print("Please enter the voltage.")
    volt = input(prompt)
#check if num
    volt = float(volt)
    print("Please enter the resistance in ohms.")
    resi = input(prompt)
#check if num
    resi = float(resi)
    amps = volt / resi
    print("The current is equal to " +  str(amps) + "A")

def calcR():
    print("Please enter the voltage.")
    volt = input(prompt)
#check if num
    volt = float(volt)
    print("Please enter the current in amps.")
    amps = input(prompt)
#check if num
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
