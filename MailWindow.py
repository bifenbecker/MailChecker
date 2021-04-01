from PyQt5.QtWidgets import QVBoxLayout

from gui import mail_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
import PyQt5.QtWebEngineWidgets

class App(QtWidgets.QWidget,mail_window.Ui_Form):
    def __init__(self,content):
        super(App, self).__init__()
        self.setupUi(self)
        self.content = content
        self.m_output = PyQt5.QtWebEngineWidgets.QWebEngineView()
        self.m_output.setHtml(self.content.decode('utf-8'))
        self.verticalLayout.addWidget(self.m_output)
