import PyQt5
from gui import dialog
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

class Dialog(QtWidgets.QWidget, dialog.Ui_Dialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton_Ok.clicked.connect(self.close)
        self.pushButton_Cancel.clicked.connect(self.close)

    def set_mes(self,mes):
        self.message.setText(mes)

