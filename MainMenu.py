from imports import *
from ChangeMenu1 import *
from AddOtherMenu import *


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainMenu.ui", self)
        self.setWindowTitle('ТК')
        self.btn_add.clicked.connect(self.add_menu)
        self.btn_change.clicked.connect(self.change_menu)
        self.btn_get.clicked.connect(self.get_menu)

    def add_menu(self):
        pass

    def change_menu(self):
        qqq = QApplication(sys.argv)
        eee = ChangeMenu()
        eee.show()

    def get_menu(self):
        pass

    def change_other_menu(self):
        qqqq = QApplication(sys.argv)
        eeee = AddOtherMenu()
        eeee.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())