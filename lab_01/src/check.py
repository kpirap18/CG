import tkinter as tk

from tkinter import messagebox
from main import *

def point_list(root):
    '''
        Считывание координат точкек.
    '''
    points = root.listdot.get(0, tk.END)
    num_points = []
    for i in points:
        buf = list(map(float, i.split(";")))
        num_points.append(buf)
    return num_points

def turn_buttons(root, flag):
    '''
        Функция включения и выключения кнопок удаления и изменения.
    '''
    if flag:
        root.button_del.configure(state="normal")
        root.button_edit.configure(state="normal")
    else:
        root.button_del.configure(state="disabled")
        root.button_edit.configure(state="disabled")

def checklist_toturn(root):
    '''
        Функция проверки, надо ли включать кнопки или нет.
    '''
    if list(map(int, root.listdot.curselection())) != []:
        turn_buttons(root, 1)
    else:
        turn_buttons(root, 0)

def clean_all(root):
    '''
        Функция очистки поля координат точек.
    '''
    root.listdot.delete(0, tk.END)
    root.dot_num.delete(0, tk.END)
    root.answer.delete("all")
    turn_buttons(root, 0)

def point_is_list(point, root):
    '''
        Проверка на наличие точки в списке точек.
    '''
    dots = root.listdot.get(0, tk.END)
    for dot in dots:
        if dot == point:
            return True
    return False

def write_point(root, editwin, mode, id):
    if mode == 1:
        try:
            xx = float(editwin.entry_x.get())
            yy = float(editwin.entry_y.get())
            point = "{};{}".format(xx, yy)
            root.listdot.delete(id)
            root.listdot.insert(id, point)
        except ValueError:
            messagebox.showerror("Ошибка",
                                 "Неверный ввод. Можно вводить только вещественные числа.")
    else:
        try:

            list_dot = root.listdot.get(0, tk.END)
            x = float(root.entry_x.get())
            y = float(root.entry_y.get())
            point = "{};{}".format(x, y)
            # if point_is_list(point, root):
            #     messagebox.showerror("Информация",
            #                          "Данная точка уже есть в списке точек")
            #     return

            root.dot_num.insert(tk.END, f"{len(list_dot) + 1}")
            root.listdot.insert(tk.END, point)
            turn_buttons(root, 1)
        except ValueError:
            messagebox.showerror("Ошибка",
            "Неверный ввод. Можно вводить только вещественные числа.")

def delete_point(root):
    '''
        Удаление точки.
    '''
    try:
        number = int(root.delentry.get())
        root.answer.delete("all")
        list_dot = list(root.listdot.get(0, tk.END))
        n = len(list_dot)
        print(number, 0 >= number > n)
        if 0 >= number or number > n:
            messagebox.showerror("Ошибка ввода данных",
                                 "Неверный номер удаляемой точки.")
            return
        list_dot.pop(number - 1)
        root.listdot.delete(0, tk.END)
        root.dot_num.delete(0, tk.END)
        for i in range(len(list_dot)):
            ii = i + 1
            s = str(ii)
            root.dot_num.insert(tk.END, s)
            root.listdot.insert(tk.END, list_dot[i])
        if len(root.listdot.get(0, tk.END)) == 0:
            turn_buttons(root, 0)
    except ValueError:
        messagebox.showerror("Ошибка ввода данных",
                             "Невозможно прочитать число.")
    except IndexError:
        messagebox.showerror("Ошибка ввода данных",
                             "Неверный номер удаляемой точки.")