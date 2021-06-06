

import sys
import win2
from math import pi, sin, cos, sqrt
from func import *
from numpy import arange


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt



wind = None

class Visual(QtWidgets.QMainWindow, win2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.graphicsView.scale(1, 1)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.h = self.graphicsView.height()
        self.w = self.graphicsView.width()
        print(self.w, self.h)
        # self.scene.setSceneRect(-w/2, -h/2, w-2, h-2)
        self.scene.setSceneRect(0, 0, self.w-2, self.h-2)
        # self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        # self.image.fill(Qt.white)
        # self.scene.setSceneRect(0, 0, w-2, h-2)
        self.pen_res = QtGui.QPen(QtCore.Qt.red)
        self.pen_res.setWidth(0)
        
        self.scale_k = 45
        self.x_begin = -10
        self.x_end = 10
        self.z_begin = -10
        self.z_end = 10
        self.x_step = 0.5
        self.z_step = 0.5
        self.number_func = 0
        self.trans_matrix = [[int(i == j) for i in range(4)] for j in range(4)]
        self.clip = None
        self.point_now = None
        self.color_back = QtCore.Qt.white
        self.flag_scale_or_not = False
        self.angles = [0, 0, 0]

        self.radioButton_func_1.clicked.connect(self.set_number_func_0)
        self.radioButton_func_2.clicked.connect(self.set_number_func_1)
        self.radioButton_func_3.clicked.connect(self.set_number_func_2)
        self.radioButton_func_4.clicked.connect(self.set_number_func_3)
        self.radioButton_func_5.clicked.connect(self.set_number_func_4)
        self.radioButton_func_6.clicked.connect(self.set_number_func_5)

        self.radioButtonBlack_res.clicked.connect(self.set_black_res)
        self.radioButtonBlue_res.clicked.connect(self.set_blue_res)
        self.radioButtonGreen_res.clicked.connect(self.set_green_res)
        self.radioButtonRed_res.clicked.connect(self.set_red_res)
        self.radioButtonWhite_res.clicked.connect(self.set_white_res)
        self.radioButtonYellow_res.clicked.connect(self.set_yellow_res)

        self.pushButton_k.clicked.connect(self.scale)
        self.pushButton_x_turn.clicked.connect(self.turn_x)
        self.pushButton_y_turn.clicked.connect(self.turn_y)
        self.pushButton_z_turn.clicked.connect(self.turn_z)
        self.pushButton_clean.clicked.connect(self.clean_screen)
        
        self.pushButton_RES.clicked.connect(self.draw_res)


    def set_number_func_0(self):
        self.number_func = 0
    def set_number_func_1(self):
        self.number_func = 1
    def set_number_func_2(self):
        self.number_func = 2
    def set_number_func_3(self):
        self.number_func = 3
    def set_number_func_4(self):
        self.number_func = 4
    def set_number_func_5(self):
        self.number_func = 5

    def clean_screen(self):
        self.scene.clear()
        self.trans_matrix = [[int(i == j) for i in range(4)] for j in range(4)]
        self.flag_scale_or_not = False
        self.angles = [0, 0, 0]

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


    # Рисование линии
    def my_draw_line(self, xb, yb, xe, ye):
        self.scene.addLine(xb, yb, xe, ye, self.pen_res)


    # Поворот вокруг Х
    def turn_x(self):
        try:
            alpha = float(self.lineEdit_x_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение угла поворота X")
            return
        alpha = alpha / 180 * pi
        reform_m = [[1, 0, 0, 0],
                    [0, cos(alpha), sin(alpha), 0], 
                    [0, -sin(alpha), cos(alpha), 0], 
                    [0, 0, 0, 1]]
        reform_matrix(reform_m)
        self.draw_res()

    # Поворот вокруг У
    def turn_y(self):
        try:
            alpha = float(self.lineEdit_y_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение угла поворота Y")
            return
        alpha = alpha / 180 * pi
        reform_m = [[cos(alpha), -sin(alpha), 0, 0],
                    [0, 1, 0, 0], 
                    [sin(alpha), cos(alpha), 1, 0], 
                    [0, 0, 0, 1]]
        reform_matrix(reform_m)
        self.draw_res()
        
    # Поворот вокруг Z
    def turn_z(self):
        try:
            alpha = float(self.lineEdit_z_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение угла поворота Z")
            return
        alpha = alpha / 180 * pi
        reform_m = [[cos(alpha), sin(alpha), 0, 0],
                    [-sin(alpha), cos(alpha), 0, 0], 
                    [0, 0, 1, 0], 
                    [0, 0, 0, 1]]
        reform_matrix(reform_m)
        self.draw_res()

    # Масштабирование
    def scale(self):
        try:
            sc_k = float(self.lineEdit_k.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение масштаба")
            return

        self.scale_k = sc_k
        self.flag_scale_or_not = True
        self.draw_res()
    
    # Чтение значений начала конца и шага по оси X и Z
    def read_x_z_value(self):
        print(self.flag_scale_or_not)
        try:
            x_b = float(self.lineEdit_x_begin.text())
            x_e = float(self.lineEdit_x_end.text())
            x_s = float(self.lineEdit_x_step.text())

            z_b = float(self.lineEdit_z_begin.text())
            z_e = float(self.lineEdit_z_end.text())
            z_s = float(self.lineEdit_z_step.text())

            # if self.flag_scale_or_not == False:
            #     f = funcs[self.number_func]
            #     y2 = max(f(x_b, z_b), f(x_b, z_e), f(x_e, z_b), f(x_e, z_e))
            #     y1 = min(f(x_b, z_b), f(x_b, z_e), f(x_e, z_b), f(x_e, z_e))
            #     k1 = int(self.h / (y2 - y1)) - 1
            #     k2 = int(self.w / (x_e - x_b)) - 1
            #     self.scale_k = min(k1, k2)
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение параметров X и Z")
            return
        if self.flag_scale_or_not == False:
                f = funcs[self.number_func]
                y2 = max(f(x_b, z_b), f(x_b, z_e), f(x_e, z_b), f(x_e, z_e))
                y1 = min(f(x_b, z_b), f(x_b, z_e), f(x_e, z_b), f(x_e, z_e))
                print(y1, y2, "y1 and y2")
                if abs(y2 - y1) < 1e-6:
                    k1 = 48
                else:
                    k1 = int(self.h / (y2 - y1)) - 1
                
                k2 = int(self.w / (x_e - x_b)) - 1
                print(k1, k2)
                self.scale_k = min(k1, k2)
        self.x_begin = int(x_b)
        self.x_end = int(x_e)
        self.x_step = x_s

        self.z_begin = int(z_b)
        self.z_end = int(z_e)
        self.z_step = z_s

        # self.angles = [alpha, alpha1, alpha2]

    # Рисование точки
    def draw_point(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen_res)


    # Рисование результата
    def draw_res(self):
        
        # self.lineEdit_k.setText(strr)
        print("DRAW_RES", self.w / (self.x_end - self.x_begin))
        self.scene.clear()
        self.read_x_z_value()

        draw_func = funcs[self.number_func]

        hight_hor = [0 for i in range(self.w)]
        low_hor = [self.h for i in range(self.w)]


        # z = self.z_end
        # while z >= self.z_begin - self.z_step / 2:
        #     print("z", z)
        #     x_prev = self.x_begin
        #     y_prev = draw_func(self.x_begin, z)

        #     # point = reform_point([x_prev, y_prev, z])
        #     # x_prev = point[0]
        #     # y_prev = point[1]
        #     x_prev, y_prev = transform(x_prev, y_prev, z, self.angles)

        #     flag_prev = visible(x_prev, y_prev, hight_hor, low_hor)

        #     x = self.x_begin
        #     while x <= self.x_end + self.x_step / 2:
        #         print("x", x)
        #         y_cur = draw_func(x, z)
        #         # point1 = reform_point([x, y_cur, z])
        #         # x_cur = point1[0]
        #         # y_cur = point1[1]
        #         x_cur, y_cur = transform(x, y_cur, z, self.angles)


        #         flag_cur = visible(x_cur, y_cur, hight_hor, low_hor)

        #         if flag_prev == flag_cur:
        #             if flag_cur != 0:
        #                 self.scene.addLine(x_prev, y_prev, x_cur, y_cur, self.pen_res)
        #                 hight_hor, low_hor = new_hor(x_prev, y_prev, x_cur, y_cur, hight_hor, low_hor)
        #         else:
        #             if flag_cur == 0:
        #                 if flag_prev == 1:
        #                     xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, hight_hor)
        #                 else:
        #                     xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, low_hor)
        #                 self.scene.addLine(x_prev, y_prev, xi, yi, self.pen_res)        
        #                 hight_hor, low_hor = new_hor(x_prev, y_prev, xi, yi, hight_hor, low_hor)
        #             else:
        #                 if flag_cur == 1:
        #                     if flag_prev == 0:
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, hight_hor)
        #                         self.scene.addLine(xi, yi, x_cur, y_cur, self.pen_res)
        #                         hight_hor, low_hor = new_hor(xi, yi, x_cur, y_cur, hight_hor, low_hor)
        #                     else:
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, low_hor)
        #                         self.scene.addLine(x_prev, y_prev, xi, yi)
        #                         hight_hor, low_hor = new_hor(x_prev, y_prev, xi, yi, hight_hor, low_hor)
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, hight_hor)
        #                         self.scene.addLine(xi, yi, x_cur, y_cur, self.pen_res)
        #                         hight_hor, low_hor = new_hor(xi, yi, x_cur, y_cur, hight_hor, low_hor)
        #                 else:       
        #                     if flag_prev == 0:
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, low_hor)
        #                         self.scene.addLine(xi, yi, x_cur, y_cur, self.pen_res)
        #                         hight_hor, low_hor = new_hor(xi, yi, x_cur, y_cur, hight_hor, low_hor)
        #                     else:
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, hight_hor)
        #                         self.scene.addLine(x_prev, y_prev, xi, yi, self.pen_res)
        #                         hight_hor, low_hor = new_hor(x_prev, y_prev, xi, yi, hight_hor, low_hor)
        #                         xi, yi = intersection(x_prev, y_prev, x_cur, y_cur, low_hor)
        #                         self.scene.addLine(xi, yi, x_cur, y_cur, self.pen_res)
        #                         hight_hor, low_hor = new_hor(xi, yi, x_cur, y_cur, hight_hor, low_hor)
        #         x_prev, y_prev = x_cur, y_cur
        #         flag_prev =  flag_cur
        #         x += self.x_step
        #         print("x_end", x)
        #     z -= self.z_step
        
        
        
        array_z = arange(self.z_end, self.z_begin - self.z_step, -self.z_step)

        for z in array_z:
            draw_hor(draw_func, hight_hor, low_hor,
                     self.x_begin, self.x_end,
                     self.x_step, z)

        array_z = arange(self.z_end - self.z_step, self.z_begin - self.z_step, -self.z_step)
        for z in array_z:
            point1 = reform_point([self.x_begin, 
                                   draw_func(self.x_begin, z), 
                                   z])
            point2 = reform_point([self.x_begin, 
                                   draw_func(self.x_begin, z + self.z_step), 
                                   z + self.z_step])
            self.scene.addLine(point1[0], point1[1], 
                               point2[0], point2[1], 
                               self.pen_res)
            
            point1 = reform_point([self.x_end, 
                                   draw_func(self.x_end, z), 
                                   z])
            point2 = reform_point([self.x_end, 
                                   draw_func(self.x_end, z + self.z_step), 
                                   z + self.z_step])
            self.scene.addLine(point1[0], point1[1], 
                               point2[0], point2[1], 
                               self.pen_res)
        

