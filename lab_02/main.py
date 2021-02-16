import sys
import numpy as np
import algebra
import mainwin
import pyqtgraph as pg

from copy import deepcopy
from PyQt5 import QtWidgets, QtCore
from math import sin, cos, pi, radians

# КОэффециенты для улитки Паскаля
A = 40
B = 30

class MainWin(QtWidgets.QMainWindow, mainwin.Ui_MainWindow):
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


    def init_base(self):
        '''
            Функция для задания начальных координат фигуры.
        '''
        # Ромб
        self.rhombus = [[0, 100], [-200, 0], [0, -100], [200, 0], [0, 100]]
        # Улитка Паскаля
        teta = np.linspace(0, 2 * pi, 1000)
        self.snail = algebra.snail(teta, A, B)
        # Штрихи
        self.hatching = algebra.hatching(self.snail)
        # Центр
        self.center = [[0, 0], [0, 0]]


    def draw_oxy(self):
        '''
            Функция переключения "показать/скрыть оси координат".
        '''
        print("flag", self.FLAG)
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        w = self.graphicsView.width()
        h = self.graphicsView.height()

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
        print(w, h)
        scene.setSceneRect(-w / 2, -h / 2, w - 2, h - 2)

        # Центр
        scene.addLine(self.center[0][0], self.center[0][1],
                      self.center[1][0], self.center[1][1],
                      pen=pg.mkPen(color='r', width=4))

        # Оси координат
        if self.FLAG:
            scene.addLine(0, -w, 0, w, pen=pg.mkPen('g'))
            scene.addLine(-h, 0, h, 0, pen=pg.mkPen('g'))

         # Отрисовка ромба
        for i in range(len(self.rhombus) - 1):
            scene.addLine(self.rhombus[i][0], self.rhombus[i][1],
                          self.rhombus[i + 1][0], self.rhombus[i + 1][1])
        # Ортисовка улитки Паскаля
        for i in range(len(self.snail) - 1):
            scene.addLine(self.snail[i][0], self.snail[i][1],
                          self.snail[i + 1][0], self.snail[i + 1][1])

        # Штриховка
        print(len(self.hatching))
        i = 0
        for _ in range(len(self.hatching) // 2):
            print("i", i)
            scene.addLine(self.hatching[i][0], self.hatching[i][1],
                          self.hatching[i + 1][0], self.hatching[i + 1][1])
            i += 2

        # Центр фигуры
        x = (self.rhombus[0][0] + self.rhombus[2][0]) / 2
        y = (self.rhombus[0][1] + self.rhombus[2][1]) / 2
        self.lineEdit_centerx.setText("%.2f" % x)
        self.lineEdit_centery.setText("%.2f" % y)

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
        self.hatching = self.hatching_duff
        self.snail = self.snail_duff
        self.rhombus = self.rhombus_duff
        self.center = self.center_duff
        self.draw()


    def draw_mode(self):
        '''
            Функция перемещения фигуры.
        '''
        try:
            dx = int(self.lineEdit_modex.text())
            dy = int(self.lineEdit_modey.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Ошибка",
                                           "Введите целые числа!!!")
        self.copy_arr()
        for i in range(len(self.rhombus)):
            self.rhombus[i][0] += dx
            self.rhombus[i][1] += dy
        for i in range(len(self.snail)):
            self.snail[i][0] += dx
            self.snail[i][1] += dy
        for i in range(len(self.hatching)):
            self.hatching[i][0] += dx
            self.hatching[i][1] += dy
        for i in range(len(self.center)):
            self.center[i][0] += dx
            self.center[i][1] += dy
        self.draw()


    def draw_scale(self):
        '''
            Функция масштабирования фигуры.
        '''
        try:
            kx = float(self.lineEdit_kx.text())
            ky = float(self.lineEdit_ky.text())
            xm = float(self.lineEdit_xm.text())
            ym = float(self.lineEdit_ym.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Ошибка",
                                           "Коэффиценты и координаты должны быть \n"
                                           "целыми или вещественными числами")
        self.copy_arr()
        for i in range(len(self.rhombus)):
            self.rhombus[i][0] = self.rhombus[i][0] * kx + (1 - kx) * xm
            self.rhombus[i][1] = self.rhombus[i][1] * ky + (1 - ky) * ym
        for i in range(len(self.snail)):
            self.snail[i][0] = self.snail[i][0] * kx + (1 - kx) * xm
            self.snail[i][1] = self.snail[i][1] * ky + (1 - ky) * ym
        for i in range(len(self.hatching)):
            self.hatching[i][0] = self.hatching[i][0] * kx + (1 - kx) * xm
            self.hatching[i][1] = self.hatching[i][1] * ky + (1 - ky) * ym
        for i in range(len(self.center)):
            self.center[i][0] = self.center[i][0] * kx + (1 - kx) * xm
            self.center[i][1] = self.center[i][1] * ky + (1 - ky) * ym
        self.draw()


    def draw_turn(self):
        '''
            Функция поворота фигуры.
        '''
        try:
            angle = float(self.lineEdit_angle.text())
            xc = float(self.lineEdit_xturn.text())
            yc = float(self.lineEdit_yturn.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Ошибка",
                                           "Угол и координаты должны быть \n"
                                           "целыми или вещественными числами")
        self.copy_arr()
        my_sin = sin(radians(360 - angle))
        my_cos = cos(radians(360 - angle))
        for i in range(len(self.rhombus)):
            x1 = xc + (self.rhombus[i][0] - xc) * my_cos + \
                 (self.rhombus[i][1] - yc) * my_sin
            self.rhombus[i][1] = yc + (self.rhombus[i][1] - yc) * my_cos - \
                                 (self.rhombus[i][0] - xc) * my_sin
            self.rhombus[i][0] = x1
        for i in range(len(self.snail)):
            x1 = xc + (self.snail[i][0] - xc) * my_cos + \
                 (self.snail[i][1] - yc) * my_sin
            self.snail[i][1] = yc + (self.snail[i][1] - yc) * my_cos - \
                                 (self.snail[i][0] - xc) * my_sin
            self.snail[i][0] = x1
        for i in range(len(self.hatching)):
            x1 = xc + (self.hatching[i][0] - xc) * my_cos + \
                 (self.hatching[i][1] - yc) * my_sin
            self.hatching[i][1] = yc + (self.hatching[i][1] - yc) * my_cos - \
                                 (self.hatching[i][0] - xc) * my_sin
            self.hatching[i][0] = x1
        for i in range(len(self.center)):
            x1 = xc + (self.center[i][0] - xc) * my_cos + \
                 (self.center[i][1] - yc) * my_sin
            self.center[i][1] = yc + (self.center[i][1] - yc) * my_cos - \
                                 (self.center[i][0] - xc) * my_sin
            self.center[i][0] = x1
        self.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()
