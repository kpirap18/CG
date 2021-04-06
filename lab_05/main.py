import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
from time import sleep, time

from numpy import sign

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
line_color = "#000000"
bg_color = "#ffffff"
point_arr = [[]]
end_arr = [[]]
min_max = [[]]

def bresenham(picture, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        picture.put(line_color, (xStart, yStart))
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
        picture.put(line_color, (curX, curY))

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
    point_arr[current_fig].append([event.x, event.y, line_color])

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
    global line_color
    global point_arr
    global current_fig
    global picture
    if len(point_arr) == 0:
        return

    buf_color = line_color
    line_color = bg_color
    if len(point_arr[current_fig]) != 0:
        # рисуем
        point_arr[current_fig].pop()
        end_arr[current_fig].pop()
    else:
        end_arr.pop()
        point_arr.pop()
        current_fig -= 1
        # рисуем
    line_color = buf_color


def set_canva_root(canva):
    global picture
    picture = tk.PhotoImage(width = 990, height = 816)

    canva.create_image((535, 508), image = picture, state = "normal")


def clear_canva(canva):
    global point_arr
    global end_arr
    global current_fig
    global min_max
    global picture

    canva.delete("all")

    point_arr = [[]]
    end_arr = [[]]
    min_max = [[]]
    current_fig = 0
    
    picture = tk.PhotoImage(width = 990, height = 816)
    canva.create_image((535, 508), image = picture, state = "normal")
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
    
def add_point(entry_x, entry_y):
    global point_arr
    global picture
    global current_fig

    x_coord = int(entry_x.get())
    y_coord = int(entry_y.get())

    point_arr[current_fig].append([x_coord, y_coord, line_color])
    if len(point_arr[current_fig]) >= 2:
        end_arr[current_fig].append([[point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 2][1]],
                                [point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                                 point_arr[current_fig][len(point_arr[current_fig]) - 1][1]]])
        bresenham(picture, point_arr[current_fig][len(point_arr[current_fig]) - 2][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][0],
                       point_arr[current_fig][len(point_arr[current_fig]) - 2][1],
                       point_arr[current_fig][len(point_arr[current_fig]) - 1][1])



def MainWindow():
    root = tk.Tk()
    root.geometry("1750x1125+100+10")
    root.title("Лабораторная работа №5")
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
                         width = 1037, 
                         height = 993, 
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
    delay_label.place(x = 10, y = 350)

    choose_delay = ttk.Combobox(root, width = 30,
                                font = ("Consolas", 16),
                                textvariable = delay, 
                                state = "readonly",
                                values = ("Рисование без задержкой", 
                                          "Рисование с задержки"))
    choose_delay.place(x = 256, y = 350)
    choose_delay.current(0)

    # Выбор цвета
    canva_line_color = tk.Canvas(root, bg = "black",
                              borderwidth = 5, relief = tk.RIDGE,
                              width = 60, height = 50)
    canva_line_color.place(x = 250, y = 800)
    line_color_button = tk.Button(root, text = "Цвет отрезков ", font = ("Consolas", 14),
                               height = 2, bg = "#7fb5b5",
                               command = lambda: choose_line_color(root, 250, 800))
    line_color_button.place(x = 40, y = 800)

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
                               bg = "#7fb5b5")
    drawfig_button.place(x = 150, y = 400)

    time_button = tk.Button(root, text = "Временные характеристики алгоритма",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5")
    time_button.place(x = 150, y = 450)

    # Окно для вывода номеров точек
    dot_num = tk.Listbox()
    dot_num["bg"] = "#ffffff"
    dot_num.configure(foreground="black",
                      font="consolas 12",
                      width = 30, height = 10,
                      selectbackground="#000000",
                      selectforeground="#ffffff")
    dot_num.place(x = 10, y = 500)

    # Ввод точки 
    label_x = tk.Label()
    label_x.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="X: ")
    label_x.place(x = 350, y = 510)
    entry_x = tk.Entry()
    entry_x["bg"] = "#ffffff"
    entry_x.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_x.insert(tk.END, "0")
    entry_x.place(x = 375, y = 510)

    label_y = tk.Label()
    label_y.configure(font="consolas 14",
                          background="#c7d0cc",
                           foreground="black",
                             text="Y: ")
    label_y.place(x = 510, y = 510)
    entry_y = tk.Entry()
    entry_y["bg"] = "#ffffff"
    entry_y.configure(foreground="#000000",
                      font="consolas 14",
                      width = 7,
                      justify="center")
    entry_y.insert(tk.END, "0")
    entry_y.place(x = 535, y = 510) 

    # Кнопка ввода точки
    entry_button = tk.Button(root, text = "Ввести точку",
                               width = 20, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5", 
                               command = lambda: add_point(entry_x, entry_y))
    entry_button.place(x = 370, y = 550)

    # Кнопка очистки
    clear_button = tk.Button(root, text = "Очистить экран",
                               width = 35, height = 1, font = ("Consolas", 14),
                               bg = "#7fb5b5",
                               command = lambda: clear_canva(canva))
    clear_button.place(x = 150, y = 730)

    root.mainloop()
# Точка входа в программу
if __name__ == "__main__":
    MainWindow()
