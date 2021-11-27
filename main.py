from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite3
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.setGeometry(100, 100, 700, 580)
        with sqlite3.connect("coffee.sqlite") as con:
            self.table = con.cursor().execute(f"""select * from coffee""").fetchall()
        self.settings()
    
    def settings(self):
        self.tableWidget.setGeometry(20, 20, 660, 540)
        self.tableWidget.setRowCount(len(self.table))
        for i in range(len(self.table)):
            for n in range(7):
                self.tableWidget.setItem(i, n, QTableWidgetItem(str(self.table[i][n])))

app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec())