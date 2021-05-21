import sys
from tkinter.constants import FALSE
from numpy import sign
import win2
import pyqtgraph as pg
import matplotlib.pyplot as plt


from time import time
from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint, endl
from math import sin, cos, pi, radians, fabs,  floor

now = None
end_rect_ = False
ctrl = False
wind = None

class Scene(QtWidgets.QGraphicsScene):
    
    def keyPressEvent(self, event):
        global ctrl
        # print(event.key() == Qt.Key_Control)
        if event.key() == Qt.Key_Control:
            # print("if")
            ctrl = True
        else:
            # print("else")
            ctrl = False
        # print("res", ctrl)
    # добавить точку по щелчку мыши
    def mousePressEvent(self, QMouseEvent):
        if (QMouseEvent.button() == Qt.LeftButton) and (end_rect_ == False):
            print("nenm")
            add_point(QMouseEvent.scenePos())
        
        if (QMouseEvent.button() == Qt.RightButton):
            end_rect()
               


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
        self.rect = []
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
        self.pushButton_RES.clicked.connect(cyrus_beck_alg)


    def cheng(self):
        global now, now_buf
        if self.radioButton_draw_line.isChecked():
            print(self.rect)
            now_buf = now
            now = None
            self.input_lines = True
            self.input_rect = False
        elif self.radioButton_draw_rest.isChecked():
            self.input_lines = False
            self.input_rect = True

    def clean_screen(self):
        global now
        self.scene.clear()
        self.lines = []
        self.rect = []
        now = None
        self.image.fill(Qt.white)
        r = self.table_line.rowCount()
        for i in range(r, -1, -1):
            self.table_line.removeRow(i)
        r = self.table_rust.rowCount()
        for i in range(r, -1, -1):
            self.table_rust.removeRow(i)

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

        add_row(wind, 1)
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
            x = float(self.lineEdit_x.text())
            y = float(self.lineEdit_y.text())
            
        except Exception:
            QMessageBox.warning(self, "Внимание!", "Неверно введены координаты!")
            return 
        
        add_point_simple(x, y)

# Добавить точку
def add_point_simple(x, y):
    global wind, ctrl, now

    if (len(wind.rect)) == 0:
        wind.rect.append([x, y])

        add_row(wind, 2)
        i = wind.table_rust.rowCount() - 1
        item_b = QTableWidgetItem("[{0}]".format(x))
        item_e = QTableWidgetItem("[{0}]".format(y))
        wind.table_rust.setItem(i, 0, item_b)
        wind.table_rust.setItem(i, 1, item_e)

    else:
        add_row(wind, 2)
        i = wind.table_rust.rowCount() - 1
        item_b = QTableWidgetItem("[{0}]".format(x))
        item_e = QTableWidgetItem("[{0}]".format(y))
        print(item_b, item_e)
        wind.table_rust.setItem(i, 0, item_b)
        wind.table_rust.setItem(i, 1, item_e)

        i = len(wind.rect)
        if ctrl:
            if abs(x - wind.rect[i - 1][0]) < abs(y - wind.rect[i - 1][1]):
                x = wind.rect[i - 1][0]
            elif abs(y - wind.rect[i - 1][1]) < abs(x - wind.rect[i - 1][0]):
                y = wind.rect[i - 1][1]
            ctrl = False
        wind.scene.addLine(wind.rect[i - 1][0], wind.rect[i - 1][1], 
                            x, y, wind.pen_rest)
        wind.rect.append([x, y])


# Добавить строку с координатами с таблицу
def add_row(win, f):
    if f == 1:
        win.table_line.insertRow(win.table_line.rowCount())
    if f == 2:
        win.table_rust.insertRow(win.table_rust.rowCount())

