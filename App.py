import PyQt5,sys,MailData,ExceptionBreak,asyncio,prev_window
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidget, QAbstractItemView, QFileDialog, QDialog


class App(QtWidgets.QMainWindow, prev_window.Ui_Form):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(App, self).__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.show()
        self.Load_Data_Button.clicked.connect(self.Load)
        self.pushButton_Load_File.clicked.connect(self.load_file())

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        if fname.split(".")[-1] == "txt":
            with open(fname) as file:
                mails = list(map(lambda x:x[:-1].split(":"),file.readlines()))
                try:
                    data_mails = MailData.MailData(mails)
                    
                except ExceptionBreak as e:
                    self.Warning_Message.setText(e.mes)

        else:
            self.Warning_Message.setText("Try again choose file(.txt)")


    def Load(self):
        print("1")

    def resizeEvent(self, event):
        self.resized.emit()
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 30, self.size().width(), self.size().height()))
        return super(App, self).resizeEvent(event)
