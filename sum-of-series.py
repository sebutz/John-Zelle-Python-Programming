# sum-of-series.py
# A program to calculate the sum of the entered numbers.

def main():
    n = eval(input("Please enter how many numbers will be in the series: "))

    sum = 0
    for i in range(1, n+1):
        j = eval(input("Please enter the number: "))

        sum = sum + j

    print("The sume of the entered numbers is", sum)

main()
