# A program that asks the user to enter grade scores.
# Start by asking the user how many scores they would like to enter.
# Then use a loop to request each score and add it to a total.
# Finally, calculate and display the average for the entered scores.
#
# Reference:
#
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
# https://www.mathsisfun.com/definitions/average.html
numbers = int(input('How many grades you would like to enter: '))

grades = [-1] * numbers

Average = 0

for i in range(numbers):
     grades[i] = int(input('Enter grade: '))
     Average = Average + grades[i]
     Average = Average / numbers



print('Average Grade:', Average)
