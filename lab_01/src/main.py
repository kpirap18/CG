import tkinter as tk

from tkinter import messagebox
from geom import *
from check import *

TASK = "На плоскости дано множество точек. Найти такой треугольник, \n\
с вершинами в этих точках, у которого угол, образованный прямой, \n\
соединяющей точку пересечения высот и начала координат,\n\
 и осью ординат максимален."
 
class MainWindow(tk.Tk):
    '''
        Класс главного окна приложения.
    '''
    def __init__(self, *arg, **kwarg):
        tk.Tk.__init__(self, *arg, **kwarg)
        
        # Главное окно
        self.geometry("1200x990+100+10")
        self.title("Лабораторная работа №1")
        self["bg"] = "#7d182e"
        self.configure(highlightcolor="red")
        self.configure(cursor="arrow")
        self.minsize(1, 1)
        self.maxsize(1465, 808)
        self.resizable(0, 0)
        self.grab_set()
        self.focus_set()
        
        # Заголовок для точек
        self.labeldot = tk.Label(self)
        self.labeldot.configure(font="consolas 14",
                                background="#e08484",
                                foreground="black",
                                text="Координаты точек")
        self.labeldot.place(relx=0.75, rely=0.047, 
                            relheight=0.05, relwidth=0.22)

        # Окно для вывода номеров точек
        self.dot_num = tk.Listbox(self)
        self.dot_num["bg"] = "#ffffff"
        self.dot_num.configure(foreground="black",
                               font="consolas 12",
                               selectbackground="#000000",
                               selectforeground="#ffffff")
        self.dot_num.place(relx=0.72, rely=0.117,
                           relheight=0.5, relwidth=0.046)

        # Окно для вывода координат точек
        self.listdot = tk.Listbox(self)
        self.listdot["bg"] = "#ffffff"
        self.listdot.configure(foreground="black",
                               font="consolas 12", 
                               selectbackground="#000000",
                               selectforeground="#ffffff")
        self.listdot.place(relx=0.77, rely=0.117,
                           relheight=0.5, relwidth=0.22)

        # Вывод условия задачи
        self.condition = tk.Label(self)
        self.condition.configure(font="consolas 12",
                                background="#e08484",
                                foreground="black", 
                                text=TASK)
        self.condition.place(relx=0.011, rely=0.017, 
                           relheight=0.15, relwidth=0.7)

        # Окно для вывода рисунка (ответ)
        self.answer = tk.Canvas(self)
        self.answer["bg"] = "#ffffff"
        self.answer.place(relx=0.064, rely=0.177,
                         relheight=0.65, relwidth=0.6)
        
        # Ввод координаты Х
        self.label_x = tk.Label(self)
        self.label_x.configure(font="consolas 16",
                                background="#e08484",
                                foreground="black",
                                text="X")
        self.label_x.place(relx=0.75, rely=0.676, 
                           relheight=0.045, relwidth=0.079)
        self.entry_x = tk.Entry(self)
        self.entry_x["bg"] = "#ffffff"
        self.entry_x.configure(foreground="#000000",
                               font="consolas 14",
                               justify="center")
        self.entry_x.insert(tk.END, "0")
        self.entry_x.place(relx=0.75, rely=0.776, 
                           relheight=0.045, relwidth=0.079)

        # Ввод координаты У
        self.label_y = tk.Label(self)
        self.label_y.configure(font="consolas 16",
                                background="#e08484",
                                foreground="black",
                                text="Y")
        self.label_y.place(relx=0.88, rely=0.676, 
                           relheight=0.045, relwidth=0.079)
        self.entry_y = tk.Entry(self)
        self.entry_y["bg"] = "#ffffff"
        self.entry_y.configure(foreground="#000000",
                               font="consolas 14",
                               justify="center")
        self.entry_y.insert(tk.END, "0")
        self.entry_y.place(relx=0.88, rely=0.776, 
                           relheight=0.045, relwidth=0.079)

        # Кнопка "Добавить точку"
        self.button_add = tk.Button(self)
        self.button_add["bg"] = "#d5d5d5"
        self.button_add.configure(foreground="black",
                                  font="consolas 14",
                                  text="Добавить точку",
                                  command=lambda:write_point(self, None, 0, 0))
        self.button_add.place(relx=0.776, rely=0.877, 
                              relheight=0.055, relwidth=0.15)


        # Ввод номера удаляемой точки
        self.dellabel = tk.Label(self)
        self.dellabel.configure(font="consolas 12",
                               background="#e08484",
                               foreground="black",
                               text="Номер точки")
        self.dellabel.place(relx=0.03, rely=0.856,
                           relheight=0.025, relwidth=0.15)
        self.delentry = tk.Entry(self)
        self.delentry["bg"] = "#ffffff"
        self.delentry.configure(foreground="#000000",
                               font="consolas 12",
                               justify="center")
        self.delentry.insert(tk.END, "0")
        self.delentry.place(relx=0.03, rely=0.896,
                           relheight=0.025, relwidth=0.15)

        # Кнопка "Удалить точку"
        self.button_del = tk.Button(self)
        self.button_del["bg"] = "#d5d5d5"
        self.button_del.configure(state="disabled",
                                  foreground="black",
                                  font="consolas 12",
                                  text="Удалить точку",
                                  command=lambda: delete_point(self))
        self.button_del.place(relx=0.03, rely=0.943,
                              relheight=0.035, relwidth=0.15)

        # Кнопка "Изменить точку"
        self.button_edit = tk.Button(self)
        self.button_edit["bg"] = "#d5d5d5"
        self.button_edit.configure(state="disabled",
                                   foreground="black",
                                   font="consolas 14",
                                   text="Изменить точку",
                                   command=lambda: edit_point(self))
        self.button_edit.place(relx=0.2, rely=0.887,
                              relheight=0.055, relwidth=0.15)

        # Кнопка "Очистить все"
        self.button_delall = tk.Button(self)
        self.button_delall["bg"] = "#d5d5d5"
        self.button_delall.configure(foreground="black",
                                  font="consolas 14",
                                  text="Очистить все",
                                  command=lambda: clean_all(self))
        self.button_delall.place(relx=0.37, rely=0.887,
                              relheight=0.055, relwidth=0.15)

        # Кнопка "Решить задачу"
        self.button_task = tk.Button(self)
        self.button_task["bg"] = "#d5d5d5"
        self.button_task.configure(foreground="black",
                                  font="consolas 14",
                                  text="Решить задачу",
                                  command=lambda: draw_answer(self))
        self.button_task.place(relx=0.54, rely=0.887,
                              relheight=0.055, relwidth=0.15)


