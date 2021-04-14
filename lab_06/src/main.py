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

TASK = "Алгоритм построчного затравочного заполнения"
INST = " - Ввод вершины производится с помощью левой кнопки мыши.\n"\
       " - Для заверщение рисования нажмите правую кнопку мыши.\n"\
       " - Для ввода точки затравки нажмите\n"\
       " среднюю кнопку мыши.\n"\
       " - Чтобы нарисовать произовльную линию - зажмите \n"\
       "левую кнопку мыши.\n"\
       " - Для проверки горизонтальных и вертикальных\n"\
       " ребер предусмотрены поля ниже."
picture = 0
delay = 0
current_fig = 0
seed_color = "#ff00ff"
bg_color = "#ffffff"
line_color = "#00000f"

line_for_check = (0, 0, 15)
seed_for_check = (255, 0, 255)
point_arr = [[]]
point_z = []


def bresenham(picture, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        picture.put(line_color, (xStart, yStart))
        return
    xStart = int(xStart)
    yStart = int(yStart)
    xEnd = int(xEnd)
    yEnd = int(yEnd)

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX <= deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    curX = xStart
    curY = yStart

    for i in range(deltaX + 1):
        picture.put(line_color, (curX, curY))

        if acc >= 0:
            if flag:
                curX += stepX
            else:
                curY += stepY
            acc -= (deltaX + deltaX)
        if acc <= 0:
            if flag:
                curY += stepY
            else:
                curX += stepX
            acc += deltaY + deltaY

def left_click(event):
    global point_arr, picture, current_fig
    point_arr[current_fig].append([event.x, event.y, seed_color])
    if len(point_arr[current_fig]) >= 2:
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][1])

def right_click(event):
    global point_arr
    global current_fig
    global picture

    bresenham(picture, point_arr[current_fig][0][0],
                   point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                   point_arr[current_fig][0][1],
                   point_arr[current_fig][len(point_arr[current_fig]) - 1][1])
    current_fig += 1
    point_arr.append(list())

def center_click(event):
    global point_z
    point_z.append([event.x, event.y])

def set_canva_root(canva):
    global picture
    picture = tk.PhotoImage(width = W_canva, height = H_canva)
    canva.create_image((W_canva / 2, H_canva / 2), image = picture, state = "normal")


def clear_canva(canva):
    global point_arr
    global current_fig
    global picture
    canva.delete("all")
    point_arr = [[]]
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

def choose_seed_color(root, r, c):
    global seed_color
    seed_color = colorchooser.askcolor()[1]
    canva_seed_color = tk.Canvas(root, bg = seed_color,
                            borderwidth = 5, relief = tk.RIDGE,
                            width = 60, height = 50)
    canva_seed_color.place(x = r, y = c)

def choose_line_color(root, r, c):
    global line_color
    line_color = colorchooser.askcolor()[1]
    canva_line_color = tk.Canvas(root, bg = line_color,
                            borderwidth = 5, relief = tk.RIDGE,
                            width = 60, height = 50)
    canva_line_color.place(x = r, y = c)
    
def add_point(root, entry_x, entry_y):
    global point_arr
    global picture
    global current_fig

    try:
        x_coord = float(entry_x.get())
        y_coord = float(entry_y.get())
    except Exception:
        messagebox.showerror("Внимание",
                             "Невозможно считать координаты!")
        return

    x_coord = int(x_coord)
    y_coord = int(y_coord)
    point_arr[current_fig].append([x_coord, y_coord, line_color])
    if len(point_arr[current_fig]) >= 2:
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                        point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                        point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                        point_arr[current_fig][len(point_arr[current_fig]) - 1][1])
    
