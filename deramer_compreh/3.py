from math import sin, cos, pi, sqrt


def rotate_square(square, angle):
"""принимает угол поворота относительно центра angle и координаты диагонали square,
далее переходит в полярную систему координат с центром в середине диагонали (центр квадрата),
считает в ней координаты и на выходе переводит обратно в изначальную систему коорд"""
    sq_new = []
    (x1, y1) = square[0]
    (x2, y2) = square[1]
    a = (x2 - x1)/sqrt(2)
    x0 = (x1 + x2)/2
    y0 = (y1 + y2)/2
    angle_rad = (angle)/360*2*pi
    x2_new = round(x0 + a*cos(pi/4 - angle_rad), 5)
    y2_new = round(y0 + a*sin(pi/4 - angle_rad), 5)
    x1_new = round(x0 - a*cos(pi/4 - angle_rad), 5)
    y1_new = round(y0 - a*sin(pi/4 - angle_rad), 5)
    sq_new = [(x1_new, y1_new), (x2_new, y2_new)]
    print(sq_new)


a = 180
M = [(0, 0), (10, 10)]
rotate_square(M, a)
