
# A program that helps the user determine how much paint is required to paint a room and how much it will cost.
# Ask the user for the length, width, and height of a room, the price of a gallon of paint, and the number of square feet that a gallon of paint will cover.
# Calculate the total area of the four walls.
# Calculate the number of gallons.
# Calculate the total cost of the paint.
# Display the result.
# References:
# https://en.wikiversity.org/wiki/Programming_Fundamentals/Functions
def get_length():
    print("Enter the length of the room: ")
    length = float(input())
    return length
    
    
def get_width():
    print("Enter the width of the room: ")
    width = float(input())
    return width
    
    
def get_height():
    print("Enter the height of the room: ")
    height = float(input())
    return height
    
    
def get_price_gallon():
    print("Enter the price per gallon of paint: ")
    price_gallon = float(input())
    return price_gallon
    
    
def get_number_gallon():
    print("Enter the number of square feet that a gallon of paint will cover: ")
    number_gallon = float(input())
    return number_gallon
    
    
def cal_area(length, height, width):
    area = 2 * length * height + 2 * width * height
    return area
    
    
def cal_number(area, number_gallon):
    number = int((area / number_gallon) + 0.999)
    return number
    
    
def cal_price(number, price_gallon):
    price = number * price_gallon
    return price
    
    
def display_result_1(number):
    print("Total paint required to paint the room is " + str(number))
    
    
def display_result_2(price):
    print("Total price for the paint required is: " + str(price))
    
    
def main():
    length = get_length()
    width = get_width()
    height = get_height()
    price_gallon = get_price_gallon()
    number_gallon = get_number_gallon()
    area = cal_area(length, height, width)
    number = cal_number(area, number_gallon)
    price = cal_price(number, price_gallon)
    display_result_1(number)
    display_result_2(price)
   

main()
