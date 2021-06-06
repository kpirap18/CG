import sys
import win2

from cut import *
from copy import deepcopy

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt

ERROR_CUTTER_ISNOT_CONVEX = -1
ERROR_CUTTER_IS_LINE = -2
ERROR_REST_ISNOT_POLYGON = -3
ERROR_REST_IS_LINE = -4
OK = 0
EPS = 1e-6

now = None
end_rect_ = False
end_lines_ = False
ctrl = False
wind = None

class Scene(QtWidgets.QGraphicsScene):
    
    def keyPressEvent(self, event):
        global ctrl
        if event.key() == Qt.Key_Control:
            ctrl = True
        else:
            ctrl = False

    # добавить точку по щелчку мыши
    def mousePressEvent(self, QMouseEvent):
        if ((QMouseEvent.button() == Qt.LeftButton) and (end_rect_ == False or end_lines_ == False)):
            print("nenm")
            point = QMouseEvent.scenePos()
            x = round(point.x())
            y = round(point.y())
            # reform_point(x, y)
            wind.add_point(x, y)
        
        if (QMouseEvent.button() == Qt.RightButton):
            wind.end_p()

        # if (QMouseEvent.button() == Qt.MidButton):
        #     if wind.input_rests:
        #         reform_point(QMouseEvent.scenePos())
        #     else:
        #         QMessageBox.warning(self, "Внимание!",
        #          "Это можно использовать только при вводе отсекаемого многоугольника!!!")




               


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
        self.pen_res_out = QtGui.QPen(QtCore.Qt.blue)
        self.pen_res_out.setWidth(0)
        self.input_cut = False
        self.input_rests = True

        self.count_rest_in = 0
        self.count_cut_in = 0
        self.rest_in = [[]]
        self.rest_out = []
        self.cut_in = [[]]
        self.cut_out = []

        self.clip = None
        self.point_now = None
        self.color_back = QtCore.Qt.white

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

        self.pushButton_RES.clicked.connect(self.my_cut)

        self.pushButton_add.clicked.connect(self.before_add_point)

    def clean_screen(self):
        global now, end_rect_, end_lines_

        self.scene.clear()
        self.count_rest_in = 0
        self.count_cut_in = 0
        self.rest_in = [[]]
        self.rest_out = []
        self.cut_in = [[]]
        self.cut_out = []
        self.image.fill(Qt.white)


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

    
    # Добавить точку 
    def add_point(self, x, y):
        x = round(x)
        y = round(y)

        # Многоугольник внешний
        if self.radioButton_draw_rest_out.isChecked():
            if len(self.rest_out) >= 2:
                if (self.rest_out[0] == self.rest_out[len(self.rest_out) - 1]):
                    QMessageBox.warning(wind, "Внимание!", "Внешний многоугольник замкнут!!!")
                    return
            self.rest_out.append([x, y])

            if len(self.rest_out) >= 2:
                l = len(self.rest_out) - 1
                self.scene.addLine(self.rest_out[l - 1][0], 
                                   self.rest_out[l - 1][1],
                                   self.rest_out[l][0], 
                                   self.rest_out[l][1],
                                   self.pen_rest)

        
        # Многоугольник внутренний
        if self.radioButton_draw_rest_in.isChecked():
            if (len(self.rest_in[self.count_rest_in]) >= 2):
                if (self.rest_in[self.count_rest_in][0] == self.rest_in[self.count_rest_in][len(self.rest_in[self.count_rest_in]) - 1]):
                    self.count_rest_in += 1
                    self.rest_in.append([])

            self.rest_in[self.count_rest_in].append([x, y])

            if len(self.rest_in[self.count_rest_in]) >= 2:
                l = len(self.rest_in[self.count_rest_in]) - 1
                self.scene.addLine(self.rest_in[self.count_rest_in][l - 1][0], 
                                   self.rest_in[self.count_rest_in][l - 1][1],
                                   self.rest_in[self.count_rest_in][l][0], 
                                   self.rest_in[self.count_rest_in][l][1],
                                   self.pen_rest)

            


        # Отсекатель внешний
        if self.radioButton_draw_cut_out.isChecked():
            if len(self.cut_out) >= 2:
                if (self.cut_out[0] == self.cut_out[len(self.cut_out) - 1]):
                    QMessageBox.warning(wind, "Внимание!", "Внешний отсекатель замкнут!!!")
                    return
            self.cut_out.append([x, y])

            if len(self.cut_out) >= 2:
                l = len(self.cut_out) - 1
                self.scene.addLine(self.cut_out[l - 1][0], 
                                   self.cut_out[l - 1][1],
                                   self.cut_out[l][0], 
                                   self.cut_out[l][1],
                                   self.pen_cut)

        # Отсекатель внутренний
        if self.radioButton_draw_cut_in.isChecked():
            if (len(self.cut_in[self.count_cut_in]) >= 2):
                if (self.cut_in[self.count_cut_in][0] == self.cut_in[self.count_cut_in][len(self.cut_in[self.count_cut_in]) - 1]):
                    self.count_cut_in += 1
                    self.cut_in.append([])

            self.cut_in[self.count_cut_in].append([x, y])

            if len(self.cut_in[self.count_cut_in]) >= 2:
                l = len(self.cut_in[self.count_cut_in]) - 1
                self.scene.addLine(self.cut_in[self.count_cut_in][l - 1][0], 
                                   self.cut_in[self.count_cut_in][l - 1][1],
                                   self.cut_in[self.count_cut_in][l][0], 
                                   self.cut_in[self.count_cut_in][l][1],
                                   self.pen_cut)

    def before_add_point(self):
        print("before_add_point")
        try:
            x = float(self.lineEdit_x.text())
            y = float(self.lineEdit_y.text())
            print(x, y)
        except Exception:
            QMessageBox.warning(wind, "Внимание!", "Невено введены координаты!")
            return
        x = round(x)
        y = round(y)

        self.add_point(x, y)

    # замыкание
    def end_p(self):
        # Многоугольник внешний
        if self.radioButton_draw_rest_out.isChecked():
            if len(self.rest_out) < 3:
                QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите многоугольник (хотя бы 3 точки)!")
                return
            self.rest_out.append([self.rest_out[0][0], self.rest_out[0][1]])

            if len(self.rest_out) >= 2:
                l = len(self.rest_out) - 1
                self.scene.addLine(self.rest_out[l - 1][0], 
                                   self.rest_out[l - 1][1],
                                   self.rest_out[l][0], 
                                   self.rest_out[l][1],
                                   self.pen_rest)
        
        # Многоугольник внутренний
        if self.radioButton_draw_rest_in.isChecked():
            if len(self.rest_in[self.count_rest_in]) < 3:
                QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите многоугольник (хотя бы 3 точки)!")
                return
            self.rest_in[self.count_rest_in].append([self.rest_in[self.count_rest_in][0][0], self.rest_in[self.count_rest_in][0][1]])

            if len(self.rest_in[self.count_rest_in]) >= 2:
                l = len(self.rest_in[self.count_rest_in]) - 1
                self.scene.addLine(self.rest_in[self.count_rest_in][l - 1][0], 
                                   self.rest_in[self.count_rest_in][l - 1][1],
                                   self.rest_in[self.count_rest_in][l][0], 
                                   self.rest_in[self.count_rest_in][l][1],
                                   self.pen_rest)


        # Отсекатель внешний
        if self.radioButton_draw_cut_out.isChecked():
            if len(self.cut_out) < 3:
                QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите отсекатель (хотя бы 3 точки)!")
                return
            self.cut_out.append([self.cut_out[0][0], self.cut_out[0][1]])

            if len(self.cut_out) >= 2:
                l = len(self.cut_out) - 1
                self.scene.addLine(self.cut_out[l - 1][0], 
                                   self.cut_out[l - 1][1],
                                   self.cut_out[l][0], 
                                   self.cut_out[l][1],
                                   self.pen_cut)

        # Отсекатель внутренний
        if self.radioButton_draw_cut_in.isChecked():
            if len(self.cut_in[self.count_cut_in]) < 3:
                QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите многоугольник (хотя бы 3 точки)!")
                return
            self.cut_in[self.count_cut_in].append([self.cut_in[self.count_cut_in][0][0], self.cut_in[self.count_cut_in][0][1]])

            if len(self.cut_in[self.count_cut_in]) >= 2:
                l = len(self.cut_in[self.count_cut_in]) - 1
                self.scene.addLine(self.cut_in[self.count_cut_in][l - 1][0], 
                                   self.cut_in[self.count_cut_in][l - 1][1],
                                   self.cut_in[self.count_cut_in][l][0], 
                                   self.cut_in[self.count_cut_in][l][1],
                                   self.pen_cut)


    #################################################################
    # Вызов отсекающей функции
    def my_cut(self):
        a = deepcopy(self.rest_out)
        c = deepcopy(self.cut_out)
        a_b = deepcopy(self.rest_in)
        c_b = deepcopy(self.cut_in)
        print(a, c, a_b, c_b)

        a.pop(len(a) - 1)
        c.pop(len(c) - 1)
        
        for i in range(len(a_b)):
            aab = a_b[i]
            if len(aab):
                aab.pop(len(aab) - 1)
        for i in range(len(c_b)):
            ccb = c_b[i]
            if len(ccb):
                ccb.pop(len(ccb) - 1)
            
        for i in range(len(a)):
            a[i].append(0)
        for i in range(len(c)):
            c[i].append(1)

        for i in range(len(a_b)):
            aab = a_b[i]
            for j in range(len(aab)):
                aab[j].append(0)
        for i in range(len(c_b)):
            ccb = c_b[i]
            for j in range(len(ccb)):
                ccb[j].append(1)

        # a = [[90, 30, 0], [150, 30, 0], [120, 90, 0], [170, 130, 0], [90, 130, 0]]
        # a_b = [[[100, 120, 0], [130, 120, 0], [110, 100, 0]]]

        # c = [[60, 50, 1], [170, 50, 1], [110, 110, 1], [130, 160, 1], [30, 160, 1]]
        # c_b = [[[70, 80, 1], [110, 80, 1], [100, 60, 1]]]

        # c = [[40, 40, 0], [140, 40, 0], [90, 120, 0]]
        # c_b = [[]]

        # a = [[90, 60, 1], [170, 50, 1], [130, 120, 1]]
        # a_b = [[]]

        print("\n\n")
        print("a", a)
        print("a_b", a_b)
        print("c", c)
        print("c_b", c_b)
        print("\n\n")
        rc, res_in, res_out = alg_cutter_baylera_azertona(a, c, a_b, c_b)
        print("IN MAIN.PY", res_in, res_out)
        draw_lines1(a, 0)
        for i in range(len(a_b)):
            draw_lines1(a_b[i], 0)
        draw_lines1(c, 1)
        for i in range(len(c_b)):
            draw_lines1(c_b[i], 1)

        if self.radioButton_draw_out.isChecked():
            for i in range(len(res_out)):
                draw_lines1(res_out[i], 3)
        if self.radioButton_draw_in.isChecked():
            for i in range(len(res_in)):
                draw_lines1(res_in[i], 2)





