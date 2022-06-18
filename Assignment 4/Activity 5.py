
# A program that calculates the area of a room to determine the amount of floor covering required
length=float(input("Enter the lenght of the room: "))
width=float(input("Enter the width of the room: "))
area = length * width
totalft= area / 9
print("Area of the room is "+ str(totalft) +" square yards")
