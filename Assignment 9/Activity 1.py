# A program aske the user to enter the value
# and the number of expressions to be dispayed.
#
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Loops
print("Enter the value: ")
value = int(input())
print("Enter the number of expressions: ")
expressions = int(input())
number = 1
while number <= expressions:
    result = value * number
    print(str(value) + " * " + str(number) + " = " + str(result))
    number = number + 1
