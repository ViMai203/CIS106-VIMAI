# a program that asks the user for a distance in miles,
# and then ask the user if they want the distance in US measurements (yards, feet, and inches) 
# or in metric measurements (kilometers, meters, and centimeters).
# Then calculate and display the results.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Conditions

def getChoice():
    print("Enter (A) if you want the distance in us measurements (yards, feet, and inches.")
    print("Enter (B) if you want the distance in metric measurements (kilometers, meters, and centimeters.")
    choice = input()
    
    return choice

def getMiles():
    print("Enter distance in miles: ")
    miles = float(input())
    
    return miles

def processA():
    miles = getMiles()
    inches = miles * 63360
    yards = miles * 1760
    feet = miles * 5280
    print("The distance in inches is " + str(inches) + " in.")
    print("The distance in yards is " + str(yards) + " yd.")
    print("The distance in feet is " + str(feet) + " ft.")

def processB():
    miles = getMiles()
    kilometers = miles * 1.60934
    meters = miles * 1609.34
    centimeters = miles * 160934
    print("The distance in kilometers is " + str(kilometers) + " km.")
    print("The distance in meters is " + str(meters) + " m.")
    print("The distance in centimeters is " + str(centimeters) + " cm.")

# Main
# A program that asks the user for a distance in miles, and then ask the user if they want the distance in US measurements(yards, feet, and inches) or in metric measurements (kilometers, meters, and centimeters)
choice = getChoice()
if choice == "A" or choice == "a":
    processA()
else:
    if choice == "B" or choice == "b":
        processB()
    else:
        print("You must choose A or B to get the right answer for you.")
