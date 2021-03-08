from my_math import sign
from math import pi, cos, sin, radians, fabs, floor

def bresen_smooth(p_start, p_end, draw=True, steps=False):
    I = 255
    # Проверка на вырожденность отрезка в точку.
    if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
        if draw:
            # тут нарисоват точку и вывести сообщение об этом
    # Вычисление приращений.
    dx = p_end[0] - p_start[0]
    dy = p_end[1] - p_start[1]
    # Вычисление шага изменение каждой координаты пикселя
    s_x = sign(dx)
    s_y = sign(dy)
    # Вычисление модуля приращения.
    dx = fabs(dx)
    dy = fabs(dy)
    # Обмен местами координат в случае m > 1 (тангенс)
    if (dy >= dx):
        dx, dy = dy, dx
        chenge = 1
    else:
        chenge = 0
    # Иницилизация начального значения ошибки.
    m = dy / dx
    e = I / 2
    # Инициализации начальных значений текущего пикселя 
    # (т е начало отрезка тут)
    x = round(p_start[0])
    y = round(p_start[1])
    # Вычисление скорректированного  значения  тангенса  угла наклона m и коэффициента W.
    m *= I
    W = I - m
    # Высвечивание пиксела  с координатами  (X,Y) интенсивностью E(f).
    if draw:
        # self.draw_pixel(x, y, round(f))
    # Цикл от i = 1 до i = dx + 1 с шагом 1
    i = 1
    step = 1
    x_buf = x
    y_buf = y
    while i <= dx + 1:
        if f < W:
            if fl == 0:
                x += sx
            else:
                y += sy
            f += m
        else:
            x += sx
            y += sy
            f -= W
        if draw:
            # self.draw_pixel(x, y, round(f))
        if steps:
            if not((x_buf == x and y_buf != y) or
                   (x_buf != x and y_buf == y)):
                step += 1
            x_buf = x
            y_buf = y
        i += 1
    if steps:
        return step

