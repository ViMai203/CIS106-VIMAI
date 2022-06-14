def calcGrossPay(hours,rate):
week=hours*rate
year=52*week
month=year/12
print("Weekly gross pay : "+str(round(week,2)))
print("Monthly gross pay : "+str(round(month,2)))
print("Annual gross pay : "+str(round(year,2)))

hours=int(input("Enter hours worked per week : "))
rate=float(input("Enter rate per hour : "))
calcGrossPay(hours,rate)
