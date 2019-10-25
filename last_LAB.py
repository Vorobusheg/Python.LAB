from tkinter import mainloop, BOTH, Canvas, Tk
from random import randrange as rnd, choice
from uuid import uuid4
import json

root = Tk()
root.geometry('800x600')

c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
global score
score = 0
obj = []


def new_obj():
    """x, y - координата появления мяча; r - радиус мяча;
    xe, ye - координата точки назначения (траектория);
    tg - tag объекта; tp - type объекта (1 - квадрат, 0 - круг)"""
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    xe = rnd(-1000, 1000)
    ye = rnd(-1000, 1000)
    L = len(obj)
    tg = str(uuid4())
    if (rnd(-10, 10)) > 0:
        c.create_rectangle(x-r, y-r, x+r, y+r, fill='black', width=0, tag=tg)
        tp = 1
    else:
        c.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0, tag=tg)
        tp = 0
    root.after(int(500*(L+1)**0.5), new_obj)
    obj.append((tg, xe, ye, tp))


def click(event):
    global score
    death_list = []
    extrapoints = 0
    for j in range(len(obj)):
        destiny = 1
        (tg, xe, ye, tp) = obj[j]
        crd = []
        crd = c.coords(tg)
        x1 = crd[0]
        y1 = crd[1]
        x2 = crd[2]
        y2 = crd[3]
        r = (x2 - x1)/2
        xm = abs(event.x - (x2 + x1)/2)
        ym = abs(event.y - (y2 + y1)/2)
        if (tp == 1) and ((xm - r) < 0) and ((ym - r) < 0):
            destiny = -1
            extrapoints += 1
        elif (xm**2 + ym**2 - ((x2 - x1)/2)**2) < 0:
            destiny = -1
        if destiny < 0:
            death_list.append(obj[j])

    for i in range(len(death_list)):
        (tg, xe, ye, tp) = death_list[i]
        c.delete(tg)
        obj.remove(death_list[i])
        score += 1
    score += extrapoints*9
    print(score)


def obj_move():
    for i in range(len(obj)):
        (tg, xe, ye, tp) = obj[i]
        c.move(tg, xe/100, ye/100)
        crd = []
        crd = c.coords(tg)
        x1 = crd[0]
        y1 = crd[1]
        x2 = crd[2]
        y2 = crd[3]
        if x1 < 0 or x2 > 800:
            xe = -xe
        if y1 < 0 or y2 > 600:
            ye = -ye
        obj[i] = (tg, xe, ye, tp)
    root.after(1, obj_move)


def score_res():
    global score
    nick = input("Enter you nickname\n")
    with open('Scoretable.json') as f:
        scoretable = json.load(f)
    if nick in scoretable:
        if scoretable[nick] < score:
            scoretable[nick] = score
    else:
        scoretable[nick] = score
    with open('Scoretable.json', 'w') as f:
        json.dump(scoretable, f, indent=1)


def close():
    if len(obj) > 10:
        root.destroy()
    else:
        root.after(1, close)


new_obj()
obj_move()
close()
c.bind('<Button-1>', click)
mainloop()
score_res()
