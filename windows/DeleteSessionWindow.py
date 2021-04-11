import os,shutil

from Settings import Settings
from PyQt5.QtWidgets import QAction

from gui import delete_session
from PyQt5 import QtWidgets, QtCore, Qt


class App(QtWidgets.QWidget, delete_session.Ui_DeleteSession):
    def __init__(self,window):
        super(App, self).__init__()
        self.setupUi(self)
        self.main_window = window
        self.path_sessions = os.path.join(os.getcwd(), 'sessions')
        self.pushButton_Cancel.clicked.connect(self.close)
        self.pushButton_Delete.clicked.connect(self.delete)
        self.init_comboBox_sessions()
        self.lang = Settings.setUp(self)[1]

    def init_comboBox_sessions(self):
        sessions = os.listdir(self.path_sessions)
        for session in sessions:
            self.comboBox_Sessions.addItem(session)

    def delete(self):
        name_session = self.comboBox_Sessions.currentText()
        try:
            path = os.path.join(self.path_sessions, name_session)
            shutil.rmtree(path)
            self.main_window.menuChoose_session.removeAction(self.main_window.findChild(QAction, name_session))
            self.main_window.label_Active_Session.setText("")
            self.main_window.show_warning_mes(self.lang["session_was_deleted"])
        except:
            self.main_window.show_warning_mes(self.lang["no_such_session"])

