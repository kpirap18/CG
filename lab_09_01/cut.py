from copy import deepcopy
from numpy import sign

EPS = 1e-06

# скалярное произведение векторов vec1 и vec2
def scalar_mult(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def get_vect(point_start, point_end):
    return [point_end[0] - point_start[0], point_end[1] - point_start[1]]


# Векторное произведение
def vector_mult(a, b):
    return a[0] * b[1] - a[1] * b[0] 
    # Ax * By - Ay * Bx --- это будет координата Z, которая нам нужна


# Уравнение прямой вида Ax + By + C = 0
def equation_line(p1, p2):
    # из уравнения прямой, проходящей через 2 точки
    # (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)
    # C = -A * x1 - B * y1
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]
    line = {'a': a, 'b': b, 'c': c}
    # print("\n\n\n\nLINE", a * (p1[0] + 1) + b * (p1[1] + 1) + c, line, "\n\n\n\n")
    return line


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
    point = [round(x0), round(y0)]
    return point


# Проверка, что точка принадлежит отрезку
def point_in_sec(p, sec):
    a = [sec[0][0] - p[0], sec[0][1] - p[1]]
    b = [sec[0][0] - sec[1][0], sec[0][1] - sec[1][1]]
    # if abs(vector_mult(a, b)) <= 1e-6:
    if (sec[0][0] < p[0] < sec[1][0] or sec[1][0] < p[0] < sec[0][0]):
        return True
    return False


# Пересечение стороны отсекателя и сторны отсекаемого
def cross_line_edge(sp1, sp2, lp1, lp2):
    a = get_vect(sp1, sp2)
    b = get_vect(lp1, lp2)
    print(a, b)
    if (a[1] == 0 and b[1] == 0) or (a[0] == 0 and b[0] == 0):
        segment = equation_line(sp1, sp2)
        line = equation_line(lp1, lp2)
        print(line['a'] * lp2[0] + line['b'] * lp2[1] + line['c'])
        if (line['a'] * lp2[0] + line['b'] * lp2[1] + line['c'] == 0):
            if (line['a'] * (lp2[0] + 1) + line['b'] * lp2[1] + line['c'] != 0):
                return [lp2[0] + 1, lp2[1]]
            if (line['a'] * (lp2[0]) + line['b'] * (lp2[1] + 1) + line['c'] != 0):
                return [lp2[0], lp2[1] + 1]
            if (line['a'] * (lp2[0] + 1) + line['b'] * (lp2[1] + 1) + line['c'] != 0):
                return [lp2[0] + 1, lp2[1] + 1]
            
    elif b[0] != 0 and b[1] != 0:
        print("elif", a[0] / b[0] == a[1] / b[1], a[0] / b[0], a[1] / b[1])
        if(a[0] / b[0] == a[1] / b[1]):
            segment = equation_line(sp1, sp2)
            line = equation_line(lp1, lp2)
            if (line['a'] * lp2[0] + line['b'] * lp2[1] + line['c'] == 0):
                if (line['a'] * (lp2[0] + 1) + line['b'] * lp2[1] + line['c'] != 0):
                    return [lp2[0] + 1, lp2[1]]
                if (line['a'] * (lp2[0]) + line['b'] * (lp2[1] + 1) + line['c'] != 0):
                    return [lp2[0], lp2[1] + 1]
                if (line['a'] * (lp2[0] + 1) + line['b'] * (lp2[1] + 1) + line['c'] != 0):
                    return [lp2[0] + 1, lp2[1] + 1]


    segment = equation_line(sp1, sp2)
    line = equation_line(lp1, lp2)
    cross = cross_2lines(segment, line)
    print("cross", cross, segment, line, sp1, sp2, lp1, lp2)


    if cross and point_in_sec(cross, [sp1, sp2]) and point_in_sec(cross, [lp1, lp2]):
        return cross
    return None


