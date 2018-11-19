# distance-two-points.py
# A program to calculate the distance between two points provided by the user

import math

def main():
    x1, y1 = eval(input("Please enter the X and Y coordinates of the first point seperated by a comma: "))
    x2, y2 = eval(input("Please enter the X and Y coordinates of the second point seperated by a comma: "))

    print("Calculating the distance between the two points...")

    n = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = math.sqrt(n)

    print("The distance between the two points is", distance, "units.")

main()
