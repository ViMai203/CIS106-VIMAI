
# A program that calculates the area of a room to determine the amount of floor covering required
length = float(input('Enter length of the room: '))
breadth = float(input('Enter breadth of the room: '))

#convert feet to yards
lengthInYards = length / 3
breadthYnYyards = breadth / 3

#multiply length and breadth
floorAarea = lengthInYards * breadthInYards


print(f'The area of the floor covering required is: {round(floorArea, 2)} sq. yards')
