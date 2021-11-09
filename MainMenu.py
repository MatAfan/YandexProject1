from ChangeMenu1 import *
from AddOtherMenu import *
from AddMenu import *
from GetMenu import *
from imports import *


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainMenu.ui", self)
        self.setWindowTitle('ТК')
        self.btn_add.clicked.connect(self.add_menu)
        self.btn_change.clicked.connect(self.change_menu)
        self.btn_get.clicked.connect(self.get_menu)

    def add_menu(self):
        add_ex = AddMenu()
        add_ex.show()

    def change_menu(self):
        change_ex = ChangeMenu()
        change_ex.show()

    def get_menu(self):
        get_ex = GetMenu()
        get_ex.show()
        
    def change_other_menu(self):
        change_other_ex = AddOtherMenu()
        change_other_ex.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainMenu()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())