# Добавить строку с координатами с таблицу
def add_row(win, f):
    if f == 1:
        win.table_rest.insertRow(win.table_rest.rowCount())
    if f == 2:
        win.table_cut.insertRow(win.table_cut.rowCount())



            
def end_cut():
    global wind, ctrl, now, end_rect_

    end_rect_ = True
    if wind.input_cut:
        if (len(wind.rect)) == 0:
            QMessageBox.warning(wind, "Внимание!", "Чтобы замкнуть, введите отсекатель!")
        else:
            i = len(wind.rect)
            wind.scene.addLine(wind.rect[i - 1][0], 
                               wind.rect[i - 1][1], 
                               wind.rect[0][0], 
                               wind.rect[0][1],
                                wind.pen_cut)

def end_rest():
    global wind, ctrl, now, end_lines_

    end_lines_ = True
    if wind.input_rests:
        if (len(wind.lines)) == 0:
            QMessageBox.warning(wind, "Внимание!", 
                                "Чтобы замкнуть, введите отсекатель!")
        else:
            i = len(wind.lines)
            wind.scene.addLine(wind.lines[i - 1][0],
                               wind.lines[i - 1][1], 
                               wind.lines[0][0], 
                               wind.lines[0][1], 
                               wind.pen_rest)


def reform_point(x, y):
    global wind


    point = [x, y]
    
    min_dist = 15 + 2
    closest_point = None
    if len(wind.cut_out) > 1:
        for i in range(len(wind.cut_out) - 1):
            cur_dist, cur_closest = dist_to_edge(point, 
                                                 wind.cut_out[i], 
                                                 wind.cut_out[i + 1])
            if cur_dist < min_dist:
                min_dist = cur_dist
                closest_point = cur_closest
        cur_dist, cur_closest = dist_to_edge(point, 
                                             wind.cut_out[1], 
                                             wind.cut_out[-1])
        
        if cur_dist < min_dist:
            min_dist = cur_dist
            closest_point = cur_closest

    for j in range(len(wind.cut_in)):
        if len(wind.cut_in[j]) > 1:
            for i in range(len(wind.cut_in[j]) - 1):
                cur_dist, cur_closest = dist_to_edge(point, 
                                                    wind.cut_in[j][i], 
                                                    wind.cut_in[j][i + 1])
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    closest_point = cur_closest
            cur_dist, cur_closest = dist_to_edge(point, 
                                                wind.cut_in[j][1], 
                                                wind.cut_in[j][-1])
            
            if cur_dist < min_dist:
                min_dist = cur_dist
                closest_point = cur_closest

    if min_dist <= 15:
        point = list(map(round, closest_point))

    wind.add_point(point[0], point[1])








