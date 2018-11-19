# cost-for-pizza.py
# A program to calculate the cost per square centimeter of a
# cilcular pizza.

import math # import math module for PI.

def main():
    diameter = float(input("Enter the diameter of the pizza in centimeters: "))
    price = float(input("Enter the price of the pizza in HUF: "))

    radius = diameter / 2

    print("Calculating price per square cm...")

    area = math.pi * radius ** 2

    price_per_square_cm = price / area

    print("The cost per square cm of the pizza is", price_per_square_cm, "HUF.")

main()
