import math

from itertools import combinations
from collections import deque
from check import *
from geom import *

def intersheightside(ax, ay, bx, by, cx, cy):
    '''
        Функция для нахождения точки пересечения высоты и стороны.
    '''
    # Нахождение координат векторов ВА и ВС
    x_bc = cx - bx
    y_bc = cy - by
    x_ba = ax - bx
    y_ba = ay - by

    # Проекция ВА на ВС
    projection = (x_bc * x_ba + y_bc * y_ba) / (x_bc * x_bc + y_bc * y_bc)

    # Координаты точки пересечения стороны ВС и высоты из точки А
    x_h_bc = (bx + projection * x_bc)
    y_h_by = (by + projection * y_bc)

    return x_h_bc, y_h_by


def intersheights(ax, ay, bx, by, cx, cy):
    '''
        Функция для нахождения точки пересечения высот.
    '''
    # Уравнение прямой рассматривается как Dy = Kx + B

    # Коэффициенты прямой BC
    # Если точки В и С лежат на одной вертикальной прямой
    if abs((cx - bx) - 0) <= 1e-6:
        k_bc = 1
        b_bc = -cx
        d_bc = 0
    else:
        k_bc = (cy - by) / (cx - bx)
        b_bc = cy - (k_bc * cx)
        d_bc = 1
    
    # Коэффициенты высоты из А
    # Когда прамая ВС лежит параллельно Ох
    if abs(k_bc - 0) <= 1e-6:
        k_ah = 1
        b_ah = -ax
        d_ah = 0
    # Когда ВС параллельна Оу
    elif abs(k_bc - 1) <= 1e-6 and abs(d_bc - 0) <= 1e-6:
        k_ah = 0
        b_ah = ay
        d_ah = 1
    else:
        k_ah = -1 / k_bc
        b_ah = ay - k_ah * ax
        d_ah = 1

    # Коэффициенты прямой АС
    # Если точки A и С лежат на одной вертикальной прямой
    if abs((cx - ax) - 0) <= 1e-6:
        k_ac = 1
        b_ac = -cx
        d_ac = 0
    else:
        k_ac = (cy - ay) / (cx - ax)
        b_ac = cy - (k_ac * cx)
        d_ac = 1

    # Коэффициенты высоты из В
    # Когда прамая АС лежит параллельно Ох
    if abs(k_ac - 0) <= 1e-6:
        k_bh = 1
        b_bh = -bx
        d_bh = 0
    # Когда АС параллельна Оу
    elif abs(k_ac - 1) <= 1e-6 and abs(d_ac - 0) <= 1e-6:
        k_bh = 0
        b_bh = by
        d_bh = 1
    else:
        k_bh = -1 / k_ac
        b_bh = by - k_bh * bx
        d_bh = 1

    # Нахождение координаты х (тока пересечение высот)
    x = (d_ah * b_bh - d_bh * b_ah) / (d_bh * k_ah - d_ah * k_bh)

    # Подставляем найденное х в уравнение той прямой,
    # которая НЕ параллельна Оу
    if abs(d_bh - 0) <= 1e-6:
        y = k_ah * x + b_ah
    else:
        y = k_bh * x + b_bh
    return x, y


def ang(ax, ay):
    '''
        Нахождение угла между прямой и осью ординат.
    '''
    # Если точка на оси ординат
    if abs(ax - 0) <= 1e-6:
        ang_res = 0
    else:
        tg = ay / ax
        print(math.degrees(math.atan(abs(tg))))
        ang_res = 90 - math.degrees(math.atan(abs(tg)))
    return ang_res


def point_in_oneline(ax, ay, bx, by, cx, cy):
    '''
        Проверка, лежат ли точки на одной прямой.
    '''
    return abs((cx - ax) * (by - ay) - (bx - ax) * (cy - ay)) <= 1e-6


