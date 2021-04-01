import os
import sqlite3
import time
import PyQt5,sys,MailData,ExceptionBreak,DialogWindow,MailsWindow,MailWindow
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
        self.checkBox_Only_Seen.setStyleSheet(file_style)

    def groupBox_style_setup(self):
        file_style = open("styles/QGroupBox_style.txt").read()
        self.groupBox_Statistic.setStyleSheet(file_style)
        self.groupBox_Filter.setStyleSheet(file_style)
        self.groupBox_Requests.setStyleSheet(file_style)

    def label_style_setup(self):
        file_style_label = open("styles/Qlable_style.txt").read()
        self.label_6.setStyleSheet(file_style_label)
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
        self.pushButton_Search.setEnabled(False)
        self.path_session = None
        self.search_result = None
        self.dialog_warning = DialogWindow.Dialog()
        self.label_style_setup()
        self.groupBox_style_setup()
        self.checkBox_style_setup()
        self.actionLoad_mails.triggered.connect(self.Load)
        self.actionAdd_Session.triggered.connect(self.add_session)
        self.actionDelete_Session.triggered.connect(self.delete_session)
        self.treeWidget.itemDoubleClicked.connect(self.show_mails_window)
        self.pushButton_Search.clicked.connect(self.search)
        self.checkBox_Date.clicked.connect(self.search_btn_enable)
        self.checkBox_Only_Seen.clicked.connect(self.search_btn_enable)
        self.show()


    def search_btn_enable(self):
        if self.checkBox_Date.isChecked() or self.checkBox_Only_Seen.isChecked():
            self.pushButton_Search.setEnabled(True)
        else:
            self.pushButton_Search.setEnabled(False)

    def search(self):
        connection = sqlite3.connect(
        os.path.join('sessions', self.label_Active_Session.text(), f'{self.label_Active_Session.text()}.db'))
        cursor = connection.cursor()
        sql_search = "SELECT * FROM mails WHERE "
        sqls = [self._check_only_seen(), self._check_date()]
        parametrs = []
        for sql in sqls:
            if sql[0]:
                sql_search += sql[-1] + "=? AND "
                parametrs.append(sql[1])
        sql_search = sql_search[:-5]
        cursor.execute(sql_search,tuple(parametrs))
        res = cursor.fetchmany(-1)
        print(len(res))



    def _check_only_seen(self):
        checked = False
        if self.checkBox_Only_Seen.isChecked():
            checked = True
            return (checked,"1", "seen")
        return (checked,"")

    def _check_date(self):
        checked = False
        if self.checkBox_Date.isChecked():
            checked = True
            date = self.dateEdit_date.text()
            return (checked,date,"date")
        return (checked,"")

    def show_mails_window(self):
        self.mails_window = MailsWindow.App(self.result)
        self.mails_window.show()

    def add_session(self):
        self.add_session_window = AddSessionWindow.App(self)
        self.add_session_window.show()


    def delete_session(self):
        self.delete_session_window = DeleteSessionWindow.App(self)
        self.delete_session_window.show()

    def select_session(self):
        self.checkBox_Only_Seen.setEnabled(True)
        self.checkBox_Date.setEnabled(True)
        self.dateEdit_date.setEnabled(True)
        self.action = self.sender()
        self.label_Active_Session.setText(self.action.objectName())
        self.path_session = os.path.join(os.getcwd(),self.action.objectName())

    def Load(self):
        if self.path_session is not None:
            self.prev_load_menu = PrevLoadWindow.App(self.label_Active_Session.text())
            self.prev_load_menu.setWindowModality(Qt.ApplicationModal)
            self.prev_load_menu.show()
        else:
           self.dialog_warning.set_mes("Select or add session")
           self.dialog_warning.setWindowModality(Qt.ApplicationModal)
           self.dialog_warning.show()

