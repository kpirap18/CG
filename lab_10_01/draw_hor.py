from func import funcs
from my_math import transform, sign

def horizon(x1, y1, x2, y2, hh, lh, image, wind, s):
    if  x1 < 0 or x1 > image.width() or x2 < 0 or x2 > image.width():
        return hh, lh
    print("hor x1", x1 , y1, x2, y2)
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    s_x = sign(dx)
    s_y = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    # print("dx == 0 and dy == 0 and 0 <= x < image.width()", dx == 0 and dy == 0 and 0 <= x < image.width())
    if dx == 0 and dy == 0 and 0 <= x < image.width():
        if s == 1 or s == 2:
            image.setPixelColor(x, image.height() - y, wind.color_res)
        if y >= hh[x]:
            hh[x] = y
            image.setPixelColor(x, image.height() - y, wind.color_res)
        if y <= lh[x]:
            lh[x] = y
            image.setPixelColor(x, image.height() - y, wind.color_res)
        return hh, lh
    flag = 0
    if dy > dx:
        dx, dy = dy, dx
        flag = 1
    y_max_cur = hh[x]
    y_min_cur = lh[x]

    e = 2 * dy - dx
    i = 1
    while i <= dx:
        if 0 <= x < image.width():
            if s == 1 or s == 2:
                image.setPixelColor(x, image.height() - y, wind.color_res)
        
            if y >= hh[x]:
                if y >= y_max_cur:
                    y_max_cur = y
                image.setPixelColor(x, image.height() - y, wind.color_res)
            if y <= lh[x]:
                if y <= y_min_cur:
                    y_min_cur = y
                image.setPixelColor(x, image.height() - y, wind.color_res)
        if e >= 0:
            if flag:
                hh[x] = y_max_cur
                lh[x] = y_min_cur
                x += s_x
                y_max_cur = hh[x]
                y_min_cur = lh[x]
            else:
                y += s_y
            e -= 2 * dx
        if e < 0:
            if not flag:
                hh[x] = y_max_cur
                lh[x] = y_min_cur
                x += s_x
                y_max_cur = hh[x]
                y_min_cur = lh[x]
            else:
                y += s_y
            e += 2 * dy
        i += 1

    return hh, lh


def float_horizon(my_win):
    print("float_hor")
    # для удобства использования
    func = funcs[my_win.number_func]
    alpha_x = my_win.alpha_x
    alpha_y = my_win.alpha_y
    alpha_z = my_win.alpha_z

    x_min = my_win.x_begin
    x_max = my_win.x_end
    x_step = my_win.x_step

    z_min = my_win.z_begin
    z_max = my_win.z_end
    z_step = my_win.z_step
    print("float_hor", alpha_x, alpha_y, alpha_z, x_min, x_max, x_step, z_min, z_max, z_step)

    # инициализация для боковых ребер
    x_r = -1
    y_r = -1
    x_l = -1
    y_l = -1

    # инициализация массивов горизонта
    hight_hor = {x: 0 for x in range(0, int(my_win.w) + 1)}
    low_hor = {x: my_win.h for x in range(0, int(my_win.w) + 1)}

    z = z_max
    shag = 0
    # print(z, z_min)
    while z > (z_min - z_step / 2):
        shag += 1
        print("z", z)
        z_buf = z
        x_prev = x_min
        y_prev = func(x_min, z)
        x_prev, y_prev, z_buf = transform(x_prev, y_prev, z,
                                          alpha_x, alpha_y, alpha_z, 
                                          my_win.scale_k, my_win.w, my_win.h)

        # Обрабатываем левое ребро(смотрим предыдущее с текущим)
        if x_l != -1:
            hight_hor, low_hor = horizon(x_prev, y_prev, x_l, y_l,
                                         hight_hor, low_hor, 
                                         my_win.image, my_win, shag)
        x_l = x_prev
        y_l = y_prev

        x = x_min
        while x < (x_max + x_step / 2):
            # print("x", x)
            y = func(x, z)
            x_cur, y_cur, z_buf = transform(x, y, z, 
                                            alpha_x, alpha_y, alpha_z,
                                            my_win.scale_k, my_win.w, my_win.h)
            # Рисуем горизонт 
            # Рисовать начинаем не от предыдущего,
            # а уже от нашего преобразованного
            hight_hor, low_hor = horizon(x_prev, y_prev, x_cur, y_cur, 
                                         hight_hor, low_hor,
                                         my_win.image, my_win, shag)
            x_prev = x_cur
            y_prev = y_cur

            x += x_step

        # Обработка правого ребра
        if not(abs(z - z_min) < 1e-6):
            x_r = x_max
            y_r = func(x_max, z - z_step)
            x_r, y_r, z_buf = transform(x_r, y_r, z - z_step, 
                                        alpha_x, alpha_y, alpha_z,
                                        my_win.scale_k, my_win.w, my_win.h)
            hight_hor, low_hor = horizon(x_prev, y_prev, x_r, y_r,
                                         hight_hor, low_hor, 
                                         my_win.image, my_win, shag)
        # print(hight_hor, low_hor)
        z -= z_step


    return my_win.image
