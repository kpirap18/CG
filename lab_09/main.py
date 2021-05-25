import sys
from tkinter.constants import FALSE, S
from numpy import sign
import win2
import pyqtgraph as pg
import matplotlib.pyplot as plt


from time import time
from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QBrush, QPen, QColor, QImage, QPixmap, QPainter, QPolygon, QTransform, QVector3D, QPolygonF
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint, endl, QPointF
from math import sin, cos, pi, radians, fabs,  floor

now = None
end_rect_ = False
end_lines_ = False
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
        if ((QMouseEvent.button() == Qt.LeftButton) and (end_rect_ == False or end_lines_ == False)):
            print("nenm")
            add_point(QMouseEvent.scenePos())
        
        if (QMouseEvent.button() == Qt.RightButton):
            if wind.input_cut:
                end_cut()
            if wind.input_rests:
                end_rest()

               


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
        self.pen_cut = QtGui.QPen(QtCore.Qt.black)
        self.pen_cut.setWidth(0)
        self.pen_rest = QtGui.QPen(QtCore.Qt.green)
        self.pen_rest.setWidth(0)
        self.pen_res = QtGui.QPen(QtCore.Qt.red)
        self.pen_res.setWidth(0)
        self.input_cut = False
        self.input_rests = True
        self.lines = []
        self.rect = []
        self.clip = None
        self.point_now = None
        self.color_back = QtCore.Qt.white

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
        self.pushButton_draw_rest.clicked.connect(self.add_rest)
        self.pushButton_draw_cut.clicked.connect(self.add_cut)

        self.pushButton_end_cut.clicked.connect(end_cut)
        self.pushButton_end_rest.clicked.connect(end_rest)

        self.pushButton_RES.clicked.connect(Sutherland_Hodgman)


    def cheng(self):
        global now, now_buf
        if self.radioButton_draw_line.isChecked():
            print(self.rect)
            now_buf = now
            now = None
            self.input_rests = True
            self.input_cut = False
        elif self.radioButton_draw_rest.isChecked():
            self.input_rests = False
            self.input_cut = True

    def clean_screen(self):
        global now
        self.scene.clear()
        self.lines = []
        self.rect = []
        now = None
        self.image.fill(Qt.white)
        r = self.table_rest.rowCount()
        for i in range(r, -1, -1):
            self.table_rest.removeRow(i)
        r = self.table_cut.rowCount()
        for i in range(r, -1, -1):
            self.table_cut.removeRow(i)

    def set_black_line(self):
        self.pen_rest.setColor(QtCore.Qt.black)

    def set_white_line(self):
        self.pen_rest.setColor(QtCore.Qt.white)
    
    def set_blue_line(self):
        self.pen_rest.setColor(QtCore.Qt.blue)

    def set_red_line(self):
        self.pen_rest.setColor(QtCore.Qt.red)

    def set_green_line(self):
        self.pen_rest.setColor(QtCore.Qt.green)

    def set_yellow_line(self):
        self.pen_rest.setColor(QtCore.Qt.yellow)



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
        self.pen_cut.setColor(QtCore.Qt.black)

    def set_white_rest(self):
        self.pen_cut.setColor(QtCore.Qt.white)
    
    def set_blue_rest(self):
        self.pen_cut.setColor(QtCore.Qt.blue)

    def set_red_rest(self):
        self.pen_cut.setColor(QtCore.Qt.red)

    def set_green_rest(self):
        self.pen_cut.setColor(QtCore.Qt.green)

    def set_yellow_rest(self):
        self.pen_cut.setColor(QtCore.Qt.yellow)



    def set_black_bg(self):
        self.graphicsView.setStyleSheet("background-color: black")
        self.color_back = QtCore.Qt.black

    def set_white_bg(self):
        self.graphicsView.setStyleSheet("background-color: white")
        self.color_back = QtCore.Qt.white

    def set_blue_bg(self):
        self.graphicsView.setStyleSheet("background-color: blue")
        self.color_back = QtCore.Qt.blue

    def set_red_bg(self):
        self.graphicsView.setStyleSheet("background-color: red")
        self.color_back = QtCore.Qt.red

    def set_green_bg(self):
        self.graphicsView.setStyleSheet("background-color: #00ff00")
        self.color_back = QtCore.Qt.green

    def set_yellow_bg(self):
        self.graphicsView.setStyleSheet("background-color: yellow")
        self.color_back = QtCore.Qt.yellow


    def add_rest(self):
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
        i = wind.table_rest.rowCount() - 1
        item_b = QTableWidgetItem("[{0}, {1}]".format(x_start, y_start))
        item_e = QTableWidgetItem("[{0}, {1}]".format(x_end, y_end))
        wind.table_rest.setItem(i, 0, item_b)
        wind.table_rest.setItem(i, 1, item_e)
        wind.scene.addLine(x_start, y_start, 
                            x_end, y_end, wind.pen_rest)
        wind.point_now = None

    def add_cut(self):
        try:
            x = float(self.lineEdit_x_cut.text())
            y = float(self.lineEdit_y_cut.text())
            
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
        i = wind.table_cut.rowCount() - 1
        item_b = QTableWidgetItem("[{0}]".format(x))
        item_e = QTableWidgetItem("[{0}]".format(y))
        wind.table_cut.setItem(i, 0, item_b)
        wind.table_cut.setItem(i, 1, item_e)

    else:
        add_row(wind, 2)
        i = wind.table_cut.rowCount() - 1
        item_b = QTableWidgetItem("[{0}]".format(x))
        item_e = QTableWidgetItem("[{0}]".format(y))
        print(item_b, item_e)
        wind.table_cut.setItem(i, 0, item_b)
        wind.table_cut.setItem(i, 1, item_e)

        i = len(wind.rect)
        if ctrl:
            if abs(x - wind.rect[i - 1][0]) < abs(y - wind.rect[i - 1][1]):
                x = wind.rect[i - 1][0]
            elif abs(y - wind.rect[i - 1][1]) < abs(x - wind.rect[i - 1][0]):
                y = wind.rect[i - 1][1]
            ctrl = False
        wind.scene.addLine(wind.rect[i - 1][0], wind.rect[i - 1][1], 
                            x, y, wind.pen_cut)
        wind.rect.append([x, y])


