import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        alls = cursor.fetchall()
        self.tableWidget.setRowCount(len(alls))
        self.tableWidget.setColumnCount(7)
        for i, row in enumerate(alls):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
        conn.close()


if __name__ == '__main__':
    app = QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec()
