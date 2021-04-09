import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
from time import sleep, time
from tkinter import messagebox

from numpy import sign

W_canva = 1038
H_canva = 992
dot_num = 0
entry_time = 0

TASK = "Задача данной программы:\nРеализовать алгоритм растового\nзаполнения сплошных областей со списком ребер\n и флагом."
INST = "Ввод вершин многоугольника при помощи мыши: " \
       "\nЛевая кнопка мыши - добавить точку (соединение\n"\
       "с прерыдущей - автоматически)\n"\
       "Правая кнопка мыши - замкнуть фигурn\n"\
       "(то есть текущая точка соединиться с началом)\n"\
       "Средняя точка - возврат на шаг назад"
picture = 0
delay = 0
current_fig = 0
line_color = "#ff00ff"
bg_color = "#ffffff"
color_flag = "#00C12B"
gran_color = "#000000"
color_for_check = (0, 193, 43)
point_arr = [[]]
end_arr = [[]]
min_max = [[]]
time_fig = []


def bresenham(picture, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        picture.put(gran_color, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    curX = xStart
    curY = yStart

    for i in range(deltaX + 1):
        picture.put(gran_color, (curX, curY))

        if flag:
            if acc >= 0:
                curX += stepX
                acc -= (deltaX + deltaX)
            curY += stepY
            acc += deltaY + deltaY
        else:
            if acc >= 0:
                curY += stepY
                acc -= (deltaX + deltaX)
            curX += stepX
            acc += deltaY + deltaY

def left_click(event):
    global point_arr
    global current_fig
    global picture
    global dot_num
    point_arr[current_fig].append([event.x, event.y, gran_color])
    dot_num.insert(tk.END, "%3d - (%5d; %5d)" % (len(point_arr[current_fig]), event.x, event.y))
    if len(point_arr[current_fig]) >= 2:
        end_arr[current_fig].append([[point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 2][1]],
                                [point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 1][1]]])
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][1])

def right_click(event):
    global point_arr
    global current_fig
    global picture

    print(current_fig)
    end_arr[current_fig].append([[point_arr[current_fig][0][0],
                             point_arr[current_fig][0][1]],
                            [point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                             point_arr[current_fig][len(point_arr[current_fig]) - 1][1]]])
    bresenham(picture, point_arr[current_fig][0][0],
                   point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                   point_arr[current_fig][0][1],
                   point_arr[current_fig][len(point_arr[current_fig]) - 1][1])
    current_fig += 1
    end_arr.append(list())
    point_arr.append(list())
    print(point_arr, end_arr)

def center_click(event):
    global bg_color
    global gran_color
    global point_arr
    global current_fig
    global picture
    global dot_num
    if len(point_arr) == 0:
        return
    
    # Удаление последней точки из списка точек
    list_dot = list(dot_num.get(0, tk.END))
    n = len(list_dot)
    list_dot.pop()
    dot_num.delete(0, tk.END)
    for i in range(len(list_dot)):
            dot_num.insert(tk.END, list_dot[i])

    # Удаление последней линии
    buf_color = gran_color
    gran_color = bg_color
    if len(point_arr[current_fig]) != 0:
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][1])
        point_arr[current_fig].pop()
        end_arr[current_fig].pop()
    else:
        end_arr.pop()
        point_arr.pop()
        current_fig -= 1
        # рисуем
    gran_color = buf_color


def set_canva_root(canva):
    global picture
    picture = tk.PhotoImage(width = W_canva, height = H_canva)

    canva.create_image((W_canva / 2, H_canva / 2), image = picture, state = "normal")


def clear_canva(canva):
    global point_arr
    global end_arr
    global current_fig
    global min_max
    global picture
    global dot_num
    canva.delete("all")
    dot_num.delete(0, tk.END)
    point_arr = [[]]
    end_arr = [[]]
    min_max = [[]]
    current_fig = 0
    
    picture = tk.PhotoImage(width = W_canva, height = H_canva)
    canva.create_image((W_canva / 2, H_canva / 2), image = picture, state = "normal")
    canva.place(x = 700, y = 0)


def choose_bg_color(root, r, c, canva):
    global bg_color
    bg_color = colorchooser.askcolor()[1]
    canva_bg_color = tk.Canvas(root, bg = bg_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 50)
    canva_bg_color.place(x = r, y = c)
    canva.configure(bg = bg_color)

