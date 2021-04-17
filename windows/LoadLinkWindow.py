from PyQt5 import QtWidgets, QtGui
from QDragPushButton import QDragPushButton
from gui import load_link_window
from Settings import Settings

class LoadLinkWindow(QtWidgets.QWidget, load_link_window.Ui_Form):
    def __init__(self):
        super(LoadLinkWindow, self).__init__()
        self.setupUi(self)
        Settings.setUp(self)

