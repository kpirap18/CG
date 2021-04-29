import sys
import numpy as np
import win2
import pyqtgraph as pg
import matplotlib.pyplot as plt

from time import time
from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
from math import sin, cos, pi, radians, fabs,  floor


now = None
ctrl = False
wind = None

class Scene(QtWidgets.QGraphicsScene):
    
    def keyPressEvent(self, event):
        global ctrl
        print(event.key() == Qt.Key_Control)
        if event.key() == Qt.Key_Control:
            print("if")
            ctrl = True
        else:
            print("else")
            ctrl = False
        print("res", ctrl)
    # добавить точку по щелчку мыши
    def mousePressEvent(self, event):
        add_point(event.scenePos())
        

    # добавить прямоугольник
    def mouseMoveEvent(self, event):
        global now, wind
        if wind.input_rect:
            if now is None:
                now = event.scenePos()
                wind.rect[0] = now.x()
                wind.rect[3] = now.y()
            else:
                self.removeItem(self.itemAt(now, QTransform()))
                p = event.scenePos()
                self.addRect(now.x(), now.y(), abs(now.x() - p.x()), abs(now.y() - p.y()), wind.pen_rest)
                wind.rect[1] = p.x()
                wind.rect[2] = p.y()
        strr = "Х левое = {0}\nХ правое = {1}\nУ нижнее = {2}\nУ верхнее = {3}\n".format(wind.rect[0],
                                                                                         wind.rect[1],
                                                                                         wind.rect[2],
                                                                                         wind.rect[3])
        wind.label_10.setText(strr)
               


