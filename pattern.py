import turtle
import turtle as t

def reset():
    pass
def setup():
    turtle.speed(0)
    turtle.setup(width=1000, height=800)
    pass
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):

    pass
def drawRectangle(offset, rotation, centerX, centerY, width, height, count):
    gap = 360 / count
    t.setpos((centerX + offset), centerY)
    for i in range(count):
        t.pd()
        t.left(rotation)
        t.backward(gap / 2)
        #t.setpos((centerX + (width / 2)), (centerY + (height / 2)))
        #t.setpos((centerX + (width / 2)), (centerY - height))
        t.pd()
        t.forward(height / 2)
        t.left(-90)
        t.forward(width)
        t.left(-90)
        t.forward(height)
        t.left(-90)
        t.forward(width)
        t.left(-90)
        t.forward(height / 2)
        t.left(-90)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    pass
def drawSuperPattern():
    pass
def setRandomColor():
    pass
def done():
    pass