# Проверка, чтобы стороны не пересекались 
# Проверяю все многоугольники
def check_cross(n, cutter):
    for i in range(n):
        line1 = equation_line(cutter[i], cutter[(i + 1) % n])
        for j in range(n):
            if (j != i) and (j != i - 1) and \
               (j != i + 1) and \
               not (((i == 0) and (j == n - 1)) \
               or ((j == 0) and (i == n - 1))):
                line2 = equation_line(cutter[j], cutter[(i + 1) % n])
                cross = cross_2lines(line1, line2)
                if (cross and point_in_sec(cross, [cutter[i], cutter[(i + 1) % n]]) and
                        point_in_sec(cross, [cutter[j], cutter[(i + 1) % n]])):
                    return True
    return False

# Поиск перпендикуляра, через точку point 
def perp_by_sige(point, line):
    an = -line['b']
    bn = line['a']
    # Ищем нормаль через точку point
    cn = -(an * point[0] + bn * point[1])
    perp = {'a': an, 'b': bn, 'c': cn}
    return perp


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



# Функция, которая определяет, точка внутри или
# точка снаружи. 
# Методом подсчета кол-ва пересечения горизонтальной прямой
# и сторонами многоугольника.
# point - точка
# arr - многоугольник   
def inside_or_outside(point, arr):
    print("inside or outside", point, arr)
    count_cross = 0
    for i in range(len(arr)):
        print("for i", i)
        cross = cross_line_edge(point, [point[0] + 1000, point[1]], arr[i], arr[(i + 1) % len(arr)])
        print("CROSS", cross)
        if cross is not None:
            count_cross += 1

    if count_cross % 2 == 0:
        print("outside")
        return False
    elif count_cross % 2 == 1:
        print("inside")
        return True

#  0 - отсекаемое
#  1 - отсекатель
#  2 - точки пересечения
# Поиск позиции, куда можно поставить точку point,
# в массив С, после c_i
def find_pos_in_arr(point, C, c_i):
    i = C.index(c_i)
    print("find_pos_in_C", i, point, C , c_i)
    print(C[i][0], C[(i + 1) % len(C)][0])

    # Если соседние точки приндлежат стороне отсекаемого или 
    # отсекателю, то сразу ставлю точку point межуд ними
    if C[i][2] == 1 and C[(i + 1) % len(C)][2] == 1:
        return i + 1
    if C[i][2] == 0 and C[(i + 1) % len(C)][2] == 0:
        return i + 1

    # В случае, когда точки идут в порядке возрастания 
    if C[i][0] < C[(i+1)% len(C)][0]:
        for j in range(i, len(C)):
            if point[0] > C[j][0]:
                if point[0] < C[(j+1) % len(C)][0]:
                    return j + 1

    # В случае, когда точки идут в порядке убывания
    elif C[i][0] > C[(i+1)% len(C)][0]:
        for j in range(i, len(C)):
            if point[0] < C[j][0]:
                if point[0] > C[(j+1) % len(C)][0]:
                    return j + 1

    # В случае, когда координаты X равны, действуем по координате Y
    elif C[i][0] == C[(i+1)% len(C)][0]:
        # Возрастание
        if C[i][1] < C[(i+1)% len(C)][1]:
            for j in range(i, len(C)):
                print("find_JJJJJ", point[1], C[j][1])
                if point[1] > C[j][1]:
                    print("find_JJJJJ", point[1], C[j][1])
                    if point[1] < C[(j+1) % len(C)][1]:
                        return j + 1

        # Убывание
        elif C[i][1] > C[(i+1)% len(C)][1]:
            for j in range(i, len(C)):
                print("find_JJJJJ", point[1], C[j][1])
                if point[1] < C[j][1]:
                    print("find_JJJJJ", point[1], C[j][1])
                    if point[1] > C[(j+1) % len(C)][1]:
                        return j + 1

