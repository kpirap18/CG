# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1020)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 1020))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 1020))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 420, 621, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBoxChooseDRAW_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBoxChooseDRAW_3.setMinimumSize(QtCore.QSize(600, 200))
        self.groupBoxChooseDRAW_3.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBoxChooseDRAW_3.setFont(font)
        self.groupBoxChooseDRAW_3.setTitle("")
        self.groupBoxChooseDRAW_3.setObjectName("groupBoxChooseDRAW_3")
        self.label_3 = QtWidgets.QLabel(self.groupBoxChooseDRAW_3)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 16, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_x_begin = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_x_begin.setGeometry(QtCore.QRect(30, 80, 113, 25))
        self.lineEdit_x_begin.setObjectName("lineEdit_x_begin")
        self.lineEdit_x_end = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_x_end.setGeometry(QtCore.QRect(190, 80, 113, 25))
        self.lineEdit_x_end.setObjectName("lineEdit_x_end")
        self.lineEdit_z_begin = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_z_begin.setGeometry(QtCore.QRect(30, 120, 113, 25))
        self.lineEdit_z_begin.setObjectName("lineEdit_z_begin")
        self.label_5 = QtWidgets.QLabel(self.groupBoxChooseDRAW_3)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 16, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_z_end = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_z_end.setGeometry(QtCore.QRect(190, 120, 113, 25))
        self.lineEdit_z_end.setObjectName("lineEdit_z_end")
        self.lineEdit_x_step = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_x_step.setGeometry(QtCore.QRect(350, 80, 113, 25))
        self.lineEdit_x_step.setObjectName("lineEdit_x_step")
        self.lineEdit_z_step = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_3)
        self.lineEdit_z_step.setGeometry(QtCore.QRect(350, 120, 113, 25))
        self.lineEdit_z_step.setObjectName("lineEdit_z_step")
        self.label_2 = QtWidgets.QLabel(self.groupBoxChooseDRAW_3)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 421, 31))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.groupBoxChooseDRAW_3)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBoxChooseDRAW_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBoxChooseDRAW_4.setMinimumSize(QtCore.QSize(600, 200))
        self.groupBoxChooseDRAW_4.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseDRAW_4.setFont(font)
        self.groupBoxChooseDRAW_4.setTitle("")
        self.groupBoxChooseDRAW_4.setObjectName("groupBoxChooseDRAW_4")
        self.label_4 = QtWidgets.QLabel(self.groupBoxChooseDRAW_4)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_k = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_4)
        self.lineEdit_k.setGeometry(QtCore.QRect(110, 40, 113, 25))
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.lineEdit_z_turn = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_4)
        self.lineEdit_z_turn.setGeometry(QtCore.QRect(110, 160, 113, 25))
        self.lineEdit_z_turn.setObjectName("lineEdit_z_turn")
        self.lineEdit_x_turn = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_4)
        self.lineEdit_x_turn.setGeometry(QtCore.QRect(110, 80, 113, 25))
        self.lineEdit_x_turn.setObjectName("lineEdit_x_turn")
        self.lineEdit_y_turn = QtWidgets.QLineEdit(self.groupBoxChooseDRAW_4)
        self.lineEdit_y_turn.setGeometry(QtCore.QRect(110, 120, 113, 25))
        self.lineEdit_y_turn.setObjectName("lineEdit_y_turn")
        self.label_7 = QtWidgets.QLabel(self.groupBoxChooseDRAW_4)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 91, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBoxChooseDRAW_4)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBoxChooseDRAW_4)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 91, 20))
        self.label_9.setObjectName("label_9")
        self.pushButton_k = QtWidgets.QPushButton(self.groupBoxChooseDRAW_4)
        self.pushButton_k.setGeometry(QtCore.QRect(250, 40, 89, 25))
        self.pushButton_k.setObjectName("pushButton_k")
        self.pushButton_x_turn = QtWidgets.QPushButton(self.groupBoxChooseDRAW_4)
        self.pushButton_x_turn.setGeometry(QtCore.QRect(250, 80, 89, 25))
        self.pushButton_x_turn.setObjectName("pushButton_x_turn")
        self.pushButton_y_turn = QtWidgets.QPushButton(self.groupBoxChooseDRAW_4)
        self.pushButton_y_turn.setGeometry(QtCore.QRect(250, 120, 89, 25))
        self.pushButton_y_turn.setObjectName("pushButton_y_turn")
        self.pushButton_z_turn = QtWidgets.QPushButton(self.groupBoxChooseDRAW_4)
        self.pushButton_z_turn.setGeometry(QtCore.QRect(250, 160, 89, 25))
        self.pushButton_z_turn.setObjectName("pushButton_z_turn")
        self.horizontalLayout_10.addWidget(self.groupBoxChooseDRAW_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(630, 20, 961, 881))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_clean = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clean.setGeometry(QtCore.QRect(10, 940, 601, 31))
        self.pushButton_clean.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_clean.setFont(font)
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 0, 131, 17))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 621, 162))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxChooserwRESULT = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBoxChooserwRESULT.setMinimumSize(QtCore.QSize(145, 160))
        self.groupBoxChooserwRESULT.setMaximumSize(QtCore.QSize(145, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooserwRESULT.setFont(font)
        self.groupBoxChooserwRESULT.setObjectName("groupBoxChooserwRESULT")
        self.radioButtonWhite_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonWhite_res.setGeometry(QtCore.QRect(10, 50, 166, 20))
        self.radioButtonWhite_res.setChecked(False)
        self.radioButtonWhite_res.setObjectName("radioButtonWhite_res")
        self.radioButtonBlack_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonBlack_res.setGeometry(QtCore.QRect(10, 70, 166, 20))
        self.radioButtonBlack_res.setObjectName("radioButtonBlack_res")
        self.radioButtonRed_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonRed_res.setGeometry(QtCore.QRect(10, 30, 166, 20))
        self.radioButtonRed_res.setChecked(True)
        self.radioButtonRed_res.setObjectName("radioButtonRed_res")
        self.radioButtonYellow_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonYellow_res.setGeometry(QtCore.QRect(10, 90, 166, 20))
        self.radioButtonYellow_res.setObjectName("radioButtonYellow_res")
        self.radioButtonGreen_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonGreen_res.setGeometry(QtCore.QRect(10, 110, 181, 20))
        self.radioButtonGreen_res.setObjectName("radioButtonGreen_res")
        self.radioButtonBlue_res = QtWidgets.QRadioButton(self.groupBoxChooserwRESULT)
        self.radioButtonBlue_res.setGeometry(QtCore.QRect(10, 130, 176, 20))
        self.radioButtonBlue_res.setObjectName("radioButtonBlue_res")
        self.horizontalLayout.addWidget(self.groupBoxChooserwRESULT)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 170, 621, 241))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBoxChooseDRAW = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBoxChooseDRAW.setMinimumSize(QtCore.QSize(600, 200))
        self.groupBoxChooseDRAW.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBoxChooseDRAW.setFont(font)
        self.groupBoxChooseDRAW.setObjectName("groupBoxChooseDRAW")
        self.radioButton_func_1 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_1.setGeometry(QtCore.QRect(20, 40, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_1.setFont(font)
        self.radioButton_func_1.setChecked(True)
        self.radioButton_func_1.setObjectName("radioButton_func_1")
        self.radioButton_func_4 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_4.setGeometry(QtCore.QRect(330, 40, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_4.setFont(font)
        self.radioButton_func_4.setChecked(False)
        self.radioButton_func_4.setObjectName("radioButton_func_4")
        self.radioButton_func_2 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_2.setGeometry(QtCore.QRect(20, 80, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_2.setFont(font)
        self.radioButton_func_2.setChecked(False)
        self.radioButton_func_2.setObjectName("radioButton_func_2")
        self.radioButton_func_5 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_5.setGeometry(QtCore.QRect(330, 90, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_5.setFont(font)
        self.radioButton_func_5.setObjectName("radioButton_func_5")
        self.radioButton_func_3 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_3.setGeometry(QtCore.QRect(20, 130, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_3.setFont(font)
        self.radioButton_func_3.setChecked(False)
        self.radioButton_func_3.setObjectName("radioButton_func_3")
        self.radioButton_func_6 = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_func_6.setGeometry(QtCore.QRect(330, 140, 166, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_func_6.setFont(font)
        self.radioButton_func_6.setObjectName("radioButton_func_6")
        self.horizontalLayout_8.addWidget(self.groupBoxChooseDRAW)
        self.pushButton_RES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RES.setGeometry(QtCore.QRect(10, 900, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_RES.setFont(font)
        self.pushButton_RES.setObjectName("pushButton_RES")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Козлова Ирина, ИУ7-42Б, Лабораторная работа №10"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.lineEdit_x_begin.setText(_translate("MainWindow", "-10"))
        self.lineEdit_x_end.setText(_translate("MainWindow", "10"))
        self.lineEdit_z_begin.setText(_translate("MainWindow", "-10"))
        self.label_5.setText(_translate("MainWindow", "Z"))
        self.lineEdit_z_end.setText(_translate("MainWindow", "10"))
        self.lineEdit_x_step.setText(_translate("MainWindow", "0.2"))
        self.lineEdit_z_step.setText(_translate("MainWindow", "0.2"))
        self.label_2.setText(_translate("MainWindow", "От                            До                          Шаг"))
        self.label_4.setText(_translate("MainWindow", "Масштаб"))
        self.lineEdit_k.setText(_translate("MainWindow", "48"))
        self.lineEdit_z_turn.setText(_translate("MainWindow", "20"))
        self.lineEdit_x_turn.setText(_translate("MainWindow", "20"))
        self.lineEdit_y_turn.setText(_translate("MainWindow", "20"))
        self.label_7.setText(_translate("MainWindow", "Y"))
        self.label_8.setText(_translate("MainWindow", "X"))
        self.label_9.setText(_translate("MainWindow", "Z"))
        self.pushButton_k.setText(_translate("MainWindow", "Масштаб"))
        self.pushButton_x_turn.setText(_translate("MainWindow", "Поворот"))
        self.pushButton_y_turn.setText(_translate("MainWindow", "Поворот"))
        self.pushButton_z_turn.setText(_translate("MainWindow", "Поворот"))
        self.pushButton_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.label.setText(_translate("MainWindow", "Рабочее место"))
        self.groupBoxChooserwRESULT.setTitle(_translate("MainWindow", "Цвет"))
        self.radioButtonWhite_res.setText(_translate("MainWindow", "Белый"))
        self.radioButtonBlack_res.setText(_translate("MainWindow", "Черный"))
        self.radioButtonRed_res.setText(_translate("MainWindow", "Красный"))
        self.radioButtonYellow_res.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_res.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonBlue_res.setText(_translate("MainWindow", "Синий"))
        self.groupBoxChooseDRAW.setTitle(_translate("MainWindow", "ФУНКЦИЯ"))
        self.radioButton_func_1.setText(_translate("MainWindow", "sin(x) * sin(z)"))
        self.radioButton_func_4.setText(_translate("MainWindow", "sqrt(x * x / 3 + z * z)"))
        self.radioButton_func_2.setText(_translate("MainWindow", "sin(cos(x)) * sin(z)"))
        self.radioButton_func_5.setText(_translate("MainWindow", "cos(x) * cos(z)"))
        self.radioButton_func_3.setText(_translate("MainWindow", "x + z"))
        self.radioButton_func_6.setText(_translate("MainWindow", "cos(sin(x * z))"))
        self.pushButton_RES.setText(_translate("MainWindow", "Нарисовать"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "О программе"))