def choose_line_color(root, r, c):
    global line_color
    line_color = colorchooser.askcolor()[1]
    canva_line_color = tk.Canvas(root, bg = line_color,
                            borderwidth = 5, relief = tk.RIDGE,
                            width = 60, height = 50)
    canva_line_color.place(x = r, y = c)

def choose_gran_color(root, r, c):
    global gran_color
    gran_color = colorchooser.askcolor()[1]
    canva_gran_color = tk.Canvas(root, bg = gran_color,
                            borderwidth = 5, relief = tk.RIDGE,
                            width = 60, height = 50)
    canva_gran_color.place(x = r, y = c)
    
def add_point(root, entry_x, entry_y):
    global point_arr
    global picture
    global current_fig
    global dot_num

    x_coord = int(entry_x.get())
    y_coord = int(entry_y.get())
    dot_num.insert(tk.END, "%3d - (%5d; %5d)" % (len(point_arr[current_fig]), x_coord, y_coo))
    point_arr[current_fig].append([x_coord, y_coord, gran_color])
    if len(point_arr[current_fig]) >= 2:
        end_arr[current_fig].append([[point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 2][1]],
                                [point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 1][1]]])
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][1])

def get_side(point_arr):
    x_right = 0
    x_left = W_canva
    y_bottom = 0
    y_top = H_canva

    for fig in point_arr:
        for i in fig:
            if i[0] > x_right:
                x_right = i[0]
            if i[0] < x_left:
                x_left = i[0]
            if i[1] > y_bottom:
                y_bottom = i[1]
            if i[1] < y_top:
                y_top = i[1]
    return y_top, x_right, y_bottom, x_left

def make_min_max(point_arr):
    global min_max
    min_max.clear()
    min_max = [[]]

    for fig in range(len(point_arr)):
        min_max[fig].append(((point_arr[fig][0][1] < point_arr[fig][len(point_arr[fig]) - 1][1] and
                                point_arr[fig][0][1] < point_arr[fig][1][1]) or
                               (point_arr[fig][0][1] > point_arr[fig][len(point_arr[fig]) - 1][1] and
                                point_arr[fig][0][1] > point_arr[fig][1][1])))
        for i in range(1, len(point_arr[fig]) - 1):
            min_max[fig].append(((point_arr[fig][i][1] < point_arr[fig][i - 1][1] and
                                    point_arr[fig][i][1] < point_arr[fig][i + 1][1]) or
                                   (point_arr[fig][i][1] > point_arr[fig][i - 1][1] and
                                    point_arr[fig][i][1] > point_arr[fig][i + 1][1])))
        min_max[fig].append((point_arr[fig][len(point_arr[fig]) - 1][1] < point_arr[fig][len(point_arr[fig]) - 2][1] and
                        point_arr[fig][len(point_arr[fig]) - 1][1] < point_arr[fig][0][1]) or
                       (point_arr[fig][len(point_arr[fig]) - 1][1] > point_arr[fig][len(point_arr[fig]) - 2][1] and
                        point_arr[fig][len(point_arr[fig]) - 1][1] > point_arr[fig][0][1]))
        min_max.append(list())
    min_max.pop()


def around_figure_edge(picture, edge):
    if edge[0][1] == edge[1][1]:
        return

    if edge[0][1] > edge[1][1]:
        edge[1], edge[0] = edge[0], edge[1]
    step_x = (edge[1][0] - edge[0][0]) / (edge[1][1] - edge[0][1])
    x = edge[0][0]
    y = edge[0][1]
    while y < edge[1][1]:
        if picture.get(int(x) + 1, y) != color_for_check:
            picture.put(color_flag, (int(x) + 1, y))
        else:
            picture.put(color_flag, (int(x), y))
        x += step_x
        y += 1

def around_figure_all(picture, end_arr):
    for fig in range(len(end_arr)):
        len_arr = len(end_arr[fig]) - 1
        for i in range(len_arr):
            around_figure_edge(picture, end_arr[fig][i])
        around_figure_edge(picture, end_arr[fig][len_arr])

