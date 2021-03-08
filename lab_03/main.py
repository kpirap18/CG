import sys
import numpy as np
import untitled
import pyqtgraph as pg
import matplotlib.pyplot as plt

from time import time
from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from math import sin, cos, pi, radians, fabs,  floor


class Visual(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphicsView.scale(1, 1)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        self.scene.setSceneRect(0, 0, w-2, h-2)
        self.pen = QtGui.QPen(QtCore.Qt.black)
        self.pen.setWidth(0)

        self.radioButtonBlack_bg.clicked.connect(self.set_black_bg)
        self.radioButtonBlue_bg.clicked.connect(self.set_blue_bg)
        self.radioButtonGreen_bg.clicked.connect(self.set_green_bg)
        self.radioButtonRed_bg.clicked.connect(self.set_red_bg)
        self.radioButtonWhite_bg.clicked.connect(self.set_white_bg)
        self.radioButtonYellow_bg.clicked.connect(self.set_yellow_bg)

        self.radioButtonBlack_line.clicked.connect(self.set_black)
        self.radioButtonBlue_line.clicked.connect(self.set_blue)
        self.radioButtonGreen_line.clicked.connect(self.set_green)
        self.radioButtonRed_line.clicked.connect(self.set_red)
        self.radioButtonWhite_line.clicked.connect(self.set_white)
        self.radioButtonYellow_line.clicked.connect(self.set_yellow)

        self.pushButton_clean.clicked.connect(self.clean_screen)

        self.pushButton_line_one.clicked.connect(self.draw_line)
        self.pushButton_step_all.clicked.connect(self.com_step)
        self.pushButton_step_ch.clicked.connect(self.com_step_one)
        self.pushButton_time_all.clicked.connect(self.com_time)
        self.pushButtonDrawSpectrum.clicked.connect(self.draw_spectr)

        self.action.triggered.connect(self.about)
        self.statusBar().showMessage("Лабораторная работа №3, выполнила Козлова Ирина")

    def about(self):
        QtWidgets.QMessageBox.information(self, "Информация", 
        'С помощью данной программы можно построить отрезки шестью способами:\n'
                        '1) методом цифрового дифференциального анализатора;\n'
                        '2) методом Брезенхема с действитльными коэфициентами;\n'
                        '3) методом Брезенхема с целыми коэфициентами;\n'
                        '4) методом Брезенхема со сглаживанием;\n'
                        '5) методом Ву;\n'
                        '6) стандартым методом (библиотека PyQt5).\n'
                        '\nДля построения отрезка необходимо задать его начало, '
                        'и конец и выбрать метод построения из списка предложенных, '
                        'а так же выбрать цвет фона и цвет линии.\n'
                        '\nДля визуального анализа (построения пучка отрезков) '
                        'необходимо задать длину и угол (центр данного пучка = центр экрана), '
                        'выбрать метод для анализа, '
                        'а также цвет фона и цвет линий.\n'
                        '\nПроанализировать ступенчатость можно выбранного метода, '
                        'а также всех сразу методов.\n'
                        'Анализ ступенчатости и времени исполнения приводится\n'
                        'в виде графиков pyplot.\n')
        return
    def clean_screen(self):
        self.scene.clear()

    def set_black(self):
        self.pen.setColor(QtCore.Qt.black)

    def set_white(self):
        self.pen.setColor(QtCore.Qt.white)
    
    def set_blue(self):
        self.pen.setColor(QtCore.Qt.blue)

    def set_red(self):
        self.pen.setColor(QtCore.Qt.red)

    def set_green(self):
        self.pen.setColor(QtCore.Qt.green)

    def set_yellow(self):
        self.pen.setColor(QtCore.Qt.yellow)


    def set_black_bg(self):
        self.graphicsView.setStyleSheet("background-color: black")

    def set_white_bg(self):
        self.graphicsView.setStyleSheet("background-color: white")

    def set_blue_bg(self):
        self.graphicsView.setStyleSheet("background-color: blue")

    def set_red_bg(self):
        self.graphicsView.setStyleSheet("background-color: red")

    def set_green_bg(self):
        self.graphicsView.setStyleSheet("background-color: green")

    def set_yellow_bg(self):
        self.graphicsView.setStyleSheet("background-color: yellow")


    def my_addline(self, p_start, p_end, draw=True):
        # print("draw in my_addline", draw)
        # print(self.radioButtonCDA.isChecked())
        if self.radioButtonCDA.isChecked():
            # print("tyt1")
            self.dda(p_start, p_end, draw=draw)
        elif self.radioButtonBresFloat.isChecked():
            # print("tyt2")
            self.bresen_float(p_start, p_end, draw=draw)
        elif self.radioButtonBresInt.isChecked():
            # print("tyt3")
            self.bresen_int(p_start, p_end, draw=draw)
        elif self.radioButtonBresSmooth.isChecked():
            # print("tyt4")
            self.bresen_smooth(p_start, p_end, draw=draw)
        elif self.radioButtonWu.isChecked():
            # print("tyt5")
            self.wu(p_start, p_end, draw=draw)
        else:
            # print("tyt6")
            self.lib(p_start, p_end)

    def draw_point(self, x, y, light=255):
        color = self.pen.color()
        QtGui.QColor.setAlpha(color, light)
        self.pen.setColor(color)
        self.scene.addLine(x, y, x, y, self.pen)
    
###############################################
    def draw_spectr(self, buf=False, draw=True):
        # print("draw_spectr", draw)
        # self.scene.addLine(0, 0, 200, 200)
        try:
            angle = int(self.lineEditAngle.text())
            lenn = int(self.lineEdiLen.text())
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "", 
                    "Угол поворота и длина должны быть целыми числами!")
            return
        if angle < 1:
            QtWidgets.QMessageBox.critical(self, "", "Угол поворота должен быть больше нуля!")
            return
        if lenn < 1:
            QtWidgets.QMessageBox.critical(self, "", "Длина отрезка должна быть больше нуля!")
            return
        teta = 0
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        while teta < 2 * pi - 0.001:
            # print("TETA", teta, 2 * pi - 0.001 )
            x = w // 2 + lenn * cos(teta)
            y = h // 2 + lenn * sin(teta)
            
            self.my_addline([w // 2, h // 2], [x, y], draw=draw)
            teta += radians(angle)

    def draw_line(self):
        try:
            x_start = float(self.lineEditStartX.text())
            x_end = float(self.lineEditEndX.text())
            y_start = float(self.lineEditStartY.text())
            y_end = float(self.lineEditEndY.text())
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "", "Координаты начала и конца отрезка должны быть целыми "
                                                     "или веществеными числами!")
            return
        self.my_addline([x_start, y_start], [x_end, y_end])
            

    def bresen_float(self, p_start, p_end, draw=True, steps=False):
        # Проверка на вырожденность отрезка в точку.
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            if draw:
                self.draw_point(round(p_start[0]), round(p_start[1]))
                QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        # Вычисление приращений.
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        # Вычисление шага изменение каждой координаты пикселя
        s_x = sign(dx)
        s_y = sign(dy)
        # Вычисление модуля приращения.
        dx = fabs(dx)
        dy = fabs(dy)
        # Обмен местами координат в случае m > 1 (тангенс)
        if (dy >= dx):
            dx, dy = dy, dx
            chenge = 1
        else:
            chenge = 0
        # Иницилизация начального значения ошибки.
        m = dy / dx # в случае INT m = 2 * dy
        e = m - 0.5 # в случае INT e = m - dx
        # Инициализации начальных значений текущего пикселя 
        # (т е начало отрезка тут)
        x = round(p_start[0])
        y = round(p_start[1])
        # Цикл от i = 1 до i = dx + 1 с шагом 1
        i = 1
        step = 1
        x_buf = x
        y_buf = y
        while i <= dx + 1:
            # Высвечивание точки с заданными координатами.
            if draw:
                self.draw_point(x, y)
            # Вычисление координат и ошибки для след пикселя.
            if e >= 0:
                if chenge == 1:
                    x += s_x
                else:
                    y += s_y
                e -= 1 # в случае INT e -= 2 * dx
            if e <= 0:
                if chenge == 1:
                    y += s_y
                else:
                    x += s_x
                e += m 
            i += 1
            if steps:
                if not((x_buf == x and y_buf != y) or
                    (x_buf != x and y_buf == y)):
                    step += 1
                x_buf = x
                y_buf = y
        if steps:
            return step
    
    def bresen_int(self, p_start, p_end, draw=True, steps=False):
        # Проверка на вырожденность отрезка в точку.
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            if draw:
                self.draw_point(round(p_start[0]), round(p_start[1]))
                QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        # Вычисление приращений.
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        # Вычисление шага изменение каждой координаты пикселя
        s_x = sign(dx)
        s_y = sign(dy)
        # Вычисление модуля приращения.
        dx = fabs(dx)
        dy = fabs(dy)
        # Обмен местами координат в случае m > 1 (тангенс)
        if (dy >= dx):
            dx, dy = dy, dx
            chenge = 1
        else:
            chenge = 0
        # Иницилизация начального значения ошибки.
        m = 2 * dy # в случае FLOAT m = dy / dx
        e = m - dx # в случае FLOAT e = m - 0.5
        # Инициализации начальных значений текущего пикселя 
        # (т е начало отрезка тут)
        x = round(p_start[0])
        y = round(p_start[1])
        # Цикл от i = 1 до i = dx + 1 с шагом 1
        i = 1
        step = 1
        x_buf = x
        y_buf = y
        while i <= dx + 1:
            # Высвечивание точки с заданными координатами.
            if draw:
                self.draw_point(x, y)
            if e >= 0:
                if chenge == 1:
                    x += s_x
                else:
                    y += s_y
                e -= 2 * dx # в случае FLOAT e -= 1
            if e <= 0:
                if chenge == 1:
                    y += s_y
                else:
                    x += s_x
                e += m
            i += 1
            if steps:
                if not((x_buf == x and y_buf != y) or
                    (x_buf != x and y_buf == y)):
                    step += 1
                x_buf = x
                y_buf = y
        if steps:
            return step


    def bresen_smooth(self, p_start, p_end, draw=True, steps=False):
        I = 255
        # print("draw in draw", draw)
        # Проверка на вырожденность отрезка в точку.
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            if draw:
                self.draw_point(round(p_start[0]), round(p_start[1]))
                QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        # Вычисление приращений.
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        # Вычисление шага изменение каждой координаты пикселя
        s_x = sign(dx)
        s_y = sign(dy)
        # Вычисление модуля приращения.
        dx = fabs(dx)
        dy = fabs(dy)
        # Обмен местами координат в случае m > 1 (тангенс)
        if (dy >= dx):
            dx, dy = dy, dx
            chenge = 1
        else:
            chenge = 0
        # Иницилизация начального значения ошибки.
        m = dy / dx
        e = I / 2
        # Инициализации начальных значений текущего пикселя 
        # (т е начало отрезка тут)
        x = round(p_start[0])
        y = round(p_start[1])
        # Вычисление скорректированного  значения  тангенса  угла наклона m и коэффициента W.
        m *= I
        W = I - m
        # Высвечивание пиксела  с координатами  (X,Y) интенсивностью E(f).
        if draw:
            # print("DDDD")
            self.draw_point(x, y, round(e))
        # Цикл от i = 1 до i = dx + 1 с шагом 1
        i = 1
        step = 1
        x_buf = x
        y_buf = y
        while i <= dx:
            if e < W:
                if chenge == 0:
                    x += s_x
                else:
                    y += s_y
                e += m
            else:
                x += s_x
                y += s_y
                e -= W
            if draw:
                # print("DDDD")
                self.draw_point(x, y, round(e))
            if steps:
                if not((x_buf == x and y_buf != y) or
                    (x_buf != x and y_buf == y)):
                    step += 1
                x_buf = x
                y_buf = y
            i += 1
        if steps:
            return step

        
    def dda(self, p_start, p_end, draw=True, steps=False):
        '''

        '''
        # Проверка на вырожденность отрезка в точку.
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            if draw:
                self.draw_point(round(p_start[0]), round(p_start[1]))
                QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        # print(p_start, p_end)
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        # print(dx, dy)
        if fabs(dx) > fabs(dy):
            L = fabs(dx)
        else:
            L = fabs(dy)

        sx = (p_end[0] - p_start[0]) / L
        sy = (p_end[1] - p_start[1]) / L

        x = p_start[0]
        y = p_start[1]
        i = 1
        step = 1
        while i <= L + 1:
            # print("LOOP, i, L + 1", i, L + 1)
            if draw:
                 self.draw_point(round(x), round(y))
            # print(x, x+dx, y, y+dy)
            if steps and i <= L:
                if not((round(x + sx) == round(x) and 
                        round(y + sy) != round(y)) or 
                        (round(x + sx) != round(x) and 
                        round(y + sy) == round(y))):
                    # print(step)
                    step += 1
            
            x += sx
            y += sy
            i += 1
        if steps:
            return step
    

    def wu(self, p_start, p_end, draw=True, steps=False):
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            if draw:
                self.draw_point(round(p_start[0]), round(p_start[1]))
                QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        dx = p_end[0] - p_start[0]
        dy = p_end[1] - p_start[1]
        if dy - dx < 0.1:
            print()
        Imax = 255
        m = 1
        step = 1
        if fabs(dy) > fabs(dx):
            if p_start[1] > p_end[1]:
                p_start[0], p_end[0] = p_end[0], p_start[0]
                p_start[1], p_end[1] = p_end[1], p_start[1]
            if dy != 0:
                m = dx / dy
            for y in range(round(p_start[1]), round(p_end[1]) + 1):
                d1 = p_start[0] - floor(p_start[0])
                d2 = 1 - d1
                if draw:
                    # нижняя точка
                    self.draw_point(int(p_start[0]), y, round(fabs(d2) * Imax))
                    # верхняя точка
                    self.draw_point(int(p_start[0]) + 1, y, round(fabs(d1) * Imax))
                if steps and y < round(p_end[1]):
                    if int(p_start[0]) != int(p_start[0] + m):
                        step += 1
                p_start[0] += m
        else:
            if p_start[0] > p_end[0]:
                p_start[0], p_end[0] = p_end[0], p_start[0]
                p_start[1], p_end[1] = p_end[1], p_start[1]
            if dx != 0:
                m = dy / dx
            for x in range(round(p_start[0]), round(p_end[0]) + 1):
                d1 = p_start[1] - floor(p_start[1])
                d2 = 1 - d1
                if draw:
                    pass
                    # нижняя точка
                    self.draw_point(x, int(p_start[1]), round(fabs(d2) * Imax))
                    # верхняя точка
                    self.draw_point(x, int(p_start[1]) + 1, round(fabs(d1) * Imax))

                if steps and x < round(p_end[0]):
                    if int(p_start[1]) != int(p_start[1] + m):
                        step += 1
                p_start[1] += m
        if steps:
            return step

    def lib(self, p_start, p_end):
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            self.draw_point(round(p_start[0]), round(p_start[1]))
            QtWidgets.QMessageBox.critical(self, "Информация", 
                "Внимание! Нарисована будет только точка.")
            return
        self.scene.addLine(round(p_start[0]), round(p_start[1]), 
                           round(p_end[0]), round(p_end[1]), self.pen)

    def com_time(self):
       
        angle = int(self.lineEditAngle.text())
        lenn = int(self.lineEdiLen.text())
        time_array= []

        self.radioButtonCDA.toggle()
        start = time()
        for _ in range(10):
            self.draw_spectr(draw=False)
            # cda_test([0,0], [200,200])
        time_array.append(time() - start)

        self.radioButtonBresFloat.toggle()
        start = time()
        for _ in range(10):
            # float_test([0,0], [200,200])
            self.draw_spectr(draw=False)
        time_array.append(time() - start)

        self.radioButtonBresInt.toggle()
        start = time()
        for _ in range(10):
            # int_test([0,0], [200,200])
            self.draw_spectr(draw=False)
        time_array.append(time() - start)
        
        self.radioButtonBresSmooth.toggle()
        start = time()
        for _ in range(10):
            # smoth_test([0,0], [200,200])
            self.draw_spectr(draw=False)
        time_array.append(time() - start)

        self.radioButtonWu.toggle()
        start = time()
        for _ in range(10):
            self.draw_spectr(draw=False)
        time_array.append(time() - start)
        
        self.radioButtonLib.toggle()
        start = time()
        for _ in range(10):
            self.draw_spectr(draw=False)
        time_array.append(time() - start)

        figur, ax = plt.subplots()

        ax.bar(["ЦДА", "Брезенхем\n(float)", "Брезенхем\n(int)", 
                "Брезенхем\n(сглаживание)", "By", "Библиотечный"], time_array, color="red")
        plt.title("Исследование времени выполнения\n{0} - длина отрезка; {1} - угол пучка".format(lenn, angle))
        plt.ylabel("Время в секундах")
        self.scene.clear()
        plt.show()
        # QtWidgets.QMessageBox.information(self, "Информация", 
        #             "Временная характеристика алгоритмов\n\n"
        #             "%5.2f - длина отрезка\n%5.2f - угол пучка"
        #             % lenn, angle)
            



    def com_step(self):
        try:
            angle = int(self.lineEditAngle.text())
            lenn = int(self.lineEdiLen.text())
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "", 
                    "Угол поворота и длина должны быть целыми числами!")
            return
        if angle < 1:
            QtWidgets.QMessageBox.critical(self, "", "Угол поворота должен быть больше нуля!")
            return
        if lenn < 1:
            QtWidgets.QMessageBox.critical(self, "", "Длина отрезка должна быть больше нуля!")
            return
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        cda = []
        b_float = []
        b_int = []
        b_smooth = []
        wu = []

        teta = 0
        angle = [i for i in range(0, 91, 2)]
        # print(angle)
        while teta <= pi / 2 + 0.01:
            x = w // 2 + lenn * cos(teta)
            y = h // 2 + lenn * sin(teta)
            cda.append(self.dda([w //2, h // 2], [x, y], False, True))
            b_float.append(self.bresen_float([w //2, h // 2], [x, y], False, True))
            b_int.append(self.bresen_int([w //2, h // 2], [x, y], False, True))
            b_smooth.append(self.bresen_smooth([w //2, h // 2], [x, y], False, True))
            wu.append(self.wu([w //2, h // 2], [x, y], False, True))
            teta += radians(2)

        fig, ax = plt.subplots()
        ax.plot(angle, cda, label='ЦДА')
        ax.plot(angle, b_float, label='Брезенхем\n(float/int)')
        ax.plot(angle, b_smooth, label='Брезенхем\nсглаживание')
        ax.plot(angle, wu, label='Ву')
        ax.set_facecolor('seashell')
        plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(lenn))
        plt.legend()
        plt.ylabel("Максимальное колличество ступенек.")
        plt.xlabel("Угол в градусах.")
        plt.show()
        # QtWidgets.QMessageBox.information(self, "Информация", 
        #             "Исследование ступенчатости отрезков\n\n"
        #             "%5.2f - длина отрезка\n"
        #             .format(lenn))

    def com_step_one(self):
        try:
            angle = int(self.lineEditAngle.text())
            lenn = int(self.lineEdiLen.text())
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "", 
                    "Угол поворота и длина должны быть целыми числами!")
            return
        if angle < 1:
            QtWidgets.QMessageBox.critical(self, "", "Угол поворота должен быть больше нуля!")
            return
        if lenn < 1:
            QtWidgets.QMessageBox.critical(self, "", "Длина отрезка должна быть больше нуля!")
            return
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        cda = []
        b_float = []
        b_int = []
        b_smooth = []
        wu = []

        teta = 0
        angle = [i for i in range(0, 91, 2)]
        # print(angle)
        while teta <= pi / 2 + 0.01:
            x = w // 2 + lenn * cos(teta)
            y = h // 2 + lenn * sin(teta)
            if (self.radioButtonCDA.isChecked()):
                cda.append(self.dda([w //2, h // 2], [x, y], False, True))
            elif (self.radioButtonBresFloat.isChecked() or
                  self.radioButtonBresInt.isChecked()):
                b_float.append(self.bresen_float([w //2, h // 2], [x, y], False, True))
            elif (self.radioButtonBresSmooth.isChecked()):
                b_smooth.append(self.bresen_smooth([w //2, h // 2], [x, y], False, True))
            elif (self.radioButtonWu.isChecked()):
                wu.append(self.wu([w //2, h // 2], [x, y], False, True))
            elif (self.radioButtonLib.isChecked()):
                QtWidgets.QMessageBox.critical(self, "", "Библиотечная функция не исследуется на ступенчатость")
                return
            teta += radians(2)

        fig, ax = plt.subplots()
        if (self.radioButtonCDA.isChecked()):
            ax.plot(angle, cda, label='ЦДА')
        elif (self.radioButtonBresFloat.isChecked() or
              self.radioButtonBresInt.isChecked()):
            ax.plot(angle, b_float, label='Брезенхем\n(float/int)')
        elif (self.radioButtonBresSmooth.isChecked()):
            ax.plot(angle, b_smooth, label='Брезенхем\nсглаживание')
        elif (self.radioButtonWu.isChecked()):
            ax.plot(angle, wu, label='Ву')
        
        ax.set_facecolor('seashell')
        plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(lenn))
        plt.legend()
        plt.ylabel("Максимальное колличество ступенек.")
        plt.xlabel("Угол в градусах.")
        plt.show()
        # QtWidgets.QMessageBox.information(self, "Информация", 
        #             "Исследование ступенчатости отрезков\n\n"
        #             "%5.2f - длина отрезка\n"
        #             .format(lenn))

    

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Visual()
    win.show()
    app.exec_()