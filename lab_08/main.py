
# Python version 3.6
import sys
from typing_extensions import ParamSpec
import numpy as np
import win2
import pyqtgraph as pg
import matplotlib.pyplot as plt

from my_math import *
from time import time
from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
from math import sin, cos, pi, radians, fabs,  floor

ctrl = False
wind = None

WIDTH = 1400
HIGHT = 1400

class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

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
    # def mousePressEvent(self, event):
    #     add_point(event.scenePos())
        

    # добавить прямоугольник
    def mouseMoveEvent(self, event):
        print("JJJ")
        parent = self.parent
        if parent.radioButton_draw_rest.isChecked():
            parent.image.fill(Qt.white)
            parent.draw_borders()

            cord = event.scenePos()

            x = cord.x()
            y = cord.y()
            if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
                x += 2
                y += 10
                num = len(parent.lines)

                if num > 0 and not parent.cutter_flag:
                    parent.image.fill(Qt.white)
                    parent.draw_borders()
                    parent.Bresenham(parent.lines[num - 1][0],
                                     parent.lines[num - 1][1],
                                     x, y, parent.pen_rest)

        if parent.radioButton_draw_line.isChecked():
            print("DDD")
            parent.image.fill(Qt.white)
            parent.draw_borders()

            cord = event.scenePos()

            x = cord.x()
            y = cord.y()
            if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
                print("FFF")
                x += 2
                y += 10
                num = len(parent.one_line)

                if num > 0:
                    print("VVV")
                    parent.image.fill(Qt.white)
                    parent.draw_borders()
                    parent.Bresenham(parent.one_line[0],
                                     parent.one_line[1],
                                     x, y, parent.pen_line)

    
    # def mousePressEvent(self, QMouseEvent):
    #     print("PPPP")
    #     parent = self.parent
    #     if parent.radioButton_draw_rest.isChecked():
    #         if parent.cutter_flag:
    #             parent.lines.clear()
    #             parent.table_rust.setRowCount(0)
    #             parent.image.fill(Qt.white)
    #             parent.draw_borders()

    #         if (QMouseEvent.button() == Qt.LeftButton):
    #             parent.cutter_flag = False

    #             cord = QMouseEvent.pos()

    #             y = cord.y()
    #             x = cord.x()

    #             if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
    #                 x -= 10
    #                 y -= 10
    #                 i = len(parent.lines)

    #                 if ctrl and i:
    #                     if y != parent.lines[i - 1][1]:
    #                         der = ((x - parent.lines[i - 1][0]) /
    #                                (y - parent.lines[i - 1][1]))
    #                     else:
    #                         der = 2
    #                     if abs(der) <= 1:
    #                         x = parent.lines[i - 1][0]
    #                     else:
    #                         y = parent.lines[i - 1][1]

    #                 if i:
    #                     parent.Bresenham(parent.lines[i - 1][0],
    #                                    parent.lines[i - 1][1],
    #                                    x, y)
    #                 parent.lines.append([x, y, 0])
    #                 # self.info_appender([x, y])

    #         elif (QMouseEvent.button() == Qt.RightButton):
    #             i = len(parent.lines)
    #             if i:
    #                 x = parent.lines[0][0]
    #                 y = parent.lines[0][1]
    #                 parent.Bresenham(parent.lines[i - 1][0],
    #                                parent.lines[i - 1][1],
    #                                x, y)
    #                 parent.lines.append([x, y, 0])
    #                 parent.cutter_flag = True
    #             parent.draw_borders()

    #     elif parent.radioButton_draw_line.isChecked():  # Input lines
    #         if (QMouseEvent.button() == Qt.LeftButton):
    #             cord = QMouseEvent.pos()

    #             y = cord.y()
    #             x = cord.x()
    #             if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
    #                 x -= 10
    #                 y -= 10
    #                 i = len(parent.one_line)

    #                 if ctrl and i:
    #                     if y != parent.one_line[1]:
    #                         der = ((x - parent.one_line[0]) /
    #                                (y - parent.one_line[1]))
    #                     else:
    #                         der = 2
    #                     if abs(der) <= 1:
    #                         x = parent.one_line[0]
    #                     else:
    #                         y = parent.one_line[1]

    #                 if i == 2:
    #                     parent.one_line.append(x)
    #                     parent.one_line.append(y)
    #                     parent.rect.append(parent.one_line)
    #                     parent.one_line = []
    #                 else:
    #                     parent.one_line.append(x)
    #                     parent.one_line.append(y)

    #             parent.image.fill(Qt.white)
    #             parent.draw_borders()



               


