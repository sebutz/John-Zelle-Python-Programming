# convert-km-to-miles.py
# A simple program used to convert KM to miles

def main():
    print("This program is used to convert KM to Miles.")

    km = eval(input("Enter the distance in kilometers:"))

    miles  = 0.62 * km

    print("The distance", km, " kilometers is ", miles, "in miles")

main()
