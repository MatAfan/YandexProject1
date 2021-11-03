import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая программа')
        # Создаем кнопку.
        # Передаем 2 параметра:
        # надпись и виджет, на котором будет размещена кнопка
        btn = QPushButton('Кнопка', self)
        # Изменяем размер кнопки. Теперь он 100 на 100 пикселей
        btn.resize(16, 16)
        # Размещаем кнопку на родительском виджете
        # по координатам (100, 100)
        btn.move(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())