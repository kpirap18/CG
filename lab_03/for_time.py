
def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

def bresen_int_test(p_start, p_end):
    # Проверка на вырожденность отрезка в точку.
    if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
        return
    # Вычисление приращений.
    dx = p_end[0] - p_start[0]
    dy = p_end[1] - p_start[1]
    # Вычисление шага изменение каждой координаты пикселя
    s_x = sign(dx)
    s_y = sign(dy)
    # Вычисление модуля приращения.
    dx = abs(dx)
    dy = abs(dy)
    # Обмен местами координат в случае m > 1 (тангенс)
    if (dy >= dx):
        dx, dy = dy, dx
        chenge = 1
    else:
        chenge = 0
    # Иницилизация начального значения ошибки.
    m = 2 * dy # в случае FLOAT m = dy / dx
    m1 = 2 * dx
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
        # Ввечивание точки с заданными координатами.
        if e >= 0:
            if chenge == 1:
                x += s_x
            else:
                y += s_y
            e -= m1 # в случае FLOAT e -= 1
        if e <= 0:
            if chenge == 1:
                y += s_y
            else:
                x += s_x
            e += m
        i += 1




def bresen_float_test(p_start, p_end):
   # Проверка на вырожденность отрезка в точку.
    if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            
        return
    # Вычисление приращений.
    dx = p_end[0] - p_start[0]
    dy = p_end[1] - p_start[1]
    # Вычисление шага изменение каждой координаты пикселя
    s_x = sign(dx)
    s_y = sign(dy)
    # Вычисление модуля приращения.
    dx = abs(dx)
    dy = abs(dy)
    # Обмен местами координат в случае m > 1 (тангенс)
    if (dy >= dx):
        dx, dy = dy, dx
        chenge = 1
    else:
        chenge = 0
    # Иницилизация начального значения ошибки.
    m = dy / dx # в случае INT m = 2 * dy
    e = m - 0.5 # в случае INT e = m - dx
    # Инициализации начальных значений текущего пикселя 
     # (т е начало отрезка тут)
    x = round(p_start[0])
    y = round(p_start[1])
        # Цикл от i = 1 до i = dx + 1 с шагом 1
    i = 1
    step = 1
    while i <= dx + 1:
            # Высвечивание точки с заданными координатами.
            
            # Вычисление координат и ошибки для след пикселя.
        if e >= 0:
            if chenge == 1:
                x += s_x
            else:
                y += s_y
            e -= 1 # в случае INT e -= 2 * dx
        if e <= 0:
            if chenge == 1:
                y += s_y
            else:
                x += s_x
            e += m 
        i += 1



def bresen_smooth_test(p_start, p_end):
    I = 255
        # Проверка на вырожденность отрезка в точку.
    if p_start[0] == p_end[0] and p_start[1] == p_end[1]:

        return
        # Вычисление приращений.
    dx = p_end[0] - p_start[0]
    dy = p_end[1] - p_start[1]
    # Вычисление шага изменение каждой координаты пикселя
    s_x = sign(dx)
    s_y = sign(dy)
        # Вычисление модуля приращения.
    dx = abs(dx)
    dy = abs(dy)
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
    E = round(e)
        # Цикл от i = 1 до i = dx + 1 с шагом 1
    i = 1
    step = 1
    x_buf = x
    y_buf = y
    while i <= dx:
        if e < W:
            if chenge == 0:
                x += s_x
            else:
                y += s_y
            e += m
        else:
            x += s_x
            y += s_y
            e -= W
        E = round(e)

        i += 1


def dda_test( p_start, p_end):
        # Проверка на вырожденность отрезка в точку.
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            return
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        if abs(dx) > abs(dy):
            L = abs(dx)
        else:
            L = abs(dy)

        sx = (p_end[0] - p_start[0]) / L
        sy = (p_end[1] - p_start[1]) / L

        x = p_start[0]
        y = p_start[1]
        i = 1
        step = 1
        while i <= L + 1:
            xx = round(x)
            yy = round(y)
            x += sx
            y += sy
            i += 1


def fpart(x):
    return x - int(x)

def rfpart(x):
    return 1 - fpart(x)

def vu_test(x_start, y_start, x_end, y_end, color='black'):
    """
        Implementation of Xiaolin Wu algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    steep = abs(dx) < abs(dy)

    def p(px, py):
        return ([px, py], [py, px])[steep]

    if steep:
        x_start, y_start, x_end, y_end, dx, dy = y_start, x_start, y_end, x_end, dy, dx
    if x_end < x_start:
        x_start, x_end, y_start, y_end = x_end, x_start, y_end, y_start

    m = dy / dx
    intery = y_start + rfpart(x_start) * m

    dots = []

    def get_endpoint(x_s, y_s):
        x_e = round(x_s)
        y_e = y_s + (x_e - x_s) * m
        x_gap = rfpart(x_s + 0.5)

        px, py = int(x_e), int(y_e)

        dens1 = rfpart(y_e) * x_gap
        dens2 = fpart(y_e) * x_gap

        dots.extend([[*p(px, py)]])#, color + (255 * dens2, 255 * dens2, 255)]])
        dots.extend([[*p(px, py)]])#, color + (255 * dens1, 255 * dens1, 255)]])

        return px

    x_s = get_endpoint(x_start, y_start) + 1
    x_e = get_endpoint(x_end, y_end)

    for x in range(x_s, x_e):
        y = int(intery)

        dens1 = rfpart(intery)
        dens2 = fpart(intery)

        dots.extend([[*p(x, y)]])#, color + (255 * dens2, 255 * dens2, 255)]])
        dots.extend([[*p(x, y+1)]])#), color + (255 * dens1, 255 * dens1, 255)]])

        intery += m

    return dots
