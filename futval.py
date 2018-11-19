# futval.py
# A program to compute the value of an investment
# carried in 10 years into the future

'''
def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))

    original_principal = principal

    for i in range(years):
        principal = principal * (1 + apr) + original_principal
        print (principal)

    print("The value in", years, "years is: ", principal)

main()
'''

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))
    period = eval(input("Enter how often is the interest compounded per year: "))

    compound_period = apr / period

    for i in range(years * period):
        principal = principal * (1 + compound_period)
        print(principal)

    print("The value in", years, "years is: ", principal)

main()