class Visual(QtWidgets.QMainWindow, win2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.graphicsView.scale(1, 1)
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        self.scene = Scene(0, 0, w - 2, h - 2)
        self.scene.win = self
        self.graphicsView.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        # self.scene.setSceneRect(0, 0, w-2, h-2)
        self.pen_rest = QtGui.QPen(QtCore.Qt.black)
        self.pen_rest.setWidth(0)
        self.pen_line = QtGui.QPen(QtCore.Qt.green)
        self.pen_line.setWidth(0)
        self.pen_res = QtGui.QPen(QtCore.Qt.red)
        self.pen_res.setWidth(0)
        self.input_rect = False
        self.input_lines = True
        self.lines = []
        self.rect = [0, 0, 0, 0]
        self.clip = None
        self.point_now = None

        self.radioButton_draw_line.clicked.connect(self.cheng)
        self.radioButton_draw_rest.clicked.connect(self.cheng) 

        self.radioButtonBlack_bg.clicked.connect(self.set_black_bg)
        self.radioButtonBlue_bg.clicked.connect(self.set_blue_bg)
        self.radioButtonGreen_bg.clicked.connect(self.set_green_bg)
        self.radioButtonRed_bg.clicked.connect(self.set_red_bg)
        self.radioButtonWhite_bg.clicked.connect(self.set_white_bg)
        self.radioButtonYellow_bg.clicked.connect(self.set_yellow_bg)

        self.radioButtonBlack_line.clicked.connect(self.set_black_line)
        self.radioButtonBlue_line.clicked.connect(self.set_blue_line)
        self.radioButtonGreen_line.clicked.connect(self.set_green_line)
        self.radioButtonRed_line.clicked.connect(self.set_red_line)
        self.radioButtonWhite_line.clicked.connect(self.set_white_line)
        self.radioButtonYellow_line.clicked.connect(self.set_yellow_line)

        self.radioButtonBlack_rest.clicked.connect(self.set_black_rest)
        self.radioButtonBlue_rest.clicked.connect(self.set_blue_rest)
        self.radioButtonGreen_rest.clicked.connect(self.set_green_rest)
        self.radioButtonRed_rest.clicked.connect(self.set_red_rest)
        self.radioButtonWhite_rest.clicked.connect(self.set_white_rest)
        self.radioButtonYellow_rest.clicked.connect(self.set_yellow_rest)

        self.radioButtonBlack_res.clicked.connect(self.set_black_res)
        self.radioButtonBlue_res.clicked.connect(self.set_blue_res)
        self.radioButtonGreen_res.clicked.connect(self.set_green_res)
        self.radioButtonRed_res.clicked.connect(self.set_red_res)
        self.radioButtonWhite_res.clicked.connect(self.set_white_res)
        self.radioButtonYellow_res.clicked.connect(self.set_yellow_res)

        self.pushButton_clean.clicked.connect(self.clean_screen)
        self.pushButton_draw_line.clicked.connect(self.add_line1)
        self.pushButton_draw_rest.clicked.connect(self.add_rect)
        self.pushButton_gran.clicked.connect(self.add_bars)
        self.pushButton_RES.clicked.connect(clipping)


    def cheng(self):
        if self.radioButton_draw_line.isChecked():
            print(self.rect)
            self.input_lines = True
            self.input_rect = False
        elif self.radioButton_draw_rest.isChecked():
            self.input_lines = False
            self.input_rect = True

    def clean_screen(self):
        global now
        self.scene.clear()
        # self.table_line.clear()
        self.lines = []
        now = None
        self.image.fill(Qt.white)
        r = self.table_line.rowCount()
        for i in range(r, -1, -1):
            self.table_line.removeRow(i)

    def set_black_line(self):
        self.pen_line.setColor(QtCore.Qt.black)

    def set_white_line(self):
        self.pen_line.setColor(QtCore.Qt.white)
    
    def set_blue_line(self):
        self.pen_line.setColor(QtCore.Qt.blue)

    def set_red_line(self):
        self.pen_line.setColor(QtCore.Qt.red)

    def set_green_line(self):
        self.pen_line.setColor(QtCore.Qt.green)

    def set_yellow_line(self):
        self.pen_line.setColor(QtCore.Qt.yellow)



    def set_black_res(self):
        self.pen_res.setColor(QtCore.Qt.black)

    def set_white_res(self):
        self.pen_res.setColor(QtCore.Qt.white)
    
    def set_blue_res(self):
        self.pen_res.setColor(QtCore.Qt.blue)

    def set_red_res(self):
        self.pen_res.setColor(QtCore.Qt.red)

    def set_green_res(self):
        self.pen_res.setColor(QtCore.Qt.green)

    def set_yellow_res(self):
        self.pen_res.setColor(QtCore.Qt.yellow)



    def set_black_rest(self):
        self.pen_rest.setColor(QtCore.Qt.black)

    def set_white_rest(self):
        self.pen_rest.setColor(QtCore.Qt.white)
    
    def set_blue_rest(self):
        self.pen_rest.setColor(QtCore.Qt.blue)

    def set_red_rest(self):
        self.pen_rest.setColor(QtCore.Qt.red)

    def set_green_rest(self):
        self.pen_rest.setColor(QtCore.Qt.green)

    def set_yellow_rest(self):
        self.pen_rest.setColor(QtCore.Qt.yellow)



    def set_black_bg(self):
        self.graphicsView.setStyleSheet("background-color: black")

    def set_white_bg(self):
        self.graphicsView.setStyleSheet("background-color: white")

    def set_blue_bg(self):
        self.graphicsView.setStyleSheet("background-color: blue")

    def set_red_bg(self):
        self.graphicsView.setStyleSheet("background-color: red")

    def set_green_bg(self):
        self.graphicsView.setStyleSheet("background-color: #00ff00")

    def set_yellow_bg(self):
        self.graphicsView.setStyleSheet("background-color: yellow")


    def add_line1(self):
        try:
            x_start = float(self.lineEdit_5.text())
            x_end = float(self.lineEdit_8.text())
            y_start = float(self.lineEdit_6.text())
            y_end = float(self.lineEdit_7.text())
        except Exception:
            QMessageBox.warning(self, "Внимание!", "Неверно введены координаты!")
            return 

        wind.lines.append([[x_start, y_start],
                            [x_end, y_end]])

        add_row(wind)
        i = wind.table_line.rowCount() - 1
        item_b = QTableWidgetItem("[{0}, {1}]".format(x_start, y_start))
        item_e = QTableWidgetItem("[{0}, {1}]".format(x_end, y_end))
        wind.table_line.setItem(i, 0, item_b)
        wind.table_line.setItem(i, 1, item_e)
        wind.scene.addLine(x_start, y_start, 
                            x_end, y_end, wind.pen_line)
        wind.point_now = None

    def add_rect(self):
        try:
            x_left = float(self.lineEdit_xleft.text())
            x_right = float(self.lineEdit_xright.text())
            y_down = float(self.lineEdit_ydown.text())
            y_up = float(self.lineEdit_yup.text())
        except Exception:
            QMessageBox.warning(self, "Внимание!", "Неверно введены координаты!")
            return 
        self.rect[0] = x_left
        self.rect[1] = x_right
        self.rect[2] = y_down
        self.rect[3] = y_up

        strr = "Х левое = {0}\nХ правое = {1}\nУ нижнее = {2}\nУ верхнее = {3}\n".format(x_left, x_right, y_down, y_up)
        self.label_10.setText(strr)


        self.scene.addRect(x_left, y_up, abs(x_right - x_left), abs(y_down - y_up), self.pen_rest)

    def add_bars(self):
        global now, wind
        if now is None:
            QMessageBox.warning(self, "Внимание!", "Не введен отсекатель!")
            return 

        buf = self.scene.itemAt(now, QTransform())
        if buf is None:
            QMessageBox.warning(self, "Внимание!", "Не введен отсекатель!")
        else:
            buf = buf.rect()
            self.clip = [buf.left(), buf.right(), buf.top(),  buf.bottom()]

            t = abs(self.clip[2] - self.clip[3]) * 0.8
            k = abs(self.clip[0] - self.clip[1]) * 0.8
            # задаем граничные отрезки
            
            self.lines.append([[self.clip[0], self.clip[2] + t],  [self.clip[0], self.clip[3] - t]])
            add_row(wind)
            i = self.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(self.clip[0], self.clip[2] + t))
            item_e = QTableWidgetItem("[{0}, {1}]".format(self.clip[0], self.clip[3] - t))
            self.table_line.setItem(i, 0, item_b)
            self.table_line.setItem(i, 1, item_e)
            self.scene.addLine(self.clip[0], self.clip[2] + t,  self.clip[0], self.clip[3] - t, self.pen_line)

            self.lines.append([[self.clip[1], self.clip[2] + t],  [self.clip[1], self.clip[3] - t]])
            add_row(wind)
            i = self.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(self.clip[1], self.clip[2] + t))
            item_e = QTableWidgetItem("[{0}, {1}]".format(self.clip[1], self.clip[3] - t))
            self.table_line.setItem(i, 0, item_b)
            self.table_line.setItem(i, 1, item_e)
            self.scene.addLine(self.clip[1], self.clip[3] - t,  self.clip[1], self.clip[2] + t, self.pen_line)

            self.lines.append([[self.clip[0] + k, self.clip[2]], [self.clip[1] - k, self.clip[2]]])
            add_row(wind)
            i = self.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(self.clip[0] + k, self.clip[2]))
            item_e = QTableWidgetItem("[{0}, {1}]".format(self.clip[1] - k, self.clip[2]))
            self.table_line.setItem(i, 0, item_b)
            self.table_line.setItem(i, 1, item_e)
            self.scene.addLine(self.clip[0] + k, self.clip[2], self.clip[1] - k, self.clip[2], self.pen_line)

            self.lines.append([[self.clip[0] + k, self.clip[3]], [self.clip[1] - k, self.clip[3]]])
            add_row(wind)
            i = self.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(self.clip[0] + k, self.clip[3]))
            item_e = QTableWidgetItem("[{0}, {1}]".format(self.clip[1] - k, self.clip[3]))
            self.table_line.setItem(i, 0, item_b)
            self.table_line.setItem(i, 1, item_e)
            self.scene.addLine(self.clip[0] + k, self.clip[3], self.clip[1] - k, self.clip[3], self.pen_line)