def draw_raster_with_flag_delay(picture, canva, end_arr, sides, coef):
    global entry_time
    start = time()

    around_figure_all(picture, end_arr)
    canva.update()
    sleep(0.001 * coef)

    for y in range(sides[2], sides[0] - 1, -1):
        flag = False
        for x in range(sides[3], sides[1] + 3):
            if picture.get(x, y) == color_for_check:
                flag = not flag
            print(flag)
            if flag:
                picture.put(line_color, (x, y, x + 1, y + 1))
            else:
                picture.put(bg_color, (x, y, x + 1, y + 1))

        canva.update()
        sleep(0.001 * coef)
        # if flag:
        #     picture.put(line_color, (x, y, x, y + 1))
        # else:
        #     picture.put(bg_color, (x, y, x, y + 1))

    for fig in range(len(end_arr)):
        for i in range(len(end_arr[fig])):
            bresenham(picture, end_arr[fig][i][0][0], end_arr[fig][i][1][0], 
                        end_arr[fig][i][0][1], end_arr[fig][i][1][1])
    
    end = time()
    time_str = str(round(end - start, 4)) + "ms"
    entry_time.delete(0, tk.END)
    entry_time.insert(tk.END, time_str)

def draw_raster_with_flag(picture, end_arr, sides):
    global entry_time
    start = time()
    around_figure_all(picture, end_arr)

    for y in range(sides[2], sides[0] - 1, -1):
        flag = False
        for x in range(sides[3], sides[1] + 3):
            if picture.get(x, y) == color_for_check:
                flag = not flag
            if flag:
                picture.put(line_color, (x, y, x + 1, y + 1))
            else:
                picture.put(bg_color, (x, y, x + 1, y + 1))
        # if flag:
        #     picture.put(line_color, (x, y, x, y + 1))
        # else:
        #     picture.put(bg_color, (x, y, x, y + 1))

    for fig in range(len(end_arr)):
        for i in range(len(end_arr[fig])):
            bresenham(picture, end_arr[fig][i][0][0], end_arr[fig][i][1][0], 
                        end_arr[fig][i][0][1], end_arr[fig][i][1][1])
    end = time()
    time_str = str(round(end - start, 4)) + "ms"
    entry_time.delete(0, tk.END)
    entry_time.insert(tk.END, time_str)

def raster_scan(delay, canva, delay_coef):
    if current_fig == 0:
        messagebox.showerror("Внимание",
                             "Фигура не замкнута или не нарисована.\nПроверьте!!!")
        return 
    global end_arr
    point_arr.pop()
    delay_ch = delay.get()
    sides = get_side(point_arr)
    end_arr.pop()
    make_min_max(point_arr)
    if delay_ch[10] == 'с':
        coef = int(delay_coef.get())
        print("coef!!!!!!!!!!!!!", coef)
        draw_raster_with_flag_delay(picture, canva, end_arr, sides, coef)
    else:
        draw_raster_with_flag(picture, end_arr, sides)

def time_res():
    global time_fig

    print(current_fig, time_fig)
    if (current_fig == 0 or len(point_arr[current_fig - 1]) == 0):
        messagebox.showerror("Внимание",
                             "На поле рисовании нет фигуры.")
        return
    point_arr.pop()
    end_arr.pop()
    sides = get_side(point_arr)
    make_min_max(point_arr)
    start = time()
    draw_raster_with_flag(picture, end_arr, sides)
    stop = time()
    time_fig.append(stop - start)
    res_time = tk.Tk()
    res_time.title("Временные характеристики.")
    res_time.geometry("400x150+800+500")
    tk.Label(res_time, text = "  Время рисования изображенной фигуры \n",
             font = ("Consolas", 12)).grid()
    for i in range(len(time_fig)):
        tk.Label(res_time, text = " Фигура номер " + str(i + 1) + ": " + str(time_fig[i]) + 
                           " с", font = ("Consolas", 12)).grid()
    res_time.mainloop()


