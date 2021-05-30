from copy import deepcopy
from numpy import sign

def get_vect(dot_start, dot_end):
    return [dot_end[0] - dot_start[0], dot_end[1] - dot_start[1]]

################# ДОП ПРОВЕРКА НА ВЫПУКЛОСТЬ ####################
def get_d_k_b(ax, ay, cx, cy):
    # Коэффициенты прямой АС
    # Если точки A и С лежат на одной вертикальной прямой
    if abs((cx - ax) - 0) <= 1e-6:
        k = 1
        b = -cx
        d = 0
    else:
        k = (cy - ay) / (cx - ax)
        b = cy - (k * cx)
        d = 1

    return d, k, b

def cross_lines(ax, ay, bx, by, cx, cy, dx, dy):
    d_ab, k_ab, b_ab = get_d_k_b(ax, ay, bx, by)
    d_cd, k_cd, b_cd = get_d_k_b(cx, cy, dx, dy)

    if abs(k_ab - k_cd) < 1e-6:
        return False
    x = (b_cd - b_ab) / (k_ab - k_cd)
    if d_cd == 0:
        y = (k_ab * x + b_ab) 
    elif d_ab == 0:
        y = (k_cd * x + b_cd)
    else:
        y = (k_ab * x + b_ab)

    b1 = ax
    b2 = bx
    ax = max(b1, b2)
    bx = min(b1, b2)
    b1 = ay
    b2 = by
    ay = max(b1, b2)
    by = min(b1, b2)

    if (abs(bx - x) < 1e-6) or (abs(ax - x) < 1e-6) or (abs(by - y) < 1e-6) or (abs(ay - y) < 1e-6):
        return False
    if (bx < x and x < ax) and (by < y and y < ay):
        return True
    else:
        return False

def check_cross(arr):
    n = len(arr)
    f = False
    for i in range(n - 1):
        for j in range(i + 1, n, 1):
            if j == n - 1:
                f = cross_lines(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1],
                                arr[j][0], arr[j][1], arr[0][0], arr[0][1])
                if f:
                    return True
            else:
                f = cross_lines(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1],
                                arr[j][0], arr[j][1], arr[j + 1][0], arr[j + 1][1])
                if f:
                    return True

    return False
##############################################################


def scalar_mult(a, b):
    return a[0] * b[0] + a[1] * b[1]


def vector_mult(a, b):
    return a[0] * b[1] - a[1] * b[0] 
    # Ax * By - Ay * Bx --- это будет координата Z, которая нам нужна


def is_convex(arr):
    if len(arr) < 3:
        return False

    a = [arr[0][0] - arr[-1][0], arr[0][1] - arr[-1][1]]
    b = [arr[-1][0] - arr[-2][0], arr[-1][1] - arr[-2][1]]
    prev = sign(vector_mult(a, b))
    for i in range(1, len(arr) - 2):
        a = [arr[i][0] - arr[i - 1][0], arr[i][1] - arr[i - 1][1]]
        b = [arr[i - 1][0] - arr[i - 2][0], arr[i - 1][1] - arr[i - 2][1]]
        cur = sign(vector_mult(a, b))
        if prev != cur:
            return False
        prev = cur

    if (check_cross(arr)):
        return False

    return True


def get_normal(a, b, pos):
    fvec = [b[0] - a[0], b[1] - a[1]]
    posvec = [pos[0] - b[0], pos[1] - b[1]]

    if fvec[1]:
        fpoint = -fvec[0] / fvec[1]
        normvec = [1, fpoint]
    else:
        normvec = [0, 1]

    if scalar_mult(posvec, normvec) < 0:
        normvec[0] = -normvec[0]
        normvec[1] = -normvec[1]

    return normvec

def get_normals(cut):
    normals = []
    cutlen = len(cut)

    for i in range(cutlen):
        normals.append(get_normal(cut[i], 
                                  cut[(i + 1) % cutlen], 
                                  cut[(i + 2) % cutlen]))
    return normals



def is_visible(point, f, s):
    v1 = [s[0] - f[0], s[1] - f[1]]
    v2 = [point[0] - f[0], point[1] - f[1]]
    if vector_mult(v1, v2) < 0:
        return False
    else:
        return True


def cross_two_segment(seg, side, normal):
    d = [seg[1][0] - seg[0][0], seg[1][1] - seg[0][1]]
    w = [seg[0][0] - side[0][0], seg[0][1] - side[0][1]]

    d_scal = scalar_mult(d, normal)
    w_scal = scalar_mult(w, normal)

    param = -w_scal / d_scal

    return [seg[0][0] + d[0] * param, seg[0][1] + d[1] * param]

def get_cut(figure, edge, normal):
    res_figure = []
    figlen = len(figure)

    if figlen < 3:
        return []

    pcheck = is_visible(figure[0], *edge)

    for i in range(1, figlen + 1):
        ccheck = is_visible(figure[i % figlen], *edge)

        if pcheck:
            if ccheck:
                res_figure.append(figure[i % figlen])
            else:
                res_figure.append(cross_two_segment([figure[i - 1], figure[i % figlen]], edge, normal))

        else:
            if ccheck:
                res_figure.append(cross_two_segment([figure[i - 1], figure[i % figlen]], edge, normal))
                res_figure.append(figure[i % figlen])

        pcheck = ccheck

    return res_figure


def Sutherland_Hodgman(figure, cutter, normals):    
    print(figure,"\n", cutter, "\n", normals)
    res_figure = figure
    for i, _ in enumerate(cutter):
        edge = [cutter[i], cutter[(i + 1) % len(cutter)]]

        print(f"Сторона - {edge}, нормаль - {normals[i]}")

        res_figure = get_cut(res_figure, edge, normals[i])

        if len(res_figure) < 3:
            return []

    return res_figure