# Добавить строку с координатами с таблицу
def add_row(win):
    win.table_line.insertRow(win.table_line.rowCount())

# Добавить точку
def add_point(point):
    global wind, ctrl
    print("add_point", ctrl)
    x = point.x()
    y = point.y()
    print("x, y", x, y)
    if wind.input_lines:
        if wind.point_now is None:
            wind.point_now = point
        else:
            if ctrl:
                if abs(point.x() - wind.point_now.x()) < abs(point.y() - wind.point_now.y()):
                    x = wind.point_now.x()
                elif abs(point.y() - wind.point_now.y()) < abs(point.x() - wind.point_now.x()):
                    y = wind.point_now.y()
                ctrl = False
            print("x, y", x, y)
            wind.lines.append([[wind.point_now.x(), wind.point_now.y()],
                            [x, y]])

            add_row(wind)
            i = wind.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(wind.point_now.x(), wind.point_now.y()))
            item_e = QTableWidgetItem("[{0}, {1}]".format(point.x(), point.y()))
            wind.table_line.setItem(i, 0, item_b)
            wind.table_line.setItem(i, 1, item_e)
            wind.scene.addLine(wind.point_now.x(), wind.point_now.y(), 
                               x, y, wind.pen_line)
            wind.point_now = None


def get_code(a, rect):
    code = [0, 0, 0, 0]
    if a[0] < rect[0]:
        code[0] = 1
    if a[0] > rect[1]:
        code[1] = 1
    if a[1] < rect[2]:
        code[2] = 1
    if a[1] > rect[3]:
        code[3] = 1

    return code

# отсекание
def clipping():
    global wind, now
    
    buf = wind.scene.itemAt(now, QTransform()).rect()
    wind.clip = [buf.left(), buf.right(), buf.top(),  buf.bottom()]
    for b in wind.lines:
        pass
        cohen_sutherland(b, wind.clip)
   


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p

#  Видимость
def is_visible(bar, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(bar[0], rect))
    s2 = sum(get_code(bar[1], rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = 1
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(bar[0], rect), get_code(bar[1], rect))
        if l != 0:
            vis = 0

    return vis




def cohen_sutherland(bar, rect):
    global wind
    # инициализация флага
    flag = 1 # общего положения
    t = 1

    # проверка вертикальности и горизонтальности отрезка
    if bar[1][0] - bar[0][0] == 0:
        flag = -1   # вертикальный отрезок
    else:
        # вычисление наклона
        t = (bar[1][1] - bar[0][1]) / (bar[1][0] - bar[0][0])
        if t == 0:
            flag = 0   # горизонтальный

    # для каждой стороны окна
    for i in range(4):
        vis = is_visible(bar, rect)
        if vis == 1:
            wind.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], wind.pen_res)
            return
        elif not vis:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(bar[0], rect)
        code2 = get_code(bar[1], rect)

        if code1[i] == code2[i]:
            continue

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if not code1[i]:
            bar[0], bar[1] = bar[1], bar[0]

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:
            if i < 2:
                bar[0][1] = t * (rect[i] - bar[0][0]) + bar[0][1]
                bar[0][0] = rect[i]
                continue
            else:
                bar[0][0] = (1 / t) * (rect[i] - bar[0][1]) + bar[0][0]

        bar[0][1] = rect[i]
    wind.scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1], wind.pen_res)



def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()