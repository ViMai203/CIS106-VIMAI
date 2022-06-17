
# A program that calculates the area of a room to determine the amount of floor covering required
length = float(input('Enter length of the room: '))
breadth = float(input('Enter breadth of the room: '))

#convert feet into yards
L = length / 3
W = breadth / 3

#multiply length and breadth 
floorarea = L * W

print(f'The area of the floor covering required is: {round(floorarea, 2)} sq. yards')