# Получение новых массивов внешних и внутренних многоугольников
# с учетом точек пересечения 
def new_a_ab_c_cb(a, a_b, c, c_b):
    A = deepcopy(a)
    Ab = deepcopy(a_b)
    C = deepcopy(c)
    Cb = deepcopy(c_b)

    len_a = len(a)
    len_c = len(c)

    # цикл по сторонам отсекателя ВНЕШНЕГО 
    for i in range(len_c):
        print("i", i)
        # цикл по сторонам отсекаемого ВНЕШНЕГО
        for j in range(len_a):
            print("j", j)
            point = cross_line_edge(c[i], c[(i+1) % len_c],
                                 a[j], a[(j+1) % len_a])
            if point is None:
                print("None")
                continue
            print(point)
            point.append(2)

            # Необходимо вставить точку point в массивы  C
            pos_c = find_pos_in_arr(point, C, c[i])
            print("pos", C[(pos_c - 1)%len(C)], C[pos_c % len(C)], pos_c, point)

            C.append(C[len(C) - 1])
            for k in range(len(C) - 2, pos_c - 1, -1):
                C[k + 1] = C[k]
            C[pos_c] = point
            
            # Необходимо вставить точку point в массивы A 
            print("перед find_pos_in_a", j, a[j])
            pos_a = find_pos_in_arr(point, A, a[j])
            print("pos", A[(pos_a - 1)%len(A)], A[(pos_a)%len(A)], pos_a, point)
            
            A.append(A[len(A) - 1])
            for k in range(len(A) - 2, pos_a - 1, -1):
                A[k + 1] = A[k]
            A[pos_a] = point

            
        # цикл по отсекаемому - ВНУТРЕННЕМУ
        # так как их может быть много, то я храню их как массив отсекателей, а отсекатель - массив точек
        for l in range(len(a_b)):
            aa_b = a_b[l]
            print("aa_b", aa_b)
            len_aab = len(aa_b)
            for j in range(len_aab):
                print("j", j)
                point = cross_line_edge(c[i], c[(i+1) % len_c],
                                    aa_b[j], aa_b[(j+1) % len_aab])
                if point is None:
                    print("None")
                    continue
                print(point)
                point.append(2)

                # Необходимо вставить точку point в массивы A и C
                pos_c = find_pos_in_arr(point, C, c[i])
                print("pos", C[(pos_c - 1)%len(C)], C[pos_c % len(C)], pos_c, point)

                C.append(C[len(C) - 1])
                for k in range(len(C) - 2, pos_c - 1, -1):
                    C[k + 1] = C[k]
                C[pos_c] = point
                
                # Необходимо вставить точку point в массивы A и C
                print("перед find_pos_in_a", j, aa_b[j])
                pos_a = find_pos_in_arr(point, Ab[l], aa_b[j])
                print("pos", Ab[l][(pos_a - 1)%len(Ab[l])], Ab[l][(pos_a)%len(Ab)], pos_a, point)

                Ab[l].append(Ab[l][len(Ab[l]) - 1])
                for k in range(len(Ab[l]) - 2, pos_a - 1, -1):
                    Ab[l][k + 1] = Ab[l][k]
                Ab[l][pos_a] = point

    # Цикл по отсекателю - ВНУТРЕННЕМУ
    # храню как массив массивов
    for t in range(len(c_b)):
        cc_b = c_b[t]
        len_ccb = len(cc_b)
        for i in range(len_ccb):
            print("i", i)
            # цикл по сторонам отсекаемого ВНЕШНЕГО
            for j in range(len_a):
                print("j", j)
                point = cross_line_edge(cc_b[i], cc_b[(i+1) % len_ccb],
                                    a[j], a[(j+1) % len_a])
                if point is None:
                    print("None")
                    continue
                print(point)
                point.append(2)

                # Необходимо вставить точку point в массивы  C
                pos_c = find_pos_in_arr(point, Cb[t], cc_b[i])
                print("pos", Cb[t][(pos_c - 1)%len(Cb[t])], Cb[t][pos_c % len(Cb[t])], pos_c, point)

                Cb[t].append(Cb[t][len(Cb[t]) - 1])
                for k in range(len(Cb[t]) - 2, pos_c - 1, -1):
                    Cb[t][k + 1] = Cb[t][k]
                Cb[t][pos_c] = point
                
                # Необходимо вставить точку point в массивы A 
                print("перед find_pos_in_a", j, a[j])
                pos_a = find_pos_in_arr(point, A, a[j])
                print("pos", A[(pos_a - 1)%len(A)], A[(pos_a)%len(A)], pos_a, point)
                
                A.append(A[len(A) - 1])
                for k in range(len(A) - 2, pos_a - 1, -1):
                    A[k + 1] = A[k]
                A[pos_a] = point

                
            # цикл по отсекаемому - ВНУТРЕННЕМУ
            # так как их может быть много, то я храню их как массив отсекателей, а отсекатель - массив точек
            for l in range(len(a_b)):
                aa_b = a_b[l]
                print("aa_b", aa_b)
                len_aab = len(aa_b)
                for j in range(len_aab):
                    print("j", j)
                    point = cross_line_edge(cc_b[i], cc_b[(i+1) % len_ccb],
                                        aa_b[j], aa_b[(j+1) % len_aab])
                    if point is None:
                        print("None")
                        continue
                    print(point)
                    point.append(2)

                    # Необходимо вставить точку point в массивы A и C
                    pos_c = find_pos_in_arr(point, Cb[t], cc_b[i])
                    print("pos", Cb[t][(pos_c - 1)%len(Cb[t])], Cb[t][pos_c % len(Cb[t])], pos_c, point)

                    Cb[t].append(Cb[t][len(Cb[t]) - 1])
                    for k in range(len(Cb[t]) - 2, pos_c - 1, -1):
                        Cb[t][k + 1] = Cb[t][k]
                    Cb[t][pos_c] = point
                    
                    # Необходимо вставить точку point в массивы A и C
                    print("перед find_pos_in_a", j, aa_b[j])
                    pos_a = find_pos_in_arr(point, Ab[l], aa_b[j])
                    print("pos", Ab[l][(pos_a - 1)%len(Ab[l])], Ab[l][(pos_a)%len(Ab)], pos_a, point)

                    Ab[l].append(Ab[l][len(Ab[l]) - 1])
                    for k in range(len(Ab[l]) - 2, pos_a - 1, -1):
                        Ab[l][k + 1] = Ab[l][k]
                    Ab[l][pos_a] = point

    C.append(C[0])
    A.append(A[0])
    for i in range(len(Ab)):
        if len(Ab[i]):
            Ab[i].append(Ab[i][0])
    for i in range(len(Cb)):
        if len(Cb[i]):
            Cb[i].append(Cb[i][0])
    print("\n\n")
    print("C", C)
    print("A", A)
    print("Ab", Ab)
    print("Cb", Cb)

    return A, C, Ab, Cb