class Visual(QtWidgets.QMainWindow, win2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.graphicsView.scale(1, 1)
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        self.graphicsView.setCursor(Qt.CrossCursor)
        self.graphicsView.setMouseTracking(True)

        self.scene = Scene(self)
        # self.scene.win = self
        self.graphicsView.setScene(self.scene)

        self.image = QImage(1400, 1400, QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.scene.addPixmap(QPixmap.fromImage(self.image))

        self.pen_rest = QtGui.QPen(QtCore.Qt.black)
        self.pen_rest.setWidth(0)
        self.pen_line = QtGui.QPen(QtCore.Qt.green)
        self.pen_line.setWidth(0)
        self.pen_res = QtGui.QPen(QtCore.Qt.red)
        self.pen_res.setWidth(0)

        self.rest = [] # отсекатель
        self.lines = [] # отрезки
        self.one_line = []
        self.cutter_flag = False


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
        # self.pushButton_draw_line.clicked.connect(self.add_line1)
        # self.pushButton_draw_rest.clicked.connect(self.add_rect)
        # self.pushButton_gran.clicked.connect(self.add_bars)
        # self.pushButton_RES.clicked.connect(clipping)




    def mousePressEvent(self, QMouseEvent):
        print("PRESS")
        if self.radioButton_draw_rest.isChecked():
            if self.cutter_flag:
                self.lines.clear()
                self.table_rest.setRowCount(0)
                self.image.fill(Qt.white)
                self.draw_borders()

            if (QMouseEvent.button() == Qt.LeftButton):
                self.cutter_flag = False
                cord = QMouseEvent.pos()

                y = cord.y()
                x = cord.x()
                if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
                    x -= 10
                    y -= 10
                    i = len(self.lines)

                    if ctrl and i:
                        if y != self.lines[i - 1][1]:
                            der = ((x - self.lines[i - 1][0]) /
                                   (y - self.lines[i - 1][1]))
                        else:
                            der = 2
                        if abs(der) <= 1:
                            x = self.lines[i - 1][0]
                        else:
                            y = self.lines[i - 1][1]

                    if i:
                        self.Bresenham(self.lines[i - 1][0],
                                       self.lines[i - 1][1],
                                       x, y)
                    self.lines.append([x, y, 0])
                    # self.info_appender([x, y])

            elif (QMouseEvent.button() == Qt.RightButton):
                i = len(self.lines)
                if i:
                    x = self.lines[0][0]
                    y = self.lines[0][1]
                    self.Bresenham(self.lines[i - 1][0],
                                   self.lines[i - 1][1],
                                   x, y)
                    self.lines.append([x, y, 0])
                    self.cutter_flag = True
                self.draw_borders()

        elif self.radioButton_draw_line.isChecked():  # Input lines
            if (QMouseEvent.button() == Qt.LeftButton):
                cord = QMouseEvent.pos()
                print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDSSSSSSSSSSSSS", cord)
                y = cord.y()
                x = cord.x()
                if (x >= 10 and y >= 10 and y <= HIGHT and x <= WIDTH):
                    x -= 10
                    y -= 10
                    i = len(self.one_line)

                    if ctrl and i:
                        if y != self.one_line[1]:
                            der = ((x - self.one_line[0]) /
                                   (y - self.one_line[1]))
                        else:
                            der = 2
                        if abs(der) <= 1:
                            x = self.one_line[0]
                        else:
                            y = self.one_line[1]

                    if i == 2:
                        self.one_line.append(x)
                        self.one_line.append(y)
                        self.rest.append(self.one_line)
                        # self.table_appender(self.one_line)
                        self.one_line = []
                    else:
                        self.one_line.append(x)
                        self.one_line.append(y)

                self.image.fill(Qt.white)
                self.draw_borders()


    def Bresenham(self, x_start, xEnd, y_start, yEnd, color, t=False):
        color = color.color().rgb()
        if x_start == xEnd and y_start == yEnd:
            self.image.setPixel(x_start + 1, y_start, color)
            return
        x_start = int(x_start)
        y_start = int(y_start)
        xEnd = int(xEnd)
        yEnd = int(yEnd)

        deltaX = xEnd - x_start
        deltaY = yEnd - y_start

        stepX = int(sign(deltaX))
        stepY = int(sign(deltaY))

        deltaX = abs(deltaX)
        deltaY = abs(deltaY)

        if deltaX <= deltaY:
            deltaX, deltaY = deltaY, deltaX
            flag = True
        else:
            flag = False

        acc = deltaY + deltaY - deltaX
        cur_x = x_start
        cur_y = y_start

        for i in range(deltaX + 1):
            self.image.setPixel(cur_x + 1, cur_y, color)

            if acc >= 0:
                if flag:
                    cur_x += stepX
                else:
                    cur_y += stepY
                acc -= (deltaX + deltaX)
            if acc <= 0:
                if flag:
                    cur_y += stepY
                else:
                    cur_x += stepX
                acc += deltaY + deltaY

    def draw_borders(self):
        print("EEE1111111111111")
        print(len(self.lines))
        print(len(self.rest))
        if len(self.rest) != 0:
            print(len(self.rest))
            for j in range(len(self.rest)):
                self.Bresenham(self.rest[j][0],
                               self.rest[j][1],
                               self.rest[j][2],
                               self.rest[j][3], self.pen_rest)

        if len(self.lines) > 1:
            print(len(self.lines))
            for i in range(len(self.lines) - 1):
                self.Bresenham(self.lines[i][0],
                               self.lines[i][1],
                               self.lines[i + 1][0],
                               self.lines[i + 1][1], self.pen_line)
        self.repaint()


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

    # def draw_all_line(self):
    #     for i in range(len(self.lines)):
    #         self.scene.addLine(self.lines[i][0][0], self.lines[i][0][1],
    #                            self.lines[i][1][0], self.lines[i][1][1], 
    #                            self.pen_line)

    
def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()