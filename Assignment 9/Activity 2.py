# Create a program that asks the user to enter grade scores.
# Start by asking the user how many scores they would like to enter. 
# Then use a loop to request each score and add it to a total. 
# Finally, calculate and display the average for the entered scores.
#
# References
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops#For_Loops
# https://www.mathsisfun.com/definitions/average.html
number = int(input("Enter the number of grades: "))
i = 0


while i < number:
    grade = int(input("Enter the grades: "))
    total = i + grade
    avg = total / number
    i += 1
    

print("Average grade: " +str(avg))   