# Вообще....
# Чтобы определить точки входа и выхода достаточно найти первую точку пересечения по массиву А
# и определить - вход это или выход
# Если точка А0 - начало отсекаемого ВНЕ отсекателя - то первая точка пересечения - ВХОД
# Если А0 - ВНУТРИ - то точка выхода
def get_enter_exit_point(a, ab, c, cb):
    print("\n\n\n\n\n\n\nget_enter_exit_point")
    print(a)
    print(ab)
    enter_flag = True

    enter = []
    exit = []

    # выбор точек входа-выхода из массива А 
    flag1 = inside_or_outside(a[0], c)
    flag2 = False
    for i in range(len(cb)):
        ccb = cb[i]
        if len(ccb):
            flag2 = inside_or_outside(a[0], ccb)
    if flag1 == True and flag2 == True:
        flag1 = False
    
    if flag1:
        enter_flag = False
    
    for i in range(len(a) - 1):
        if a[i][2] == 2:
            if enter_flag:
                enter.append(a[i])
                enter_flag = False
            else:
                exit.append(a[i])
                enter_flag = True

    # выбор точек выхода-выхода из массива Ab
    for j in range(len(ab)):
        aab = ab[j]
        if len(aab):
            enter_flag = True

            flag1 = inside_or_outside(aab[0], c)
            flag2 = False
            for i in range(len(cb)):
                ccb = cb[i]
                flag2 = inside_or_outside(aab[0], ccb)
            if flag1 == True and flag2 == True:
                flag1 = False
            
            if flag1:
                enter_flag = False

            
            for i in range(len(aab) - 1):
                print(i)
                if aab[i][2] == 2:
                    if enter_flag:
                        print("enter")
                        enter.append(aab[i])
                        enter_flag = False
                    else:
                        print("exit")
                        exit.append(aab[i])
                        enter_flag = True
    print(enter, exit, "\n\n\n\n")
    return enter, exit

