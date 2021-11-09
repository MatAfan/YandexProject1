from imports import *


class AddOtherMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect(DBNAME)
        uic.loadUi("AddOtherMenu2.ui", self)
        self.setWindowTitle('Добавить значение')
        self.btn_add.clicked.connect(self.add)

    def closeEvent(self, event):
        self.connection.close()

    def add(self):
        cur = self.con.cursor()
        result = cur.execute(f"INSERT into {cbbx_tblchoose.text()}(Value) VALUES ('{ln_new.text()}') ")
        self.con.commit()
