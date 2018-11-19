# area-triangle.py
# A program to calculate the area of a triangle from the 3 sides

import math

def main():

    a, b, c = eval(input("Please enter the length of the three sides seperated by a comma: "))

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of the provided triangle is ", area, "square cm.")

main()
