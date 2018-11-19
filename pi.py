# pi.py
# The program is used for pi approximation.

import math

def main():

    terms = int(input("Please enter how many terms to sum: "))

    value = 0

    for k in range(1, 2 * terms + 1, 2):
        sign = - (k % 4 - 2)
        value += float(sign) / k

    print(4 * value)

    print("Comparing approximation with function...")

    diff = math.pi - 4 * value

    print("The difference between the function and the approximation is", diff)

main()
