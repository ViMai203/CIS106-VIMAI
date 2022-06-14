
# This program is used to calculate monthly. weekly and anual gross for user
print("Enter hours worked per week: ")
hour = int(input())
print("Enter rate per hour: ")
rate = int(input())
week = hour * rate
year = 52 * week
month = year / 12
print("Weekly gross pay: " + str(week))
print("Monthly gross pay: " + str(month))
print("Anual gross pay; " + str(year))
