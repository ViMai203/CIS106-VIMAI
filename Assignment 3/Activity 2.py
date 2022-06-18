
# This program used to asking user age.
age=float(input("Enter age:"))
month = age * 12
day = (age * 365) 
hour = (age * 365 + float(age) / 4) * 24
second = age * 365 * 24 * 60 
print("Person is " + str(age) + " years old")
print("Person is " + str(month) + " months old")
print("Person is " + str(day) + " days old")
print("Person is " + str(hour) + " hours old")
print("Person is " + str(second) + " seconds old")
