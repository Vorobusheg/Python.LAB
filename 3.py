from graph import *
"""x и y для каждой функции - координаты СО перехода (для дома середина нижней грани, для чувака центр лица),
s характеризует размер (для дома пол длины основания, для чувака расстояние от центра лица до середины нижней части шубы),
пропорции учтены вручную элементами  s/n, где n рациональное число (=
ВАЖНО: запустить прогу и увидеть картинку перед оцениванием кода"""


def background():
    canvasSize(1000, 1000)
    windowSize(1000, 1000)
    penColor(220, 220, 220)
    penSize(600)
    line(0, 0, 6000, 0)


def house_body(x, y, s):
    penSize(2)
    penColor(0, 0, 0)
    brushColor(235, 235, 235)
    circle(x, y, s)

    #белый прямоугольник обрезания до полукруга
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    rectangle(x - s - 20, y, x + s + 20, y + s + 5)


def house_lining(x, y, s):
    # высота уровня
    d = s/4
    penSize(1)
    penColor(130, 130, 130)
    for i in range(4):
        # sLoc длина половины гориз хорды для конкретного уровня
        sLoc = (s**2 - (i*d)**2)**(1/2)
        line(x - sLoc, y - i*d, x + sLoc, y - i*d)
        # delta расстояние между верт отрезками
        delta = 2*sLoc/(5 - i)
        for j in range(4 - i):
            # xLoc x координата верт отрезка в главной СО
            xLoc = x - sLoc + delta*(j + 1)
            line(xLoc, y - i*d, xLoc, y - (i + 1)*d)


def house(x, y, s):
    house_body(x, y, s)
    house_lining(x, y, s)


def guy_shuba(x, y, s):
    # белый капюшон
    penColor(240, 240, 240)
    brushColor(240, 240, 240)
    changeCoords(circle(x, y, s/3), [(x - s/3, y + s/5), (x + s/3, y - s/5)])
    # овал шубы
    penColor(135, 119, 97)
    brushColor(135, 119, 97)
    changeCoords(circle(x, y + s, s), [(x - 3*s/7, y + 2*s), (x + 3*s/7, y + s/10)])
    # обрезание овала
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    rectangle(x - s/2, y + s, x + s/2, y + 3*s)


def guy_legs(x, y, s):
    penColor(135, 119, 97)
    brushColor(135, 119, 97)
    changeCoords(circle(x - s/4, y + s, s/6), [(x - s/4 - s/30, y + s - s/6), (x - s/4 + s/6 + s/30, y + s + s/6)])
    changeCoords(circle(x + s/4, y + s, s/6), [(x + s/4 + s/30, y + s - s/6), (x + s/4 - s/6 - s/30, y + s + s/6)])
    changeCoords(circle(x + s/4, y + s, s/6), [(x + s/3 + s/30, y + s + s/5 - s/9), (x + s/4 - s/6, y + s + s/5)])
    changeCoords(circle(0, 0, 10), [(x - s/3 - s/30, y + s + s/5 - s/9), (x - s/4 + s/6, y + s + s/5)])


def guy_hands(x, y, s):
    penColor(135, 119, 97)
    brushColor(135, 119, 97)
    changeCoords(circle(0, 0, 10), [(x - s/6, y + s/2), (x - s/2 - s/10, y + s/2 - s/7)])
    changeCoords(circle(0, 0, 10), [(x + s/6, y + s/2), (x + s/2 + s/10, y + s/2 - s/7)])


def guy_face(x, y, s):
    # коричневая хрень вокруг лица
    penColor(181, 169, 154)
    brushColor(181, 169, 154) 
    changeCoords(circle(0, 0, 10), [(x - s/4, y + s/6), (x + s/4, y - s/6 + s/30)])
    # овал лица
    penColor(240, 240, 240)
    brushColor(240, 240, 240) 
    changeCoords(circle(0, 0, 10), [(x - s/5 + s/30, y + s/7), (x + s/5 - s/30, y - s/11)])
    # лицо
    penColor(0, 0, 0)
    mass = ((x - s/20, y + s/10), (x - s/30, y + s/30), (x + s/30, y + s/30), (x + s/20, y + s/ 9))
    polyline(mass)
    line(x - s/8, y - s/30, x - s/25, y)
    line(x + s/8, y - s/30, x + s/25, y)

def guy_shuba_modify(x, y, s):
    #Коричневые шняги на шубе
    penColor(56, 44, 30)
    brushColor(56, 44, 30) 
    rectangle(x - 3*s/7, y + s - s/10, x + 3*s/7, y + s)
    rectangle(x - s/20, y + s/6, x + s/20, y + s - s/25)


def guy_spear(x, y, s):
    penColor(0, 0, 0)
    line(x - s/2 - s/20, y - s/5, x - s/2 - s/19, y + s + s/10)


def guy(x, y, s):
    guy_shuba(x, y, s)
    guy_legs(x, y, s)
    guy_hands(x, y, s)
    guy_face(x, y, s)
    guy_shuba_modify(x, y, s)
    guy_spear(x, y, s)


background()
house(500, 430, 90)
house(110, 400, 90)
house(300, 530, 180)
house(130, 600, 90)
house(290, 630, 90)

guy(690, 300, 100)
guy(800, 400, 100)
guy(750, 430, 100)
guy(570, 370, 100)
guy(680, 510, 100)
guy(830, 520, 100)
guy(490, 550, 100)
guy(750, 600, 200)

run()
