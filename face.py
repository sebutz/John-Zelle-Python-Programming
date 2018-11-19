# face.py

from graphics import *

def main():

    win = GraphWin("face", 400, 400)

    face = Circle(Point(200,200), 150)
    face.setFill("yellow")
    face.setOutline("yellow")
    face.draw(win)

    left_eye = Circle(Point(150, 140), 30)
    left_eye.setFill("white")
    left_eye.setOutline("white")
    left_eye.draw(win)

    right_eye = left_eye.clone()
    right_eye.move(100, 0)
    right_eye.draw(win)

    nose = Polygon(Point(200, 180), Point(180, 220), Point(220, 220))
    nose.setFill("brown")
    nose.setOutline("brown")
    nose.draw(win)

    mouth = Line(Point(150, 270), Point(250, 270))
    mouth.setWidth("3")
    mouth.setOutline("red")
    mouth.setFill("black")
    mouth.draw(win)

    win.getMouse()
    win.close()
main()
