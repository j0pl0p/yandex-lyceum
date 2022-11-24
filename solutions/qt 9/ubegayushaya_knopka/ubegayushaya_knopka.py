import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Кнопка')
        self.coords = (30, 30)
        self.w, self.h = list(map(int, input('Введите размеры окна через пробел\n').split()))
        self.w, self.h = max(100, self.w), max(100, self.h)
        self.setMouseTracking(True)
        self.setGeometry(300, 300, self.w, self.h)
        self.btn = QPushButton(self)
        self.btn.setText('click me!')
        self.btn.resize(50, 30)
        self.btn.move(30, 30)
        self.show()

    def mouseMoveEvent(self, event):
        # print(range(self.coords[0], self.coords[0]+50), range(self.coords[1], self.coords[1]+30))
        if event.x() in range(self.coords[0]-10, self.coords[0]+60) and event.y() in range(self.coords[1]-10, self.coords[1]+40):
            x, y = random.randint(0, self.w - 50), random.randint(0, self.h - 30)
            #  while x in range(self.coords[0]-10, self.coords[0]+60) or y in range(self.coords[1]-10, self.coords[1]+40):
            #      x, y = random.randint(0, self.w - 50), random.randint(0, self.h - 30)
            self.btn.move(x, y)
            self.coords = (x, y)

    def onResize(self, event):
        print(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
