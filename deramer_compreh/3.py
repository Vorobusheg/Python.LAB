from math import sin,cos

def rotate_square(square, angle):
    M_new = []
    (x1, y1) = square[0]
    (x2, y2) = square[1]
    a = x2 - x1
    angle_rad = (angle + 45)/360*6.28
    delt_x = a/2*(sin(angle_rad) - 1)
    delt_y = a/2*(1 - cos(angle_rad))
    x1_ex = x1 - delt_x 
    y1_ex = y1 + delt_y 
    x2_ex = x2 + delt_x 
    y2_ex = y2 - delt_y
    M_new = [(x1_ex, y1_ex), (x2_ex, y2_ex)]
    print(M_new)

a = 360
M = [(0, 0),(10, 10)]
rotate_square(M, a)
