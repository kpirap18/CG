import design  # мой интерфейс
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPen, QImage, QPixmap, QPainter, QBrush, QPolygon, QColor
from PyQt5.QtCore import Qt, QPoint
from sh_cut import *
import sys
from copy import deepcopy

global w

MINDIST = 15


# код цвета по названию
def find_color_code(color_name):
    if color_name == 'Красный':
        return Qt.red
    elif color_name == 'Зеленый':
        return Qt.green
    elif color_name == 'Синий':
        return Qt.darkBlue
    elif color_name == 'Желтый':
        return Qt.yellow
    elif color_name == 'Голубой':
        return Qt.blue
    elif color_name == 'Бирюзовый':
        return Qt.cyan
    elif color_name == 'Розовый':
        return Qt.magenta
    elif color_name == 'Черный':
        return Qt.black


# для добаления точки по нажатию мышкой
class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        point = [round(event.scenePos().x()), round(event.scenePos().y())]
        if event.buttons() == Qt.LeftButton:
            w.add_segmennt_point_pic(point)
        if event.buttons() == Qt.RightButton:
            w.add_cutter_point(point)


class MyWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # для доступа к переменным, методам и т.д. в файле design.py
        super().__init__()
        # инициализация дизайна
        self.setupUi(self)
        # настройка кнопок
        self.but_clean.clicked.connect(self.on_bt_clean_clicked)
        self.but_connect_cutter.clicked.connect(self.on_bt_connect_cutter_clicked)
        self.but_connect_segment.clicked.connect(self.on_bt_connect_segment_clicked)
        self.but_input_point_cutter.clicked.connect(self.on_bt_input_point_cutter_clicked)
        self.but_input_point_segment.clicked.connect(self.on_bt_input_point_segment_clicked)
        self.but_cut.clicked.connect(self.on_bt_cut_clicked)

        self.color_back = Qt.white
        self.color_cutter = None
        self.color_segment = None
        self.color_result = None

        self.cutter_points = []
        self.direction = 0
        self.segment_points = []

        # создание сцены
        self.scene = myScene(0, 0, 1600, 1100)
        self.scene.win = self
        self.graph.setScene(self.scene)
        # изображение
        self.image = QImage(1600, 1100, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(self.color_back)

    # обработка ошибки
    def handle_error(self, title, error):
        em = QtWidgets.QMessageBox(self.centralwidget)
        em.setText(error)
        em.setWindowTitle(title)
        em.exec()

    # очистка экрана и данных
    def on_bt_clean_clicked(self):
        self.scene.clear()
        self.image.fill(self.color_back)

        for i in range(self.table_cutter.rowCount(), -1, -1):
            self.table_cutter.removeRow(i)
        self.table_cutter.clearContents()

        for i in range(self.table_segments.rowCount(), -1, -1):
            self.table_segments.removeRow(i)
        self.table_segments.clearContents()

        self.color_back = Qt.white
        self.color_cutter = None
        self.color_segment = None
        self.color_result = None

        self.cutter_points = []
        self.segment_points = []
        self.direction = 0

    # добавление строки в таблицу
    def add_row_to_table_cutter(self):
        self.table_cutter.insertRow(self.table_cutter.rowCount())

    def add_row_to_table_segments(self):
        self.table_segments.insertRow(self.table_segments.rowCount())

    # настройка цвета отсекателя
    def get_color_cutter(self):
        color_name = self.box_color_cutter.currentText()
        color_code = find_color_code(color_name)
        self.color_cutter = color_code

    # настройка цвета отрезков
    def get_color_segment(self):
        color_name = self.box_color_segment.currentText()
        color_code = find_color_code(color_name)
        self.color_segment = color_code

    # настройка цвета результата
    def get_color_result(self):
        color_name = self.box_color_result.currentText()
        color_code = find_color_code(color_name)
        self.color_result = color_code

    def add_segmennt_point_pic(self, point):
        min_dist = MINDIST + 2
        closest_point = None
        if len(self.cutter_points) > 1:
            for i in range(len(self.cutter_points) - 1):
                cur_dist, cur_closest = dist_to_edge(point, self.cutter_points[i], self.cutter_points[i + 1])
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    closest_point = cur_closest
            cur_dist, cur_closest = dist_to_edge(point, self.cutter_points[1], self.cutter_points[-1])
            if cur_dist < min_dist:
                min_dist = cur_dist
                closest_point = cur_closest

            if min_dist <= MINDIST:
                point = list(map(round, closest_point))

        self.add_segment_point(point)

    # общий алгоритм добавления вершины отcекаемого
    def add_segment_point(self, point):
        self.segment_points.append(point)
        self.draw_segments()

        # добавление в таблицу
        i = self.table_segments.rowCount()
        self.add_row_to_table_segments()
        x = QTableWidgetItem("{}".format(point[0]))
        y = QTableWidgetItem("{}".format(point[1]))
        self.table_segments.setItem(i, 0, x)
        self.table_segments.setItem(i, 1, y)

    # добавление вершины отсекаемого по кнопке
    def on_bt_input_point_segment_clicked(self):
        self.add_segment_point([self.box_x.value(), self.box_y.value()])

    # отрисовка отсекаемого
    def draw_segments(self):
        p = QPainter()
        p.begin(self.image)
        self.get_color_segment()
        p.setPen(QPen(self.color_segment))
        for i in range(len(self.segment_points) - 1):
            segment = [self.segment_points[i][0], self.segment_points[i][1],
                       self.segment_points[i + 1][0], self.segment_points[i + 1][1]]
            self.my_darw_line(p, segment)

        if len(self.segment_points) == 1:
            segment = [self.segment_points[0][0], self.segment_points[0][1],
                       self.segment_points[0][0], self.segment_points[0][1]]
            self.my_darw_line(p, segment)
        p.end()

        pix = QPixmap()  # отрисовываемая картинка
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)

    # замыкание контура отсекаемого
    def on_bt_connect_segment_clicked(self):
        if not self.segment_points:
            self.handle_error("Ошибка", "Не было введено ни одной точки отсекаемого")
        else:
            self.add_segment_point(self.segment_points[0])

    # отрисовка отсекателя
    def draw_cutter(self):
        p = QPainter()
        p.begin(self.image)
        self.get_color_cutter()
        p.setPen(QPen(self.color_cutter))
        for i in range(len(self.cutter_points) - 1):
            segment = [self.cutter_points[i][0], self.cutter_points[i][1],
                       self.cutter_points[i + 1][0], self.cutter_points[i + 1][1]]
            self.my_darw_line(p, segment)

        if len(self.cutter_points) == 1:
            segment = [self.cutter_points[0][0], self.cutter_points[0][1],
                       self.cutter_points[0][0], self.cutter_points[0][1]]
            self.my_darw_line(p, segment)
        p.end()

        pix = QPixmap()  # отрисовываемая картинка
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)

    # добавление вершины отcекателя по кнопке
    def on_bt_input_point_cutter_clicked(self):
        self.add_cutter_point([self.box_x.value(), self.box_y.value()])

    # добавление вершины отсекателя
    def add_cutter_point(self, point):
        cur_direction = 0
        if len(self.cutter_points) > 1:
            cur_direction = vect_mult_sign_z(self.cutter_points[-2], self.cutter_points[-1], point)
            if self.direction == 0:
                self.direction = cur_direction

        if (self.direction != cur_direction) and (self.direction != 0) and (cur_direction != 0):
            self.handle_error('Ошибка.', 'Отсекатель должен быть выпуклым многоугольником')
            return

        self.cutter_points.append(point)
        self.draw_cutter()

        # добавление в таблицу
        i = self.table_cutter.rowCount()
        self.add_row_to_table_cutter()
        x = QTableWidgetItem("{}".format(point[0]))
        y = QTableWidgetItem("{}".format(point[1]))
        self.table_cutter.setItem(i, 0, x)
        self.table_cutter.setItem(i, 1, y)

    # замыкание контура отсекателя
    def on_bt_connect_cutter_clicked(self):
        if not self.cutter_points:
            self.handle_error("Ошибка", "Не было введено ни одной точки отсекателя")
        else:
            self.add_cutter_point(self.cutter_points[0])

    def my_repaint(self):
        self.image.fill(self.color_back)
        self.draw_segments()
        self.draw_cutter()

    def my_help(self, p):
        a = QPolygon()
        for point in self.cutter_points:
            new_point = QPoint(point[0], point[1])
            a.append(new_point)
        p.setPen(QPen(self.color_cutter, 1))
        p.setBrush(self.color_back)
        p.drawPolygon(a, 1)

    # рисование отрезка
    def my_darw_line(self, p, segment):
        p.drawLine(*segment)
        # points = bresenham_int(*segment)
        # for point in points:
        #     p.drawPoint(*point)

    # отсечение
    def on_bt_cut_clicked(self):
        if not self.cutter_points:
            self.handle_error("Ошибка", "Сначала введите отсекатель")
            return
        if (self.cutter_points[0][0] != self.cutter_points[-1][0]) or \
                (self.cutter_points[0][1] != self.cutter_points[-1][1]):
            self.handle_error("Ошибка", "Отсекатель не замкнут")
            return

        if not self.segment_points:
            self.handle_error("Ошибка", "Сначала введите отсекаемое")
            return
        if (self.segment_points[0][0] != self.segment_points[-1][0]) or \
                (self.segment_points[0][1] != self.segment_points[-1][1]):
            self.handle_error("Ошибка", "Отсекаемое не замкнуто")
            return

        flag_delete = self.rb_delete.isChecked()
        print('here')
        width = 2
        self.get_color_result()

        self.my_repaint()
        p = QPainter()
        p.begin(self.image)
        self.get_color_result()
        p.setPen(QPen(self.color_result, width))
        rc, result = sh_cut(deepcopy(self.segment_points), deepcopy(self.cutter_points), flag_delete)
        if rc == OK:
            self.my_help(p)
            p.setPen(QPen(self.color_result, width))
            if result:
                for edge in result:
                    self.my_darw_line(p, list(map(round, edge)))
        else:
            if rc == ERR_DEG:
                self.handle_error("Ошибка", "Отсекатель вырожден")
                return
            elif rc == ERR_CONV:
                self.handle_error("Ошибка", "Отсекатель должен быть выпуклым многоугольником")
                return
            elif rc == ERR_POLY_CONV:
                self.handle_error("Ошибка", "Отсекаемое должно быть многоугольником")
                return
            elif rc == ERR_POLY_DEG:
                self.handle_error("Ошибка", "Отсекаемый многоугольник вырожден")
                return

        p.end()
        pix = QPixmap()  # отрисовываемая картинка
        pix.convertFromImage(self.image)
        self.scene.addPixmap(pix)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    w = MyWindow()  # Создаём объект класса ExampleApp
    w.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение