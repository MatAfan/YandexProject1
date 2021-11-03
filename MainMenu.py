from imports import *
from ChangeMenu1 import *


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainMenu.ui", self)
        self.setWindowTitle('ТК')
        self.btn_add.clicked.connect(self.add_menu)
        self.btn_change.clicked.connect(self.change_menu)
        self.btn_get.clicked.connect(self.get_menu)
        self.btn_changeother.clicked.connect(self.change_other_menu)

    def add_menu(self):
        pass

    def change_menu(self):
        ex = ChangeMenu
        ex.show()

    def get_menu(self):
        pass

    def change_other_menu(self):
        pass
