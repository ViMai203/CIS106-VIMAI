# A program that asks the user how old they are in years.
# Ask the user if they would like to know how old they are in (M)onths, (D)ays, (H)ours, or (S)econds.
# Use if/else conditional statements to calculate.
# Display their approximate age in the selected timeframe.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Conditions
def choice():
    print("M - For Age in months")
    print("D - For Age in days")
    print("H - For Age in hours")
    print("S - For Age in seconds")
    c = input()
    return c


def age():
    print("Enter age in year: ")
    a = float(input())
    return a

    
def months(a):
    mo = a * 12
    return mo

    
def days(a):
    da = a * 365
    return da
    
    
def hours(a):
    ho = a * 365 * 24
    return ho


def seconds(a):
    se = a * 365 * 24 * 60 * 60
    return se
    

def display1(mo):
    print("You are " + str(mo) + " months old")
    

def display2(da):
    print("You are " + str(da) + " days old")
    
    
def display3(ho):
    print("You are " + str(ho) + " hours old")
    
    
def display4(se):
    print("You are " + str(se) + " seconds old")

    
def main():
    a = age()
    c = choice()
    if c == "M" or c == "m":
        mo = months(a)
        display1(mo)
    elif c == "D" or c == "d":
        da = days(a)
        display2(da)
    elif c == "H" or c == "h":
        ho = hours(a)
        display3(ho)
    elif c == "S" or c == "s":
        se = seconds(a)
        display4(se)
    else:
        print("You must enter the answears.")
        
        
main()
