import json
import os
import datetime as DT
import sqlite3
import time
from collections import defaultdict

import PyQt5, sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog, QMessageBox

from QTreeItem import QTreeItem
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
        connection = sqlite3.connect(os.path.join(self.path_session, 'database.db'))
        cursor = connection.cursor()
        self.search_result, data, req = self.get_search_result()

        for key in data:
            user = cursor.execute("SELECT * FROM Account WHERE id=?",(key,)).fetchall()[0]
            item = QTreeItem(data[key])
            item.setText(0, user[1])
            item.setText(1, user[2])
            item.setText(2, req)
            item.setText(3, str(len(data[key])))
            self.treeWidget.addTopLevelItem(item)


    def get_search_result(self):
        connection = sqlite3.connect(os.path.join(self.path_session, 'database.db'))
        cursor = connection.cursor()
        filtres = [self._check_only_seen(),self._check_date()]
        text_search = [self._check_from(),self._check_subject(),self._check_body()]
        req = ""
        parameters = []
        sql_search = "SELECT * FROM Message WHERE "
        for fl in filtres:
            if fl[0]:
                req += fl[2] + " = " + fl[-1] + ","
                sql_search += fl[1] + " AND "
                parameters.append(fl[-1])

        for ts in text_search:
            if ts[0] and self.checkBox_Search.isChecked():
                req += ts[2] + " = " + ts[-1]
                sql_search += ts[1] + " OR "
                parameters.append("%" + ts[-1] + "%")

        if not self.checkBox_Search.isChecked():
            sql_search = sql_search[:-4]
        else:
            sql_search = sql_search[:-3]
        req = req[:-1]
        cursor.execute(sql_search,tuple(parameters))
        res = cursor.fetchall()
        data = {}
        for mail in res:
            if mail[-1] not in list(data.keys()):
                data[mail[-1]] = []

            data[mail[-1]].append(mail)


        return res,data,req


    def _check_from(self):
        if self.lineEdit_From.text() != "":
            return True, "UPPER(sender) LIKE UPPER(?)", "from", self.lineEdit_From.text()
        return False, "", ""

    def _check_subject(self):
        if self.lineEdit_Subject.text() != "":
            return True, "UPPER(subject) LIKE UPPER(?)", "subject", self.lineEdit_Subject.text()
        return False, "", ""

    def _check_body(self):
        if self.lineEdit_Body.text() != "":
            return True, "UPPER(content) LIKE UPPER(?)","body", self.lineEdit_Body.text()
        return False, "", ""

    def _check_only_seen(self):
        if self.checkBox_Only_Seen.isChecked():
            return True,"seen =? ","seen", "1"
        return False,"",""

    def _check_date(self):
        if self.checkBox_Date.isChecked():
            date = str(int(self.dateEdit_date.dateTime().toPyDateTime().timestamp()))
            return True,"date >= ?" ,"date", date
        return False,"",""

    def show_mails_window(self,item,column):
        self.mails_window = MailsWindow.App(item.data)
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
        self.checkBox_Only_Seen.setEnabled(True)
        self.checkBox_Date.setEnabled(True)
        self.dateEdit_date.setEnabled(True)
        self.checkBox_Search.setEnabled(True)
        self.treeWidget.clear()
        self.action = self.sender()
        self.label_Active_Session.setText(self.action.objectName())
        self.path_session = os.path.join(os.getcwd(),'sessions', self.action.objectName())

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
