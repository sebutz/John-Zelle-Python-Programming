# winter-scene.py

from graphics import *

def main():
    win = GraphWin("Winter scene", 400, 400)
    win.setBackground("#87CEFA")

    earth = Rectangle(Point(0, 400), Point(400, 360))
    earth.setFill("brown")
    earth.setOutline("brown")
    earth.draw(win)

    tree = Rectangle(Point(80, 360), Point(95, 250))
    tree.setFill("brown")
    tree.setOutline("brown")
    tree.draw(win)

    leaves_1 = Polygon(Point(175/2, 230), Point(65, 280), Point(110, 280))
    leaves_1.setFill("green")
    leaves_1.setOutline("green")
    leaves_1.draw(win)

    leaves_2 = Polygon(Point(175/2, 260), Point(40, 330), Point(135, 330))
    leaves_2.setFill("green")
    leaves_2.setOutline("green")
    leaves_2.draw(win)

    snowman_1 = Circle(Point(240, 350), 10)
    snowman_1.setFill("white")
    snowman_1.setOutline("white")
    snowman_1.draw(win)

    snowman_2 = Circle(Point(240, 340), 7)
    snowman_2.setFill("white")
    snowman_2.setOutline("white")
    snowman_2.draw(win)

    snowman_3 = Circle(Point(240, 333), 5)
    snowman_3.setFill("white")
    snowman_3.setOutline("white")
    snowman_3.draw(win)

    Text(Point(200, 10), "Click to close").draw(win)
    win.getMouse()
    win.close()

main()