# Добавить строку с координатами с таблицу
def add_row(win, f):
    if f == 1:
        win.table_rest.insertRow(win.table_rest.rowCount())
    if f == 2:
        win.table_cut.insertRow(win.table_cut.rowCount())

# Добавить точку
def add_point(point):
    global wind, ctrl, now
    x = point.x()
    y = point.y()

    if wind.input_rests:
        if (len(wind.lines)) == 0:
            wind.lines.append([point.x(), point.y()])

            add_row(wind, 1)
            i = wind.table_rest.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            wind.table_rest.setItem(i, 0, item_b)
            wind.table_rest.setItem(i, 1, item_e)

        else:
            add_row(wind, 1)
            i = wind.table_rest.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            print(item_b, item_e)
            wind.table_rest.setItem(i, 0, item_b)
            wind.table_rest.setItem(i, 1, item_e)

            x = point.x()
            y = point.y()

            i = len(wind.lines)
            if ctrl:
                if abs(point.x() - wind.lines[i - 1][0]) < abs(point.y() - wind.lines[i - 1][1]):
                    x = wind.lines[i - 1][0]
                elif abs(point.y() - wind.lines[i - 1][1]) < abs(point.x() - wind.lines[i - 1][0]):
                    y = wind.lines[i - 1][1]
                ctrl = False
            wind.scene.addLine(wind.lines[i - 1][0], wind.lines[i - 1][1], 
                               x, y, wind.pen_rest)
            wind.lines.append([x, y])

    if wind.input_cut:
        if (len(wind.rect)) == 0:
            wind.rect.append([point.x(), point.y()])

            add_row(wind, 2)
            i = wind.table_cut.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            wind.table_cut.setItem(i, 0, item_b)
            wind.table_cut.setItem(i, 1, item_e)

        else:
            add_row(wind, 2)
            i = wind.table_cut.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(point.x()))
            item_e = QTableWidgetItem("[{0}]".format(point.y()))
            print(item_b, item_e)
            wind.table_cut.setItem(i, 0, item_b)
            wind.table_cut.setItem(i, 1, item_e)

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
                               x, y, wind.pen_cut)
            wind.rect.append([x, y])


def end_cut():
    global wind, ctrl, now, end_rect_

    end_rect_ == True
    if wind.input_cut:
        print("SSSSSSSSSSSSS", len(wind.rect))
        if (len(wind.rect)) == 0:
            QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите отсекатель!")
        else:
            i = len(wind.rect)
            wind.scene.addLine(wind.rect[i - 1][0], wind.rect[i - 1][1], 
                               wind.rect[0][0], wind.rect[0][1], wind.pen_cut)

def end_rest():
    global wind, ctrl, now, end_lines_

    end_lines_ == True
    if wind.input_rests:
        print("SSSSSSSSSSSSS", len(wind.lines))
        if (len(wind.lines)) == 0:
            QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите отсекатель!")
        else:
            i = len(wind.lines)
            wind.scene.addLine(wind.lines[i - 1][0], wind.lines[i - 1][1], 
                               wind.lines[0][0], wind.lines[0][1], wind.pen_rest)


################# ДОП ПРОВЕРКА НА ВЫПУКЛОСТЬ ####################
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

    if abs(k_ab - k_cd) < 1e-6:
        return False
    x = (b_cd - b_ab) / (k_ab - k_cd)
    if d_cd == 0:
        y = (k_ab * x + b_ab) 
    elif d_ab == 0:
        y = (k_cd * x + b_cd)
    else:
        y = (k_ab * x + b_ab)

    b1 = ax
    b2 = bx
    ax = max(b1, b2)
    bx = min(b1, b2)
    b1 = ay
    b2 = by
    ay = max(b1, b2)
    by = min(b1, b2)

    if (abs(bx - x) < 1e-6) or (abs(ax - x) < 1e-6) or (abs(by - y) < 1e-6) or (abs(ay - y) < 1e-6):
        return False
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
                if f:
                    return True
            else:
                f = cross_lines(arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1],
                                arr[j][0], arr[j][1], arr[j + 1][0], arr[j + 1][1])
                if f:
                    return True

    return False