def MainWindow():
    global dot_num
    global entry_time
    root = tk.Tk()
    root.geometry("1750x1125+100+10")
    root.title("Лабораторная работа №5 Козлова Ирина ИУ7-42Б")
    root["bg"] = "#c7d0cc"
    root.minsize(1, 1)
    root.maxsize(1765, 1008)
    root.resizable(0, 0)

    # Условие и инструкция
    start_label = tk.Label(text = TASK,
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 16),
                           width = 53, height = 5)
    start_label.place(x = 5, y = 10)

    inct_label = tk.Label(text = INST,
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 16),
                           width = 53, height = 6)
    inct_label.place(x = 5, y = 150)

    
    # Поле рисования
    canva = tk.Canvas(root, bg = "white", 
                         width = W_canva, 
                         height = H_canva, 
                         borderwidth = 5, 
                         relief = tk.RIDGE)
    set_canva_root(canva)

    canva.bind('<1>', left_click)
    canva.bind('<2>', center_click)
    canva.bind('<3>', right_click)

    canva.place(x = 700, y = 0)

    # Выбор с задержкой или нет рисование идет!
    delay_label = tk.Label(root)
    delay_label.configure(text = "Задержка рисования",
                          bg = "#c7d0cc",
                          font = ("Consolas", 16))
    delay_label.place(x = 10, y = 325)

    choose_delay = ttk.Combobox(root, width = 30,
                                font = ("Consolas", 16),
                                textvariable = delay, 
                                state = "readonly",
                                values = ("Рисование без задержки", 
                                          "Рисование с задержкой"))
    choose_delay.place(x = 256, y = 330)
    choose_delay.current(0)

    delay_coef_label = tk.Label(root)
    delay_coef_label.configure(text = "Коэффициент задержки",
                          bg = "#c7d0cc",
                          font = ("Consolas", 16))
    delay_coef_label.place(x = 10, y = 370)    
    entry_delay_coef = tk.Entry()
    entry_delay_coef["bg"] = "#ffffff"
    entry_delay_coef.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_delay_coef.insert(tk.END, "1")
    entry_delay_coef.place(x = 280, y = 370)

    # Выбор цвета
    canva_line_color = tk.Canvas(root, bg = line_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 50)
    canva_line_color.place(x = 250, y = 800)
    line_color_button = tk.Button(root, text = "Цвет заливки ", font = ("Consolas", 14),
                               height = 2, bg = "#7fb5b5",
                               command = lambda: choose_line_color(root, 250, 800))
    line_color_button.place(x = 40, y = 800)

    canva_gran_color = tk.Canvas(root, bg = gran_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 50)
    canva_gran_color.place(x = 250, y = 900)
    gran_color_button = tk.Button(root, text = "Цвет границ ", font = ("Consolas", 14),
                               height = 2, bg = "#7fb5b5",
                               command = lambda: choose_gran_color(root, 250, 900))
    gran_color_button.place(x = 40, y = 900)

    canva_bg_color = tk.Canvas(root, bg = "white",
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 50)
    canva_bg_color.place(x = 560, y = 800)
    bg_color_button = tk.Button(root, text = "Цвет фона ", font = ("Consolas", 14),
                               height = 2, bg = "#7fb5b5",
                               command = lambda: choose_bg_color(root, 560, 800, canva))
    bg_color_button.place(x = 400, y = 800)

    

    # Кнопки закрасить и время
    drawfig_button = tk.Button(root, text = "Закрасить изображенную фигуру",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: raster_scan(choose_delay, canva, entry_delay_coef))
    drawfig_button.place(x = 150, y = 420)

    time_button = tk.Button(root, text = "Временные характеристики алгоритма",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: time_res())
    time_button.place(x = 150, y = 470)

    # Окно для вывода номеров точек
    dot_num = tk.Listbox()
    dot_num["bg"] = "#ffffff"
    dot_num.configure(foreground="black",
                      font="consolas 12",
                      width = 30, height = 10,
                      selectbackground="#000000",
                      selectforeground="#ffffff")
    dot_num.place(x = 10, y = 520)


    # Ввод точки 
    label_x = tk.Label()
    label_x.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="X: ")
    label_x.place(x = 350, y = 530)
    entry_x = tk.Entry()
    entry_x["bg"] = "#ffffff"
    entry_x.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_x.insert(tk.END, "0")
    entry_x.place(x = 375, y = 530)

    label_y = tk.Label()
    label_y.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="Y: ")
    label_y.place(x = 510, y = 530)
    entry_y = tk.Entry()
    entry_y["bg"] = "#ffffff"
    entry_y.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_y.insert(tk.END, "0")
    entry_y.place(x = 535, y = 530) 

    # Кнопка ввода точки
    entry_button = tk.Button(root, text = "Ввести точку",
                               width = 20, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5", 
                               command = lambda: add_point(root, entry_x, entry_y))
    entry_button.place(x = 370, y = 570)

    # Кнопка очистки
    clear_button = tk.Button(root, text = "Очистить экран",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: clear_canva(canva))
    clear_button.place(x = 150, y = 750)

    label_time = tk.Label()
    label_time.configure(font="consolas 14",
                         background="#ffffff",
                         foreground="black",
                         text="Время рисования")
    label_time.place(x = 1410, y = 960)
    entry_time = tk.Entry()
    entry_time["bg"] = "#ffffff"
    entry_time.configure(foreground="#000000",
                         font="consolas 12",
                         width = 10,
                         justify="center")
    entry_time.insert(tk.END, "0")
    entry_time.place(x = 1590, y = 960) 

    root.mainloop()
# Точка входа в программу
if __name__ == "__main__":
    MainWindow()
