from copy import deepcopy
from numpy import sign

ERROR_CUTTER_ISNOT_CONVEX    = -1
ERROR_CUTTER_IS_LINE         = -2
ERROR_REST_ISNOT_POLYGON     = -3
ERROR_REST_IS_LINE           = -4
OK                           = 0
EPS = 1e-6

def get_vect(point_start, point_end):
    return [point_end[0] - point_start[0], point_end[1] - point_start[1]]

def vector_mult(a, b):
    return a[0] * b[1] - a[1] * b[0] 
    # Ax * By - Ay * Bx --- это будет координата Z, которая нам нужна


# скалярное произведение векторов vec1 и vec2
def scalar_mult(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


# Нормаль к стороне AB, с помощью доп точки - pos
def get_normal(a, b, pos):
    fvec = [b[0] - a[0], b[1] - a[1]]
    posvec = [pos[0] - b[0], pos[1] - b[1]]

    if fvec[1]:
        fpoint = -fvec[0] / fvec[1]
        normvec = [1, fpoint]
    else:
        normvec = [0, 1]

    if sign(scalar_mult(posvec, normvec)) < 0:
        normvec[0] = -normvec[0]
        normvec[1] = -normvec[1]

    return normvec


# Уравнение прямой вида Ax + By + C = 0
def equation_line(p1, p2):
    # из уравнения прямой, проходящей через 2 точки
    # (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)
    # C = -A * x1 - B * y1
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]
    line = {'a': a, 'b': b, 'c': c}
    return line


# Поиск перпендикуляра, через точку point 
def perp_by_sige(point, line):
    an = -line['b']
    bn = line['a']
    # Ищем нормаль через точку point
    cn = -(an * point[0] + bn * point[1])
    perp = {'a': an, 'b': bn, 'c': cn}
    return perp


# Проверка видимости точки относительно стороны SF
def is_visible(point, f, s):
    v1 = [s[0] - f[0], s[1] - f[1]]
    v2 = [point[0] - f[0], point[1] - f[1]]
    if vector_mult(v1, v2) < 0:
        return False
    else:
        return True


# Поиск точек пересечения двух прямых
def cross_2lines(line1, line2):
    # параллельные
    if abs(line1['a'] * line2['b'] - line2['a'] * line1['b']) < EPS:
        return None
    if abs(line1['a']) < EPS and abs(line1['b']) < EPS:
        return None

    # Решаем систему 
    # a1x + b1y + c1 = 0
    # a2x + b2y + c2 = 0
    if abs(line1['a']) < EPS:
        y0 = -1 * line1['c'] / line1['b']
        x0 = ((line2['b'] * line1['c'] - line1['b'] * line2['c']) /
              (line1['b'] * line2['a']))
    else:
        y0 = ((line2['a'] * line1['c'] - line1['a'] * line2['c']) /
              (line1['a'] * line2['b'] - line2['a'] * line1['b']))
        x0 = -1 * (line1['b'] * y0 + line1['c']) / line1['a']
    point = [x0, y0]
    return point


# Pастояние от отчки point до прямой, 
# проходящей через точки A и B
def dist_to_edge(point, a, b):
    if (a[0] == b[0]) and (a[1] == b[1]):
        dist = ((point[0] - a[0])**2 + (point[1] - a[1])**2) ** 0.5
        cross = a
    else:
        line = equation_line(a, b)
        perp = perp_by_sige(point, line)
        cross = cross_2lines(line, perp)
        dist = ((point[0] - cross[0])**2 + (point[1] - cross[1])**2) ** 0.5
    return dist, cross


# Проверка, что точка принадлежит отрезку
def point_in_sec(p, sec):
    a = [sec[0][0] - p[0], sec[0][1] - p[1]]
    b = [sec[0][0] - sec[1][0], sec[0][1] - sec[1][1]]
    if abs(vector_mult(a, b)) <= 1e-6:
        if (sec[0] < p < sec[1] or sec[1] < p < sec[0]):
            return True
    return False


# Пересечение прямой отсекателя и отрезка отсекаемого
def cross_line_edge(sp1, sp2, lp1, lp2):
    segment = equation_line(sp1, sp2)
    line = equation_line(lp1, lp2)
    cross = cross_2lines(segment, line)
    if cross and point_in_sec(cross, [sp1, sp2]):
        return cross
    return None


# Проверка, чтобы стороны не пересекались 
def check_cross(n, cutter):
    for i in range(n):
        line1 = equation_line(cutter[i], cutter[i + 1])
        for j in range(n):
            if (j != i) and (j != i - 1) and (j != i + 1) and \
                    not (((i == 0) and (j == n - 1)) or ((j == 0) and (i == n - 1))):
                line2 = equation_line(cutter[j], cutter[j + 1])
                cross = cross_2lines(line1, line2)
                if (cross and point_in_sec(cross, [cutter[i], cutter[i + 1]]) and
                        point_in_sec(cross, [cutter[j], cutter[j + 1]])):
                    return True
    return False


