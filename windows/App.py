import json
import os
import sqlite3, ThreadProc
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog, QMessageBox
from Connections import *
from Connections import Connections
from Settings import Settings
from windows import PrevLoadWindow, AddSessionWindow, DeleteSessionWindow, SettingsWindow, MailsWindow, MailWindow
from gui import MainWindow


class App(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.initUi()

    def init_sesions(self):
        path_sesions = os.path.join(os.getcwd(), 'sessions')
        sessions = os.listdir(path_sesions)
        for session in sessions:
            if os.path.isdir(os.path.join('sessions',session)):
                self.action = QtWidgets.QAction(self)
                self.action.setObjectName(session)
                self.action.setText(session)
                self.action.triggered.connect(self.select_session)
                self.menuChoose_session.addAction(self.action)

    def initUi(self):
        self.setupUi(self)
        self.init_sesions()
        self.pushButton_Search.setEnabled(False)
        self.thread = None
        self.path_session = None
        self.search_result = None
        self.setup()
        self.actionLoad_mails.triggered.connect(self.Load)
        self.actionAdd_Session.triggered.connect(self.add_session)
        self.actionDelete_Session.triggered.connect(self.delete_session)
        self.actionSettings.triggered.connect(self.show_settings_window)
        self.treeWidget.itemDoubleClicked.connect(self.show_mails_window)
        self.pushButton_Search.clicked.connect(self.search)
        self.checkBox_Date.clicked.connect(self.search_btn_enable)
        self.checkBox_Only_Seen.clicked.connect(self.search_btn_enable)
        self.checkBox_Search.clicked.connect(self.search_btn_enable)
        self.checkBox_Search.clicked.connect(self.enable_search_lines)
        Connections.load_main_window(self)
        self.show()

    def setup(self):
        self.lang = Settings.setUp(self)[1]

    def enable_search_lines(self):
        if self.checkBox_Search.isChecked():
            self.lineEdit_Body.setEnabled(True)
            self.lineEdit_From.setEnabled(True)
            self.lineEdit_Subject.setEnabled(True)
        else:
            self.lineEdit_Body.setEnabled(False)
            self.lineEdit_From.setEnabled(False)
            self.lineEdit_Subject.setEnabled(False)

    def search_btn_enable(self):
        if self.checkBox_Date.isChecked() or self.checkBox_Only_Seen.isChecked() or self.checkBox_Search.isChecked():
            self.pushButton_Search.setEnabled(True)
        else:
            self.pushButton_Search.setEnabled(False)

    def search(self):
        pass

    def show_mails_window(self):
        self.mails_window = MailsWindow.App(self.result)
        self.mails_window.show()

    def show_settings_window(self):
        self.settings_window = SettingsWindow.App(self)
        self.settings_window.show()

    def add_session(self):
        self.add_session_window = AddSessionWindow.App(self)
        self.add_session_window.show()

    def delete_session(self):
        self.delete_session_window = DeleteSessionWindow.App(self)
        self.delete_session_window.show()

    def select_session(self):
        Connections.reset()
        self.checkBox_Only_Seen.setEnabled(True)
        self.checkBox_Date.setEnabled(True)
        self.dateEdit_date.setEnabled(True)
        self.checkBox_Search.setEnabled(True)
        self.action = self.sender()
        self.label_Active_Session.setText(self.action.objectName())
        self.path_session = os.path.join(os.getcwd(),'sessions', self.action.objectName())
        if self.thread is None:
            self.thread = ThreadProc.TreadProc(path=self.path_session)
            self.thread.change_value.connect(self.set_progress_bar)
            self.thread.finished.connect(self.succsessful_load)
            self.thread.start()
            self.label_status.setText("Load...")

    def succsessful_load(self):
        self.progressBar.setValue(0)
        self.label_status.setText("OK")
        self.thread.change_value.disconnect(self.set_progress_bar)
        self.thread.finished.disconnect(self.succsessful_load)
        self.thread = None

    def set_progress_bar(self,value):
        self.progressBar.setValue(value)

    def Load(self):
        if self.path_session is not None:
            self.prev_load_menu = PrevLoadWindow.PrevLoad(self.path_session)
            self.prev_load_menu.setWindowModality(Qt.ApplicationModal)
            self.prev_load_menu.show()
        else:
            App.show_warning_mes(self.lang["select_session"])

    @staticmethod
    def show_warning_mes(mes):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(mes)
        msgBox.setStyleSheet("font-size:12px;\n")
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