class EditWin(tk.Toplevel):
    '''
        Класс, отвечающий за окно при нажатии кнопки
        "Изменить точку".
    '''
    def __init__(self, *arg, **kwarg):
        tk.Toplevel.__init__(self, *arg, **kwarg)

        # Главное окно
        self.geometry("200x150+300+10")
        self.title("Лабораторная работа №1")
        self["bg"] = "#7d123e"
        self.configure(highlightcolor="red")
        self.configure(cursor="watch")
        self.grab_set()
        self.focus_set()

        # Ввод координаты Х (чтобы изменить)
        self.label_x = tk.Label(self)
        self.label_x.configure(font="consolas 14",
                               background="#e08484",
                               foreground="black",
                               text="X")
        self.label_x.place(relx=0.2, rely=0.16,
                           relheight=0.1, relwidth=0.2)
        self.entry_x = tk.Entry(self)
        self.entry_x["bg"] = "#ffffff"
        self.entry_x.configure(foreground="#000000",
                               font="consolas 10",
                               justify="center")
        self.entry_x.insert(tk.END, "0")
        self.entry_x.place(relx=0.2, rely=0.36,
                           relheight=0.18, relwidth=0.24)

        # Ввод координаты У (чтобы изменить)
        self.label_y = tk.Label(self)
        self.label_y.configure(font="consolas 14",
                               background="#e08484",
                               foreground="black",
                               text="Y")
        self.label_y.place(relx=0.65, rely=0.16,
                           relheight=0.1, relwidth=0.2)
        self.entry_y = tk.Entry(self)
        self.entry_y["bg"] = "#ffffff"
        self.entry_y.configure(foreground="#000000",
                               font="consolas 10",
                               justify="center")
        self.entry_y.insert(tk.END, "0")
        self.entry_y.place(relx=0.65, rely=0.36,
                           relheight=0.18, relwidth=0.24)

        # Кнопка "Изменить"
        self.button_ok = tk.Button(self)
        self.button_ok.configure(foreground="black",
                                 font="consolas 12",
                                 text="Изменить",
                                 command=lambda: write_point(MAIN_WIN, self, MODE, EDIT))
        self.button_ok.place(relx=0.22, rely=0.66,
                             relheight=0.2, relwidth=0.6)


def edit_point(root):
    '''
        Функция, отвечающая за изменения точки.
        (правильный вызов нужных окон и функций)
    '''
    global SOME_WIN, MODE, EDIT
    MODE = 1
    SOME_WIN = EditWin(root)
    EDIT = root.listdot.curselection()
    dot = root.listdot.get(EDIT).split(";")
    SOME_WIN.entry_x.delete(0, tk.END)
    SOME_WIN.entry_x.insert(0, dot[0])
    SOME_WIN.entry_y.delete(0, tk.END)
    SOME_WIN.entry_y.insert(0, dot[1])

# Точка входа в программу
if __name__ == "__main__":
    MAIN_WIN = MainWindow()
    MODE = None
    EDIT = None
    SOME_WIN = None
    MAIN_WIN.mainloop()
