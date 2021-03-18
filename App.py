import PyQt5,sys,form
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView


class App(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.show()

