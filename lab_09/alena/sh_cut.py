from copy import deepcopy

ERR_CONV = -1
ERR_DEG = -2
ERR_POLY_CONV = -3
ERR_POLY_DEG = -4
OK = 0
EPS = 1e-6


# определение "знака" (знака проекции на ось z) векторного произведения
# векторов [point1, point2] и [point2, point3]
def vect_mult_sign_z(point1, point2, point3):
    x1 = point2[0] - point1[0]
    y1 = point2[1] - point1[1]
    x2 = point3[0] - point2[0]
    y2 = point3[1] - point2[1]
    z = x1 * y2 - y1 * x2
    if z > EPS:
        return 1
    elif z < -EPS:
        return -1
    return 0


# скалярное произведение векторов vec1 и vec2
def scalar_mult(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


# знак скалярного произведения векторов vec1 и vec2
def scalar_mult_sign(vec1, vec2):
    sm = scalar_mult(vec1, vec2)
    if sm > EPS:
        return 1
    elif sm < -EPS:
        return -1
    return 0


# внутренняя нормаль к стороне [point1, point2] (следующая вершина служит для
# проверки того, какая нормаль найдена: внутренняя или внешняя)
# точки не должны лежать на одной прямой
def inner_normal(point1, point2, point3):
    i = point2[0] - point1[0]
    j = point2[1] - point1[1]

    if j == 0:
        normal = [0, 1]
    else:
        normal = [j, -i]

    if scalar_mult_sign(normal, [point3[0] - point2[0], point3[1] - point2[1]]) < 0:
        normal[0] *= -1
        normal[1] *= -1

    return normal


# найти уравнение прямой вида ax+by+c=0, проходящей через точки dot1 и dot2
def find_line_by_2points(dot1, dot2):
    # из уравнения прямой, проходящей через 2 точки
    # (x - x1)/ (x2 - x1) = (y - y1) / (y2 - y1)
    a = dot2[1] - dot1[1]
    b = dot1[0] - dot2[0]
    c = dot2[0] * dot1[1] - dot1[0] * dot2[1]
    line = {'a': a, 'b': b, 'c': c}
    return line


# найти перпендикуляр из точки dot к прямой line
def find_perp(dot, line):
    # находим коэффициент наклона семейства прямых, перпендикулярных line
    # k1 * k2 = -1
    an = -line['b']
    bn = line['a']
    # из семейства прямых, перпендикулярных line, выбираем ту, которая проходит
    # проходит через точку dot из уравнения прямой
    # an * x + bn * y + cn = 0
    cn = -(an * dot[0] + bn * dot[1])
    perp = {'a': an, 'b': bn, 'c': cn}
    return perp


# проверка видимости точки dot относительно ребра point1-point2
# с помощью скалярного произведения нормали и вектора от point1 до точки
def is_visible(dot, point1, point2, point3):
    normal = inner_normal(point1, point2, point3)
    vector = [dot[0] - point1[0], dot[1] - point1[1]]
    if scalar_mult_sign(normal, vector) >= 0:
        return True
    return False


# найти точку пересечения 2 прямых line1 и line2
def find_lines_intersection(line1, line2):
    # параллельные
    if abs(line1['a'] * line2['b'] - line2['a'] * line1['b']) < EPS:
        return None
    if abs(line1['a']) < EPS and abs(line1['b']) < EPS:
        return None
    # точка должна принадлежать обеим прямым, поэтому получаем систему
    # a1x + b1y + c1 = 0
    # a2x + b2y + c2 = 0
    # если первая прямая параллельна оси ox
    if abs(line1['a']) < EPS:
        y0 = -1 * line1['c'] / line1['b']
        x0 = ((line2['b'] * line1['c'] - line1['b'] * line2['c']) /
              (line1['b'] * line2['a']))
    else:
        y0 = ((line2['a'] * line1['c'] - line1['a'] * line2['c']) /
              (line1['a'] * line2['b'] - line2['a'] * line1['b']))
        x0 = -1 * (line1['b'] * y0 + line1['c']) / line1['a']
    dot = [x0, y0]
    return dot


# растояние от отчки dot до прямой, проходящей через точки point1 и point 2
def dist_to_edge(dot, point1, point2):
    if (point1[0] == point2[0]) and (point1[1] == point2[1]):
        dist = ((dot[0] - point1[0]) ** 2 + (dot[1] - point1[1]) ** 2) ** 0.5
        intersection = point1
    else:
        line = find_line_by_2points(point1, point2)
        perp = find_perp(dot, line)
        intersection = find_lines_intersection(line, perp)
        dist = ((dot[0] - intersection[0]) ** 2 + (dot[1] - intersection[1]) ** 2) ** 0.5
    return dist, intersection


# принадлежность точки прямой отрезку
def check_fit(dot, point1, point2):
    if ((min(point1[0], point2[0]) <= dot[0] <= max(point1[0], point2[0])) and
            (min(point1[1], point2[1]) <= dot[1] <= max(point1[1], point2[1]))):
        return True
    return False


# точка пересечения отрезка и прямой (none, если не пересекаются)
def segment_and_line_intersection(sp1, sp2, lp1, lp2):
    segment = find_line_by_2points(sp1, sp2)
    line = find_line_by_2points(lp1, lp2)
    intersection = find_lines_intersection(segment, line)
    if intersection and check_fit(intersection, sp1, sp2):
        return intersection
    return None


# проверка на пересечение сторон многоугольника
def do_intersect(n, cutter):
    for i in range(n):
        line1 = find_line_by_2points(cutter[i], cutter[i + 1])
        for j in range(n):
            if (j != i) and (j != i - 1) and (j != i + 1) and \
                    not (((i == 0) and (j == n - 1)) or ((j == 0) and (i == n - 1))):
                line2 = find_line_by_2points(cutter[j], cutter[j + 1])
                intersection = find_lines_intersection(line1, line2)
                if (intersection and check_fit(intersection, cutter[i], cutter[i + 1]) and
                        check_fit(intersection, cutter[j], cutter[j + 1])):
                    return True
    return False


# подготовка массива вершин отсекателя
#   отсекатель проверяется на выпуклость
#   если три точки, идущие подряд, лежат на одной прямой, то средняя из них удаляется
#   в конец массива повторно записывается первая и вторая вершина
def prepare_cutter(cutter):
    n = len(cutter)
    global_direction = 0
    i = 0
    while i < n - 1:
        if i < n - 2:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[i + 1], cutter[i + 2])
        elif i == n - 2:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[i + 1], cutter[0])
        else:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[0], cutter[1])
        if cur_direction == 0:
            if i == n - 1:
                cutter.pop(0)
            else:
                cutter.pop(i + 1)
            n -= 1
        else:
            if global_direction == 0:
                global_direction = cur_direction
            else:
                if global_direction != cur_direction:
                    return ERR_CONV, n, cutter
            i += 1
    if n < 3:
        return ERR_DEG, n, cutter

    cutter.append(cutter[0])
    if do_intersect(n, cutter):
        return ERR_CONV, n, cutter
    cutter.append(cutter[1])
    return OK, n, cutter


