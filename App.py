import os
import time
import PyQt5,sys,MailData,ExceptionBreak,DialogWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog

import PrevLoadWindow,AddSessionWindow, DeleteSessionWindow
from gui import MainWindow


class App(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.initUi()

    def checkBox_style_setup(self):
        file_style = open("styles/QCheckBox_style.txt").read()
        self.checkBox_Date.setStyleSheet(file_style)
        self.checkBox_Amount.setStyleSheet(file_style)
        self.checkBox_Only_Seen.setStyleSheet(file_style)

    def groupBox_style_setup(self):
        file_style = open("styles/QGroupBox_style.txt").read()
        self.groupBox_Statistic.setStyleSheet(file_style)
        self.groupBox_Filter.setStyleSheet(file_style)
        self.groupBox_Requests.setStyleSheet(file_style)

    def label_style_setup(self):
        file_style_label = open("styles/Qlable_style.txt").read()
        self.label_5.setStyleSheet(file_style_label)
        self.label_Active_Session.setStyleSheet(file_style_label)
        self.label.setStyleSheet(file_style_label)
        self.label_2.setStyleSheet(file_style_label)
        self.label_3.setStyleSheet(file_style_label)
        self.label_4.setStyleSheet(file_style_label)
        self.label_Accounts.setStyleSheet(file_style_label)
        self.label_Checked.setStyleSheet(file_style_label)
        self.label_Valid.setStyleSheet(file_style_label)
        self.label_Unvalid.setStyleSheet(file_style_label)

    def init_sesions(self):
        path_sesions = os.path.join(os.getcwd(),'sessions')
        sessions = os.listdir(path_sesions)
        for session in sessions:
            self.action = QtWidgets.QAction(self)
            self.action.setObjectName(session)
            self.action.setText(session)
            self.action.triggered.connect(self.select_session)
            self.menuChoose_session.addAction(self.action)

    def initUi(self):
        self.setupUi(self)
        self.init_sesions()
        self.label_style_setup()
        self.groupBox_style_setup()
        self.checkBox_style_setup()
        self.actionLoad_mails.triggered.connect(self.Load)
        self.actionAdd_Session.triggered.connect(self.add_session)
        self.actionDelete_Session.triggered.connect(self.delete_session)

        #tabWidget set default size
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)  # !!!
        self.tableWidget.verticalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Fixed)
        #

        self.path_session = None
        self.show()


    def add_session(self):
        self.add_session_window = AddSessionWindow.App(self)
        self.add_session_window.show()


    def delete_session(self):
        self.delete_session_window = DeleteSessionWindow.App(self)
        self.delete_session_window.show()

    def select_session(self):
        self.action = self.sender()
        self.label_Active_Session.setText(self.action.objectName())
        self.path_session = os.path.join(os.getcwd(),self.action.objectName())

    def Load(self):
        self.prev_load_menu = PrevLoadWindow.App(self.path_session)
        self.prev_load_menu.setWindowModality(Qt.ApplicationModal)
        self.prev_load_menu.show()