# Проверка отсекатель на выпуклось, а также удаление ненужных точек.
# - удаляются те точки С, которые подходят к схеме А....С....В
def new_cutter(cutter):
    n = len(cutter)
    prev_gl_d = 0
    i = 0
    while i < n - 1:
        cur_d = sign(vector_mult(get_vect(cutter[i], cutter[i + 1]),
                                 get_vect(cutter[(i + 1) % len(cutter)],
                                          cutter[(i + 2) % len(cutter)])))
        if cur_d == 0:
            if i == n - 1:
                cutter.pop(0)
            else:
                cutter.pop(i + 1)
            n -= 1
        else:
            if prev_gl_d == 0:
                prev_gl_d = cur_d
            else:
                if prev_gl_d != cur_d:
                    return ERROR_CUTTER_ISNOT_CONVEX, None, None
            i += 1
    if n < 3:
        return ERROR_CUTTER_IS_LINE, None, None

    cutter.append(cutter[0])
    if check_cross(n, cutter):
        return ERROR_CUTTER_ISNOT_CONVEX, n, cutter

    cutter.append(cutter[1])
    return OK, n, cutter


# Проверка на многоугольность отсекаемого, а также удаление ненужных точек.
# - удаляются те точки С, которые подходят к схеме А....С....В
def new_rest(cutter):
    len_cutter = len(cutter)
    i = 0
    while i < len_cutter - 1:
        cur_d = sign(vector_mult(get_vect(cutter[i], cutter[i + 1]),
                                 get_vect(cutter[(i + 1) % len(cutter)],
                                          cutter[(i + 2) % len(cutter)])))
        if cur_d == 0:
            if i == len_cutter - 1:
                cutter.pop(0)
            else:
                cutter.pop(i + 1)
            len_cutter -= 1
        else:
            i += 1
    if len_cutter < 3:
        return ERROR_REST_IS_LINE, None, None

    cutter.append(cutter[0])

    if check_cross(len_cutter, cutter):
        return ERROR_REST_ISNOT_POLYGON, None, None

    return OK, len_cutter, cutter


# Алгоритм Сазерленда-Ходжмена (спасибо большое мой подруге Алене за помощь с этим ужасом
# потому что у меня в реализации были неточности, и я не могла их найти!!!)
def Sutherland_Hodgman1(rest, cutter, flag):
    # Ввод отсекателя и отсекаемого, а также прверка 
    rc, len_cutter, cutter = new_cutter(cutter)
    if rc:
        return rc, None
    rc, len_rest, rest = new_rest(rest)
    if rc:
        return rc, None

    # Цикл по всем рёбрам отсекателя
    # (переменная цикла i изменяется от 1 до len_cutter
    for i in range(len_cutter):
        print("i", i, cutter[i], cutter[i + 1])
        # Обнуление количества вершин результирующего многоугольника
        len_res = 0
        res = []
        # Цикл по всем рёбрам отсекаемого многоугольника
        for j in range(1, len_rest + 1):
            print("    j", j, rest[j - 1], rest[j])
            # Определение факта пересечения 
            # ребра многоугольника и ребра отсекателя
            cross = cross_line_edge(rest[j - 1], rest[j], 
                                    cutter[i], cutter[i + 1])
            print("cross", cross)
            # Если пересечение рёбер многоугольников
            #  установлено, то определени координат точки 
            # T пересечения этих рёбер

            # Увеличение на единицу количества вершин 
            # результирующего многоугольника
            # Занесение в массив координат результирующего 
            # многоугольника координат найденной точки
            if cross:
                print("if cross")
                len_res += 1
                res.append(cross)

            # Проверка видимости вершины rest[j] относительно ребра отсекателя
            # Если вершина видима, то занесение её координат в массив
            if is_visible(rest[j], cutter[i], cutter[i + 1]):
                print("is_visible",rest[j], cutter[i], cutter[i + 1] )
                len_res += 1
                res.append(rest[j])

        # Проверка ненулевого количества вершин в результирующем массиве
        # многоугольник невидим относительно текущей
        #  границы отсекателя, следовательно, он невидим
        #  относительно всего отсекателя
        if len_res == 0:
            print("if len_res == 0")
            return OK, []

        # Подготовка многоугольника к новому циклу
        res.append(res[0])
        len_rest, rest = len_res, deepcopy(res)
        print("end for i", len_rest, rest)

    print("FLAG", flag)
    return OK, rest


####################### УДАЛЕНИЕ ЛОЖНЫХ РЕБЕР #######################
def point_in_sec(p, sec):
    a = [sec[0][0] - p[0], sec[0][1] - p[1]]
    b = [sec[0][0] - sec[1][0], sec[0][1] - sec[1][1]]
    if abs(vector_mult(a, b)) <= 1e-6:
        if (sec[0] < p < sec[1] or sec[1] < p < sec[0]):
            return True
    return False

def make_uniq(sec):
    for s in sec:
        s.sort()
    return list(filter(lambda x: (sec.count(x) % 2) == 1, sec))

def get_sect(sec, rest):
    p_list = [sec[0], sec[1]]
    for p in rest:
        if point_in_sec(p, sec):
            p_list.append(p)
    p_list.sort()

    sec_list = list()
    for i in range(len(p_list) - 1):
        sec_list.append([p_list[i], p_list[i + 1]])
    return sec_list

def remove_false_side(figure):
    all_sections = list()
    rest = deepcopy(figure)
    for i in range(len(figure)):
        cur_section = [figure[i], figure[(i + 1) % len(figure)]]

        all_sections.extend(get_sect(cur_section, rest))

        rest.pop(0)
        rest.append(figure[i])

    return make_uniq(all_sections)
#####################################################################
