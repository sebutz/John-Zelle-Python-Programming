# height-ladder.py
# A program to compute the height of a ladder from the heigh and the degree.

import math

def main():
    height = eval(input("Please enter the height: "))
    angle  = eval(input("Please enter the angle of the ladder in degrees: "))

    radians = math.pi / 180 * angle

    print(radians)
    print(math.radians(angle))

    length = height / math.sin(radians)

    print("The required length for the ladder is", length, "meters.")

main()
