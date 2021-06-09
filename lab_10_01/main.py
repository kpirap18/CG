import sys
import win2

from func import funcs
from draw_hor import float_horizon


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
                dy = y2 - y1
                if abs(y2 - y1) < 1e-6:
                    dy = 1

                k1 = int(self.h / dy) - 7
                k2 = int(self.w / (x_e - x_b)) - 7 

                print("SCALE START", k1, k2)
                self.scale_k = min(k1, k2)
        self.x_begin = int(x_b)
        self.x_end = int(x_e)
        self.x_step = x_s

        self.z_begin = int(z_b)
        self.z_end = int(z_e)
        self.z_step = z_s

    def draw_res(self):

        # print("draw_res", self.alpha_x, self.alpha_y, self.alpha_z)
        self.scene.clear()
        self.image.fill(QtCore.Qt.white)

        self.read_x_z_value()

        self.image = float_horizon(self)

        p = QPixmap()
        p.convertFromImage(self.image)
        self.scene.addPixmap(p)


def main():
    global wind
    app = QtWidgets.QApplication(sys.argv)
    wind = Visual()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()