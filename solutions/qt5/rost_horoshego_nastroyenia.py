import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('rost_horoshego_nastroyenia.ui', self)

        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_smiley(qp)
        # Завершаем рисование
        qp.end()

    def draw_smiley(self, qp):
        n = self.slider.value() * 4
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(0, 0, n, n)
        qp.drawEllipse(n // 5, n // 4, n // 5, n // 5)
        qp.drawEllipse(n // 2, n // 4, n // 5, n // 5)
        qp.drawArc(n//5, n//1.5, n//2, n//6, 0, -180 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
