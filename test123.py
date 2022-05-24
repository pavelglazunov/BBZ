import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget

class Loading(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pos_x = -80
        self.pos_y = 300

        self.loading_background = QWidget()
        self.loading_background.setGeometry(1000, 1000, 1000, 700)
        self.loading_background.resize(1000, 700)
        self.loading_background.setFixedSize(1000, 700)
        # self.loading_background.move(0, 0)

        self.background = QLabel(self)
        self.background.resize(1000, 700)
        self.background.setFixedSize(1000, 700)
        self.background.setPixmap(QPixmap('./texture/loading_texture/loading_background.png'))

        self.later_B1 = QLabel(self)
        self.later_B1.move(-80, 300)
        self.later_B1.setPixmap(QPixmap('./texture/loading_texture/later_B1.png'))




    def bonus_mouse_run(self):
        self.bonus_mouse_btn.hide()
        if self.mouse_y < 700:
            self.bonus_mouse.show()
            self.mouse_x -= 1
            self.mouse_y += 2
            self.bonus_mouse.move(self.mouse_x, self.mouse_y)
            QTimer().singleShot(10, self.bonus_mouse_run)
        else:
            self.mouse_x = 660
            self.mouse_y = -10
            self.bonus_mouse.move(self.mouse_x, self.mouse_y)
            self.bonus_mouse_btn.show()


# class Politic(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.text = QLabel( self)
#
#         L = open('politic.txt', encoding='utf-8').read().split('\n')
#         for i in L:
#             self.text.setText(self.text.text() + i + '\n')
#
#         self.scroll_area = QScrollArea()
#         self.scroll_area.setFixedSize(400, 500)
#         self.scroll_area.setWidget(self.text)
#
#         self.scroll_area.show()


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex1 = Loading()
    # ex = Politic()
    ex1.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())