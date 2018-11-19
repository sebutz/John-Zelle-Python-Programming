# price-coffee.py
# A program to calculate cost of coffee orders.

def main():

    pounds = float(input("How many pounds would you like to order? "))

    price = pounds * 10.5 + pounds * .86 + 1.5

    print("The price for", pounds, "pound is", price, "USD.")

main()