##################### ОТРИСОВКА РЕЗУЛЬТАТА ######################
def draw_lines1(arr, f):
    if f == 3:
        wind.pen_res_out.setWidth(2)
        print(arr)
        for i in range(len(arr)):
            l = [arr[i], arr[(i + 1) % len(arr)]]
            wind.scene.addLine(l[1][0], l[1][1], 
                            l[0][0], l[0][1], 
                            wind.pen_res_out)
    if f == 2:
        wind.pen_res.setWidth(2)
        print(arr)
        for i in range(len(arr)):
            l = [arr[i], arr[(i + 1) % len(arr)]]
            wind.scene.addLine(l[1][0], l[1][1], 
                            l[0][0], l[0][1], 
                            wind.pen_res)
    if f == 1:
        for i in range(len(arr)):
            l = [arr[i], arr[(i + 1) % len(arr)]]
            wind.scene.addLine(l[1][0], l[1][1], 
                            l[0][0], l[0][1], 
                            wind.pen_cut)

    if f == 0:
        for i in range(len(arr)):
            l = [arr[i], arr[(i + 1) % len(arr)]]
            wind.scene.addLine(l[1][0], l[1][1], 
                            l[0][0], l[0][1], 
                            wind.pen_rest)

def draw_section(xb, yb, xe, ye):
    global wind
    pen = QtGui.QPen(wind.color_back)
    wind.scene.addLine(xb, yb, xe, ye, pen)
    wind.scene.addLine(xb, yb, xe, ye, wind.pen_res)


def draw_lines_remove_false_side(figure):
    global wind
    try:
        w = int(wind.spinBox_w.text())
    except Exception:
        QMessageBox.warning(wind, "Внимание!", "Не целове значение толщины!")
        return 
    wind.pen_res.setWidth(w)
    buf = remove_false_side(figure)
    for section in buf:
        draw_section(round(section[0][0]), 
                     round(section[0][1]), 
                     round(section[1][0]), 
                     round(section[1][1]))
#################################################################

def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()
