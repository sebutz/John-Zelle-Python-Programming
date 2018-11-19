# factorial.py
# Program to compute the factorial of a number
# Illustrates for loop with an accumulator.

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(2, n + 1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
