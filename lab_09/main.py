import sys
import win2

from my_cut import *

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
            reform_point(QMouseEvent.scenePos())
            # add_point(x, y)
        
        if (QMouseEvent.button() == Qt.RightButton):
            if wind.input_cut:
                end_cut()
            if wind.input_rests:
                end_rest()

        if (QMouseEvent.button() == Qt.MidButton):
            if wind.input_rests:
                reform_point(QMouseEvent.scenePos())
            else:
                QMessageBox.warning(self, "Внимание!",
                 "Это можно использовать только при вводе отсекаемого многоугольника!!!")




               


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

        self.pushButton_RES.clicked.connect(self.what_cut)

    def what_cut(self):
        if self.radioButton_FALSE_BE.isChecked():
            flag_ = False
        elif self.radioButton_FALSE_DEL.isChecked():
            flag_ = True
        print("flag_", flag_)
        cut(flag_)

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
        global now, end_rect_, end_lines_
        end_lines_ = False
        end_rect_ = False
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

    def print_error(self, rc):
        if rc == ERROR_CUTTER_IS_LINE:
            QMessageBox.warning(self, "Ошибка", "Отсекатель вырожден")
            return
        elif rc == ERROR_CUTTER_ISNOT_CONVEX:
            QMessageBox.warning(self, "Ошибка", "Отсекатель невыпуклый!!! Введите выпуклый")
            return
        elif rc == ERROR_REST_ISNOT_POLYGON:
            QMessageBox.warning(self, "Ошибка", "Отсекаемое должно быть многоугольником")
            return
        elif rc == ERROR_REST_IS_LINE:
            QMessageBox.warning(self, "Ошибка", "Отсекаемый многоугольник вырожден")
            return

    def add_rest(self):
        try:
            x = float(self.lineEdit_x_rest.text())
            y = float(self.lineEdit_y_rest.text())
        except Exception:
            QMessageBox.warning(self, "Внимание!",
                                "Неверно введены координаты!")
            return 
        buf_l, buf_r = wind.input_rests, wind.input_cut
        wind.input_cut = False
        wind.input_rests = True
        add_point(x, y)
        wind.input_rests, wind.input_cut = buf_l, buf_r

    def add_cut(self):
        try:
            x = float(self.lineEdit_x_cut.text())
            y = float(self.lineEdit_y_cut.text())
            
        except Exception:
            QMessageBox.warning(self, "Внимание!", 
                                "Неверно введены координаты!")
            return 
        
        buf_l, buf_r = wind.input_rests, wind.input_cut
        wind.input_cut = True
        wind.input_rests = False
        add_point(x, y)
        wind.input_rests, wind.input_cut = buf_l, buf_r
    


# Добавить строку с координатами с таблицу
def add_row(win, f):
    if f == 1:
        win.table_rest.insertRow(win.table_rest.rowCount())
    if f == 2:
        win.table_cut.insertRow(win.table_cut.rowCount())


