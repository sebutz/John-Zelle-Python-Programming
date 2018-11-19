# slope.py
# Program to calculate the slope of a line that goes through
# the points provided by the user.

def main():

    x1, y1 = eval(input("Please enter the X and Y coordinates of the first point seperated by a comma: "))
    x2, y2 = eval(input("Please enter the X and Y coordinates of the second point seperated by a comma: "))

    print("Calculating the slope of the line going through the two points...")

    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line is", slope)

main()
