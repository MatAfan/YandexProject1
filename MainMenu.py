from imports import *
from ChangeMenu1 import *
from AddOtherMenu import *
from AddMenu import *


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainMenu.ui", self)
        self.setWindowTitle('ТК')
        self.btn_add.clicked.connect(self.add_menu)
        self.btn_change.clicked.connect(self.change_menu)
        self.btn_get.clicked.connect(self.get_menu)

    def add_menu(self):
        add = QApplication(sys.argv)
        add_ex = ChangeMenu()
        add_ex.show()
        print(1)
        sys.exit(add.exec())

    def change_menu(self):
        change = QApplication(sys.argv)
        change_ex = ChangeMenu()
        change_ex.show()
        print(2)
        sys.exit(change.exec())

    def get_menu(self):
        pass

    def change_other_menu(self):
        change_other = QApplication(sys.argv)
        change_other_ex = AddOtherMenu()
        change_other_ex.show()
        print(3)
        sys.exit(change_other.exec())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())