import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from math import sin, cos, pi, sqrt, tan


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('func.ui', self)
        self.a, self.b = list(map(int, input('Введите диапазон: ').split()))

        self.btn.clicked.connect(self.run)

    def run(self):
        f = self.func.text()
        try:
            self.gView.clear()
            self.gView.plot([y for y in range(self.a, self.b+1)], [eval(f) for x in range(self.a, self.b+1)])
            self.error.setText(f'y = {f}')
        except ZeroDivisionError:
            self.error.setText('Ошибка! Деление на 0')
        except Exception:
            self.error.setText('Ошибка! Введите корректную функцию')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())