# Добавить точку
def add_point(point):
    global wind, ctrl, now
    x = point.x()
    y = point.y()

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
            wind.lines.append([[wind.point_now.x(), wind.point_now.y()],
                            [x, y]])

            add_row(wind, 1)
            i = wind.table_line.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(wind.point_now.x(), wind.point_now.y()))
            item_e = QTableWidgetItem("[{0}, {1}]".format(point.x(), point.y()))
            wind.table_line.setItem(i, 0, item_b)
            wind.table_line.setItem(i, 1, item_e)

            wind.scene.addLine(wind.point_now.x(), wind.point_now.y(), 
                               x, y, wind.pen_line)
            wind.point_now = None

    if wind.input_rect:
        if (len(wind.rect)) == 0:
            wind.rect.append([point.x(), point.y()])

            add_row(wind, 2)
            i = wind.table_rust.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            wind.table_rust.setItem(i, 0, item_b)
            wind.table_rust.setItem(i, 1, item_e)

        else:
            add_row(wind, 2)
            i = wind.table_rust.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            print(item_b, item_e)
            wind.table_rust.setItem(i, 0, item_b)
            wind.table_rust.setItem(i, 1, item_e)

            x = point.x()
            y = point.y()

            i = len(wind.rect)
            if ctrl:
                if abs(point.x() - wind.rect[i - 1][0]) < abs(point.y() - wind.rect[i - 1][1]):
                    x = wind.rect[i - 1][0]
                elif abs(point.y() - wind.rect[i - 1][1]) < abs(point.x() - wind.rect[i - 1][0]):
                    y = wind.rect[i - 1][1]
                ctrl = False
            wind.scene.addLine(wind.rect[i - 1][0], wind.rect[i - 1][1], 
                               x, y, wind.pen_rest)
            wind.rect.append([x, y])


def end_rect():
    global wind, ctrl, now, end_rect_

    end_rect_ == True
    if wind.input_rect:
        print("SSSSSSSSSSSSS", len(wind.rect))
        if (len(wind.rect)) == 0:
            QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите отсекатель!")
        else:
            i = len(wind.rect)
            wind.scene.addLine(wind.rect[i - 1][0], wind.rect[i - 1][1], 
                               wind.rect[0][0], wind.rect[0][1], wind.pen_rest)

def get_d_k_b(ax, ay, cx, cy):
        # Коэффициенты прямой АС
    # Если точки A и С лежат на одной вертикальной прямой
    if abs((cx - ax) - 0) <= 1e-6:
        k = 1
        b = -cx
        d = 0
    else:
        k = (cy - ay) / (cx - ax)
        b = cy - (k * cx)
        d = 1

    return d, k, b


def cross_lines(ax, ay, bx, by, cx, cy, dx, dy):
    d_ab, k_ab, b_ab = get_d_k_b(ax, ay, bx, by)
    d_cd, k_cd, b_cd = get_d_k_b(cx, cy, dx, dy)

    print("ab", d_ab, k_ab, b_ab)
    print("cd", d_cd, k_cd, b_cd)

    if abs(k_ab - k_cd) < 1e-6:
        return False
    x = (b_cd - b_ab) / (k_ab - k_cd)
    if d_cd == 0:
        y = (k_ab * x + b_ab) 
    elif d_ab == 0:
        y = (k_cd * x + b_cd)
    else:
        y = (k_ab * x + b_ab)

    print(x, y)

    b1 = ax
    b2 = bx
    ax = max(b1, b2)
    bx = min(b1, b2)
    b1 = ay
    b2 = by
    ay = max(b1, b2)
    by = min(b1, b2)

    print((bx < x and x < ax) and (by < y and y < ay), "aaaa", ax, x, bx, ay, y, by)
    if (bx < x and x < ax) and (by < y and y < ay):
        return True
    else:
        return False

    

def check_cross(arr):
    n = len(arr)
    f = False
    for i in range(n - 1):
        for j in range(i + 1, n, 1):
            if j == n - 1:
                f = cross_lines(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1],
                                arr[j][0], arr[j][1], arr[0][0], arr[0][1])
                print("n-1 f", f, i, j, arr[i], arr[j])
                if f:
                    return True
            else:
                f = cross_lines(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1],
                                arr[j][0], arr[j][1], arr[j + 1][0], arr[j + 1][1])
                print("simple f", f, i, j, arr[i], arr[j])
                if f:
                    return True

    return False


def scalar_mult(a, b):
    return a[0] * b[0] + a[1] * b[1]

def vector_mult(a, b):
    return a[0] * b[1] - a[1] * b[0] # Ax * By - Ay * Bx --- это будет координата Z, которая нам нужна


def is_convex(arr):
    if len(arr) < 3:
        return False

    a = [arr[0][0] - arr[-1][0], arr[0][1] - arr[-1][1]]
    b = [arr[-1][0] - arr[-2][0], arr[-1][1] - arr[-2][1]]
    prev = sign(vector_mult(a, b))
    for i in range(1, len(arr) - 2):
        a = [arr[i][0] - arr[i - 1][0], arr[i][1] - arr[i - 1][1]]
        b = [arr[i - 1][0] - arr[i - 2][0], arr[i - 1][1] - arr[i - 2][1]]
        cur = sign(vector_mult(a, b))
        if prev != cur:
            return False
        prev = cur

    if (check_cross(arr)):
        return False

    return True