# Делаю имитацию списка, то есть храню координаты точки, где они 
# встречаются в другом массиве
# То есть точки массива А содержат координаты массива С, 
# где расположены эти точки
# и наоборот 
def do_list_all_link(a, c, ab, cb):
    a_copy = deepcopy(a)
    c_copy = deepcopy(c)
    ab_copy = deepcopy(ab)
    cb_copy = deepcopy(cb)

    # По массиву А, и ищу точки в массиве С
    # ВНЕШНИЙ массив А
    for i in range(len(a) - 1):
        if a[i][2] == 2:
            print(a[i][2])
            if a[i] in c:
                pos = c.index(a[i])
                a_copy[i].append(-1)
                a_copy[i].append(pos)
                continue

            for j in range(len(cb)):
                if a[i] in cb[j]:
                    pos = cb[j].index(a[i])
                    a_copy[i].append(j)
                    a_copy[i].append(pos)
                    continue
    
    # По массиву А, и ищу точки в массиве С
    # ВНУТРЕННИЙ массив А
    for l in range(len(ab)):
        aab = ab[l]
        for i in range(len(aab)):
            if aab[i][2] == 2:
                if aab[i] in c:
                    pos = c.index(aab[i])
                    ab_copy[l][i].append(-1)
                    ab_copy[l][i].append(pos)
                    continue

                for j in range(len(cb)):
                    if aab[i] in cb[j]:
                        pos = cb[j].index(aab[i])
                        ab_copy[l][i].append(j)
                        ab_copy[l][i].append(pos)
                        continue
    
    # По массиву С, и ищу точки в массиве А
    # ВНЕШНИЙ массив С
    for i in range(len(c) - 1):
        if c[i][2] == 2:
            if c[i] in a:
                pos = a.index(c[i])
                c_copy[i].append(-1)
                c_copy[i].append(pos)
                continue
            for j in range(len(ab)):
                if c[i] in ab[j]:
                    pos = ab[j].index(c[i])
                    c_copy[i].append(j)
                    c_copy[i].append(pos)
                    continue

    # По массиву С, и ищу точки в массиве А
    # ВНУТРЕННИЙ массив С
    for l in range(len(cb)):
        ccb = cb[l]
        for i in range(len(ccb)):
            if ccb[i][2] == 2:
                if ccb[i] in a:
                    pos = a.index(ccb[i])
                    cb_copy[l][i].append(-1)
                    cb_copy[l][i].append(pos)
                    continue

                for j in range(len(ab)):
                    if ccb[i] in ab[j]:
                        pos = ab[j].index(ccb[i])
                        cb_copy[l][i].append(j)
                        cb_copy[l][i].append(pos)
                        continue
    
    print("\n\n")
    print("a", a_copy)
    print("c", c_copy)
    print("ab", ab_copy)
    print("cb", cb_copy)

    return a_copy, c_copy, ab_copy, cb_copy

# Поиск точки следующей за заданной
# точки 2ого типа 
def get_next_point2(i, arr):
    print(i, arr)
    for j in range(i + 1, len(arr) * 2):
        if arr[(j) % len(arr)][2] == 2:
            return (j) % len(arr)

# Поиск точки перед заданной
# точки 2ого типа
def get_before_point2(i, arr):
    print("get_before_point2", i, arr)
    for j in range(i - 1, -len(arr) * 2, -1):
        print(arr[(j) % len(arr)])
        if arr[(j) % len(arr)][2] == 2:
            return (j) % len(arr)


