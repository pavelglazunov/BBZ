import sys
from _testcapi import getbuffer_with_null_view

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

from osu2 import Osuu
from cats import Cat


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False

        self.mouse_x = 660
        self.mouse_y = -10
        self.bonus_mouse_wait = 1

        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setGeometry(300, 300, 1000, 700)
        self.main_window.setFixedSize(1000, 700)

        self.background = QLabel(self)
        background1 = QPixmap('./texture/menu_texture/background_menu')
        self.background.setPixmap(background1)
        self.background.move(0, 0)



        self.logoThoto = QLabel(self)
        logo = QPixmap('./texture/menu_texture/logo1.png')
        self.logoThoto.setPixmap(logo)
        self.logoThoto.move(30, -30)

        # self.setStyleSheet("background-color: #7fc7ff")



        self.logo_bbz = QLabel(self)
        self.logo_bbz.move(400, 65)
        self.logo_bbz.setText('<b>BBZ</b>')
        self.logo_bbz.setStyleSheet("QLabel{font-size: 80pt;}")

        self.one_player_game = QLabel(self)
        self.one_player_game.setText('<b>Игры на одного</b>')
        self.one_player_game.setStyleSheet("QLabel{font-size: 20pt;}")
        self.one_player_game.move(240, 230)

        self.two_player_game = QLabel(self)
        self.two_player_game.setText('<b>Игры на двоих</b>')
        self.two_player_game.setStyleSheet("QLabel{font-size: 20pt;}")
        self.two_player_game.move(530, 230)




        self.xo_btn = QPushButton('', self)
        self.xo_btn.resize(100, 100)
        self.xo_btn.move(550, 300)
        self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo.png'))
        self.xo_btn.setIconSize(QSize(95, 95))

        self.xo_rules = QPushButton('Правила', self)
        self.xo_rules.resize(100, 50)
        self.xo_rules.move(550, 420)
        self.xo_rules.clicked.connect(self.xo_rule)

        self.xo_rules_create = QLabel(self)
        self.xo_rules_create.resize(180, 200)
        self.xo_rules_create.move(510, 470)
        self.xo_rules_create.setPixmap(QPixmap('./texture/menu_texture/xo_rules.png'))
        self.xo_rules_create.hide()



        self.osu_btn = QPushButton('', self)
        self.osu_btn.resize(100, 100)
        self.osu_btn.move(350, 300)
        self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo.png'))
        self.osu_btn.setIconSize(QSize(95, 95))
        self.osu_btn.clicked.connect(self.osu_game)

        self.osu_rules_btn = QPushButton('Правила', self)
        self.osu_rules_btn.resize(100, 50)
        self.osu_rules_btn.move(350, 420)
        self.osu_rules_btn.clicked.connect(self.osu_rules)

        self.osu_rules_create = QLabel(self)
        self.osu_rules_create.resize(180, 200)
        self.osu_rules_create.move(310, 470)
        self.osu_rules_create.setPixmap(QPixmap('./texture/menu_texture/osu_rules_texture.png'))
        self.osu_rules_create.hide()



        self.city_game_btn = QPushButton('', self)
        self.city_game_btn.resize(100, 100)
        self.city_game_btn.move(150, 300)
        self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo.png'))
        self.city_game_btn.setIconSize(QSize(95, 95))

        self.city_game_rules = QPushButton('Правила', self)
        self.city_game_rules.resize(100, 50)
        self.city_game_rules.move(150, 420)
        self.city_game_rules.clicked.connect(self.city_game_rule)

        self.city_game_rules_create = QLabel(self)
        self.city_game_rules_create.resize(180, 200)
        self.city_game_rules_create.move(110, 470)
        self.city_game_rules_create.setPixmap(QPixmap('./texture/menu_texture/city_game_rules.png'))
        self.city_game_rules_create.hide()



        self.cats_btn = QPushButton('', self)
        self.cats_btn.resize(100, 100)
        self.cats_btn.move(750, 300)
        self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo'))
        self.cats_btn.setIconSize(QSize(95, 95))
        self.cats_btn.clicked.connect(self.cats_game)

        self.cats_rules = QPushButton('Правила', self)
        self.cats_rules.resize(100, 50)
        self.cats_rules.move(750, 420)
        self.cats_rules.clicked.connect(self.cat_rules)

        self.cats_rules_create = QLabel(self)
        self.cats_rules_create.resize(180, 200)
        self.cats_rules_create.move(710, 470)
        self.cats_rules_create.setPixmap(QPixmap('./texture/menu_texture/cats_rules.png'))
        self.cats_rules_create.hide()



        self.exit_btn = QPushButton('', self)
        self.exit_btn.resize(100, 50)
        self.exit_btn.move(0, 650)
        self.exit_btn.setIcon(QIcon('./texture/menu_texture/exit_button_texture.png'))
        self.exit_btn.setIconSize(QSize(100, 50))
        self.exit_btn.clicked.connect(self.exit)

        # self.calc_btn = QPushButton('', self)
        # self.calc_btn.resize(100, 100)
        # self.calc_btn.move(450, 550)
        # self.calc_btn.setIcon(QIcon('./texture/menu_texture/calc.png'))
        # self.calc_btn.setIconSize(QSize(90, 90))

        self.crash_btn = QPushButton('', self)
        self.crash_btn.resize(50, 50)
        self.crash_btn.move(950, 650)
        self.crash_btn.setIcon(QIcon('./texture/menu_texture/crash_button.png'))
        self.crash_btn.setIconSize(QSize(90, 90))
        self.crash_btn.clicked.connect(self.crash)



        # бонус кнопки
        self.bonus_btn = QPushButton('', self)
        self.bonus_btn.setIcon(QIcon('./texture/menu_texture/bonus_btn'))
        self.bonus_btn.setIconSize(QSize(100, 100))
        self.bonus_btn.resize(100, 100)
        self.bonus_btn.move(50, 80)
        self.bonus_btn.clicked.connect(self.bonus)

        self.bonus_btn2 = QPushButton('', self)
        self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2'))
        self.bonus_btn2.setIconSize(QSize(100, 100))
        self.bonus_btn2.resize(100, 100)
        self.bonus_btn2.move(888, 10)
        self.bonus_btn2.clicked.connect(self.bonus2)

        self.bonus_mouse = QLabel(self)
        self.bonus_mouse.setPixmap(QPixmap('./texture/menu_texture/bonus_btn_mouse.png'))
        self.bonus_mouse.resize(100, 100)
        self.bonus_mouse.move(self.mouse_x, self.mouse_y)

        self.bonus_mouse_btn = QPushButton(self)
        self.bonus_mouse_btn.setIcon(QIcon('./texture/menu_texture/bonus_mouse_btn'))
        self.bonus_mouse_btn.setIconSize(QSize(100, 100))
        self.bonus_mouse_btn.resize(100, 100)
        self.bonus_mouse_btn.move(self.mouse_x, self.mouse_y)
        self.bonus_mouse_btn.clicked.connect(self.bonus_mouse_run)


    def xo_rule(self):
        if not (self.xo_rules_is_active):
            self.xo_rules_create.show()
            self.osu_rules_create.hide()
            self.city_game_rules_create.hide()
            self.cats_rules_create.hide()

            self.xo_rules_is_active = True
            self.osu_rules_is_active = False
            self.city_game_rules_is_active = False
            self.cats_rules_is_active = False
        elif self.xo_rules_is_active:
            self.xo_rules_create.hide()
            self.xo_rules_is_active = False

    def osu_rules(self):
        if not (self.osu_rules_is_active):
            self.xo_rules_create.hide()
            self.osu_rules_create.show()
            self.city_game_rules_create.hide()
            self.cats_rules_create.hide()

            self.xo_rules_is_active = False
            self.osu_rules_is_active = True
            self.city_game_rules_is_active = False
            self.cats_rules_is_active = False
        elif self.osu_rules_is_active:
            self.osu_rules_create.hide()
            self.osu_rules_is_active = False

    def city_game_rule(self):
        if not (self.city_game_rules_is_active):
            self.xo_rules_create.hide()
            self.osu_rules_create.hide()
            self.city_game_rules_create.show()
            self.cats_rules_create.hide()

            self.xo_rules_is_active = False
            self.osu_rules_is_active = False
            self.city_game_rules_is_active = True
            self.cats_rules_is_active = False
        elif self.city_game_rules_is_active:
            self.city_game_rules_create.hide()
            self.city_game_rules_is_active = False

    def cat_rules(self):
        if not (self.cats_rules_is_active):
            self.xo_rules_create.hide()
            self.osu_rules_create.hide()
            self.city_game_rules_create.hide()
            self.cats_rules_create.show()

            self.xo_rules_is_active = False
            self.osu_rules_is_active = False
            self.city_game_rules_is_active = False
            self.cats_rules_is_active = True
        elif self.cats_rules_is_active:
            self.cats_rules_create.hide()
            self.cats_rules_is_active = False

    def hide_ruled(self):
        self.xo_rules_create.hide()
        self.osu_rules_create.hide()
        self.city_game_rules_create.hide()
        self.cats_rules_create.hide()

        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False

    def bonus(self):
        self.bonus_animation_wait = 1
        self.bonus_btn.setIcon(QIcon('./texture/menu_texture/bonus_btn_animation'))
        self.bonus_animation_timer()

    def bonus2(self):
        self.bonus_animation_wait2 = 1
        self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2_animation'))
        self.bonus_animation_timer2()



    def bonus_animation_timer(self):
        if self.bonus_animation_wait > 0:
            self.bonus_animation_wait -= 1  # Устанавливаем значение на 1 меньше
            QTimer().singleShot(1000, self.bonus_animation_timer)
        else:
            self.bonus_btn.setIcon(QIcon('./texture/menu_texture/bonus_btn'))
            self.bonus_animation_wait = 1

    def bonus_animation_timer2(self):
        if self.bonus_animation_wait2 > 0:
            self.bonus_animation_wait2 -= 1  # Устанавливаем значение на 1 меньше
            QTimer().singleShot(1000, self.bonus_animation_timer2)
        else:
            self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2'))
            self.bonus_animation_wait2 = 1

    # def bonus_mouse_timer(self):
    #     if self.bonus_mouse_wait > 0:
    #         self.bonus_mouse_wait -= 1  # Устанавливаем значение на 1 меньше
    #         QTimer().singleShot(1000, self.bonus_mouse_timer)
    #     else:
    #         self.bonus_mouse_wait = 1

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

            # self.bonus_mouse_timer()




    def osu_game(self):
        self.hide_ruled()
        osu_window.get_windows(list_of_windows)
        list_of_windows.setCurrentIndex(1)

    def cats_game(self):
        self.hide_ruled()
        cat_window.get_windows(list_of_windows)
        list_of_windows.setCurrentIndex(2)



    def crash(self):
        pass

    def exit(selfs):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_of_windows = QStackedWidget()
    main_window = Example()
    osu_window = Osuu()
    cat_window = Cat()

    list_of_windows.addWidget(main_window) # 0
    list_of_windows.addWidget(osu_window) # 1
    list_of_windows.addWidget(cat_window) # 2


    list_of_windows.resize(1000, 700)
    list_of_windows.setFixedSize(1000, 700)
    list_of_windows.show()
    sys.exit(app.exec())