# подготовка массива вершин отсекаемого
#   ребра не должны перессекаться
#   если три точки, идущие подряд, лежат на одной прямой, то средняя из них удаляется
#   в конец массива повторно записывается первая вершина
def prepare_poly(cutter):
    n = len(cutter)
    i = 0
    while i < n - 1:
        if i < n - 2:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[i + 1], cutter[i + 2])
        elif i == n - 2:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[i + 1], cutter[0])
        else:
            cur_direction = vect_mult_sign_z(cutter[i], cutter[0], cutter[1])
        if cur_direction == 0:
            if i == n - 1:
                cutter.pop(0)
            else:
                cutter.pop(i + 1)
            n -= 1
        else:
            i += 1
    if n < 3:
        return ERR_POLY_DEG, n, cutter

    cutter.append(cutter[0])
    if do_intersect(n, cutter):
        return ERR_POLY_CONV, n, cutter
    return OK, n, cutter


# алгоритм отсечения произвольного многоуголника выпуклым отсекателем
# (Алгоритм Сазерленда и Ходжмена)
# np, p - количество и вершины отсекаемого
# nc, c - отсекателя
# в конец массива вершин отсекателя повторно дописываются первая и вторая вершины
# в конец массива вершин отсекаемого - первая вершина
# возвращает массив ребер полученного в результате отсечения многоугольника
# если установлен flag_delete, то ложные ребра удаляются
def sh_cut(p, c, flag_delete):
    # проверка и подготовка отсекателя и отсекаемого
    rc, nc, c = prepare_cutter(c)
    if rc:
        return rc, None
    rc, np, p = prepare_poly(p)
    if rc:
        return rc, None

    # цикл по всем ребрам отсекателя
    for i in range(nc):
        # обнуляем количество вершин результирующего многоугольника
        nq = 0
        q = []
        # цикл по все ребрам отсекаемого
        # вершина j рассматривается как конечная точка ребра
        for j in range(1, np + 1):
            # если текущее ребро отсекаемого и прямая,
            # проходящая через текущее ребро отсекателя, пересекаются
            intersection = segment_and_line_intersection(p[j - 1], p[j], c[i], c[i + 1])
            if intersection:
                # то заносим точку пересечения в результирующий
                nq += 1
                q.append(intersection)
            # если текущая вершина видима относительно текущего ребра то заносим в результирующий
            if is_visible(p[j], c[i], c[i + 1], c[i + 2]):
                nq += 1
                q.append(p[j])

        # если отсекаемый невидим относительно текущего ребра, то он невидим относительно всего отсекателя
        if nq == 0:
            return OK, None

        # готовим исходный отсекаемый для следующего шага отсечения
        q.append(q[0])
        np, p = nq, deepcopy(q)

    result = make_edges(p, flag_delete)
    return OK, result


# создание списка ребер по вершинам многоугольника
# если установлен flag_delete, то ложные ребра удаляются
def make_edges(poly, flag_delete):
    n = len(poly) - 1
    result = set()
    for i in range(n):
        point_begin = min(poly[i], poly[i + 1])
        point_end = max(poly[i], poly[i + 1])
        list_of_intersections = []

        if flag_delete:
            for j in range(n):
                if ((j < i) or (j > i + 1)) and check_fit(poly[j], point_begin, point_end):
                    intersection = poly[j]
                    if vect_mult_sign_z(point_begin, intersection, point_end) == 0:
                        list_of_intersections.append(intersection)

        if len(list_of_intersections) == 0:
            new_edge = (point_begin[0], point_begin[1], point_end[0], point_end[1])
            if new_edge in result:
                result.discard(new_edge)
            else:
                result.add(new_edge)
        else:
            list_of_intersections.sort()
            for intersection in list_of_intersections:
                new_edge = (point_begin[0], point_begin[1], intersection[0], intersection[1])
                if new_edge in result:
                    result.discard(new_edge)
                else:
                    result.add(new_edge)
                point_begin = intersection

            new_edge = (point_begin[0], point_begin[1], point_end[0], point_end[1])
            if new_edge in result:
                result.discard(new_edge)
            else:
                result.add(new_edge)

    return list(result)