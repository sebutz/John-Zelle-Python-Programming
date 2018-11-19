# rectangle-information.py

from graphics import *

def main():

    win = GraphWin("Rectangle information", 320, 240)
    win.setBackground("white")

    instructions = Text(Point(160, 20), "Click twice for the apex of the rectangle.")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    rectangle = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    rectangle.setFill("yellow")
    rectangle.setWidth(2)
    rectangle.setOutline("black")
    rectangle.draw(win)

    instructions.setText("Calculating the area and perimeter of the rectangle.")

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()

    area = dx * dy
    perimeter = 2 * (dx + dy)

    print("The area of the rectangle is", area, ", and the perimeter is", perimeter, ".")

    print("Press <ENTER> to quit")

    win.getKey()
    win.close()

main()
