# A program that asks the user for a distance in miles, 
# then converts it to a distance in meters, feet, and inches, 
# and displays the answear.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions
# https://www.mathsisfun.com/measure/us-standard-length.html
def get_miles():
    print("Input distance in miles: ")
    miles = float(input())
    return miles


def cal_inches(miles):
    inches = miles * 63360
    return inches


def cal_yards(miles):
    yards = miles * 1760
    return yards


def cal_feet(miles):
    feet = miles * 5280
    return feet


def display_result_i(inches):
    print("The distance in inches is " + str(inches) +"in")
    
    
def display_result_y(yards):
    print("The distance in yards is " + str(yards) +"yd")
    
    
def display_result_f(feet):
    print("The distance in feet is " + str(feet) +"ft")
    
    
def main():
    miles = get_miles()
    inches = cal_inches(miles)
    yards = cal_yards(miles)
    feet = cal_feet(miles)
    display_result_i(inches)
    display_result_y(yards)
    display_result_f(feet)

main()
   
