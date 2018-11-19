# futval_graph.py

from graphics import *

def main():
    # introduction
    print("This program plots the growth of a 10-year investment.")

    # get principal and interest rate
    '''
    principal = float(input("Enter the inital principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    '''

    # create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    input_principal = Entry(Point(160, 120), 5)
    input_apr = Entry(Point(160, 150), 5)
    input_apr.setText("0.0")
    input_principal.setText("0.0")
    input_apr.draw(win)
    input_principal.draw(win)

    win.getMouse()

    input_principal.undraw()
    input_apr.undraw()

    principal = float(input_principal.getText())
    apr = float(input_apr.getText())

    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # draw a bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for successive years
    for year in range (1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw a bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <ENTER> to quit.")
    win.close()

main()
