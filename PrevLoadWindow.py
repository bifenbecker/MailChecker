import PyQt5,DialogWindow,MailData,ThreadProc
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from gui import prev_window


class App(QtWidgets.QWidget, prev_window.Ui_Form):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.thread = None
        self.f = None
        self.dialog_warning = DialogWindow.Dialog()
        self.pushButton_swap_file.clicked.connect(self.swap_to_file_load)
        self.pushButton_swap_link.clicked.connect(self.swap_to_link_load)
        self.pushButton_load_file.clicked.connect(self.load_file)
        self.pushButton_load_data_file.clicked.connect(self.load_data)
        self.pushButton_load_data_link.clicked.connect(self.load_data)
        self.pushButton_Cancel_Load.clicked.connect(self.close)


    def load_file(self):
        res = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        fname = res[0]
        if fname.split(".")[-1] == "txt":
            with open(fname) as file:
                self.dialog_warning.set_mes("File is opened\nLines:{0}".format(len(file.readlines())))
                self.dialog_warning.show()
                self.f = fname
        elif res[1] != "" and fname.split(".")[-1] != "text":
            self.dialog_warning.set_mes("File is not .txt")
            self.dialog_warning.show()

    def load_data(self):
        if self.f is not None:
            with open(self.f) as file:
                if self.thread is None:
                    self.thread = ThreadProc.TreadProc(file.readlines())
                    self.thread.change_value.connect(self.set_progress_bar)
                    self.thread.finished.connect(self.go_main_window)
                    self.thread.start()
        else:
            self.dialog_warning.set_mes("Input link or choose file")
            self.dialog_warning.show()



    def go_main_window(self):
        self.thread.change_value.disconnect(self.set_progress_bar)
        self.thread.finished.disconnect(self.go_main_window)
        self.thread = None

    def set_progress_bar(self,value):
        self.progressBar.setValue(value)

    def swap_to_file_load(self):
        self.stackedWidget.setCurrentIndex(1)

    def swap_to_link_load(self):
        self.stackedWidget.setCurrentIndex(0)


    def resizeEvent(self, event):
        self.resized.emit()
        self.stackedWidget.setGeometry(QtCore.QRect(0,0,self.size().width(),self.size().height()))
        self.gridLayout.setGeometry(QtCore.QRect(0,0,self.stackedWidget.size().width(),self.stackedWidget.size().height()))
        self.gridLayout_Load.setGeometry(QtCore.QRect(0, 0, self.size().width(), self.size().height()))
        return super(App, self).resizeEvent(event)