def scale(x, y):
    x *= wind.scale_k
    y *= wind.scale_k
    x += wind.w // 2
    y += wind.h // 2 # - y
    return round(x), round(y)
    
def convers(arg):
    return arg * pi / 180


def rotateX(x, y, z, angle):
    angle = convers(angle)
    y = cos(angle) * y - sin(angle) * z
    return x, y


def rotateY(x, y, z, angle):
    angle = convers(angle)
    x = cos(angle) * x - sin(angle) * z
    return x, y


def rotateZ(x, y, z, angle):
    angle = convers(angle)
    buf = x
    x = cos(angle) * x - sin(angle) * y
    y = cos(angle) * y + sin(angle) * buf
    return x, y


def transform(x, y, z, angles):
    x, y = rotateX(x, y, z, angles[0])
    x, y = rotateY(x, y, z, angles[1])
    x, y = rotateZ(x, y, z, angles[2])
    return scale(x, y)



# Подпрограмма вычисляет пересечение с горизонтом.
def intersection(x1, y1, x2, y2, arr):
    dx = x2 - x1
    dyc = y2 - y1
    dyp = arr[x2] - arr[x1]
    if dx == 0:
        xi = x2
        yi = arr[x2]
        return xi, yi
    if y1 == arr[x1] and y2 == arr[x2]:
        return x1, y1
    m = dyc / dx
    xi = x1 - round(dx * (y1 - arr[x1]) / (dyc - dyp))
    yi = round((xi - x1) * m + y1)
    return xi, yi

