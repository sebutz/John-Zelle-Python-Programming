# archery-target.py

from graphics import *

def main():

    win = GraphWin( "Archery target", 400, 400)

    Text(Point(200,10), "Click to draw an archery target!").draw(win)

    win.getMouse()

    yellow_circle = Circle(Point(200,200), 150)
    yellow_circle.setFill("yellow")
    yellow_circle.draw(win)

    red_circle = Circle(Point(200,200), 150/2)
    red_circle.setFill("red")
    red_circle.draw(win)

    blue_circle = Circle(Point(200,200), 150/4)
    blue_circle.setFill("blue")
    blue_circle.draw(win)

    black_circle = Circle(Point(200,200), 150/8)
    black_circle.setFill("black")
    black_circle.draw(win)

    white_circle = Circle(Point(200,200), 150/16)
    white_circle.setFill("white")
    white_circle.draw(win)

    Text(Point(200, 380),"Click again to close").draw(win)
    win.getMouse()
    win.close

main()
