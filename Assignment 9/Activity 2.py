
print("Enter the value: ")
value = int(input())
print("Enter the number of expressions: ")
expressions = int(input())
number = 1
while number <= expressions:
    result = value * number
    print(str(value) + " * " + str(number) + " = " + str(result))
    number = number + 1
