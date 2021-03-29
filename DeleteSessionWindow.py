import os,DialogWindow,shutil

from PyQt5.QtWidgets import QAction

from gui import delete_session
from PyQt5 import QtWidgets, QtCore, Qt


class App(QtWidgets.QWidget, delete_session.Ui_Form):
    def __init__(self,window):
        super(App, self).__init__()
        self.setupUi(self)
        self.main_window = window
        self.path_sessions = os.path.join(os.getcwd(), 'sessions')
        self.dialog_warning = DialogWindow.Dialog()
        self.pushButton_Cancel.clicked.connect(self.close)
        self.pushButton_Delete.clicked.connect(self.delete)
        self.init_comboBox_sessions()

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
            self.dialog_warning.set_mes("Session was deleted")
            self.dialog_warning.show()
        except:
            self.dialog_warning.set_mes("No such session")
            self.dialog_warning.show()
