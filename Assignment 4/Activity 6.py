
#a program that calculate and determine how much paint is required to paint a room and how much it will cost.
length =float(input("Enter the length of the room:"))
width =float(input("Enter the width of the room:"))
height =float(input("Enter the height of the room:"))
price_per_gallon =float(input("Enter the price per gallon of paint:"))
number_square_feet_per_gallon =float(input("Enter the number of square feet that a gallon of paint will cover:"))
area_total =2*length*height + 2*width*height
number = int((area_total/number_square_feet_per_gallon) + 0.999)
price = number*price_per_gallon
print("Total paint required to paint the room is: " + str(number))
print("Total price for the paint required is: " +str(price))
