import time

import PyQt5,sys,MailData,ExceptionBreak,DialogWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog

import PrevLoadWindow
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
        self.label.setStyleSheet(file_style_label)
        self.label_2.setStyleSheet(file_style_label)
        self.label_3.setStyleSheet(file_style_label)
        self.label_4.setStyleSheet(file_style_label)
        self.label_Accounts.setStyleSheet(file_style_label)
        self.label_Checked.setStyleSheet(file_style_label)
        self.label_Valid.setStyleSheet(file_style_label)
        self.label_Unvalid.setStyleSheet(file_style_label)

    def initUi(self):
        self.setupUi(self)
        self.label_style_setup()
        self.groupBox_style_setup()
        self.checkBox_style_setup()
        self.actionLoad_mails.triggered.connect(self.Load)
        self.show()

    def Load(self):
        self.prev_load_menu = PrevLoadWindow.App()
        self.prev_load_menu.setWindowModality(Qt.ApplicationModal)
        self.prev_load_menu.show()

