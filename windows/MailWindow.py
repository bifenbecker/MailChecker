from PyQt5.QtWidgets import QVBoxLayout
from bs4 import BeautifulSoup
from Settings import Settings
from gui import mail_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
import PyQt5.QtWebEngineWidgets
import html.parser

class App(QtWidgets.QWidget,mail_window.Ui_MailWindow):
    def __init__(self,content):
        super(App, self).__init__()
        self.setupUi(self)

        # soup = BeautifulSoup(content, features="html.parser")
        #
        # # kill all script and style elements
        # for script in soup(["script", "style"]):
        #     script.extract()  # rip it out
        #
        # # get text
        # text = soup.get_text()
        #
        # # break into lines and remove leading and trailing space on each
        # lines = (line.strip() for line in text.splitlines())
        # # break multi-headlines into a line each
        # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # # drop blank lines
        # text = '\n'.join(chunk for chunk in chunks if chunk)
        # self.content = text.replace('\n','').replace('\t','').replace('\r','')

        self.content = content
        self.m_output = PyQt5.QtWebEngineWidgets.QWebEngineView()
        self.m_output.setHtml(self.content)
        self.verticalLayout.addWidget(self.m_output)
        Settings.setUp(self)
