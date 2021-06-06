import sys
import win2
from math import pi, sin, cos
from func import *


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt



wind = None

class Visual(QtWidgets.QMainWindow, win2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.h = self.graphicsView.height()
        self.w = self.graphicsView.width()
        print(self.w, self.h)
        self.scene.setSceneRect(0, 0, self.w-2, self.h-2)
        self.image = QImage(self.w, self.h, QImage.Format_RGB30)
        self.image.fill(Qt.white)
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
        self.alpha_x = 0
        self.alpha_y = 0
        self.alpha_z = 0
        self.color_back = QtCore.Qt.white
        self.flag_scale_or_not = False
        self.color_res = QtCore.Qt.red

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
        self.pushButton_x_turn.clicked.connect(self.turn_x1)
        self.pushButton_y_turn.clicked.connect(self.turn_y1)
        self.pushButton_z_turn.clicked.connect(self.turn_z1)
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
        self.alpha_x = 0
        self.alpha_y = 0
        self.alpha_z = 0

    def set_black_res(self):
        self.pen_res.setColor(QtCore.Qt.black)
        self.color_res = QtCore.Qt.black

    def set_white_res(self):
        self.pen_res.setColor(QtCore.Qt.white)
        self.color_res = QtCore.Qt.white
    
    def set_blue_res(self):
        self.pen_res.setColor(QtCore.Qt.blue)
        self.color_res = QtCore.Qt.blue

    def set_red_res(self):
        self.pen_res.setColor(QtCore.Qt.red)
        self.color_res = QtCore.Qt.red

    def set_green_res(self):
        self.pen_res.setColor(QtCore.Qt.green)
        self.color_res = QtCore.Qt.green

    def set_yellow_res(self):
        self.pen_res.setColor(QtCore.Qt.yellow)
        self.color_res = QtCore.Qt.yellow

    # Поворот вокруг Х
    def turn_x1(self):
        try:
            alpha = float(self.lineEdit_x_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Неверное значение угла поворота X")
            return
        self.alpha_x += alpha
        self.alpha_y += 0
        self.alpha_z += 0
        self.draw_res()

    # Поворот вокруг У
    def turn_y1(self):
        try:
            alpha = float(self.lineEdit_y_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!", 
                                "Неверное значение угла поворота Y")
            return
        self.alpha_x += 0
        self.alpha_y += alpha
        self.alpha_z += 0
        self.draw_res()
        
    # Поворот вокруг Z
    def turn_z1(self):
        try:
            alpha = float(self.lineEdit_z_turn.text())
        except Exception:
            QMessageBox.warning(wind, "Внимание!",
                              "Неверное значение угла поворота Z")
            return
        self.alpha_x += 0 
        self.alpha_y += 0
        self.alpha_z += alpha
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

        except Exception:
            QMessageBox.warning(wind, "Внимание!",
                               "Неверное значение параметров X и Z")
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

    def draw_res(self):

        print("draw_res", self.alpha_x, self.alpha_y, self.alpha_z)
        self.scene.clear()
        self.image.fill(QtCore.Qt.white)
        # f = funcs[self.number_func]

        self.read_x_z_value()

        self.image = self.float_horizon()

        p = QPixmap()
        p.convertFromImage(self.image)
        self.scene.addPixmap(p)


    def float_horizon(self):
        print("float_hor")
        # для удобства использования
        func = funcs[self.number_func]
        alpha_x = self.alpha_x
        alpha_y = self.alpha_y
        alpha_z = self.alpha_z

        x_min = self.x_begin
        x_max = self.x_end
        x_step = self.x_step

        z_min = self.z_begin
        z_max = self.z_end
        z_step = self.z_step

        # инициализация для боковых ребер
        x_r = -1
        y_r = -1
        x_l = -1
        y_l = -1

        # инициализация массивов горизонта
        hight_hor = {x: 0 for x in range(0, int(self.w) + 1)}
        low_hor = {x: self.h for x in range(0, int(self.w) + 1)}

        z = z_max
        print(z, z_min)
        while z >= z_min:
            print("z", z)
            z_buf = z
            x_prev = x_min
            y_prev = func(x_min, z)
            x_prev, y_prev, z_buf = transform(x_prev, y_prev, z,
                                              alpha_x, alpha_y, alpha_z, 
                                              self.scale_k, self.w, self.h)

            if x_l != -1:
                # if not is_visible([x_l, y_l]) or not is_visible([x_prev, y_prev]):
                #     z -= z_step
                #     continue
                hight_hor, low_hor = horizon(x_prev, y_prev, x_l, y_l,
                                             hight_hor, low_hor, 
                                             self.image)
            x_l = x_prev
            y_l = y_prev

            x = x_min
            while x <= x_max:
                print("x", x)
                y = func(x, z)
                x_cur, y_cur, z_buf = transform(x, y, z, alpha_x, alpha_y, alpha_z,
                                                self.scale_k, self.w, self.h)
                # if not is_visible([x_cur, y_cur]) or not  is_visible([x_prev, y_prev]):
                #     x += x_step
                #     continue
                hight_hor, low_hor = horizon(x_prev, y_prev, x_cur, y_cur, hight_hor, low_hor, self.image)
                x_prev = x_cur
                y_prev = y_cur

                x += x_step

            if z != z_max:
                x_r = x_max
                y_r = func(x_max, z - z_step)
                x_r, y_r, z_buf = transform(x_r, y_r, z - z_step, alpha_x, alpha_y, alpha_z, self.scale_k, self.w, self.h)
                # if not is_visible([x_r, y_r]) or not is_visible([x_prev, y_prev]):
                #     x += x_step
                #     continue
                hight_hor, low_hor = horizon(x_prev, y_prev, x_r, y_r, hight_hor, low_hor, self.image)

            z -= z_step

        return self.image

def sign(x):
    if not x:
        return 0
    else:
        return x / abs(x)

# Проверка точки на видимость
def is_visible(point):
    return 0 <= point[0] < wind.w  - 1 and 0 <= point[1] < wind.h - 1



def horizon(x1, y1, x2, y2, hh, lh, image):
    if  x1 < 0 or x1 > image.width() or x2 < 0 or x2 > image.width():
        return hh, lh
    print("hor x1", x1)
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    s_x = sign(dx)
    s_y = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    print("dx == 0 and dy == 0 and 0 <= x < image.width()", dx == 0 and dy == 0 and 0 <= x < image.width())
    if dx == 0 and dy == 0 and 0 <= x < image.width():
        if y >= hh[x]:
            hh[x] = y
            image.setPixelColor(x, image.height() - y, wind.color_res)
        if y <= lh[x]:
            lh[x] = y
            image.setPixelColor(x, image.height() - y, wind.color_res)
        return hh, lh
    flag = 0
    if dy > dx:
        dx, dy = dy, dx
        flag = 1
    y_max_cur = hh[x]
    y_min_cur = lh[x]

    e = 2 * dy - dx
    i = 1
    while i <= dx:
        if 0 <= x < image.width():
            if y >= hh[x]:
                if y >= y_max_cur:
                    y_max_cur = y
                image.setPixelColor(x, image.height() - y, wind.color_res)
            if y <= lh[x]:
                if y <= y_min_cur:
                    y_min_cur = y
                image.setPixelColor(x, image.height() - y, wind.color_res)
        if e >= 0:
            if flag:
                hh[x] = y_max_cur
                lh[x] = y_min_cur
                x += s_x
                y_max_cur = hh[x]
                y_min_cur = lh[x]
            else:
                y += s_y
            e -= 2 * dx
        if e < 0:
            if not flag:
                hh[x] = y_max_cur
                lh[x] = y_min_cur
                x += s_x
                y_max_cur = hh[x]
                y_min_cur = lh[x]
            else:
                y += s_y
            e += 2 * dy
        i += 1
    return hh, lh



def turn_x(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = y
    y = cos(alpha) * y - sin(alpha) * z
    z = cos(alpha) * z + sin(alpha) * buf
    return x, y, z
        

def turn_y(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = x
    x = cos(alpha) * x - sin(alpha) * z
    z = cos(alpha) * z + sin(alpha) * buf
    return x, y, z


def turn_z(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = x
    x = cos(alpha) * x - sin(alpha) * y
    y = cos(alpha) * y + sin(alpha) * buf
    return x, y, z


def transform(x, y, z, alpha_x, alpha_y, alpha_z, scale_k, w, h):
    print("transform", scale_k, w, h)
    x, y, z = turn_x(x, y, z, alpha_x)
    x, y, z = turn_y(x, y, z, alpha_y)
    x, y, z = turn_z(x, y, z, alpha_z)
    print(x, y, z)
    x = x * scale_k + w / 2 
    y = y * scale_k + h / 2 
    print("transform end", x, y, z)
    return round(x), round(y), round(z)


def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()