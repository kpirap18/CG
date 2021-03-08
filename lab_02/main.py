import sys
import numpy as np
import algebra
import mainwin
import pyqtgraph as pg

from copy import deepcopy
from PyQt5 import QtWidgets, QtCore, QtGui
from math import sin, cos, pi, radians

# Коэффециенты для улитки Паскаля
A = 40
B = 30

# Размер пикселей на оси
SHAG = 50

class MainWin(QtWidgets.QMainWindow, mainwin.Ui_Kozlova_lab_02):
    def __init__(self):
        self.FLAG = 0
        self.FLAG_BUTTON = 1
        super().__init__()
        self.setupUi(self)
        self.graphicsView.scale(1, -1)

        # Массивы для рисования текущего состояния фигуры
        # Ромб
        self.rhombus = []
        # Улитка Паскаля
        self.snail = []
        # Штрихи
        self.hatching = []
        # Центр
        self.center = []

        # Массивы для возврата на шаг назад
        self.rhombus_duff = []
        self.hatching_duff = []
        self.snail_duff = []
        self.center_duff = []

        # Кнопки и функции к ним
        self.pushButton_back.clicked.connect(self.draw_back)
        self.pushButton_mode.clicked.connect(self.draw_mode)
        self.pushButton_scale.clicked.connect(self.draw_scale)
        self.pushButton_throw.clicked.connect(self.draw_base)
        self.pushButton_turn.clicked.connect(self.draw_turn)
        self.pushButton_oxy.clicked.connect(self.draw_oxy)

        self.label.setText("Отметки на осях координат поставлены по {} пикселей".format(SHAG))
        self.repaint()


    def init_base(self):
        '''
            Функция для задания начальных координат фигуры.
        '''
        # Ромб
        self.rhombus = [[0, SHAG * 2], [-SHAG * 4, 0],
                        [0, -SHAG * 2], [SHAG * 4, 0], [0, SHAG * 2]]
        # Улитка Паскаля
        teta = np.linspace(0, 2 * pi, 1000)
        self.snail = algebra.snail(teta, A, B)
        # Штрихи
        self.hatching = algebra.hatching(self.snail, SHAG)
        # Центр
        self.center = [[0, 0], [0, 0]]


    def draw_oxy(self):
        '''
            Функция переключения "показать/скрыть оси координат".
        '''
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)

        if self.FLAG:
            self.pushButton_oxy.setText("Скрыть оси координат")
            self.draw()
            self.FLAG = self.FLAG_BUTTON
            self.FLAG_BUTTON = 0
        else:
            self.pushButton_oxy.setText("Показать оси координат")
            self.draw()
            self.FLAG = self.FLAG_BUTTON
            self.FLAG_BUTTON = 1
        self.graphicsView.repaint()
        self.repaint()


    def draw(self):
        '''
            Функция для рисования текущего состояния фигуры.
            (Координаты уже высчитаны)
        '''
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        w = self.graphicsView.width()
        h = self.graphicsView.height()
        scene.setSceneRect(-w / 2, -h / 2, w - 2, h - 2)

        # Центр
        scene.addLine(self.center[0][0], self.center[0][1],
                      self.center[1][0], self.center[1][1],
                      pen=pg.mkPen(color='r', width=4))

        # Оси координат
        if self.FLAG:
            scene.addLine(0, -w, 0, w, pen=pg.mkPen('g'))
            scene.addLine(-h, 0, h, 0, pen=pg.mkPen('g'))
            scene.addLine(0, h // 2, -5, h // 2 - 20, pen=pg.mkPen('#77dd77'))
            scene.addLine(0, h // 2, 5, h // 2 - 20, pen=pg.mkPen('g'))
            scene.addLine(w // 2, 0, w // 2 - 20, 5, pen=pg.mkPen('g'))
            scene.addLine(w // 2, 0, w // 2 - 20, -5, pen=pg.mkPen('g'))
            # Отсечки
            for i in range(SHAG, 501, SHAG):
                scene.addLine(i, 5, i, -5, pen=pg.mkPen('g'))
                scene.addLine(-i, 5, -i, -5, pen=pg.mkPen('g'))
                scene.addLine(5, i, -5, i, pen=pg.mkPen('g'))
                scene.addLine(5, -i, -5, -i, pen=pg.mkPen('g'))

        # Отрисовка ромба
        for i in range(len(self.rhombus) - 1):
            scene.addLine(self.rhombus[i][0], self.rhombus[i][1],
                          self.rhombus[i + 1][0], self.rhombus[i + 1][1])

        # Отрисовка улитки Паскаля
        for i in range(len(self.snail) - 1):
            scene.addLine(self.snail[i][0], self.snail[i][1],
                          self.snail[i + 1][0], self.snail[i + 1][1])

        # Штриховка
        print(len(self.hatching))
        i = 0
        for _ in range(len(self.hatching) // 2):
            scene.addLine(self.hatching[i][0], self.hatching[i][1],
                          self.hatching[i + 1][0], self.hatching[i + 1][1])
            i += 2

        # Центр фигуры (координаты)
        x = (self.rhombus[0][0] + self.rhombus[2][0]) / 2
        y = (self.rhombus[0][1] + self.rhombus[2][1]) / 2
        self.lineEdit_centerx.setText("%.3f" % x)
        self.lineEdit_centery.setText("%.3f" % y)

        self.graphicsView.repaint()
        self.repaint()


    def copy_arr(self):
        '''
            Копирование текущего положения для возврата назад.
        '''
        self.hatching_duff = deepcopy(self.hatching)
        self.rhombus_duff = deepcopy(self.rhombus)
        self.snail_duff = deepcopy(self.snail)
        self.center_duff = deepcopy(self.center)


    def draw_base(self):
        '''
            Рисование исходного изображения.
        '''
        self.copy_arr()
        self.init_base()
        self.draw()


    def draw_back(self):
        '''
            Функция на шаг назад.
        '''
        self.hatching_duff, self.hatching = self.hatching, self.hatching_duff
        self.snail_duff, self.snail = self.snail, self.snail_duff
        self.rhombus_duff, self.rhombus = self.rhombus, self.rhombus_duff
        self.center_duff, self.center = self.center, self.center_duff
        self.draw()


    def mode(point, d):
        '''
            Формула перемещения для точки.
        '''
        point[0] += d[0]
        point[1] += d[1]
        return point


    def scale(point, k, m):
        '''
            Формула масштабирования дл точки.
        '''
        point[0] = point[0] * k[0] + (1 - k[0]) * m[0]
        point[1] = point[1] * k[1] + (1 - k[1]) * m[1]
        return point


    def turn(point, c, ang):
        '''
            Формула поворота для точки.
        '''
        my_sin = sin(radians(ang))
        my_cos = cos(radians(ang))
        x1 = c[0] + (point[0] - c[0]) * my_cos + \
             (point[1] - c[1]) * my_sin
        point[1] = c[1] + (point[1] - c[1]) * my_cos - \
                   (point[0] - c[0]) * my_sin
        point[0] = x1
        return point


    def draw_mode(self):
        '''
            Функция перемещения фигуры.
        '''
        try:
            dx = int(self.lineEdit_modex.text())
            dy = int(self.lineEdit_modey.text())

            self.copy_arr()
            for i in range(len(self.rhombus)):
                self.rhombus[i] = MainWin.mode(self.rhombus[i], [dx, dy])
            for i in range(len(self.snail)):
                self.snail[i] = MainWin.mode(self.snail[i], [dx, dy])
            for i in range(len(self.hatching)):
                self.hatching[i] = MainWin.mode(self.hatching[i], [dx, dy])
            for i in range(len(self.center)):
                self.center[i] = MainWin.mode(self.center[i], [dx, dy])
            self.check()
            self.draw()
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Невозможно прочитать числа!",
                                           "Значения dx и dy должны быть целые\n"
                                           "(так как значения в пикселях).")
        

    def draw_scale(self):
        '''
            Функция масштабирования фигуры.
        '''
        try:
            kx = float(self.lineEdit_kx.text())
            ky = float(self.lineEdit_ky.text())
            xm = int(self.lineEdit_xm.text())
            ym = int(self.lineEdit_ym.text())

            self.copy_arr()
            for i in range(len(self.rhombus)):
                self.rhombus[i] = MainWin.scale(self.rhombus[i], [kx, ky], [xm, ym])
            for i in range(len(self.snail)):
                self.snail[i] = MainWin.scale(self.snail[i], [kx, ky], [xm, ym])
            for i in range(len(self.hatching)):
                self.hatching[i] = MainWin.scale(self.hatching[i], [kx, ky], [xm, ym])
            for i in range(len(self.center)):
                self.center[i] = MainWin.scale(self.center[i], [kx, ky], [xm, ym])

            self.lineEdit_xturn.setText("%2.f" % xm)
            self.lineEdit_yturn.setText("%2.f" % ym)
            self.check()
            self.draw()
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Невозможно прочитать числа",
                                           "Координаты центра - целые числа \n"
                                           "(так как значения в пикселях).\n"
                                           "Коэффециенты - вещественные числа.")
        

    def draw_turn(self):
        '''
            Функция поворота фигуры.
        '''
        try:
            angle = float(self.lineEdit_angle.text())
            xc = int(self.lineEdit_xturn.text())
            yc = int(self.lineEdit_yturn.text())

            self.copy_arr()
            for i in range(len(self.rhombus)):
                self.rhombus[i] = MainWin.turn(self.rhombus[i], [xc, yc], angle)
            for i in range(len(self.snail)):
                self.snail[i] = MainWin.turn(self.snail[i], [xc, yc], angle)
            for i in range(len(self.hatching)):
                self.hatching[i] = MainWin.turn(self.hatching[i], [xc, yc], angle)
            for i in range(len(self.center)):
                self.center[i] = MainWin.turn(self.center[i], [xc, yc], angle)

            self.lineEdit_xm.setText("%2.f" % xc)
            self.lineEdit_ym.setText("%2.f" % yc)
            self.check()
            self.draw()
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Невозможно прочитать числа",
                                           "Координаты центра - целые числа \n"
                                           "(так как значения в пикселях).\n"
                                           "Угол - вещественное число.")
        

    def check(self):
        '''
            Функция для проверки, выходит ли фигура за пределы экрана.
        '''
        w = self.graphicsView.width()
        h = self.graphicsView.height()


        for i in range(len(self.rhombus)):
            if (w / 2 < self.rhombus[i][0]) or \
                (-w / 2 > self.rhombus[i][0]) or \
                (h / 2 < self.rhombus[i][1]) or \
                (-h / 2 > self.rhombus[i][1]):
                QtWidgets.QMessageBox.critical(self, "ВНИМАНИЕ",
                                    "Фигура вышла за пределы экрана\n")
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()