
# A program to prompt the users for hours worked per week and rate per hour.
# Ask users about their hours worked per week and rate per hour.
# Calculate their weekly, monthly, and annual gross pay.
# Display their weekly, monthly, and annual gross pay.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions

def get_hours():
    print("Enter hours worked per week: ")
    hours = float(input())
    return hours


def get_rate():
    print("Enter rate per hour: ")
    rate = float(input())
    return rate

    
def calculate_week(hours, rate):
    week = hours * rate
    return week

    
def calculate_year(week):
    year = 52 * week
    return year
    
    
def calculate_month(year):
    month = year / 12
    return month

    
def display_weekly(week):
    print("Weekly gross pay: " + str(week))
    
    
def display_monthly(month):
    print("Monthly gross pay: " + str(month))
    
    
def display_yearly(year):
    print("Annual gross pay: " + str(year))
    
    
def main():
    hours = get_hours()
    rate = get_rate()
    week = calculate_week(hours, rate)
    year = calculate_year(week)
    month = calculate_month(year)
    display_weekly(week)
    display_monthly(month)
    display_yearly(year)
    
    
main()