def seed_fill(img, xSeed, ySeed):
    stack = list()
    stack.append([xSeed, ySeed])
    print(stack)
    while len(stack):
        gotDot = stack.pop()

        curX = gotDot[0]
        curY = gotDot[1]

        gotColor = img.get(curX, curY)
        while gotColor != line_for_check and gotColor != seed_for_check:
            img.put(seed_color, (curX, curY))    
            curX -= 1
            gotColor = img.get(curX, curY)
        xLeft = curX + 1
        img.put(seed_color, (xLeft, curY, gotDot[0] + 1, curY + 1))

        curX = gotDot[0] + 1
        gotColor = img.get(curX, curY)
        while gotColor != line_for_check and gotColor != seed_for_check:
            img.put(seed_color, (curX, curY))
            curX += 1
            gotColor = img.get(curX, curY)
        xRight = curX - 1
        img.put(seed_color, (gotDot[0], curY, xRight + 1, curY + 1))

        curX = xLeft
        curY += 1

        flag = False
        while curX <= xRight:
            gotColor = img.get(curX, curY)
            while gotColor != line_for_check and gotColor != seed_for_check and curX <= xRight:
                flag = True
                curX += 1
                gotColor = img.get(curX, curY)

            if flag:
                if curX == xRight and gotColor != line_for_check and gotColor != seed_for_check:
                    stack.append([curX, curY])
                else:
                    stack.append([curX - 1, curY])
                flag = False

            xStart = curX
            while (gotColor == line_for_check or gotColor == seed_for_check) and curX < xRight:
                curX += 1
                gotColor = img.get(curX, curY)

            if curX == xStart:
                curX += 1

        curX = xLeft
        curY -= 2

        flag = False
        while curX <= xRight:
            gotColor = img.get(curX, curY)
            while gotColor != line_for_check and gotColor != seed_for_check and curX <= xRight:
                flag = True
                curX += 1
                gotColor = img.get(curX, curY)

            if flag:
                if curX == xRight and gotColor != line_for_check and gotColor != seed_for_check:
                    stack.append([curX, curY])
                else:
                    stack.append([curX - 1, curY])
                flag = False

            xStart = curX
            while (gotColor == line_for_check or gotColor == seed_for_check) and curX < xRight:
                curX += 1
                gotColor = img.get(curX, curY)

            if curX == xStart:
                curX += 1

    
def seed_fill_delay(img, canva, coef, xSeed, ySeed):
    stack = list()
    stack.append([xSeed, ySeed])
    print(stack, coef)
    while len(stack):
        gotDot = stack.pop()

        curX = gotDot[0]
        curY = gotDot[1]

        gotColor = img.get(curX, curY)
        while gotColor != line_for_check and gotColor != seed_for_check:
            img.put(seed_color, (curX, curY))   
            curX -= 1
            gotColor = img.get(curX, curY)
        xLeft = curX + 1
        img.put(seed_color, (xLeft, curY, gotDot[0] + 1, curY + 1))

        curX = gotDot[0] + 1
        gotColor = img.get(curX, curY)
        while gotColor != line_for_check and gotColor != seed_for_check:
            img.put(seed_color, (curX, curY))
            curX += 1
            gotColor = img.get(curX, curY)
        xRight = curX - 1
        img.put(seed_color, (gotDot[0], curY, xRight + 1, curY + 1))

        canva.update()
        sleep(0.001 * coef)

        curX = xLeft
        curY += 1

        flag = False
        while curX <= xRight:
            gotColor = img.get(curX, curY)
            while gotColor != line_for_check and gotColor != seed_for_check and curX <= xRight:
                flag = True
                curX += 1
                gotColor = img.get(curX, curY)

            if flag:
                if curX == xRight and gotColor != line_for_check and gotColor != seed_for_check:
                    stack.append([curX, curY])
                else:
                    stack.append([curX - 1, curY])
                flag = False

            xStart = curX
            while (gotColor == line_for_check or gotColor == seed_for_check) and curX < xRight:
                curX += 1
                gotColor = img.get(curX, curY)

            if curX == xStart:
                curX += 1

        curX = xLeft
        curY -= 2

        flag = False
        while curX <= xRight:
            gotColor = img.get(curX, curY)
            while gotColor != line_for_check and gotColor != seed_for_check and curX <= xRight:
                flag = True
                curX += 1
                gotColor = img.get(curX, curY)

            if flag:
                if curX == xRight and gotColor != line_for_check and gotColor != seed_for_check:
                    stack.append([curX, curY])
                else:
                    stack.append([curX - 1, curY])
                flag = False

            xStart = curX
            while (gotColor == line_for_check or gotColor == seed_for_check) and curX < xRight:
                curX += 1
                gotColor = img.get(curX, curY)

            if curX == xStart:
                curX += 1

