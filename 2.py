from graph import *

canvasSize(1000, 1000)
windowSize(1000, 1000)
penColor(220, 220, 220)
penSize(600)
line(0, 0, 6000, 0)

def house(x, y, s):
    penSize(2)
    penColor(0, 0, 0)
    brushColor(235, 235, 235)
    circle(x, y, s)
    
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    rectangle(x - s - 20, y, x + s + 20, y + s + 5)

    d = s/4
    penSize(1)
    penColor(130, 130, 130)
    for i in range(4):
        sLoc = (s**2 - (i*d)**2)**(1/2)
        line(x - sLoc, y - i*d, x + sLoc, y - i*d)
        delta = 2*sLoc/(5 - i)
        for j in range(4 - i):
            xLoc = x - sLoc + delta*(j + 1)
            line(xLoc , y - i*d, xLoc, y - (i + 1)*d)

    
def guy(x, y, s):
    penColor(240, 240, 240)
    brushColor(240, 240, 240)
    changeCoords(circle(x, y, s/3), [(x - s/3, y + s/5), (x + s/3, y - s/5)])
    
    penColor(135, 119, 97)
    brushColor(135, 119, 97)
    changeCoords(circle(x, y + s, s), [(x - 3*s/7, y + 2*s), (x + 3*s/7, y + s/10)])
    
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    rectangle(x - s/2, y + s, x + s/2, y + 3*s)

    penColor(135, 119, 97)
    brushColor(135, 119, 97)
    changeCoords(circle(x - s/4, y + s, s/6), [(x - s/4 - s/30, y + s - s/6), (x - s/4 + s/6 + s/30, y + s + s/6)])
    changeCoords(circle(x + s/4, y + s, s/6), [(x + s/4 + s/30, y + s - s/6), (x + s/4 - s/6 - s/30, y + s + s/6)])
    changeCoords(circle(x + s/4, y + s, s/6), [(x + s/3 + s/30, y + s + s/5 - s/9), (x + s/4 - s/6, y + s + s/5)])
    changeCoords(circle(0, 0, 10), [(x - s/3 - s/30, y + s + s/5 - s/9), (x - s/4 + s/6, y + s + s/5)])
    changeCoords(circle(0, 0, 10), [(x - s/6, y + s/2), (x - s/2 - s/10, y + s/2 - s/7)])
    changeCoords(circle(0, 0, 10), [(x + s/6, y + s/2), (x + s/2 + s/10, y + s/2 - s/7)])

    penColor(181, 169, 154)
    brushColor(181, 169, 154)
    changeCoords(circle(0, 0, 10), [(x - s/4, y + s/6), (x + s/4, y - s/6 + s/30)])
    
    penColor(240, 240, 240)
    brushColor(240, 240, 240)
    changeCoords(circle(0, 0, 10), [(x - s/5 + s/30, y + s/7), (x + s/5 - s/30, y - s/11)])

    penColor(0, 0, 0)
    line(x - s/2 - s/20, y - s/5, x - s/2 - s/19, y + s + s/10)
    line(x - s/8, y - s/30, x - s/25, y)
    line(x + s/8, y - s/30, x + s/25, y)
    mass = ((x - s/20, y + s/10), (x - s/30, y + s/30), (x + s/30, y + s/30), (x + s/20, y + s/ 9))
    polyline(mass)

    penColor(56, 44, 30)
    brushColor(56, 44, 30)
    rectangle(x - 3*s/7, y + s - s/10, x + 3*s/7, y + s)
    rectangle(x - s/20, y + s/6, x + s/20, y + s - s/25)
    
house(300, 530, 180)
guy(700, 400, 200)
run()
