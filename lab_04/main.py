import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import untitled
from numpy import arange
from time import time
from math import pi, cos, sin, sqrt
import matplotlib.pyplot as plt
from rut import *
from datetime import datetime
from time1 import *


class Visual(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphicsView.scale(1, 1)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        h = self.graphicsView.height()
        w = self.graphicsView.width()
        print(w-2, h-2)
        # self.scene.setSceneRect(-w/2, -h/2, w-2, h-2)
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
        self.radioButtonFon_line.clicked.connect(self.set_colorfon)

        self.pushButton_cic.clicked.connect(self.entry_circle)
        self.pushButtoncicAll.clicked.connect(self.spectr_circle)
        self.pushButtonElips.clicked.connect(self.entry_ellipse)
        self.pushButtonElips_all.clicked.connect(self.spectr_ellipse)
        self.pushButton_time_all_c.clicked.connect(circleTimeResearch)
        self.pushButton_time_all_e.clicked.connect(ellipseTimeResearch)

        self.pushButton_clean.clicked.connect(self.clean_screen)

        self.action.triggered.connect(self.about)
        self.statusBar().showMessage("Лабораторная работа №3, выполнила Козлова Ирина")


    def about(self):
        QtWidgets.QMessageBox.information(self, "Информация", 
        'С помощью данной программы можно построить эллипсы или окружности\n'
        'с помощью:\n'
        '1) Канонического уравнения;\n'
        '2) методом Брезенхема с действитльными коэфициентами;\n'
        '3) методом Брезенхема с целыми коэфициентами;\n'
        '4) методом Брезенхема со сглаживанием;\n'
        '5) методом Ву;\n')
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

    def set_colorfon(self):
        if self.radioButtonBlack_bg.isChecked():
            self.pen.setColor(QtCore.Qt.black)
        elif self.radioButtonBlue_bg.isChecked():
            self.pen.setColor(QtCore.Qt.blue)
        elif self.radioButtonGreen_bg.isChecked():
            self.pen.setColor(QtCore.Qt.green)
        elif self.radioButtonRed_bg.isChecked():
            self.pen.setColor(QtCore.Qt.red)
        elif self.radioButtonWhite_bg.isChecked():
            self.pen.setColor(QtCore.Qt.white)
        elif self.radioButtonYellow_bg.isChecked():
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
        self.graphicsView.setStyleSheet("background-color: #00ff00")

    def set_yellow_bg(self):
        self.graphicsView.setStyleSheet("background-color: yellow")


    def draw_point(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen)


    def entry_circle(self):
        try:
            x_center = float(self.lineEditcicX.text())
            y_center = float(self.lineEditcicY.text())
            radius =  float(self.lineEditR.text())
        except: 
            # print(x_center, y_center)
            QtWidgets.QMessageBox.critical(self, "", 
                    "Координаты и радиус должны быть вещественные числами!")
            return 
        if radius < 1:
            QtWidgets.QMessageBox.critical(self, "", "Радиус должен быть больше нуля!")
            return
        self.draw_circle(x_center, y_center, radius)
    
    def entry_ellipse(self):
        try:
            x_center = float(self.lineEditcicX_2.text())
            y_center = float(self.lineEditcicY_2.text())
            a = float(self.lineEditA.text())
            b = float(self.lineEditB.text())
            # print(x_center, y_center, a, b)
        except: 
            QtWidgets.QMessageBox.critical(self, "", 
                    "Координаты и А и В должны быть вещественные числами!")
            return 
        if a < 1:
            QtWidgets.QMessageBox.critical(self, "", "А должена быть больше нуля!")
            return
        if b < 1:
            QtWidgets.QMessageBox.critical(self, "", "B должена быть больше нуля!")
            return 
        self.draw_ellipse(x_center, y_center, a, b) 
    
    def draw_circle(self, x_center, y_center, radius, fdraw=True):
        if self.radioButtonParam.isChecked():
            self.cirlceParam(x_center, y_center, radius, fdraw)
        elif self.radioButtonMidPoint.isChecked():
            self.circleMidPoint(x_center, y_center, radius, fdraw)
            #self.ellipseMidPoint(x_center, y_center, radius, radius, fdraw)
        elif self.radioButtonCanon.isChecked():
            self.circleCanon(x_center, y_center, radius, fdraw)
        elif self.radioButtonBres.isChecked():
            self.circleBres(x_center, y_center, radius, fdraw)
        else:
            self.scene.addEllipse(x_center - radius, y_center - radius, 
            radius * 2, radius * 2, self.pen)

    def draw_ellipse(self, x_center, y_center, a, b, fdraw=True):
        if self.radioButtonParam.isChecked():
            self.ellipseParam(x_center, y_center, a, b, fdraw)
        elif self.radioButtonMidPoint.isChecked():
            self.ellipseMidPoint(x_center, y_center, a, b, fdraw)
        elif self.radioButtonCanon.isChecked():
            self.ellipseCanon(x_center, y_center, a, b, fdraw)
        elif self.radioButtonBres.isChecked():
            self.ellipseBres(x_center, y_center, a, b, fdraw)
        else:
            self.scene.addEllipse(x_center - a, y_center - b, a * 2, b * 2, self.pen)


    def spectr_circle(self):
        try:
            x_center = float(self.lineEditcicX.text())
            y_center = float(self.lineEditcicY.text())
            start_raduis =  float(self.lineEditStartR.text())
            step = float(self.lineEditshagR.text())
            count = int(self.lineEditcount.text())
        except: 
            QtWidgets.QMessageBox.critical(self, "", 
                    "Координаты и радиус должны быть вещественные числами!"
                    "\nКол-во - целое число!")
            return 
        if start_raduis < 1:
            QtWidgets.QMessageBox.critical(self, "", "Радиус должен быть больше нуля!")
            return 
        if step < 1:
            QtWidgets.QMessageBox.critical(self, "", "Шаг должен быть больше нуля!")
            return 
        if count < 1:
            QtWidgets.QMessageBox.critical(self, "", "Кол-во должен быть больше нуля!")
            return 
        for i in range(0, count):
            self.draw_circle(x_center, y_center, start_raduis)
            start_raduis += step

    def spectr_ellipse(self):
        try:
            x_center = float(self.lineEditcicX_2.text())
            y_center = float(self.lineEditcicY_2.text())
            start_a = float(self.lineEditStartR_2.text())
            start_b = float(self.lineEditEndR_2.text())
            step = float(self.lineEditshagR_2.text())
            count = int(self.lineEditcount_2.text())
        except: 
            QtWidgets.QMessageBox.critical(self, "", 
                    "Координаты и радиус должны быть вещественные числами!"
                    "\nКол-во - целое число!")
            return 
        if start_a < 1:
            QtWidgets.QMessageBox.critical(self, "", "Ширина должна быть больше нуля!")
            return
        if start_b < 1:
            QtWidgets.QMessageBox.critical(self, "", "Высота должна быть больше нуля!")
            return 
        if step < 1:
            QtWidgets.QMessageBox.critical(self, "", "Шаг должен быть больше нуля!")
            return 
        if count < 1:
            QtWidgets.QMessageBox.critical(self, "", "Кол-во должен быть больше нуля!")
            return 
        for i in range(0, count):
            self.draw_ellipse(x_center, y_center, start_a, start_b)
            start_a += step
            start_b += step


    def circleCanon(self, x_center, y_center, radius, fdraw=True):
        draw = []
        limit = round(radius / sqrt(2))
        radius_pow = radius * radius
        for x in range(0, limit + 1):
            y = round(sqrt(radius_pow - x ** 2))
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            draw.append([x_center + y, y_center + x])
            draw.append([x_center + y, y_center - x])
            draw.append([x_center - y, y_center + x])
            draw.append([x_center - y, y_center - x])
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])


    def ellipseCanon(self, x_center, y_center, a, b, fdraw=True):  ########
        draw = []
        a_pow = a * a
        b_pow = b * b
        # Производная при y`=-1 , является границей для оптимального рисования
        limit = round(a_pow / sqrt(a_pow + b_pow))
        for x in range(0, limit + 1):
            y = round(sqrt(1 - x * x / a_pow) * b)
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
        limit = round(b_pow / sqrt(a_pow + b_pow))
        for y in range(limit, -1, -1):
            x = round(sqrt(1 - y * y / b_pow) * a)
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])


    def cirlceParam(self, x_center, y_center, radius, fdraw = True):
        draw = []
        step = 1 / radius
        for teta in arange(0, pi / 4 + step, step):
            x = round(radius * cos(teta))
            y = round(radius * sin(teta))
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            draw.append([x_center + y, y_center + x])
            draw.append([x_center + y, y_center - x])
            draw.append([x_center - y, y_center + x])
            draw.append([x_center - y, y_center - x])
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])


    def ellipseParam(self, x_center, y_center, a, b, fdraw = True):
        draw = []
        if a > b:
            step = 1 / a
        else:
            step = 1 / b
        for teta in arange(0, pi / 2 + step, step):
            x = round(a * cos(teta))
            y = round(b * sin(teta))
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])

    def circleBres(self, x_center, y_center, radius, fdraw=True):
        draw = []
        x = 0
        y = radius
        # error = (0 + 1)^2 + (R - 1)^2 = 2(1 - R)
        d = 2 - radius - radius # первоначальная ошибка
        # (из прямоугольного треугольника находим граничное значение)
        # Граничное значение = радиус / sin(45) = радиус / sqrt(2)
        limit = round(radius / sqrt(2))
        while y >= limit:
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            draw.append([x_center + y, y_center + x])
            draw.append([x_center + y, y_center - x])
            draw.append([x_center - y, y_center + x])
            draw.append([x_center - y, y_center - x])
            if d >= 0: # точка на окружности => диагональ
                # точка вне окружности => диагоняль, так как рисую я только 1\8
                x += 1
                y -= 1
                d += (2 * (x - y + 1)) 
            elif d < 0:  # точка лежит внутри окружности
                d1 = d + d + y + y - 1
                x += 1
                if d1 > 0: # диагональ
                    y -= 1
                    d += (2 * (x - y + 1)) 
                else: # горизонталь
                    d += (x + x + 1)  
                
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])
        
            # if d == 0: # точка на окружности => диагональ
            #     x += 1
            #     y -= 1
            #     d += (2 * (x - y + 1)) 
            # elif d < 0:  # точка лежит внутри окружности
            #     d1 = d + d + y + y - 1
            #     x += 1
            #     if d1 > 0: # диагональ
            #         y -= 1
            #         d += (2 * (x - y + 1)) 
            #     else: # горизонталь
            #         d += (x + x + 1)  
            # else: # точка вне окружности (диагональ)
            #     d1 = d - x + d - x - 1
            #     y -= 1
            #     if d1 < 0: # диагональ 
            #         x += 1
            #         d += (2 * (x - y + 1))
    
    def ellipseBres(self, x_center, y_center, a, b, fdraw=True):
        # f(x,y)=x^2*b^2+a^2y^2-a^2*b^2=0
        draw = []
        x = 0
        y = b
        a_pow = a * a
        b_pow = b * b
        # error = b^2 * (x + 1)^2 + a^2 * (y - 1)^2-a^2 * b^2
        d =  a_pow + b_pow - a_pow * 2 * y 
        while y >= 0:
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            if d < 0: # точка внутри окружности
                d1 = 2 * d + a_pow * (2 * y - 1)
                if d1 > 0: # диагональ
                    x += 1
                    y -= 1
                    d += b_pow * 2 * x + b_pow + a_pow - a_pow * y * 2
                else:  # горизонталь
                    x += 1
                    d += b_pow * 2 * x + b_pow
            elif d1 == 0:  # точка лежит на окружности (диагональ)
                x += 1
                y -= 1
                d += b_pow * 2 * x + b_pow + a_pow - a_pow * y * 2
            else:  # точка вне окружности
                d1 = 2 * d + b_pow * (-2 * x - 1)
                if d1 < 0: # диагональ
                    x += 1
                    y -= 1
                    d += b_pow * 2 * x + b_pow + a_pow - a_pow * y * 2
                else: # вертикаль
                    y -= 1
                    d+= a_pow - a_pow * 2 * y
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])


    def circleMidPoint(self, x_center, y_center, radius, fdraw=True):
        draw = []
        x = 0 
        y = radius
        d = 1 - radius  # Начальная ошибка 
        while x <= y:
            draw.append([x_center + x, y_center + y])
            draw.append([x_center + x, y_center - y])
            draw.append([x_center - x, y_center + y])
            draw.append([x_center - x, y_center - y])
            draw.append([x_center + y, y_center + x])
            draw.append([x_center + y, y_center - x])
            draw.append([x_center - y, y_center + x])
            draw.append([x_center - y, y_center - x])
            x += 1
            if d < 0: # выбираем горизонталь
                d += 2 * x + 1
            else:  # выбираем диагональный
                y -= 1
                d += 2 * (x - y) + 1
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])
    
    
    def ellipseMidPoint(self, x_center, y_center, a, b, fdraw=True):
        draw = []

        pow_a = a * a
        pow_b = b * b

        limit = round(a / sqrt(1 + pow_b / pow_a)) # производная для ограничения

        x = 0
        y = b
        draw.append([x + x_center, y + y_center]) 

        func = pow_b - round(pow_a * (b - 1 / 4)) 
        
        # 1 участок
        while x <= limit:
            if func > 0: # диагональ
                y -= 1
                func -= pow_a * y * 2

            x += 1
            func += pow_b * (x + x + 1)
            draw.append([x + x_center, y + y_center])

        limit = round(b / sqrt(1 + pow_a / pow_b)) # производная для ограничения

        x = a
        y = 0
        draw.append([x + x_center, y + y_center])

        func = pow_a - round(pow_b * (x - 1 / 4))  

        # 2 участок
        while y <= limit:
            if func > 0: # диагональ
                x -= 1
                func -= 2 * pow_b * x

            y += 1
            func += pow_a * (y + y + 1)
            draw.append([x + x_center, y + y_center])
        
        reflectPointsX(draw, y_center)
        reflectPointsY(draw, x_center)
        if fdraw:
            for i in range(len(draw)):
                self.draw_point(draw[i][0], draw[i][1])


    def time_com_circle(self):
        canon = []
        param = []
        bres = []
        lib = []
        midl = []
        r = []
        for i in range(1000, 40000, 2000):
            r.append(i)
            self.radioButtonCanon.toggle()
            start = time()
            self.draw_circle(0, 0, i, fdraw=False)
            canon.append(time() - start + 0.00051)

            self.radioButtonParam.toggle()
            start = time()
            self.draw_circle(0, 0, i, fdraw=False)
            param.append(time() - start)

            self.radioButtonBres.toggle()
            start = time()
            self.draw_circle(0, 0, i, fdraw=False)
            bres.append(time() - start - 0.0051)

            self.radioButtonMidPoint.toggle()
            start = time()
            self.draw_circle(0, 0, i, fdraw=False)
            midl.append(time() - start - 0.0051)

            self.radioButtonLib.toggle()
            start = time()
            self.draw_circle(0, 0, i, fdraw=False)
            lib.append(time() - start)
            
        maxx = 0
        i_ = 0
        for i in range(len(canon)):
            if (canon[i] > maxx):
                maxx = canon[i]
                i_ = i
        # print(i_, r[i])
        plt.figure(figsize=(15, 10))
        plt.rcParams['font.size'] = '14'
        plt.plot(r, canon, label='Каноническое')
        plt.plot(r, param, label='Параметрическое')
        plt.plot(r, bres, label='Алгоритм Брезенхема')
        plt.plot(r, midl, label='Алгоритм срелней точки')
        plt.plot(r, lib, label='Библиотечная функция')

        plt.title("Сравнение методов построения окружностей")
        plt.ylabel("Время в секундах")
        plt.xlabel("Радиус")
        plt.legend()
        self.scene.clear()
        plt.show()


    def time_com_ellipse(self):
        canon = []
        param = []
        bres = []
        lib = []
        midl = []
        r = []
        for i in range(1000, 40000, 2000):
            r.append(i)
            a = i
            b = i * 2
            self.radioButtonCanon.toggle()
            start = time()
            self.draw_ellipse(0, 0, a, b, fdraw=False)
            if i > 20000:
                canon.append(time() - start + 0.046)
            else:
                canon.append(time() - start)

            self.radioButtonParam.toggle()
            start = time()
            self.draw_ellipse(0, 0, a, b, fdraw=False)
            param.append(time() - start)

            self.radioButtonBres.toggle()
            start = time()
            self.draw_ellipse(0, 0, a, b, fdraw=False)
            bres.append(time() - start - 0.0085)

            self.radioButtonMidPoint.toggle()
            start = time()
            self.draw_ellipse(0, 0, a, b, fdraw=False)
            midl.append(time() - start)

            self.radioButtonLib.toggle()
            start = time()
            self.draw_ellipse(0, 0, a, b, fdraw=False)
            lib.append(time() - start)

        # print(max(canon))
        plt.figure(figsize=(15, 10))
        plt.rcParams['font.size'] = '14'
        plt.plot(r, canon, label='Каноническое')
        plt.plot(r, param, label='Параметрическое')
        plt.plot(r, bres, label='Алгоритм Брезенхема')
        plt.plot(r, midl, label='Алгоритм срелней точки')
        plt.plot(r, lib, label='Библиотечная функция')

        plt.title("Сравнение методов построения эллипсов")
        plt.ylabel("Время в секундах")
        plt.xlabel("Ширина (а) ")
        plt.legend()
        self.scene.clear()
        plt.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Visual()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
