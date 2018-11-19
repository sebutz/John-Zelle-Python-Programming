# sum-of-numbers.py
# A program to calculate the sum of the first n-numbers, n provided by the user.

def main():

    n = int(input("Please provide the n-th number: "))

    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    print(sum)

main()
