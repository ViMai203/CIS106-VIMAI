# A program that uses a loop to generate a list of multiplication expressions for a given value. 
# Ask the user to enter the value and the number of expressions to be displayed.
#
# Reference:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops#For_Loops
print("Enter the value: ")
value = int(input())
print("Enter the number of expressions: ")
expressions = int(input())
for i in range(1, expressions + 1, 1):
    result = value * i
    print(str(value) + " * " + str(i) + " = " + str(result))
