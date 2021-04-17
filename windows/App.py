import json
import os
import re
import Internet
from threads import ThreadProc,ThreadSearch
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog, QMessageBox
from Connections import Connections
from Settings import Settings
from windows import LoadLinkWindow,LoadFileWindow, AddSessionWindow, DeleteSessionWindow, SettingsWindow, MailsWindow, MailWindow
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
        self.setup()
        self.actionLoad_file.triggered.connect(self.load_from_file)
        self.actionLoad_link.triggered.connect(self.load_from_link)
        self.actionAdd_Session.triggered.connect(self.add_session)
        self.actionDelete_Session.triggered.connect(self.delete_session)
        self.actionSettings.triggered.connect(self.show_settings_window)
        self.treeWidget.itemDoubleClicked.connect(self.show_mails_window)
        self.pushButton_Search.clicked.connect(self.search)
        self.checkBox_Date.clicked.connect(self.search_btn_enable)
        self.checkBox_Only_Seen.clicked.connect(self.search_btn_enable)
        self.checkBox_Search.clicked.connect(self.search_btn_enable)
        self.checkBox_Search.clicked.connect(self.enable_search_lines)
        self.isLoad_Mails = False
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

    def _check_checkBoxes(self):
        if self.checkBox_Date.isChecked() or self.checkBox_Only_Seen.isChecked() or self.checkBox_Search.isChecked():
            return True
        else:
            return False

    def search_btn_enable(self):
        if self._check_checkBoxes() and self.isLoad_Mails:
            self.pushButton_Search.setEnabled(True)
        else:
            self.pushButton_Search.setEnabled(False)

    def _check_latin(self,requsts: list):
        for req in requsts:
            if re.search(r'[а-яА-Я]', req):
                return False
        return True


    def search(self):
        if self.checkBox_Search.isChecked() or self.checkBox_Date.isChecked() or self.checkBox_Only_Seen.isChecked():
            if len(Connections.connections) != 0:
                filtres = [self._check_only_seen(), self._check_date()]
                text_search = [self._check_from(), self._check_subject(), self._check_body()]
                table_request = ""
                requests = []

                for filter in filtres:
                    if filter[0]:
                        request = '({0} "{1}")'.format(filter[1], filter[2]).replace(' ""', '')
                        table_req = '{0} {1},'.format(filter[1], filter[2]).replace(' ""', '')
                        table_request += table_req
                        requests.append(request)

                if self.checkBox_Search.isChecked():
                    search_req = "(OR "
                    r = 0
                    empty_lines = 0
                    for st in text_search:
                        if st[0]:
                            r += 1
                            req = '({0} "{1}") '.format(st[1], st[2])
                            table_req = '{0} {1},'.format(st[1], st[2])
                            table_request += table_req
                            search_req += req
                        else:
                            empty_lines += 1

                    if r == 1:
                        search_req = search_req[4:-1]
                    else:
                        search_req = search_req[:-1] + ")"

                    if empty_lines != len(text_search):
                        requests.append(search_req)

                if self._check_latin(requests) and len(requests) != 0:
                    if Internet.run_check():
                        self.treeWidget.clear()
                        if self.thread is None:
                            table_request = table_request[:-1]
                            self.thread = ThreadSearch.ThreadSearch(tuple(requests), table_request)
                            self.thread.finished.connect(self.search_finish)
                            self.thread.start()
                    else:
                        App.show_warning_mes("Check Internet connection")

            else:
                App.show_warning_mes("Load")
        else:
            App.show_warning_mes("Choose filters or search text")


    def search_finish(self):
        self.thread = None

    def _check_from(self):
        if self.lineEdit_From.text() != "":
            return True, "FROM", self.lineEdit_From.text()
        return False, "", ""

    def _check_subject(self):
        if self.lineEdit_Subject.text() != "":
            return True, "SUBJECT", self.lineEdit_Subject.text()
        return False, "", ""

    def _check_body(self):
        if self.lineEdit_Body.text() != "":
            return True, "BODY", self.lineEdit_Body.text()
        return False, "", ""

    def _check_only_seen(self):
        if self.checkBox_Only_Seen.isChecked():
            return True, "SEEN", ""
        return False, "", ""

    def _check_date(self):
        if self.checkBox_Date.isChecked():
            date = Connections.parse_date(self.dateEdit_date.date())
            return True, "SINCE", date
        return False, "", ""

    def show_mails_window(self,item,col):
        limit = int(self.spinBox_Amount_letters.text())
        lim = -1 if limit == 0 else limit
        uids = item.uids[0].split()[-1:-lim - 1:-1]
        self.mails_window = MailsWindow.Mails(item,uids,self.path_session)
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


    def isFile_json_in_session(self):
        isFile = False
        files = os.listdir(self.path_session)
        for file in files:
            if ".json" in file:
                isFile = True

        return isFile

    def select_session(self):
        action = self.sender()
        self.path_session = os.path.join(os.getcwd(), 'sessions', action.objectName())
        self.label_Active_Session.setText(action.objectName())

        if self.isFile_json_in_session():
            if Internet.run_check():
                if self.thread is None:
                    Connections.reset()
                    # self.checkBox_Only_Seen.setEnabled(True)
                    # self.checkBox_Date.setEnabled(True)
                    # self.dateEdit_date.setEnabled(True)
                    # self.checkBox_Search.setEnabled(True)
                    self.thread = ThreadProc.TreadProc(path=self.path_session)
                    self.thread.change_value.connect(self.set_progress_bar)
                    self.thread.finished.connect(self.succsessful_load)
                    self.thread.start()
                    self.label_status.setText("Load...")
                else:
                    App.show_warning_mes("Wait ending of process")
            else:
                App.show_warning_mes("Check Internet connection")


    def succsessful_load(self):
        self.progressBar.setValue(0)
        self.label_status.setText("OK")
        self.isLoad_Mails = True
        self.checkBox_Only_Seen.setEnabled(True)
        self.checkBox_Date.setEnabled(True)
        self.checkBox_Search.setEnabled(True)
        self.dateEdit_date.setEnabled(True)
        self.thread.change_value.disconnect(self.set_progress_bar)
        self.thread.finished.disconnect(self.succsessful_load)
        self.thread = None


    def set_progress_bar(self,value):
        self.progressBar.setValue(value)

    def load_from_file(self):
        if self.path_session is not None:
            self.load_from_file_window = LoadFileWindow.LoadFileWindow(self,self.path_session)
            self.load_from_file_window.show()
        else:
            App.show_warning_mes(self.lang["select_session"])

    def load_from_link(self):
        if self.path_session is not None:
            self.load_from_link_window = LoadLinkWindow.LoadLinkWindow()
            self.load_from_link_window.show()
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