def new_hor(x1, y1, x2, y2, hh, lh):
    if x2 - x1 == 0:
        hh[int(x2)] = max(hh[int(x2)], y2)
        lh[int(x2)] = min(lh[int(x2)], y2)
        return hh, lh

    m = (y2-y1) / (x2-x1)

    for x in range(x1, x2 + 1):
        y = round(m *(x-x1) + y1)
        hh[int(x)] = max(hh[int(x)], y)
        lh[int(x)] = min(lh[int(x)], y)
    
    return hh, lh
        
def visible(x, y, hh, lh):  # Visible point
    # Если точка, ниже нижнего горизонта (или на нем)
    # То она видима. 
    if y <= lh[int(x)]:
        return -1
    # Если точка выше верхнего горизонта (или на нем)
    # То она видима.
    if y >= hh[int(x)]:  
        return 1
    # Иначе она невидима.
    return 0


# Трансформация матрицы
def reform_matrix(reform_m):
    global wind
    res_matrix = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += wind.trans_matrix[i][k] * reform_m[k][j]

    wind.trans_matrix = res_matrix

# Трансформация точки
def reform_point(point):
    point.append(1)
    res_point = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            res_point[i] += point[j] * wind.trans_matrix[j][i]
    print(res_point)
    for i in range(3):
        res_point[i] *= wind.scale_k
    
    print("DDDDDDDDDDDDD", res_point)
    res_point[0] += wind.w / 2
    res_point[1] += wind.h / 2
    print("DDDDDDDDDDDDDDDDDDDDDDDDD", res_point)
    res_point.pop(3)
    res_point[0] = round(res_point[0])
    res_point[1] = round(res_point[1])
    return res_point

