import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from math import sin, cos, pi


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('znakomstvo_s_l-systemami.ui', self)

        self.file = open(QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0], 'r', encoding='utf8').readlines()
        self.setWindowTitle(self.file[0].strip())
        self.a = 360 / int(self.file[1].strip())
        self.axiome = self.file[2].strip()
        self.theorems = {}
        self.save = (0, 0, 0)
        for i in self.file[3:]:
            i = i.strip().split()
            self.theorems[i[0]] = i[1]

        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_system(qp)
        qp.end()

    def draw_system(self, qp):
        n = self.slider.value()
        a = 5
        cur_angle = 0
        cur_x, cur_y = 75, 450
        qp.setPen(QColor(0, 0, 0))
        for _ in range(n):
            new_axiome = ''
            for i in self.axiome:
                if i in self.theorems.keys():
                    new_axiome += self.theorems[i]
                else:
                    new_axiome += i
            self.axiome = new_axiome

        for task in self.axiome:
            if task == 'F':
                new_x, new_y = cur_x + a * cos(cur_angle * pi / 180), \
                               cur_y + a * sin(cur_angle * pi / 180)
                qp.drawLine(cur_x, cur_y, new_x, new_y)
                cur_x, cur_y = new_x, new_y
            elif task == 'f':
                new_x, new_y = cur_x + a * cos(cur_angle * pi / 180), \
                               cur_y + a * sin(cur_angle * pi / 180)
                cur_x, cur_y = new_x, new_y
            elif task == '+':
                cur_angle += self.a
            elif task == '-':
                cur_angle -= self.a
            elif task == '[':
                self.save = (cur_x, cur_y, cur_angle)
            elif task == ']':
                cur_x, cur_y, cur_angle = self.save
            elif task == '|':
                cur_angle += 180

        self.axiome = self.file[2].strip()
        self.save = (0, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())