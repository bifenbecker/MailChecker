import json
import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import Internet
from Connections import Connections
from QDragPushButton import QDragPushButton
from gui import load_file_window
from Settings import Settings
from threads import ThreadProc
from windows import App

class LoadFileWindow(QtWidgets.QWidget, load_file_window.Ui_Form):
    def __init__(self,main_window,path_session):
        super(LoadFileWindow, self).__init__()
        self.setupUi(self)
        self.isFileOpen = False
        self.thread = None
        self.main_window = main_window
        self.path_session = path_session
        Settings.setUp(self)
        self.pushButton_Cancel.clicked.connect(self.cancel_load)
        self.pushButton_OK.clicked.connect(self.ok)
        self.pushButton_LoadFile.clicked.connect(self.load)
        self.lang = Settings.setUp(self)[1]


    def load(self):
        res = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        fname = res[0]
        self.file_name = res[0].split('/')[-1]
        if fname.split(".")[-1] == "txt":
            with open(fname) as file:
                self.isFileOpen = True
                self.save_json_file(file.readlines(),self.file_name)
                self.label.setText(self.file_name)
        elif res[1] != "" and fname.split(".")[-1] != "text":
            App.App.show_warning_mes(self.lang['file_is_not_.txt'])

    def save_json_file(self, data,file_name):
        res = []
        for line in data:
            user_mail = line.split(":")[0]
            user_pass = line.split(":")[-1].strip()
            user = {"mail": user_mail, "password": user_pass}
            res.append(user)
        path = os.path.join(self.path_session, "{0}.json".format(file_name.split('.')[0]))
        with open(path, 'w+') as json_file:
            json.dump(res, json_file)

    def ok(self):
        if self.isFileOpen:
            Connections.reset()
            if Internet.run_check():
                if self.thread is None:
                    self.thread = ThreadProc.TreadProc(path=self.path_session)
                    self.thread.change_value.connect(self.set_progress_bar)
                    self.thread.finished.connect(self.succsessful_load)
                    self.thread.start()
                    self.main_window.label_status.setText("Load...")
            else:
                App.App.show_warning_mes("Check Internet connection")
        else:
            App.App.show_warning_mes(self.lang["input_link_or_choose_file"])

    def set_progress_bar(self,value):
        self.main_window.progressBar.setValue(value)

    def succsessful_load(self):
        self.main_window.progressBar.setValue(0)
        self.main_window.label_status.setText("OK")
        self.main_window.isLoad_Mails = True
        self.main_window.search_btn_enable()
        self.thread.change_value.disconnect(self.set_progress_bar)
        self.thread.finished.disconnect(self.succsessful_load)
        self.thread = None
        self.close()

    def cancel_load(self):
        if self.thread is not None:
            self.thread.stop()
            self.thread.isStop = True
            self.thread = None
        self.close()

