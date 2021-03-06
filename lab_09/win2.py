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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 621, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBoxChooseBG_8 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBoxChooseBG_8.setMinimumSize(QtCore.QSize(350, 250))
        self.groupBoxChooseBG_8.setMaximumSize(QtCore.QSize(350, 250))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseBG_8.setFont(font)
        self.groupBoxChooseBG_8.setObjectName("groupBoxChooseBG_8")
        self.label_2 = QtWidgets.QLabel(self.groupBoxChooseBG_8)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBoxChooseBG_8)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_x_cut = QtWidgets.QLineEdit(self.groupBoxChooseBG_8)
        self.lineEdit_x_cut.setGeometry(QtCore.QRect(110, 40, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_x_cut.setFont(font)
        self.lineEdit_x_cut.setObjectName("lineEdit_x_cut")
        self.lineEdit_y_cut = QtWidgets.QLineEdit(self.groupBoxChooseBG_8)
        self.lineEdit_y_cut.setGeometry(QtCore.QRect(110, 70, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_y_cut.setFont(font)
        self.lineEdit_y_cut.setObjectName("lineEdit_y_cut")
        self.pushButton_draw_cut = QtWidgets.QPushButton(self.groupBoxChooseBG_8)
        self.pushButton_draw_cut.setGeometry(QtCore.QRect(100, 110, 231, 41))
        self.pushButton_draw_cut.setObjectName("pushButton_draw_cut")
        self.pushButton_end_cut = QtWidgets.QPushButton(self.groupBoxChooseBG_8)
        self.pushButton_end_cut.setGeometry(QtCore.QRect(100, 180, 231, 41))
        self.pushButton_end_cut.setObjectName("pushButton_end_cut")
        self.horizontalLayout_9.addWidget(self.groupBoxChooseBG_8)
        self.table_cut = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_cut.setMinimumSize(QtCore.QSize(220, 250))
        self.table_cut.setMaximumSize(QtCore.QSize(220, 250))
        self.table_cut.setObjectName("table_cut")
        self.table_cut.setColumnCount(2)
        self.table_cut.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.table_cut.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.table_cut.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_9.addWidget(self.table_cut)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBoxChooseBG_9 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBoxChooseBG_9.setMinimumSize(QtCore.QSize(350, 250))
        self.groupBoxChooseBG_9.setMaximumSize(QtCore.QSize(350, 250))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseBG_9.setFont(font)
        self.groupBoxChooseBG_9.setObjectName("groupBoxChooseBG_9")
        self.label_6 = QtWidgets.QLabel(self.groupBoxChooseBG_9)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBoxChooseBG_9)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_x_rest = QtWidgets.QLineEdit(self.groupBoxChooseBG_9)
        self.lineEdit_x_rest.setGeometry(QtCore.QRect(110, 40, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_x_rest.setFont(font)
        self.lineEdit_x_rest.setObjectName("lineEdit_x_rest")
        self.lineEdit_y_rest = QtWidgets.QLineEdit(self.groupBoxChooseBG_9)
        self.lineEdit_y_rest.setGeometry(QtCore.QRect(110, 70, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_y_rest.setFont(font)
        self.lineEdit_y_rest.setObjectName("lineEdit_y_rest")
        self.pushButton_draw_rest = QtWidgets.QPushButton(self.groupBoxChooseBG_9)
        self.pushButton_draw_rest.setGeometry(QtCore.QRect(100, 120, 231, 41))
        self.pushButton_draw_rest.setObjectName("pushButton_draw_rest")
        self.label_11 = QtWidgets.QLabel(self.groupBoxChooseBG_9)
        self.label_11.setGeometry(QtCore.QRect(250, 40, 101, 31))
        self.label_11.setObjectName("label_11")
        self.spinBox_w = QtWidgets.QSpinBox(self.groupBoxChooseBG_9)
        self.spinBox_w.setGeometry(QtCore.QRect(260, 70, 61, 31))
        self.spinBox_w.setProperty("value", 2)
        self.spinBox_w.setObjectName("spinBox_w")
        self.pushButton_end_rest = QtWidgets.QPushButton(self.groupBoxChooseBG_9)
        self.pushButton_end_rest.setGeometry(QtCore.QRect(100, 180, 231, 41))
        self.pushButton_end_rest.setObjectName("pushButton_end_rest")
        self.horizontalLayout_11.addWidget(self.groupBoxChooseBG_9)
        self.table_rest = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_rest.setMinimumSize(QtCore.QSize(220, 250))
        self.table_rest.setMaximumSize(QtCore.QSize(220, 250))
        self.table_rest.setObjectName("table_rest")
        self.table_rest.setColumnCount(2)
        self.table_rest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.table_rest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.table_rest.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_11.addWidget(self.table_rest)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
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
        self.groupBoxChooseREST = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBoxChooseREST.setMinimumSize(QtCore.QSize(145, 160))
        self.groupBoxChooseREST.setMaximumSize(QtCore.QSize(145, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseREST.setFont(font)
        self.groupBoxChooseREST.setObjectName("groupBoxChooseREST")
        self.radioButtonWhite_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonWhite_rest.setGeometry(QtCore.QRect(10, 50, 166, 20))
        self.radioButtonWhite_rest.setChecked(False)
        self.radioButtonWhite_rest.setObjectName("radioButtonWhite_rest")
        self.radioButtonBlack_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonBlack_rest.setGeometry(QtCore.QRect(10, 30, 166, 20))
        self.radioButtonBlack_rest.setChecked(True)
        self.radioButtonBlack_rest.setObjectName("radioButtonBlack_rest")
        self.radioButtonRed_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonRed_rest.setGeometry(QtCore.QRect(10, 110, 166, 20))
        self.radioButtonRed_rest.setObjectName("radioButtonRed_rest")
        self.radioButtonYellow_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonYellow_rest.setGeometry(QtCore.QRect(10, 70, 166, 20))
        self.radioButtonYellow_rest.setObjectName("radioButtonYellow_rest")
        self.radioButtonGreen_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonGreen_rest.setGeometry(QtCore.QRect(10, 90, 181, 20))
        self.radioButtonGreen_rest.setObjectName("radioButtonGreen_rest")
        self.radioButtonBlue_rest = QtWidgets.QRadioButton(self.groupBoxChooseREST)
        self.radioButtonBlue_rest.setGeometry(QtCore.QRect(10, 130, 176, 20))
        self.radioButtonBlue_rest.setObjectName("radioButtonBlue_rest")
        self.horizontalLayout.addWidget(self.groupBoxChooseREST)
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
        self.groupBoxChooseLINE = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBoxChooseLINE.setMinimumSize(QtCore.QSize(160, 160))
        self.groupBoxChooseLINE.setMaximumSize(QtCore.QSize(160, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseLINE.setFont(font)
        self.groupBoxChooseLINE.setObjectName("groupBoxChooseLINE")
        self.radioButtonWhite_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonWhite_line.setGeometry(QtCore.QRect(10, 50, 166, 20))
        self.radioButtonWhite_line.setChecked(False)
        self.radioButtonWhite_line.setObjectName("radioButtonWhite_line")
        self.radioButtonBlack_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonBlack_line.setGeometry(QtCore.QRect(10, 70, 166, 20))
        self.radioButtonBlack_line.setObjectName("radioButtonBlack_line")
        self.radioButtonRed_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonRed_line.setGeometry(QtCore.QRect(10, 110, 166, 20))
        self.radioButtonRed_line.setObjectName("radioButtonRed_line")
        self.radioButtonYellow_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonYellow_line.setGeometry(QtCore.QRect(10, 90, 166, 20))
        self.radioButtonYellow_line.setObjectName("radioButtonYellow_line")
        self.radioButtonGreen_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonGreen_line.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.radioButtonGreen_line.setChecked(True)
        self.radioButtonGreen_line.setObjectName("radioButtonGreen_line")
        self.radioButtonBlue_line = QtWidgets.QRadioButton(self.groupBoxChooseLINE)
        self.radioButtonBlue_line.setGeometry(QtCore.QRect(10, 130, 176, 20))
        self.radioButtonBlue_line.setObjectName("radioButtonBlue_line")
        self.horizontalLayout.addWidget(self.groupBoxChooseLINE)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 170, 621, 102))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBoxChooseDRAW = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBoxChooseDRAW.setMinimumSize(QtCore.QSize(600, 90))
        self.groupBoxChooseDRAW.setMaximumSize(QtCore.QSize(500, 90))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBoxChooseDRAW.setFont(font)
        self.groupBoxChooseDRAW.setObjectName("groupBoxChooseDRAW")
        self.radioButton_draw_line = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_draw_line.setGeometry(QtCore.QRect(20, 50, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_draw_line.setFont(font)
        self.radioButton_draw_line.setChecked(True)
        self.radioButton_draw_line.setObjectName("radioButton_draw_line")
        self.radioButton_draw_rest = QtWidgets.QRadioButton(self.groupBoxChooseDRAW)
        self.radioButton_draw_rest.setGeometry(QtCore.QRect(410, 50, 166, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_draw_rest.setFont(font)
        self.radioButton_draw_rest.setObjectName("radioButton_draw_rest")
        self.horizontalLayout_8.addWidget(self.groupBoxChooseDRAW)
        self.pushButton_RES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RES.setGeometry(QtCore.QRect(10, 900, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_RES.setFont(font)
        self.pushButton_RES.setObjectName("pushButton_RES")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(630, 900, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1080, 900, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.groupBoxChooseLINE_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxChooseLINE_2.setGeometry(QtCore.QRect(70, 840, 500, 50))
        self.groupBoxChooseLINE_2.setMinimumSize(QtCore.QSize(500, 50))
        self.groupBoxChooseLINE_2.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxChooseLINE_2.setFont(font)
        self.groupBoxChooseLINE_2.setObjectName("groupBoxChooseLINE_2")
        self.radioButton_FALSE_BE = QtWidgets.QRadioButton(self.groupBoxChooseLINE_2)
        self.radioButton_FALSE_BE.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.radioButton_FALSE_BE.setObjectName("radioButton_FALSE_BE")
        self.radioButton_FALSE_DEL = QtWidgets.QRadioButton(self.groupBoxChooseLINE_2)
        self.radioButton_FALSE_DEL.setGeometry(QtCore.QRect(240, 30, 231, 20))
        self.radioButton_FALSE_DEL.setChecked(True)
        self.radioButton_FALSE_DEL.setObjectName("radioButton_FALSE_DEL")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Козлова Ирина, ИУ7-42Б, Лабораторная работа 9"))
        self.groupBoxChooseBG_8.setTitle(_translate("MainWindow", "Ввод отсекателя "))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Х"))
        self.lineEdit_x_cut.setText(_translate("MainWindow", "100"))
        self.lineEdit_y_cut.setText(_translate("MainWindow", "100"))
        self.pushButton_draw_cut.setText(_translate("MainWindow", "Ввести точку"))
        self.pushButton_end_cut.setText(_translate("MainWindow", "Замкнуть контур"))
        item = self.table_cut.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.table_cut.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.groupBoxChooseBG_9.setTitle(_translate("MainWindow", "Ввод отсекаемого многоугольника"))
        self.label_6.setText(_translate("MainWindow", "У "))
        self.label_7.setText(_translate("MainWindow", "Х "))
        self.lineEdit_x_rest.setText(_translate("MainWindow", "100"))
        self.lineEdit_y_rest.setText(_translate("MainWindow", "100"))
        self.pushButton_draw_rest.setText(_translate("MainWindow", "Ввести точку"))
        self.label_11.setText(_translate("MainWindow", "Толщина"))
        self.pushButton_end_rest.setText(_translate("MainWindow", "Замкнуть контур"))
        item = self.table_rest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.table_rest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.pushButton_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.label.setText(_translate("MainWindow", "Рабочее место"))
        self.groupBoxChooseREST.setTitle(_translate("MainWindow", "Отсекатель"))
        self.radioButtonWhite_rest.setText(_translate("MainWindow", "Белый"))
        self.radioButtonBlack_rest.setText(_translate("MainWindow", "Черный"))
        self.radioButtonRed_rest.setText(_translate("MainWindow", "Красный"))
        self.radioButtonYellow_rest.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_rest.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonBlue_rest.setText(_translate("MainWindow", "Синий"))
        self.groupBoxChooserwRESULT.setTitle(_translate("MainWindow", "Отсечение"))
        self.radioButtonWhite_res.setText(_translate("MainWindow", "Белый"))
        self.radioButtonBlack_res.setText(_translate("MainWindow", "Черный"))
        self.radioButtonRed_res.setText(_translate("MainWindow", "Красный"))
        self.radioButtonYellow_res.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_res.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonBlue_res.setText(_translate("MainWindow", "Синий"))
        self.groupBoxChooseLINE.setTitle(_translate("MainWindow", "Отсекаемый мн-ник"))
        self.radioButtonWhite_line.setText(_translate("MainWindow", "Белый"))
        self.radioButtonBlack_line.setText(_translate("MainWindow", "Черный"))
        self.radioButtonRed_line.setText(_translate("MainWindow", "Красный"))
        self.radioButtonYellow_line.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_line.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonBlue_line.setText(_translate("MainWindow", "Синий"))
        self.groupBoxChooseDRAW.setTitle(_translate("MainWindow", "РИСОВАНИЕ"))
        self.radioButton_draw_line.setText(_translate("MainWindow", "Отсекаемый многоугольник"))
        self.radioButton_draw_rest.setText(_translate("MainWindow", "Отсекатель"))
        self.pushButton_RES.setText(_translate("MainWindow", "Отсечение"))
        self.label_12.setText(_translate("MainWindow", "Для отрисовки горизонтальных и вертикальных линий:\n"
"1 - Нарисуйте первую вершину отрезка\n"
"2 - Зажмите кнопку CTRL и нарисуйте вторую вершину"))
        self.label_13.setText(_translate("MainWindow", "Для отрисовки отсекателя:\n"
"1 - Нарисуйте верхнюю левую вершину \n"
"2 - В случае добавления точки на границу отсекателя, \n"
" нажмите на среднюю кнопку, (точка будет на ближней стороне)"))
        self.groupBoxChooseLINE_2.setTitle(_translate("MainWindow", "ЛОЖНЫЕ РЕБРА"))
        self.radioButton_FALSE_BE.setText(_translate("MainWindow", "ОСТАВИТЬ"))
        self.radioButton_FALSE_DEL.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "О программе"))
