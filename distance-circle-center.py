# distance-circle-center.py

from graphics import *

'''
def main():
    win = GraphWin()
    shape = Circle(Point(50, 50), 20)
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

main()
'''

'''
def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

main()
'''

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setFill("red")
    shape.setOutline("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        new_shape = Rectangle(Point(p.getX()+25, p.getY()+25), Point(p.getX()-25, p.getY()-25))
        new_shape.setFill("green")
        new_shape.setOutline("green")
        new_shape.draw(win)

    Text(Point(100, 10), "Click again to quit!").draw(win)
    win.getMouse()
    win.close()
main()
