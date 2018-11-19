# sum-of-cubed-numbers.py
# A program to calculate the sum of the cubes of the first n numbers, where
# n is provided by the user.

def main():

    n = int(input("Please enter the n-th number: "))

    cubed_sum = 0

    for i in range(1, n + 1):
        cubed_sum = cubed_sum + i ** 3

    print(cubed_sum)

main()
