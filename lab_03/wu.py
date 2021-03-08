from my_math import sign
from math import pi, cos, sin, radians, fabs, floor

def wu(p_start, p_end, draw=True, steps=False):
    dx = p_end[0] - p_start[0]
    dy = p_end[1] - p_start[1]

    Imax = 255
    m = 1
    step = 1
    if fabs(dy) > fabs(dx):
        if p_end[1] > p_start[1]:
            p_start[0], p_end[0] = p_end[0], p_start[0]
            p_start[1], p_end[1] = p_end[1], p_start[1]
        if dy != 0:
            m = dx / dy
        for y in range(round(p_start[1]), round(p_end[1]) + 1):
            d1 = p_start[0] - floor(p_start[0])
            d2 = 1 - d1
            if draw:
                # нижняя точка
                # рисовать 
                # верхняя точка
                # рисовать
            if steps and y < round(p_end[1]):
                if int(p_start[0]) != int(p_start[0] + m):
                    step += 1
            p_start[0] += m
    else:
        if p_end[0] < p_start[0]:
            p_start[0], p_end[0] = p_end[0], p_start[0]
            p_start[1], p_end[1] = p_end[1], p_start[1]
        if dx != 0:
            m = dx / dy
        for x in range(round(p_start[0]), round(p_end[0]) + 1):
            d1 = p_start[1] - floor(p_start[1])
            d2 = 1 - d1
            if draw:
                # нижняя точка
                # рисовать 
                # верхняя точка
                # рисовать
            if steps and y < round(p_end[1]):
                if int(p_start[1]) != int(p_start[1] + m):
                    step += 1
            p_start[0] += m