def do_seed_fill(canva, delay, coef_delay, x_seed, y_seed):
    x = x_seed.get()
    y = y_seed.get()
    print(point_z)

    if x == "" or y == "":
        x = point_z[0][0]
        y = point_z[0][1]
    else:
        x = int(x)
        y = int(y)

    delay_d = delay.get()
    print(delay_d)
    print(delay_d[10] == 'с')
    if delay_d[10] == 'с':
        print("c")
        try:
            coef = int(coef_delay.get())
            
        except Exception:
            messagebox.showerror("Внимание",
                             "Невозможно считать координаты затравочной точки!")
            return
        seed_fill_delay(picture, canva, coef, x, y)
    else:
        seed_fill(picture, x, y)


def time_res():
    pass


def MainWindow():
    global dot_num
    global entry_time
    root = tk.Tk()
    root.geometry("1750x1125+100+10")
    root.title("Лабораторная работа №6 Козлова Ирина ИУ7-42Б")
    root["bg"] = "#c7d0cc"
    root.minsize(1, 1)
    root.maxsize(1765, 1008)
    root.resizable(0, 0)

    # Условие и инструкция
    start_label = tk.Label(text = TASK,
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 16, "italic bold"),
                           width = 53, height = 1)
    start_label.place(x = 5, y = 10)

    inct_label = tk.Label(text = INST,
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 14),
                           width = 63, height = 8)
    inct_label.place(x = 5, y = 45)

    
    # Поле рисования
    canva = tk.Canvas(root, bg = "white", 
                         width = W_canva, 
                         height = H_canva, 
                         borderwidth = 5, 
                         relief = tk.RIDGE)
    set_canva_root(canva)
    canva.bind('<B1-Motion>', left_click)
    canva.bind('<1>', left_click)
    canva.bind('<2>', center_click)
    canva.bind('<3>', right_click)

    canva.place(x = 700, y = 0)

    # Выбор с задержкой или нет рисование идет!
    delay_label = tk.Label(root)
    delay_label.configure(text = "Задержка рисования",
                          bg = "#c7d0cc",
                          font = ("Consolas", 16))
    delay_label.place(x = 10, y = 240)

    choose_delay = ttk.Combobox(root, width = 30,
                                font = ("Consolas", 16),
                                textvariable = delay, 
                                state = "readonly",
                                values = ("Рисование без задержки", 
                                          "Рисование с задержкой"))
    choose_delay.place(x = 256, y = 240)
    choose_delay.current(0)

    delay_coef_label = tk.Label(root)
    delay_coef_label.configure(text = "Коэффициент задержки",
                          bg = "#c7d0cc",
                          font = ("Consolas", 16))
    delay_coef_label.place(x = 10, y = 275)    
    entry_delay_coef = tk.Entry()
    entry_delay_coef["bg"] = "#ffffff"
    entry_delay_coef.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_delay_coef.insert(tk.END, "1")
    entry_delay_coef.place(x = 280, y = 275)

     # Выбор цвета
    canva_seed_color = tk.Canvas(root, bg = seed_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 26)
    canva_seed_color.place(x = 155, y = 310)
    seed_color_button = tk.Button(root, text = "Цвет заливки", font = ("Consolas", 14),
                               height = 1, bg = "#7fb5b5", width = 11,
                               command = lambda: choose_seed_color(root, 150, 310))
    seed_color_button.place(x = 10, y = 310)

    canva_line_color = tk.Canvas(root, bg = line_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 26)
    canva_line_color.place(x = 400, y = 310)
    line_color_button = tk.Button(root, text = "Цвет границ", font = ("Consolas", 14),
                               height = 1, bg = "#7fb5b5", width = 11,
                               command = lambda: choose_line_color(root, 250, 310))
    line_color_button.place(x = 250, y = 310)

    canva_bg_color = tk.Canvas(root, bg = bg_color,
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 26)
    canva_bg_color.place(x = 625, y = 310)
    bg_color_button = tk.Button(root, text = "Цвет фона", font = ("Consolas", 14),
                               height = 1, bg = "#7fb5b5", width = 10,
                               command = lambda: choose_bg_color(root, 560, 310, canva))
    bg_color_button.place(x = 490, y = 310)


    # Ввод точки 
    pointentry_label = tk.Label(text = "Ввод точек для отслеживания горизонтали и вертикали",
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 16, "italic"),
                           width = 53, height = 1)
    pointentry_label.place(x = 5, y = 375)
    label_x = tk.Label()
    label_x.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="X: ")
    label_x.place(x = 10, y = 420)
    entry_x = tk.Entry()
    entry_x["bg"] = "#ffffff"
    entry_x.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_x.insert(tk.END, "0")
    entry_x.place(x = 45, y = 420)

    label_y = tk.Label()
    label_y.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="Y: ")
    label_y.place(x = 160, y = 420)
    entry_y = tk.Entry()
    entry_y["bg"] = "#ffffff"
    entry_y.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_y.insert(tk.END, "0")
    entry_y.place(x = 195, y = 420) 

    # Кнопка ввода точки
    entry_button = tk.Button(root, text = "Ввести точку",
                               width = 20, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5", 
                               command = lambda: add_point(root, entry_x, entry_y))
    entry_button.place(x = 370, y = 415)


    # Ввод точек затравки
    pointentry_z_label = tk.Label(text = "Ввод координаты точки затравки\n(или ввод через среднюю кнопку мыши)",
                           relief = tk.RIDGE, bg = "#c7d0cc",
                           fg = "#000000", font = ("Consolas", 16, "italic"),
                           width = 53, height = 2)
    pointentry_z_label.place(x = 5, y = 505)
    label_x_z = tk.Label()
    label_x_z.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="X: ")
    label_x_z.place(x = 10, y = 570)
    entry_x_z = tk.Entry()
    entry_x_z["bg"] = "#ffffff"
    entry_x_z.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_x_z.insert(tk.END, "")
    entry_x_z.place(x = 45, y = 570)

    label_y_z = tk.Label()
    label_y_z.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="Y: ")
    label_y_z.place(x = 160, y = 570)
    entry_y_z = tk.Entry()
    entry_y_z["bg"] = "#ffffff"
    entry_y_z.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_y_z.insert(tk.END, "")
    entry_y_z.place(x = 195, y = 570) 

    # # Кнопка ввода точки затравки
    # entry_button_z = tk.Button(root, text = "Ввести точку затравки",
    #                            width = 20, height = 1, font = ("Consolas", 14),
    #                            bg = "#7fb5b5", 
    #                            command = lambda: add_point(root, entry_x, entry_y))
    # entry_button_z.place(x = 370, y = 565)

    # Кнопки закрасить и время
    drawfig_button = tk.Button(root, text = "Закрасить изображенную фигуру",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: do_seed_fill(canva, choose_delay, entry_delay_coef, entry_x_z, entry_y_z))
    drawfig_button.place(x = 150, y = 650)

    time_button = tk.Button(root, text = "Временные характеристики алгоритма",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: time_res())
    time_button.place(x = 150, y = 700)

    # Кнопка очистки
    clear_button = tk.Button(root, text = "Очистить экран",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: clear_canva(canva))
    clear_button.place(x = 150, y = 750)

    # Время закраски
    label_time = tk.Label()
    label_time.configure(font="consolas 14",
                         background="#ffffff",
                         foreground="black",
                         text="Время закраски")
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