# Добавить точку 
def add_point(x, y):
    x = round(x)
    y = round(y)
    global wind, ctrl, now


    if wind.input_rests:
        if end_lines_:
            QMessageBox.warning(wind, "Внимание!", 
                                "Отсекаеоме нарисовано и замкнуто!!!")
            return

        if (len(wind.lines)) == 0:
            wind.lines.append([x, y])

            add_row(wind, 1)
            i = wind.table_rest.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(x))
            item_e = QTableWidgetItem("[{0}]".format(y))
            wind.table_rest.setItem(i, 0, item_b)
            wind.table_rest.setItem(i, 1, item_e)

        else:

            i = len(wind.lines)
            if ctrl:
                if abs(x - wind.lines[i - 1][0]) < abs(y - wind.lines[i - 1][1]):
                    x = wind.lines[i - 1][0]
                elif abs(y - wind.lines[i - 1][1]) < abs(x - wind.lines[i - 1][0]):
                    y = wind.lines[i - 1][1]
                ctrl = False
            wind.scene.addLine(wind.lines[i - 1][0], 
                               wind.lines[i - 1][1], 
                               x, y, wind.pen_rest)
            wind.lines.append([x, y])

            add_row(wind, 1)
            i = wind.table_rest.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(x))
            item_e = QTableWidgetItem("[{0}]".format(y))
            print(item_b, item_e)
            wind.table_rest.setItem(i, 0, item_b)
            wind.table_rest.setItem(i, 1, item_e)

    if wind.input_cut:
        if end_rect_:
            QMessageBox.warning(wind, "Внимание!",
                                "Отсекатель нарисован и замкнут!!!")
            return
            
        if (len(wind.rect)) == 0:
            wind.rect.append([x, y])

            add_row(wind, 2)
            i = wind.table_cut.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(x))
            item_e = QTableWidgetItem("[{0}]".format(y))
            wind.table_cut.setItem(i, 0, item_b)
            wind.table_cut.setItem(i, 1, item_e)

        else:
            i = len(wind.rect)
            if ctrl:
                if abs(x - wind.rect[i - 1][0]) < abs(y - wind.rect[i - 1][1]):
                    x = wind.rect[i - 1][0]
                elif abs(y - wind.rect[i - 1][1]) < abs(x - wind.rect[i - 1][0]):
                    y = wind.rect[i - 1][1]
                ctrl = False
            wind.scene.addLine(wind.rect[i - 1][0],
                               wind.rect[i - 1][1], 
                               x, y, wind.pen_cut)
            wind.rect.append([x, y])


            add_row(wind, 2)
            i = wind.table_cut.rowCount() - 1
            item_b = QTableWidgetItem("[{0}]".format(x))
            item_e = QTableWidgetItem("[{0}]".format(y))
            print(item_b, item_e)
            wind.table_cut.setItem(i, 0, item_b)
            wind.table_cut.setItem(i, 1, item_e)

            
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


def reform_point(point1):
    global wind
    x = point1.x()
    y = point1.y()

    x = round(x)
    y = round(y)

    point = [x, y]
    
    min_dist = 15 + 2
    closest_point = None
    if len(wind.rect) > 1:
        for i in range(len(wind.rect) - 1):
            cur_dist, cur_closest = dist_to_edge(point, 
                                                 wind.rect[i], 
                                                 wind.rect[i + 1])
            if cur_dist < min_dist:
                min_dist = cur_dist
                closest_point = cur_closest
        cur_dist, cur_closest = dist_to_edge(point, 
                                             wind.rect[1], 
                                             wind.rect[-1])
        
        if cur_dist < min_dist:
            min_dist = cur_dist
            closest_point = cur_closest

    if min_dist <= 15:
        point = list(map(round, closest_point))

    add_point(point[0], point[1])


#################################################################
# Вызов отсекающей функции
def cut(flag):
    figure = wind.lines
    cutter = wind.rect

    rc, res = Sutherland_Hodgman1(figure, cutter, flag)
    if rc:
        wind.print_error(rc)
        return

    print("RES", res)
    if flag:
        draw_lines_remove_false_side(res)
    else:
        draw_lines1(res)

    if rc == OK:
        QMessageBox.information(wind, "Внимание!", 
                               "ОТсечение выполнено!")




##################### ОТРИСОВКА РЕЗУЛЬТАТА ######################
def draw_lines1(arr):
    print("draw", arr)
    global wind
    try:
        w = int(wind.spinBox_w.text())
    except Exception:
        QMessageBox.warning(wind, "Внимание!", 
                            "Не целове значение толщины!")
        return 
    wind.pen_res.setWidth(w)
    print(arr)
    for i in range(len(arr)):
        l = [arr[i], arr[(i + 1) % len(arr)]]
        wind.scene.addLine(l[1][0], l[1][1], 
                           l[0][0], l[0][1], 
                           wind.pen_res)

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