# Надо ли рисовать точку или нет, если надо, то отрисовка
def need_draw_point(x, y, hight, low):
    if not is_visible([x, y]):
        return False

    if y > hight[x]:
        hight[x] = y
        wind.draw_point(x, y)

    if y < low[x]:
        low[x] = y
        wind.draw_point(x, y)
    return True

# Проверка точки на видимость
def is_visible(point):
    return 0 <= point[0] < wind.w and 0 <= point[1] < wind.h

# РИсование видимой части кривой
def draw_visirble_part_of_hor(hight_hor, low_hor, point1, point2):
    # рисовать для удобства слева направо

    if point2[0] < point1[0]:
        point1, point2 = point2, point1
    
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    if dx > dy:
        param = dx
    else:
        param = dy

    dx = dx / param
    dy = dy / param

    x_cur = point1[0]
    y_cur = point1[1]

    for i in range(int(param) + 1):
        if not need_draw_point(int(round(x_cur)), y_cur, hight_hor, low_hor):
            return
        x_cur += dx
        y_cur += dy


# Рисование горизонта очередного
def draw_hor(func, hight_hor, low_hor, xb, xe, xs, z):
    array_x = arange(xb, xe + xs, xs)
    prev = None

    for x in array_x:
        y = func(x, z)
        cur = reform_point([x, y, z])
        if prev:
            draw_visirble_part_of_hor(hight_hor, low_hor, prev, cur)
        prev = cur



def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()