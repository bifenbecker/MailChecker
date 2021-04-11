import json
from Settings import Settings
import sqlite3,os
from gui import add_session

from PyQt5 import QtWidgets, QtCore, Qt


class App(QtWidgets.QWidget, add_session.Ui_AddSession):
    def __init__(self,window):
        super(App, self).__init__()
        self.setupUi(self)
        self.win = window
        self.pushButton_Cancel.clicked.connect(self.close)
        self.pushButton_Ok.clicked.connect(self.add_session)
        self.lang = Settings.setUp(self)[1]

    def add_session(self):
        name_session = self.lineEdit.text()
        if name_session == "":
            self.win.show_warning_mes(self.lang["name_is_empty"])

        elif self.is_non_symbol_in_name(name_session):
            self.win.show_warning_mes(self.lang["wrong_name"])

        else:
            path = os.path.join(os.getcwd(), "sessions",name_session)
            if not os.path.exists(path):
                os.makedirs(path)

                #Create file db
                # DB_NAME = os.path.join(path,f'{name_session}.db')
                # connection = sqlite3.connect(DB_NAME)
                # cursor = connection.cursor()
                # cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT, valid INT)""")
                # connection.commit()

                self.action = QtWidgets.QAction(self.win)
                self.action.setObjectName(name_session)
                self.action.setText(name_session)
                self.action.triggered.connect(self.win.select_session)
                self.win.menuChoose_session.addAction(self.action)
                self.win.show_warning_mes(self.lang["session_was_added"])
            else:
                self.win.show_warning_mes(self.lang["session_is_already_exists"])

    def is_non_symbol_in_name(self,name):
        non_symbols = ['/', ':', '*', '?', '"', '<', '>', '|']
        for symbol in non_symbols:
            if symbol in name:
                return True
        return False