def all_polynom():
    p = QPolygonF()
    for i in wind.rect:
        new_p = QPointF(i[0], i[1])
        p.append(new_p)
    
    pen = QPen(wind.pen_cut.color())
    p_brush = QBrush(wind.color_back)
    wind.scene.addPolygon(p, pen, p_brush)
##############################################################



def scalar_mult(a, b):
    return a[0] * b[0] + a[1] * b[1]


def vector_mult(a, b):
    return a[0] * b[1] - a[1] * b[0] 
    # Ax * By - Ay * Bx --- это будет координата Z, которая нам нужна


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


def get_normal(a, b, pos):
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


def is_visible_for(point, f, s):
    v1 = [s[0] - f[0], s[1] - f[1]]
    v2 = [point[0] - f[0], point[1] - f[1]]
    if vector_mult(v1, v2) < 0:
        return False
    else:
        return True


def cross_two_segment(seg, side, normal):
    d = [seg[1][0] - seg[0][0], seg[1][1] - seg[0][1]]
    w = [seg[0][0] - side[0][0], seg[0][1] - side[0][1]]

    d_scal = scalar_mult(d, normal)
    w_scal = scalar_mult(w, normal)

    param = -w_scal / d_scal

    return [seg[0][0] +d[0] * param, seg[0][1] + d[1] * param]


def cut_side(res, side, pos):
    print("cut_side")
    ret = []

    normal = get_normal(side[0], side[1], pos)

    prev_vis = is_visible_for(res[-2], side[0], side[1])
    print(prev_vis)

    for cur_point in range(-1, len(res)):
        print(cur_point)
        cur_vis = is_visible_for(res[cur_point], side[0], side[1])
        print(cur_vis)
        if prev_vis:
            if cur_vis:
                ret.append(res[cur_point])
            else:
                ret.append(cross_two_segment([res[cur_point - 1], res[cur_point]], side, normal))
        else:
            if cur_vis:
                ret.append(cross_two_segment([res[cur_point - 1], res[cur_point]], side, normal))
                ret.append(res[cur_point])    

        prev_vis = cur_vis

    print(ret)
    return ret


def Sutherland_Hodgman():    
    figure = wind.lines
    cutter = wind.rect

    print(figure, cutter, len(cutter))

    if not is_convex(cutter):
        QMessageBox.warning(wind, "Внимание!", "Отсекатель невыпусклый!!!")
        return 

    result = figure
    for cur_point in range(-1, len(cutter) - 1):
        print(cur_point)
        result = cut_side(result, [cutter[cur_point], cutter[cur_point + 1]],
                          cutter[cur_point + 1])
        if len(result) <= 2:
            return []
    
    print("!!!!!!@@@@@@@@@@@@@@@@@@@@", result)

    draw_lines(result)
    return


####################### УДАЛЕНИЕ ЛОЖНЫХ РЕБЕР #######################
def point_in_sec(p, sec):
    a = [sec[0][0] - p[0], sec[0][1] - p[1]]
    b = [sec[0][0] - sec[1][0], sec[0][1] - sec[1][1]]
    if abs(vector_mult(a, b)) <= 1e-6:
        if (sec[0] < p < sec[1] or sec[1] < p < sec[0]):
            return True
    return False

def make_uniq(sec):
    for s in sec:
        s.sort()
    return list(filter(lambda x: (sec.count(x) % 2) == 1, sec))

def get_sect(sec, rest):
    p_list = [sec[0], sec[1]]
    for p in rest:
        if point_in_sec(p, sec):
            p_list.append(p)
    p_list.sort()

    sec_list = list()
    for i in range(len(p_list) - 1):
        sec_list.append([p_list[i], p_list[i + 1]])
    return sec_list

def remove_false_side(figure):
    all_sections = list()
    rest = figure[2:]
    for i in range(len(figure)):
        cur_section = [figure[i], figure[(i + 1) % len(figure)]]

        all_sections.extend(get_sect(cur_section, rest))

        rest.pop(0)
        rest.append(figure[i])

    return make_uniq(all_sections)
#####################################################################


def draw_section(xb, yb, xe, ye):
    global wind
    pen = QtGui.QPen(wind.color_back)
    wind.scene.addLine(xb, yb, xe, ye, pen)
    wind.scene.addLine(xb, yb, xe, ye, wind.pen_res)


def draw_lines(figure):
    global wind
    try:
        w = int(wind.spinBox_w.text())
    except Exception:
        QMessageBox.warning(wind, "Внимание!", "Не целове значение толщины!")
        return 
    print(figure, "\n\n\n")
    wind.pen_res.setWidth(w)
    for section in remove_false_side(figure):
        draw_section(round(section[0][0]), round(section[0][1]), round(section[1][0]), round(section[1][1]))


def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()