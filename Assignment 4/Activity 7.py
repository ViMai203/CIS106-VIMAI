
#This software will calculate the age of dog breed according to human age.
name =(input("Enter dog's name:"))
age = int(input("Enter dog's age:"))
if age < 0 :
    raise ValueError
elif age <= 1 :
    dog_age_in_Human_years = age * 15.0
elif age <= 2 :
    dog_age_in_Human_years = age * 12.0
elif age <= 3 :
    dog_age_in_Human_years = age * 9.3
elif age <= 4 :
    dog_age_in_Human_years = age * 8
elif age <= 5 :
    dog_age_in_Human_years = age * 7.2
else:
    dog_age_in_Human_years  = 4 * 7 + (float(age) - 5) * 7
print(str(name)+" is "+ str( dog_age_in_Human_years)+" years old in dog years")
