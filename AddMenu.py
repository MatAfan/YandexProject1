from imports import *


class AddMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect(DBNAME)
        self.cur = self.con.cursor()
        uic.loadUi("AddMenu.ui", self)
        self.setWindowTitle('Добавить значение')
        self.btn_add.clicked.connect(self.add)
        for i in self.cur.execute('SELECT Value from Study').fetchall():
            self.cbbx_Study.addItem(i[0])
        for i in self.cur.execute('SELECT Value from Jobs').fetchall():
            self.cbbx_job.addItem(i[0])
        for i in self.cur.execute('SELECT Value from FamilySituation').fetchall():
            self.cbbx_family.addItem(i[0])

    def add(self):
        birthday = self.ledit_Birthday.text().split('.')
        if len(birthday) != 3:
            return
        cur = self.con.cursor()
        name = self.ledit_Name.text()
        surname = self.ledit_Surname.text()
        sname = self.ledit_SName.text()
        kids = int(self.spbx_Kids.text())
        floor = self.cbbx_Floor.text()


        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddMenu()
    ex.show()
    sys.exit(app.exec())