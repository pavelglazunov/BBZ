from PyQt5 import uic, QtGui
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    x0_na_matrix = ['X', '0']
    count_x0 = 0
    otstup_x = 210
    otstup_y = 45
    spi_matrix = []
    btn_grp = QButtonGroup()
    btn_grp.setExclusive(True)
    spi_btn = []
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('calc.ui', self)
        self.resize(1000, 700)
        self.pole()
        self.matrix()
        self.btn_grp.buttonClicked.connect(self.najata)

    def matrix(self):
        for i in range(31):
            k = []
            self.spi_matrix.append(k)
            for j in range(26):
                self.spi_matrix[i].append('N')

    def najata(self, btn):
        f = False
        for i in self.spi_btn:
            if btn in i and self.spi_matrix[self.spi_btn.index(i)][i.index(btn)] == 'N':
                self.spi_matrix[self.spi_btn.index(i)][i.index(btn)] = self.x0_na_matrix[self.count_x0]
                f = True
                y = self.spi_btn.index(i)
                x = i.index(btn)
                break
        if f:
            btn.setText(self.x0_na_matrix[self.count_x0])
            if self.proverka_pobedi(x, y):
                print('Победили ' + self.x0_na_matrix[self.count_x0])
            self.count_x0 = (self.count_x0 + 1) % 2
        # for i in self.spi_matrix:
        #     for j in i:
        #         print(j, end=' ')
        #     print()
        # print('=====================================')

    def pole(self):
        for i in range(31):
            self.spi_btn.append([])
            for j in range(26):
                k = QPushButton('', self)
                k.setFont(QtGui.QFont("Arial", 20))
                k.resize(30, 30)
                k.move(j * 30 + self.otstup_x, 30 * i + self.otstup_y)
                self.btn_grp.addButton(k)
                self.spi_btn[i].append(k)

    def proverka_pobedi(self, x, y):
        spi_gorizont = self.spi_matrix[y][min(abs(x - 4), abs(x - 3), abs(x - 2), abs(x - 1), x): x + 5]
        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_gorizont):
            return True
        print(spi_gorizont)
        spi_vertical = []

        spi_of_spi = self.spi_matrix[min(abs(y - 4), abs(y - 3), abs(y - 2), abs(y - 1), y): y + 5]
        for i in spi_of_spi:
            spi_vertical.append(i[x])
        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_vertical):
            return True

        spi_dioganal1 = []
        # for i in spi_of_spi:
        #     if x + self.spi_matrix.index(i) - y >= 0:
        #         spi_dioganal1.append(i[x + self.spi_matrix.index(i) - y])
        # if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_dioganal1):
        #     return True





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())