# fibonacci.py
# A program to calcule the n-th Fibonacci number.

def main():

    n = int(input("Please enter the n-th number in the Fobinacci sequence: "))

    k = 1
    j = 0

    for i in range(1, n+1):
        high = k
        j = k
        k = k + j

    print(high)

main()
