# volume-surface.py
# A program to calculate the volume and surface area of a sphere
# from radius which is provided by the user.

import math # import math module for PI

def main():
    radius = float(input("Please enter the radius of the sphere: "))

    print("Calculating...")

    volume = 4/3 * math.pi * radius ** 3

    surface = 4 * math.pi * radius ** 2

    print("The volume of the sphere is", volume, ". And the area is", surface, ".")

main()
