
# A program that helps the user determine how much paint is required
# to paint a room and how much it will cost.
# Ask the user for the length, width, and height of a room, the price
# of a gallon of paint, and the number of square feet that a gallon of
# paint will cover.
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
    print("Enter the number of square feet "
        "that a gallon of paint will cover: ")
    number_gallon = float(input())
    return number_gallon
    
    
def calculate_area(length, height, width):
    area = 2 * length * height + 2 * width * height
    return area
    
    
def calculate_number(area, number_gallon):
    number = int((area / number_gallon) + 0.999)
    return number
    
    
def calculate_price(number, price_gallon):
    price = number * price_gallon
    return price
    
    
def display_gallons(number):
    print("Total paint required to paint the room is " + str(number))
    
    
def display_cost(price):
    print("Total price for the paint required is: " + str(price))
    
    
def main():
    length = get_length()
    width = get_width()
    height = get_height()
    price_gallon = get_price_gallon()
    number_gallon = get_number_gallon()
    area = calculate_area(length, height, width)
    number = calculate_number(area, number_gallon)
    price = calculate_price(number, price_gallon)
    display_gallons(number)
    display_cost(price)
   

main()
