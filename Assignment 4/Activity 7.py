
#This software will calculate the age of dog breed according to human age.
hage = int(input("Input a dog's age in human years: "))

if hage < 0:
	print("Age must be positive number.")
	exit()
elif hage <= 2:
	dage = hage * 10.5
else:
	dage = 21 + (hage - 2)*4

print("The dog's age in dog's years is", dage)
