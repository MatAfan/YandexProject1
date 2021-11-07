from imports import *


class GetMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect(DBNAME)
        self.cur = self.con.cursor()
        uic.loadUi("GetMenu.ui", self)
        self.setWindowTitle('Получить данные')
        self.btn_get.clicked.connect(self.getinfo)

    def closeEvent(self, event):
        self.connection.close()

    def getinfo(self):
        total = ''
        Surname = self.ledit_Surname.text()
        SName = self.ledit_SName.text()
        Name = self.ledit_Name.text()
        result = self.cur.execute(f'SELECT * FROM Staff WHERE Surname={Surname} and Name={Name} and SecondName={SName}').fetchone()
        total += f'Табельный номер:\t{result[0]}\n'
        total += f'Фамилия:\t{result[0]}\n'
        total += f'Имя:\t{result[0]}\n'
        total += f'Отчество:\t{result[0]}\n'
        total += f'Дата рождения:\t{result[0]}\n'
        total += f'Должность:\t{result[0]}\n'
        total += f'Пол:\t{result[0]}\n'
        total += f'Семейное положение:\t{result[0]}\n'
        total += f'Образование:\t{result[0]}\n'
        total += f'Дети:\t{result[0]}\n'
        total += f'Дата приема на должность:\t{result[0]}\n'
        total += f'Дата увольнения:\t{result[0]}\n'
        self.pte_output.setPlainText(total)
