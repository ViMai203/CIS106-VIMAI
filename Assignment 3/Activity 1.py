hours = 0 
rate = 0
#reading hours and rates from user
hours = int(input("Enter daily hours: "))
rate = float(input("Enter rate: "))
#finding daily salary
daily = hours * rate;
#finding monthly salary
monthly = daily * 30
#finding weekly salary
weekly = daily * 7
#finding annual salary
annualy = weekly * 52

print("Weekly gross salary: $",weekly)
print("Monthly gross salary: $",monthly)
print("Annual gross salary: $",annualy)
