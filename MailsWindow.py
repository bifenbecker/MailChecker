from PyQt5 import QtWidgets

from gui import mails_window

class App(QtWidgets.QWidget, mails_window.Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)