from imports import *


class AddOtherMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect(DBNAME)
        uic.loadUi("AddOtherMenu.ui", self)
        self.setWindowTitle('Добавить значение')
        self.btn_add.clicked.connect(self.add)

    def add(self):
        cur = self.con.cursor()
        result = cur.execute(f"INSERT into {cbbx_tblchoose.text()}(Value) VALUES ('{ln_new.text()}') ")
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddOtherMenu()
    ex.show()
    sys.exit(app.exec())