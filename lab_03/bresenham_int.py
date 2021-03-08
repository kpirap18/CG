from my_math import sign
from math import pi, cos, sin, radians, fabs, floor

def bresen_int(p_start, p_end, draw=True, steps=False):
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
    m = 2 * dy # в случае FLOAT m = dy / dx
    e = m - dx # в случае FLOAT e = m - 0.5
    # Инициализации начальных значений текущего пикселя 
    # (т е начало отрезка тут)
    x = round(p_start[0])
    y = round(p_start[1])
    # Цикл от i = 1 до i = dx + 1 с шагом 1
    i = 1
    step = 1
    x_buf = x
    y_buf = y
    while i <= dx + 1:
        # Высвечивание точки с заданными координатами.
        if draw:
            # тут надо нарисовать этот пиксель 
        if e >= 0:
            if chenge == 1:
                x += s_x
            else:
                y += s_y
            e -= 2 * dx # в случае FLOAT e -= 1
        if e <= 0:
            if chenge == 1:
                y += s_y
            else:
                x += s_x
            e += m
        i += 1
        if steps:
            if not((x_buf == x and y_buf != y) or
                   (x_buf != x and y_buf == y)):
                step += 1
            x_buf = x
            y_buf = y
    if steps:
        return step

