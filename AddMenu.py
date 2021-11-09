from imports import *


class AddMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect(DBNAME)
        self.cur = self.con.cursor()
        uic.loadUi("AddMenu2.ui", self)
        self.setWindowTitle('Добавить значение')
        self.btn_add.clicked.connect(self.add)
        for i in self.cur.execute('SELECT Value from Study').fetchall():
            self.cbbx_Study.addItem(i[0])
        for i in self.cur.execute('SELECT Value from Jobs').fetchall():
            self.cbbx_job.addItem(i[0])
        for i in self.cur.execute('SELECT Value from FamilySituation').fetchall():
            self.cbbx_family.addItem(i[0])

    def closeEvent(self, event):
        self.connection.close()

    def add(self):
        birthday = self.ledit_Birthday.text().split('.')
        if len(birthday) != 3:
            return
        name = self.ledit_Name.text()
        surname = self.ledit_Surname.text()
        sname = self.ledit_SName.text()
        kids = int(self.spbx_Kids.text())
        floor = self.cbbx_Floor.text()
        job = self.cur.execute(f'SELECT id FROM Jobs WHERE Value={self.cbbx_job.text()}')
        study = self.cur.execute(f'SELECT id FROM Study WHERE Value={self.cbbx_Study.text()}')
        family = self.cur.execute(f'SELECT id FROM FamilySituations WHERE Value={self.cbbx_family.text()}')
        birthday = self.ledit_Birthday.text().split('.')
        dateTo = self.ledit_Employment.text().split('.')
        values = '(Surname, Name, SecondName, Birthday, Job, Gender, Family, Studies, Children, EmploymentDate)'
        things = '(surname, name, sname, birthday, job, floor, family, study, kids, dateTo)'
        self.con.execute(f'INSERT INTO Staff{values} VALUES {things}')
        self.con.commit()
