import asyncio
import json

import PyQt5,MailData,ThreadProc
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

from Settings import Settings
from gui import prev_window
from windows import App



class PrevLoad(QtWidgets.QWidget, prev_window.Ui_PrevWindow):
    def __init__(self,path):
        super(PrevLoad, self).__init__()

        self.setupUi(self)
        self.path = path
        self.thread = None
        self.f = None
        self.pushButton_swap_file.clicked.connect(self.swap_to_file_load)
        self.pushButton_swap_link.clicked.connect(self.swap_to_link_load)
        self.pushButton_load_file.clicked.connect(self.load_file)
        self.pushButton_load_data_file.clicked.connect(self.load_data)
        self.pushButton_load_data_link.clicked.connect(self.load_data)
        self.pushButton_Cancel_Load.clicked.connect(self.cancel_load)
        self.lang = Settings.setUp(self)[1]

    def load_file(self):
        res = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        fname = res[0]
        if fname.split(".")[-1] == "txt":
            with open(fname) as file:
                self.f = fname
        elif res[1] != "" and fname.split(".")[-1] != "text":
            App.App.show_warning_mes(self.lang['file_is_not_.txt'])

    def load_data(self):
        if self.f is not None:
            with open(self.f) as file:
                if self.thread is None:
                    self.thread = ThreadProc.TreadProc(path=self.path,args=file.readlines())
                    self.thread.change_value.connect(self.set_progress_bar)
                    self.thread.finished.connect(self.go_main_window)
                    self.thread.start()
        else:
            App.App.show_warning_mes(self.lang["input_link_or_choose_file"])


    def cancel_load(self):
        if self.thread is not None:
            self.thread.stop()
            self.thread = None
        self.close()


    def go_main_window(self):
        self.thread.change_value.disconnect(self.set_progress_bar)
        self.thread.finished.disconnect(self.go_main_window)
        self.thread = None
        App.App.show_warning_mes(self.lang["mails_were_loaded"])
        self.close()

    def set_progress_bar(self,value):
        self.progressBar.setValue(value)

    def swap_to_file_load(self):
        self.stackedWidget.setCurrentIndex(1)

    def swap_to_link_load(self):
        self.stackedWidget.setCurrentIndex(0)