##### Внутренние многоугольники #####
# По массиву А идем слева направо
# По массиву С идем слева направо
def get_inside_rest(enter, a, c, ab, cb):
    res = []
    all_res = []
    count = 0
    print("get_inside_rest", enter)

    i = 0
    # Ищу внутренние многоугольники пока длина входных точек не равна 0
    while len(enter) != 0:
        res = []
        res.append(enter[i])
        print(res)

        # начало внутреннего многоугольника (точка начала из списка enter)
        # первый раз идем по массиву А слева направо

        ##### Поиск точки в массиве А #####
        fl = -1
        pos_on_arr = 0
        for k in range(len(a)):
            if res[0][0] == a[k][0] and res[0][1] == a[k][1]:
                fl = -1 
                pos_on_arr = k
        for k in range(len(ab)):
            aab = ab[k]
            for l in range(len(aab)):
                if res[0][0] == aab[l][0] and res[0][1] == aab[l][1]:
                    fl = k
                    pos_on_arr = l
        #####
        
        # Если точка лежит в массиве А, то есть массив внешнего отсекаемого
        if fl == -1:
            pos = get_next_point2(pos_on_arr, a)
            count += 1
            end = pos
            if pos_on_arr > pos:
                end = pos + len(a) 
            for k in range(pos_on_arr + 1, end):
                res.append(a[k % len(a)])
            print(res, count, pos)
            res.append(a[pos])
        # Иначе точка лежит в fl-ом массиве Аb - внутренние отсекаемые
        else:
            pos = get_next_point2(pos_on_arr, ab[fl])
            count += 1
            end = pos
            if pos_on_arr > pos:
                end = pos + len(a) 
            for k in range(pos_on_arr + 1, end):
                res.append(ab[fl][k % len(ab[fl])])
            res.append(ab[fl][pos])

        # Ищу остальные точки - условие пока 0 не будет равно последней
        while (res[len(res) - 1][0] != res[0][0] or res[len(res) - 1][1] != res[0][1]):
            print("\n\n\nwhile", res)
            
            # Когда идем четное кол-во (начинаем считать с 0)
            # то идем по массиву А слева направо
            if count % 2 == 0:
                if res[len(res) - 1][3] == -1:
                    p = res[len(res) - 1][4]
                    pos = get_next_point2(p, a)
                    count += 1
                    end = pos
                    if p > pos:
                        end = pos + len(a)
                    print("PPP1", res, count, end)
                    for k in range(p + 1, end):
                        res.append(a[k % len(a)])
                    res.append(a[pos])
                else:
                    p = res[len(res) - 1][3]
                    pp = res[len(res) - 1][4]
                    pos = get_next_point2(pp, ab[p])
                    count += 1
                    end = pos
                    print("pp, pos", pp, pos)
                    if pp > pos:
                        end = pos + len(ab[p])
                    print("PPP2", res, count, end)
                    
                    for k in range(pp + 1, end):
                        res.append(ab[p][k % len(ab[p])])
                    res.append(ab[p][pos])
            else:
                # Когда идем нечетное кол-во (начинаем счет с 0)
                # то идем по массиву С слева направо 
                if res[len(res) - 1][3] == -1:
                    p = res[len(res) - 1][4]
                    pos = get_next_point2(p, c)
                    count += 1
                    end = pos
                    if p > pos:
                        end = pos + len(c)
                    print("PPP1", res, count, end)
                    for k in range(p + 1, end):
                        res.append(c[k % len(c)])
                    res.append(c[pos])
                else:
                    p = res[len(res) - 1][3]
                    pp = res[len(res) - 1][4]
                    pos = get_next_point2(pp, cb[p])
                    count += 1
                    end = pos
                    print("pp, pos", pp, pos)
                    if pp > pos:
                        end = pos + len(cb[p])
                    print("PPP2", res, count, end)
                    
                    for k in range(pp + 1, end):
                        res.append(cb[p][k % len(cb[p])])
                    res.append(cb[p][pos])
            
            
        # результирующий массив заносим в список всех массивов, 
        # далее удаляем из enter все точки второго типа, которые
        # есть в списке res
        print("\n\n\n")
        all_res.append(res)
        pop_arr = []
        for j in range(len(res) - 1):
            print(res[j])
            if res[j][2] == 2:
                print("res[j][2] == 2", res[j])
                for k in range(len(enter)):
                    print(enter)
                    if res[j][0] == enter[k][0] and \
                       res[j][1] == enter[k][1]:
                        print("res in enter", res[j])
                        pop_arr.append(enter[k])
        print("pop_arr", pop_arr)
        for j in pop_arr:
            print(j)
            enter.remove(j)
        print("enter after remove", enter)



        print("\n\n\n\n", pos, res)
    return all_res