def normal(a, b, pos):
    fvec = [b[0] - a[0], b[1] - a[1]]
    posvec = [pos[0] - b[0], pos[1] - b[1]]

    if fvec[1]:
        fpoint = -fvec[0] / fvec[1]
        normvec = [1, fpoint]
    else:
        normvec = [0, 1]

    if scalar_mult(posvec, normvec) < 0:
        normvec[0] = -normvec[0]
        normvec[1] = -normvec[1]

    return normvec

def cut_one(line, count):
    d = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
    top = 0
    bottom = 1
    for i in range(-2, count - 2):
        norm = normal(wind.rect[i], wind.rect[i + 1], wind.rect[i + 2])
        w = [line[0][0] - wind.rect[i][0], line[0][1] - wind.rect[i][1]]
        d_scal = scalar_mult(d, norm)
        w_scal = scalar_mult(w, norm)
        if d_scal == 0:
            if w_scal < 0:
                return []
            else:
                continue
        param = -w_scal / d_scal
        if d_scal > 0:
            top = max(top, param)
        elif d_scal < 0:
            bottom = min(bottom, param)

        if top > bottom:
            break
    if top <= bottom:
        return [[round(line[0][0] + d[0] * top), round(line[0][1] + d[1] * top)],
                        [round(line[0][0] + d[0] * bottom), round(line[0][1] + d[1] * bottom)]]

    return []

def cyrus_beck_alg():
    lines = wind.lines
    rect = wind.rect
    print(lines, rect)
    if not is_convex(rect):
        QMessageBox.warning(wind, "Внимание!", "Отсекатель невыпусклый!!!")
        return 
    count_sides = len(rect)

    drawarr = []
    for line in lines:
        cutt = cut_one(line, count_sides)
        if cutt:
            drawarr.append(cutt)

    draw_lines(drawarr)
    return

def draw_lines(arr):
    print(arr)
    global wind
    try:
        w = int(wind.spinBox_w.text())
    except Exception:
        QMessageBox.warning(wind, "Внимание!", "Не целове значение толщины!")
        return 
    wind.pen_res.setWidth(w)
    for l in arr:

        wind.scene.addLine(l[1][0], l[1][1], l[0][0], l[0][1], wind.pen_res)


# def digitBresenhamForCuted(image, xStart, yStart, xEnd, yEnd, color):
#     if xStart == xEnd and yStart == yEnd:
#         image.put(color, (xStart, yStart))
#         return

#     deltaX = xEnd - xStart
#     deltaY = yEnd - yStart

#     stepX = int(np.round(sign(deltaX)))
#     stepY = int(np.round(sign(deltaY)))

#     deltaX = abs(deltaX)
#     deltaY = abs(deltaY)

#     if deltaX < deltaY:
#         deltaX, deltaY = deltaY, deltaX
#         flag = True
#     else:
#         flag = False

#     acc = deltaY + deltaY - deltaX
#     curX = xStart
#     curY = yStart

#     for i in range(1, deltaX + 1):
#         magicColor = wind.pen_line
#         print(magicColor)
#         if image.get(curX, curY) == magicColor:
#             image.put(color, (curX, curY))
#         if image.get(curX, curY + 1) == magicColor:
#             image.put(color, (curX, curY + 1))
#         if image.get(curX, curY - 1) == magicColor:
#             image.put(color, (curX, curY - 1))
#         if image.get(curX + 1, curY) == magicColor:
#             image.put(color, (curX + 1, curY))
#         if image.get(curX - 1, curY) == magicColor:
#             image.put(color, (curX - 1, curY))
#         if image.get(curX - 1, curY - 1) == magicColor:
#             image.put(color, (curX - 1, curY - 1))
#         if image.get(curX - 1, curY + 1) == magicColor:
#             image.put(color, (curX - 1, curY + 1))
#         if image.get(curX + 1, curY - 1) == magicColor:
#             image.put(color, (curX + 1, curY - 1))
#         if image.get(curX + 1, curY + 1) == magicColor:
#             image.put(color, (curX + 1, curY + 1))

#         if flag:
#             if acc >= 0:
#                 curX += stepX
#                 acc -= (deltaX + deltaX)
#             curY += stepY
#             acc += deltaY + deltaY
#         else:
#             if acc >= 0:
#                 curY += stepY
#                 acc -= (deltaX + deltaX)
#             curX += stepX
#             acc += deltaY + deltaY


def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()