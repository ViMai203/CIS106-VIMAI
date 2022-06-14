# This program used to asking user age.
print("Enter age:")
age = float(input())
month = age * 12
day = age * 12 * 365 + float(age) / 4
hour = (age * 12 * 365 + float(age) / 4) * 24
second = (age * 12 * 365 + float(age) / 4) * 24 * 60 * 60
print("Person is " + str(age) + " years old")
print("Person is " + str(month) + " months old")
print("Person is " + str(day) + " days old")
print("Person is " + str(hour) + " hours old")
print("Person is " + str(second) + " seconds old")