def find_combin_point(points):
    '''
        Поиск треугольника, удовлетворяющего условию задачи.
    '''
    max_ang = 0
    ortho = None
    h_abc = None
    best_index = None

    if len(points) == 0:
        return  -1, None, None, None, None
    elif  0 < len(points) < 3:
        return points, None, None, None, None
    else:
        best_points = None

    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                com = [points[i], points[j], points[k]]
                index = [i, j, k]
                if point_in_oneline(com[0][0], com[0][1],
                                    com[1][0], com[1][1],
                                    com[2][0], com[2][1]):
                    continue
                point_h = list(intersheights(com[0][0], com[0][1],
                                             com[1][0], com[1][1],
                                             com[2][0], com[2][1]))
                angl = ang(point_h[0], point_h[1])
                if (angl >= max_ang):
                    max_ang = angl
                    best_points = com.copy()
                    best_index = index.copy()
                    h_abc = []
                    h_abc.append(intersheightside(best_points[0][0], best_points[0][1],
                                                  best_points[1][0], best_points[1][1],
                                                  best_points[2][0], best_points[2][1]))
                    h_abc.append(intersheightside(best_points[1][0], best_points[1][1],
                                                  best_points[0][0], best_points[0][1],
                                                  best_points[2][0], best_points[2][1]))
                    h_abc.append(intersheightside(best_points[2][0], best_points[2][1],
                                                  best_points[1][0], best_points[1][1],
                                                  best_points[0][0], best_points[0][1]))

                    ortho = list(intersheights(best_points[0][0], best_points[0][1],
                                               best_points[1][0], best_points[1][1],
                                               best_points[2][0], best_points[2][1]))
    return best_points, h_abc, ortho, best_index


def info_win(root, angle):
    info = tk.Toplevel(root)
    info.title("ОТВЕТ!")
    info["bg"] = "#ffffff"
    info.geometry("500x250+300+10")
    text = tk.Label(info, text="Зеленый цвет - найденный треугольник",
                    fg="green", bg="#ffffff",
                    font="consolas 12")
    text.pack()
    text = tk.Label(info, text="Синий цвет - высоты треугольника",
                    fg="blue", bg="#ffffff",
                    font="consolas 12")
    text.pack()
    text = tk.Label(info, text="Красный цвет - линия, соединяющая ортоцент и (0;0)",
                    fg="red", bg="#ffffff",
                    font="consolas 12")
    text.pack()
    text = tk.Label(info, text="Серый цвет - оси координат\n"
                    "(декартовая система координат)\n",
                    fg="grey", bg="#ffffff",
                    font="consolas 12")
    text.pack()
    text = tk.Label(info, text="ОТВЕТ: Угол между красной линии и Осью ординат\n"
                               " равен %.3f градусов\n"
                               % angle,
                    fg="black", bg="#ffffff",
                    font="consolas 12")
    text.pack()


