# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kozlova_lab_02(object):
    def setupUi(self, Kozlova_lab_02):
        Kozlova_lab_02.setObjectName("Kozlova_lab_02")
        Kozlova_lab_02.setEnabled(True)
        Kozlova_lab_02.resize(1300, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Kozlova_lab_02.sizePolicy().hasHeightForWidth())
        Kozlova_lab_02.setSizePolicy(sizePolicy)
        Kozlova_lab_02.setMinimumSize(QtCore.QSize(1300, 1000))
        Kozlova_lab_02.setMaximumSize(QtCore.QSize(1300, 1000))
        Kozlova_lab_02.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(Kozlova_lab_02)
        self.centralwidget.setObjectName("centralwidget")
        self.mode = QtWidgets.QGroupBox(self.centralwidget)
        self.mode.setGeometry(QtCore.QRect(20, 100, 381, 181))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mode.setFont(font)
        self.mode.setObjectName("mode")
        self.label_dx = QtWidgets.QLabel(self.mode)
        self.label_dx.setGeometry(QtCore.QRect(30, 90, 55, 31))
        self.label_dx.setObjectName("label_dx")
        self.label_dy = QtWidgets.QLabel(self.mode)
        self.label_dy.setGeometry(QtCore.QRect(200, 90, 55, 31))
        self.label_dy.setObjectName("label_dy")
        self.pushButton_mode = QtWidgets.QPushButton(self.mode)
        self.pushButton_mode.setGeometry(QtCore.QRect(250, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_mode.setFont(font)
        self.pushButton_mode.setObjectName("pushButton_mode")
        self.lineEdit_modex = QtWidgets.QLineEdit(self.mode)
        self.lineEdit_modex.setGeometry(QtCore.QRect(60, 90, 121, 31))
        self.lineEdit_modex.setObjectName("lineEdit_modex")
        self.lineEdit_modey = QtWidgets.QLineEdit(self.mode)
        self.lineEdit_modey.setGeometry(QtCore.QRect(230, 90, 121, 31))
        self.lineEdit_modey.setObjectName("lineEdit_modey")
        self.label_2 = QtWidgets.QLabel(self.mode)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 201, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_centermode_3 = QtWidgets.QLabel(self.mode)
        self.label_centermode_3.setGeometry(QtCore.QRect(20, 50, 271, 31))
        self.label_centermode_3.setObjectName("label_centermode_3")
        self.scale = QtWidgets.QGroupBox(self.centralwidget)
        self.scale.setGeometry(QtCore.QRect(20, 300, 381, 341))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.scale.setFont(font)
        self.scale.setFlat(False)
        self.scale.setCheckable(False)
        self.scale.setObjectName("scale")
        self.label_xm = QtWidgets.QLabel(self.scale)
        self.label_xm.setGeometry(QtCore.QRect(20, 130, 55, 31))
        self.label_xm.setObjectName("label_xm")
        self.label_ym = QtWidgets.QLabel(self.scale)
        self.label_ym.setGeometry(QtCore.QRect(190, 130, 55, 31))
        self.label_ym.setObjectName("label_ym")
        self.pushButton_scale = QtWidgets.QPushButton(self.scale)
        self.pushButton_scale.setGeometry(QtCore.QRect(250, 290, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_scale.setFont(font)
        self.pushButton_scale.setObjectName("pushButton_scale")
        self.lineEdit_xm = QtWidgets.QLineEdit(self.scale)
        self.lineEdit_xm.setGeometry(QtCore.QRect(60, 130, 121, 31))
        self.lineEdit_xm.setObjectName("lineEdit_xm")
        self.lineEdit_ym = QtWidgets.QLineEdit(self.scale)
        self.lineEdit_ym.setGeometry(QtCore.QRect(230, 130, 121, 31))
        self.lineEdit_ym.setObjectName("lineEdit_ym")
        self.label_centermode = QtWidgets.QLabel(self.scale)
        self.label_centermode.setGeometry(QtCore.QRect(20, 80, 271, 51))
        self.label_centermode.setObjectName("label_centermode")
        self.label_coef = QtWidgets.QLabel(self.scale)
        self.label_coef.setGeometry(QtCore.QRect(20, 200, 241, 51))
        self.label_coef.setObjectName("label_coef")
        self.label_ky = QtWidgets.QLabel(self.scale)
        self.label_ky.setGeometry(QtCore.QRect(200, 250, 55, 31))
        self.label_ky.setObjectName("label_ky")
        self.lineEdit_ky = QtWidgets.QLineEdit(self.scale)
        self.lineEdit_ky.setGeometry(QtCore.QRect(230, 250, 121, 31))
        self.lineEdit_ky.setObjectName("lineEdit_ky")
        self.lineEdit_kx = QtWidgets.QLineEdit(self.scale)
        self.lineEdit_kx.setGeometry(QtCore.QRect(60, 250, 121, 31))
        self.lineEdit_kx.setObjectName("lineEdit_kx")
        self.label_kx = QtWidgets.QLabel(self.scale)
        self.label_kx.setGeometry(QtCore.QRect(30, 250, 55, 31))
        self.label_kx.setObjectName("label_kx")
        self.label_3 = QtWidgets.QLabel(self.scale)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 201, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.turn = QtWidgets.QGroupBox(self.centralwidget)
        self.turn.setGeometry(QtCore.QRect(20, 660, 381, 271))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.turn.setFont(font)
        self.turn.setFlat(False)
        self.turn.setCheckable(False)
        self.turn.setObjectName("turn")
        self.pushButton_turn = QtWidgets.QPushButton(self.turn)
        self.pushButton_turn.setGeometry(QtCore.QRect(250, 220, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_turn.setFont(font)
        self.pushButton_turn.setObjectName("pushButton_turn")
        self.label_angle = QtWidgets.QLabel(self.turn)
        self.label_angle.setGeometry(QtCore.QRect(20, 60, 271, 41))
        self.label_angle.setObjectName("label_angle")
        self.label_centerturn = QtWidgets.QLabel(self.turn)
        self.label_centerturn.setGeometry(QtCore.QRect(20, 130, 361, 51))
        self.label_centerturn.setObjectName("label_centerturn")
        self.label_yturn = QtWidgets.QLabel(self.turn)
        self.label_yturn.setGeometry(QtCore.QRect(210, 170, 55, 41))
        self.label_yturn.setObjectName("label_yturn")
        self.lineEdit_yturn = QtWidgets.QLineEdit(self.turn)
        self.lineEdit_yturn.setGeometry(QtCore.QRect(230, 180, 121, 31))
        self.lineEdit_yturn.setObjectName("lineEdit_yturn")
        self.lineEdit_xturn = QtWidgets.QLineEdit(self.turn)
        self.lineEdit_xturn.setGeometry(QtCore.QRect(60, 180, 121, 31))
        self.lineEdit_xturn.setObjectName("lineEdit_xturn")
        self.label_xturn = QtWidgets.QLabel(self.turn)
        self.label_xturn.setGeometry(QtCore.QRect(40, 170, 55, 41))
        self.label_xturn.setObjectName("label_xturn")
        self.lineEdit_angle = QtWidgets.QLineEdit(self.turn)
        self.lineEdit_angle.setGeometry(QtCore.QRect(190, 60, 161, 31))
        self.lineEdit_angle.setObjectName("lineEdit_angle")
        self.info = QtWidgets.QGroupBox(self.centralwidget)
        self.info.setEnabled(True)
        self.info.setGeometry(QtCore.QRect(990, 10, 281, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.info.setFont(font)
        self.info.setMouseTracking(True)
        self.info.setTabletTracking(True)
        self.info.setAcceptDrops(False)
        self.info.setAutoFillBackground(False)
        self.info.setFlat(False)
        self.info.setCheckable(False)
        self.info.setObjectName("info")
        self.label_centerx = QtWidgets.QLabel(self.info)
        self.label_centerx.setGeometry(QtCore.QRect(10, 50, 55, 41))
        self.label_centerx.setObjectName("label_centerx")
        self.label_centery = QtWidgets.QLabel(self.info)
        self.label_centery.setGeometry(QtCore.QRect(150, 50, 55, 41))
        self.label_centery.setObjectName("label_centery")
        self.lineEdit_centerx = QtWidgets.QLineEdit(self.info)
        self.lineEdit_centerx.setEnabled(False)
        self.lineEdit_centerx.setGeometry(QtCore.QRect(30, 60, 101, 31))
        self.lineEdit_centerx.setDragEnabled(False)
        self.lineEdit_centerx.setObjectName("lineEdit_centerx")
        self.lineEdit_centery = QtWidgets.QLineEdit(self.info)
        self.lineEdit_centery.setEnabled(False)
        self.lineEdit_centery.setGeometry(QtCore.QRect(170, 60, 101, 31))
        self.lineEdit_centery.setObjectName("lineEdit_centery")
        self.pushButton_throw = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_throw.setGeometry(QtCore.QRect(340, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_throw.setFont(font)
        self.pushButton_throw.setObjectName("pushButton_throw")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(660, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(420, 120, 861, 821))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_oxy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_oxy.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_oxy.setFont(font)
        self.pushButton_oxy.setObjectName("pushButton_oxy")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 80, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Kozlova_lab_02.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Kozlova_lab_02)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        Kozlova_lab_02.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Kozlova_lab_02)
        self.statusbar.setObjectName("statusbar")
        Kozlova_lab_02.setStatusBar(self.statusbar)

        self.retranslateUi(Kozlova_lab_02)
        QtCore.QMetaObject.connectSlotsByName(Kozlova_lab_02)

    def retranslateUi(self, Kozlova_lab_02):
        _translate = QtCore.QCoreApplication.translate
        Kozlova_lab_02.setWindowTitle(_translate("Kozlova_lab_02", "MainWindow"))
        self.mode.setTitle(_translate("Kozlova_lab_02", "Перенос"))
        self.label_dx.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">dx</span></p></body></html>"))
        self.label_dy.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">dy</span></p></body></html>"))
        self.pushButton_mode.setText(_translate("Kozlova_lab_02", "Перенос"))
        self.label_centermode_3.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:14pt;\">Значение в пикселях</span></p><p><span style=\" font-size:14pt;\"><br/></span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.scale.setTitle(_translate("Kozlova_lab_02", "Масштаб"))
        self.label_xm.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">Xm</span></p></body></html>"))
        self.label_ym.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">Ym</span></p><p><span style=\" font-size:20pt;\"><br/></span></p></body></html>"))
        self.pushButton_scale.setText(_translate("Kozlova_lab_02", "Масштаб"))
        self.label_centermode.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:14pt;\">Центр масштабирования<br/>(значение в пикселях)</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label_coef.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:14pt;\">Коэффециенты<br/>масштабирования</span></p></body></html>"))
        self.label_ky.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">ky</span></p></body></html>"))
        self.label_kx.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">kx</span></p></body></html>"))
        self.turn.setTitle(_translate("Kozlova_lab_02", "Поворот"))
        self.pushButton_turn.setText(_translate("Kozlova_lab_02", "Поворот"))
        self.label_angle.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:14pt;\">Угол (в градусах)</span></p><p><span style=\" font-size:14pt;\"><br/></span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label_centerturn.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:14pt;\">Центр вращения <br/>(значение в пикселях)<br/></span></p></body></html>"))
        self.label_yturn.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">y</span></p></body></html>"))
        self.label_xturn.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">x</span></p></body></html>"))
        self.info.setTitle(_translate("Kozlova_lab_02", "Центр Фигуры"))
        self.label_centerx.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">x</span></p></body></html>"))
        self.label_centery.setText(_translate("Kozlova_lab_02", "<html><head/><body><p><span style=\" font-size:20pt;\">y</span></p></body></html>"))
        self.pushButton_throw.setText(_translate("Kozlova_lab_02", "Изначальное изображение"))
        self.pushButton_back.setText(_translate("Kozlova_lab_02", "Назад"))
        self.pushButton_oxy.setText(_translate("Kozlova_lab_02", "Показать оси координат"))
        self.label.setText(_translate("Kozlova_lab_02", "Отметки на осях координат поставлены по 50 пикселей"))
