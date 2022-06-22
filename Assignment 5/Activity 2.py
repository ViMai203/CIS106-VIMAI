
# This program used to calculate month, day, hours and second of age.
print("What's your age ?:")
age = int(input())
months = age * 12
days = age * 365
hours = age * 24 * 365
seconds = age * 365 * 24 * 60 * 60
print("You are " + str(months) + " months old.")
print("You are " + str(days) + " days old.")
print("You are " + str(hours) + " hours old.")
print("You are " + str(seconds) + " seconds old.")