##### Внешние многоугольники ####
# По массиву А идем слева направо
# По массиву С идем справо налево
def get_outside_rest(exit_point, a, c, ab, cb):
    res = []
    all_res = []
    count = 0
    print("get_outside_rest", exit_point)

    i = 0
    while len(exit_point) != 0:
        res = []
        res.append(exit_point[i])
        print(res)

        # начало внутреннего многоугольника (точки из списка exit_point)
        # первый раз идем по массиву А слева направо
        fl = -1
        pos_on_arr = 0
        for k in range(len(a)):
            if res[0][0] == a[k][0] and res[0][1] == a[k][1]:
                fl = -1 
                pos_on_arr = k
        for k in range(len(ab)):
            aab = ab[k]
            for l in range(len(aab)):
                if res[0][0] == aab[l][0] and res[0][1] == aab[l][1]:
                    fl = k
                    pos_on_arr = l
        print("FL", fl)
        if fl == -1:
            pos = get_next_point2(pos_on_arr, a)
            count += 1
            end = pos
            if pos_on_arr > pos:
                end = pos + len(a) 
            for k in range(pos_on_arr + 1, end):
                res.append(a[k % len(a)])
            print(res, count, pos)
            res.append(a[pos])
        else:
            pos = get_next_point2(pos_on_arr, ab[fl])
            count += 1
            end = pos
            if pos_on_arr > pos:
                end = pos + len(a) 
            for k in range(pos_on_arr + 1, end):
                res.append(ab[fl][k % len(ab[fl])])
            res.append(ab[fl][pos])

        # все остальные - пока не замкну...
        while (res[len(res) - 1][0] != res[0][0] or res[len(res) - 1][1] != res[0][1]):
            print("\n\n\nwhile", res)
            
            # Когда идем четное кол-во (начинаем считать с 0)
            # то идем по массиву А слева направо
            if count % 2 == 0:
                if res[len(res) - 1][3] == -1:
                    p = res[len(res) - 1][4]
                    pos = get_next_point2(p, a)
                    count += 1
                    end = pos
                    if p > pos:
                        end = pos + len(a)
                    print("PPP1", res, count, end)
                    for k in range(p + 1, end):
                        res.append(a[k % len(a)])
                    res.append(a[pos])
                else:
                    p = res[len(res) - 1][3]
                    pp = res[len(res) - 1][4]
                    pos = get_next_point2(pp, ab[p])
                    count += 1
                    end = pos
                    print("pp, pos", pp, pos)
                    if pp > pos:
                        end = pos + len(ab[p])
                    print("PPP2", res, count, end)
                    
                    for k in range(pp + 1, end):
                        res.append(ab[p][k % len(ab[p])])
                    res.append(ab[p][pos])
            else:
                # Когда идем нечетное кол-во (начинаем счет с 0)
                # то идем по массиву С справо налево 
                if res[len(res) - 1][3] == -1:
                    p = res[len(res) - 1][4]
                    pos = get_before_point2(p, c)
                    count += 1
                    end = pos
                    if p < pos:
                        end = pos - len(c) - 1
                    print("PPP1", res, count, end)
                    for k in range(p - 1, end, -1):
                        res.append(c[k % len(c)])
                    res.append(c[pos])

                else:
                    p = res[len(res) - 1][3]
                    pp = res[len(res) - 1][4]
                    print("p, pp, cb[p]", p, pp, cb[p])
                    pos = get_before_point2(pp, cb[p])
                    count += 1
                    end = pos
                    print("pp, pos", pp, pos)
                    if pp < pos:
                        end = pos - len(cb[p]) - 1
                    print("PPP2", res, count, end)
                    
                    for k in range(pp - 1, end, -1):
                        res.append(cb[p][k % len(cb[p])])
                    res.append(cb[p][pos])
            
        # результирующий массив заносим в список всех массивов, 
        # далее удаляем из exit_point все точки второго типа, которые
        # есть в списке res
        print("\n\n\n")
        all_res.append(res)
        pop_arr = []
        for j in range(len(res) - 1):
            print(res[j])
            if res[j][2] == 2:
                print("res[j][2] == 2", res[j])
                for k in range(len(exit_point)):
                    print(exit_point)
                    if res[j][0] == exit_point[k][0] and \
                       res[j][1] == exit_point[k][1]:
                        print("res in exit_point", res[j])
                        if exit_point[k] not in pop_arr:
                            pop_arr.append(exit_point[k])
        print("pop_arr", pop_arr)
        for j in pop_arr:
            print(j)
            exit_point.remove(j)
        print("exit_point after remove", exit_point)
        
        print("\n\n\n\n", pos, res)
    return all_res


