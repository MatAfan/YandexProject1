from imports import *


class ChangeMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ChangeMenu.ui", self)
        self.setWindowTitle('Изменить данные')
        self.con = sqlite3.connect(DBNAME)
        self.btn_search.clicked.connect(self.update_result)
        self.table_Main.itemChanged.connect(self.item_changed)
        self.btn_changeinfo.clicked.connect(self.save_results)
        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM Staff WHERE Surname=?""",
                             (item_id := self.txt_input.text(), )).fetchall()
        self.table_Main.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return

        self.table_Main.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table_Main.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE films SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()

    def closeEvent(self, event):
        if self.modified == {}:
            event.accept()
        else:
            reply = QMessageBox.question(self, '', "Вы точно хотите выйти?", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


