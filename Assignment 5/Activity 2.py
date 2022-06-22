
def caldays(age):
    days = age * 365
    
    return days

def calhours(age):
    hours = age * 24 * 365
    
    return hours

def calmonths(age):
    months = age * 12
    
    return months

def calseconds(age):
    seconds = age * 365 * 24 * 60 * 60
    
    return seconds

def displayResultmonths(age, months):
    print("You are " + str(months) + " months old")

def displayResultdays(age, days):
    print("You are " + str(days) + " days old")

def displayResulthours(age, hours):
    print("You are " + str(hours) + " hours old")

def displayResultseconds(age, seconds):
    print("You are " + str(seconds) + " seconds old")

def getage():
    print("Enter age: ")
    age = float(input())
    
    return age

# Main
# This program used to calculate month, day, hours and second of age.
age = getage()
months = calmonths(age)
days = caldays(age)
hours = calhours(age)
seconds = calseconds(age)
displayResultmonths(age, months)
displayResultdays(age, days)
displayResulthours(age, hours)
displayResultseconds(age, seconds)