def draw_answer(root):
    root.answer.delete("all")
    points = point_list(root)
    combin_h = find_combin_point(points)
    combin = combin_h[0]
    h_abc = combin_h[1]
    ortho_point = combin_h[2]
    index = combin_h[3]

    if combin is None:
        messagebox.showerror("Нет решения", "Для данного набора точек"
                             " невозможно найти решение.")
        return
    if combin == -1:
        messagebox.showerror("Нет решения", "Впишите точки в поле ввода.")
        return
    if 0 < len(combin) < 3:
        messagebox.showerror("Нет решения", "Из данных точек нельзя "
                             "построить треугольник. (точек меньше 3)")
        return

    x_win = root.answer.winfo_height() + 100
    y_win = root.answer.winfo_width() - 190
    x_min = x_max = ortho_point[0]
    y_min = y_max = ortho_point[1]
    
    for point in combin:
        if point[0] > x_max:
            x_max = point[0]
        if point[0] < x_min:
            x_min = point[0]
        if point[1] > y_max:
            y_max = point[1]
        if point[1] < y_min:
            y_min = point[1]
    if y_min > 0:
        y_min = -1
    if x_min > 0:
        x_min = -1
    if x_max < 0:
        x_max = 1
    if y_max < 0:
        y_max = 1

    scale_x = (x_win - 100) / (x_max - x_min)
    scale_y = (y_win - 100) / (y_max - y_min)
    scale_all = scale_x if scale_x < scale_y else scale_y
    setfor_x = -x_min * scale_all + 50
    setfor_y = -y_min * scale_all + 40

    # Массив для координат осей
    line_oxy = [[0, y_min - 30], [0, y_win - 100],
                [x_min - 30, 0], [x_win, 0]]
    line_res = []
    for dot in line_oxy:
        if dot[0] == x_win:
            x = dot[0] * scale_all + setfor_x
            x -= 10 * scale_all + setfor_x
        else:
            x = dot[0] * scale_all + setfor_x
        line_res.append(x)
        if dot[1] == y_win:
            y = y_win - (dot[1] * scale_all + setfor_y) - 40
            y -= y_win - (10 * scale_all + setfor_y) - 40
        else:
            y = y_win - (dot[1] * scale_all + setfor_y) - 40
        line_res.append(y)

    # Координаты треугольника
    res = []
    for dot in combin:
        x = dot[0] * scale_all + setfor_x
        res.append(x)
        y = y_win - (dot[1] * scale_all + setfor_y) - 40
        res.append(y)
    res.append(res[0])
    res.append(res[1])

    # Координаты линии по условию задачи
    line_ortho = [[0, 0], ortho_point]
    ortho = []
    for dot in line_ortho:
        x = dot[0] * scale_all + setfor_x
        ortho.append(x)
        y = y_win - (dot[1] * scale_all + setfor_y) - 40
        ortho.append(y)

    # Координаты высот
    h_res = []
    for dot in h_abc:
        x = dot[0] * scale_all + setfor_x
        h_res.append(x)
        y = y_win - (dot[1] * scale_all + setfor_y) - 40
        h_res.append(y)

    # Рисунок треугольник
    root.answer.create_line(*res, fill="#3caa3c", width=5)

    # Рисунок высоты треугольника
    buf_h = [res[0], res[1],
             ortho[2], ortho[3]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)
    buf_h = [res[2], res[3],
             ortho[2], ortho[3]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)
    buf_h = [res[4], res[5],
             ortho[2], ortho[3]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)
    buf_h = [res[0], res[1],
             h_res[0], h_res[1]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)
    buf_h = [res[2], res[3],
             h_res[2], h_res[3]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)
    buf_h = [res[4], res[5],
             h_res[4], h_res[5]]
    root.answer.create_line(*buf_h,
                            fill="#7b68ee",
                            width=3)

    # Рисунок оси Ох Оу
    root.answer.create_line(line_res[0], line_res[1],
                            line_res[2], line_res[3],
                            fill="grey",
                            arrow=tk.LAST,
                            width=2)
    root.answer.create_line(line_res[4], line_res[5],
                            line_res[6], line_res[7],
                            fill="grey",
                            arrow=tk.LAST,
                            width=2)

    # Рисунок линии по условию
    root.answer.create_line(*ortho,
                            fill="#ff5349",
                            width=1.5)


    # Написание координат в окне ответа
    for i in range(1, 6, 2):
        if res[i] == max(res[1], res[3], res[5]):
            root.answer.create_text(res[i - 1], res[i] + 10,
                                    fill="black",
                                    font="consolas 10",
                                    text="%d (%.2f;%.2f)" % (index[i // 2] + 1,
                                                            combin[i // 2][0],
                                                            combin[i // 2][1]))
        elif res[i] == min(res[1], res[3], res[5]):
            root.answer.create_text(res[i - 1], res[i] - 10,
                                    fill="black",
                                    font="consolas 10",
                                    text="%d (%.2f;%.2f)" % (index[i // 2] + 1,
                                                             combin[i // 2][0],
                                                             combin[i // 2][1]))
        elif res[i - 1] == max(res[0], res[2], res[4]):
            root.answer.create_text(res[i - 1] + 20, res[i] + 10,
                                    fill="black",
                                    font="consolas 10",
                                    text="%d (%.2f;%.2f)" % (index[i // 2] + 1,
                                                             combin[i // 2][0],
                                                             combin[i // 2][1]))
        else:
            root.answer.create_text(res[i - 1] + 10, res[i] + 10,
                                    fill="black",
                                    font="consolas 10",
                                    text="%d (%.2f;%.2f)" % (index[i // 2] + 1,
                                                             combin[i // 2][0],
                                                             combin[i // 2][1]))

    for i in range(3, 4, 2):
        if ortho[i] == max(ortho[1], ortho[3]):
            root.answer.create_text(ortho[i - 1], ortho[i] + 10,
                                    fill="red",
                                    font="consolas 10",
                                    text="  (%.2f;%.2f)" % (line_ortho[i // 2][0],
                                                            line_ortho[i // 2][1]))
        elif ortho[i] == min(ortho[1], ortho[3]):
            root.answer.create_text(ortho[i - 1], ortho[i] - 10,
                                    fill="red",
                                    font="consolas 10",
                                    text="  (%.2f;%.2f)" % (line_ortho[i // 2][0],
                                                            line_ortho[i // 2][1]))
        elif ortho[i - 1] == max(ortho[0], ortho[2]):
            root.answer.create_text(ortho[i - 1] + 20, ortho[i] + 10,
                                    fill="red",
                                    font="consolas 10",
                                    text="  (%.2f;%.2f)" % (line_ortho[i // 2][0],
                                                            line_ortho[i // 2][1]))
        else:
            root.answer.create_text(ortho[i - 1] + 10, ortho[i] + 10,
                                    fill="grey",
                                    font="consolas 10",
                                    text="  (%.2f;%.2f)" % (line_ortho[i // 2][0],
                                                            line_ortho[i // 2][1]))
        info_win(root, ang(ortho_point[0], ortho_point[1]))
