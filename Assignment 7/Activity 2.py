# A program that asks the user how old they are in years.
# Ask the user if they would like to know how old they are in (M)onths, (D)ays, (H)ours, or (S)econds.
# Use if/else conditional statements to calculate.
# Display their approximate age in the selected timeframe.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Conditions
def get_choice() :
    print("Would you like to know your age in (M)onths, (D)ays, (H)ours, or (S)econds")
    print("M - For Age in months")
    print("D - For Age in days")
    print("H - For Age in hours")
    print("S - For Age in seconds")
    choice = input()
    return choice


def get_age():
    print("Enter age in year: ")
    age = float(input())
    return age

    
def cal_months(age):
    months = age * 12
    return months

    
def cal_days(age):
    days = age * 365
    return days
    
    
def cal_hours(age):
    hours = age * 365 * 24
    return hours


def cal_seconds(age):
    seconds = age * 365 * 24 * 60 * 60
    return seconds
    

def display_months(months):
    print("You are " + str(months) + " months old")
    

def display_days(days):
    print("You are " + str(days) + " days old")
    
    
def display_hours(hours):
    print("You are " + str(hours) + " hours old")
    
    
def display_seconds(seconds):
    print("You are " + str(seconds) + " seconds old")

    
def main():
    age = get_age()
    choice = get_choice()
    if choice == "M" or choice == "m":
        months = cal_months(age)
        display_months(months)
    elif choice == "D" or choice == "d":
        days = cal_days(age)
        display_days(days)
    elif choice == "H" or choice == "h":
        hours = cal_hours(age)
        display_hours(hours)
    elif choice == "S" or choice == "s":
        seconds = cal_seconds(age)
        display_seconds(seconds)
    else:
        print("You must enter the answears.")
        
        
main()
