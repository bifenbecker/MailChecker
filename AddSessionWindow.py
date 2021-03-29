import os,DialogWindow
import sqlite3

from gui import add_session
from PyQt5 import QtWidgets, QtCore, Qt


class App(QtWidgets.QWidget, add_session.Ui_Form):
    def __init__(self,window):
        super(App, self).__init__()
        self.setupUi(self)
        self.win = window
        self.dialog_warning = DialogWindow.Dialog()
        self.pushButton_Cancel.clicked.connect(self.close)
        self.pushButton_Ok.clicked.connect(self.add_session)

    def add_session(self):
        name_session = self.lineEdit.text()
        if name_session == "":
            self.dialog_warning.setWindowModality(Qt.Qt.ApplicationModal)
            self.dialog_warning.set_mes("Name is empty")
            self.dialog_warning.show()

        elif self.is_non_symbol_in_name(name_session):
            self.dialog_warning.setWindowModality(Qt.Qt.ApplicationModal)
            self.dialog_warning.set_mes("Wrong name ( {0} , {1} , {2} , {3} , {4} , {5} , {6} , {7} )".format('/', ':', '*', '?', '"', '<', '>', '|'))
            self.dialog_warning.show()
        else:
            path = os.path.join(os.getcwd(), "sessions",name_session)
            if not os.path.exists(path):
                os.makedirs(path)
                DB_NAME = os.path.join(path,f'{name_session}.db')
                connection = sqlite3.connect(DB_NAME)
                cursor = connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS mails(mail TEXT, password TEXT, valid INT)""")
                connection.commit()
                self.action = QtWidgets.QAction(self.win)
                self.action.setObjectName(name_session)
                self.action.setText(name_session)
                self.action.triggered.connect(self.win.select_session)
                self.win.menuChoose_session.addAction(self.action)
                self.dialog_warning.set_mes(f"Session: {name_session} was added")
                self.dialog_warning.show()
            else:
                self.dialog_warning.setWindowModality(Qt.Qt.ApplicationModal)
                self.dialog_warning.set_mes(f"Session {name_session} already  exists")
                self.dialog_warning.show()

    def is_non_symbol_in_name(self,name):
        non_symbols = ['/', ':', '*', '?', '"', '<', '>', '|']
        for symbol in non_symbols:
            if symbol in name:
                return True
        return False

