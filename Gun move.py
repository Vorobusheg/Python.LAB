
from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.focus_set()
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 1.5
        self.life = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.vx > 780:
            self.vx = -self.vx / 2
            self.vy = self.vy / 2
        if self.y - self.vy > 550:
            self.vx = self.vx / 2
            self.vy = -self.vy / 2
            if self.vy < 3:
                self.g = self.g / 2
                self.x += self.vx
                self.vy = 0
                self.y = 550
            if math.fabs(self.vx) < 1:
                self.vx = 0
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.g
        canv.delete(self, self.id)
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            obj.life = False
            return True
        else:
            return False

    def dell(self):
        canv.delete(self.id)


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.y = 450
        self.x = 20
        self.id = canv.create_line(self.x, self.y, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 5

    def moveup(self, event):
        self.y -= 5
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def movedown(self, event):
        self.y += 5
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def moveleft(self, event):
        self.x -= 5
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def moveright(self, event):
        self.x += 5
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        if self.dir == 1:
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
        else:
            new_ball.vx = -self.f2_power * math.cos(self.an)
            new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.x == self.x:
                self.dir = 1
                self.an = 9999999999999
            elif event.x > self.x:
                self.dir = 1
                self.an = math.atan((event.y - self.y) / (event.x - self.x))
            elif event.y > self.y:
                self.dir = 0
                self.an = math.pi + math.atan((event.y - self.y) / (event.x - self.x))
            else:
                self.dir = 0
                self.an = -math.pi + math.atan((event.y - self.y) / (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.vx = 0
        self.vy = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(10, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.x = -100
        self.y = -100
        self.vx = 0
        self.vy = 0
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def movement(self):
        if self.x + self.vx > 780 or self.x + self.vx < 60:
            self.vx = -self.vx
        if self.y - self.vy > 550 or self.y - self.vy < 50:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        canv.delete(self, self.id)
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )


t1 = Target()
t2 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game():
    global t1, t2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Up>', g1.moveup)
    canv.bind('<Down>', g1.movedown)
    canv.bind('<Left>', g1.moveleft)
    canv.bind('<Right>', g1.moveright)
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    t1.live = 1
    t2.live = 1
    while True:
        t1.movement()
        t2.movement()
        if balls:
            for b in balls:
                b.move()
                if b.life == 200:
                    b.dell()
                    balls.pop(balls.index(b))
                else:
                    b.life += 1
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit()
                    if t2.live == 0:
                        canv.bind('<Button-1>', '')
                        canv.bind('<ButtonRelease-1>', '')
                        canv.itemconfig(screen1, text='Потраченные снаряды: ' + str(bullet) + '')
                if b.hittest(t2) and t2.live:
                    t2.live = 0
                    t2.hit()
                    if t1.live == 0:
                        canv.bind('<Button-1>', '')
                        canv.bind('<ButtonRelease-1>', '')
                        canv.itemconfig(screen1, text='Потраченные снаряды: ' + str(bullet) + '')
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
        if t1.live == 0 and t2.live == 0:
            for i in balls:
                i.dell()
            balls = []
            break
    time.sleep(3)
    canv.itemconfig(screen1, text='')
    root.after(0, new_game())


new_game()
root.mainloop()