def alg_cutter_baylera_azertona(a, c, a_b, c_b):
    inside_rest = [[]]
    outside_rest = []
    # if check_cross(len(a), a) or \
    #    check_cross(len(c), c) or \
    #    check_cross(len(a_b), a_b) or \
    #    check_cross(len(c_b), c_b):
    #    return -1, None, None

    new_a, new_c, new_ab, new_ac = new_a_ab_c_cb(a, a_b, c, c_b)

    new_a, new_c, new_ab, new_cb = do_list_all_link(new_a, new_c, new_ab, new_ac)
    enter_point, exit_point = get_enter_exit_point(new_a, new_ab, c, c_b)
    print("enter", enter_point)
    print("exit", exit_point)

    flag  = False
    for i in range(len(new_a)):
        if new_a[i][2] == 2:
            flag = True
    print("ALGORITM flag", flag)

    # Если в массиве А - нет точек пересечения
    if flag == False:
        # А не в С и С не в А
        if ((inside_or_outside(new_a[0], new_c) == False and inside_or_outside(new_a[1], new_c) == False)
            and inside_or_outside(new_c[0], new_a) == False):
            print("a не в с и с не в а")
            for i in range(len(new_a)):
                for j in range(len(new_c)):
                    if new_a[i][0] == new_c[j][0] and new_a[i][1] == new_c[j][1]:
                        inside_rest.append([new_a[i], new_a[i]])
            outside_rest.append(new_a)

        # А не в С и С в А
        if (inside_or_outside(new_a[0], new_c) == False and inside_or_outside(new_c[0], new_a) == True):
            print("a не в с и с в а")
            outside_rest.append(new_a)


        # А в С и С не в А
        if ((inside_or_outside(new_a[0], new_c) == True or inside_or_outside(new_a[1], new_c))
            and inside_or_outside(new_c[0], new_a) == False):
            print("while a в с и с не в а", len(new_cb))
            if len(new_cb) == 0:
                inside_rest.append(new_a)
            else:
                for j in range(len(new_cb)):
                    ccb = new_cb[j]
                    if (inside_or_outside(new_a[0], ccb) or inside_or_outside(new_a[1], ccb)):
                        outside_rest.append(new_a)
                    else:
                        inside_rest.append(new_a)



    if len(enter_point) == 0 and len(exit_point) == 0:
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
# >>>>>>> 082f65a4d92ff2bb2cbcf72f7e118942e9f4c949
    else:
        inside_rest = get_inside_rest(enter_point, new_a, new_c, new_ab, new_cb)
        print("RES inside_rest", inside_rest)

        print("\n\n\n\n\n\n\n\n\n")

        outside_rest = get_outside_rest(exit_point, new_a, new_c, new_ab, new_cb)
        print("RES outside_rest", outside_rest)
        print("\n\n\n\n\n\n\n\n\n")
    return 0, inside_rest, outside_rest

# def main():
#     # a = [[90, 30, 0], [150, 30, 0], [120, 90, 0], [170, 130, 0], [90, 130, 0]]
#     # a_b = [[[100, 120, 0], [130, 120, 0], [110, 100, 0]]]

#     # c = [[60, 50, 1], [170, 50, 1], [110, 110, 1], [130, 160, 1], [30, 160, 1], [60, 50, 1]]
#     # c_b = [[[70, 80, 1], [110, 80, 1], [100, 60, 1]]]

#     c = [[40, 40, 0], [140, 40, 0], [90, 120, 0]]
#     c_b = [[]]

#     a = [[90, 60, 1], [170, 50, 1], [130, 120, 1]]
#     a_b = [[]]

#     res_in, res_out = alg_cutter_baylera_azertona(a, c, a_b, c_b)
#     print("IN MAIN.PY", res_in, res_out)




# if __name__ == "__main__":
#     main()
