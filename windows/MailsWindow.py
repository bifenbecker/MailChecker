from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QScrollArea
from ThreadShowMails import ThreadShowMails
from QTreeItem import QTreeItem
from Settings import Settings
from gui import mails_window
from windows import MailWindow

class App(QtWidgets.QWidget, mails_window.Ui_MailsWindow):
    def __init__(self,item: QTreeItem,limit):
        super(App, self).__init__()
        self.setupUi(self)
        self.thread = None
        self.conn = item.conn
        self.uids = item.uids
        self.treeWidget.itemDoubleClicked.connect(self.show_mail)
        self.fill_tree_widget(limit)
        Settings.setUp(self)

    # def wheelEvent(self, event):
    #     if event.angleDelta().y() < 0:


    def fill_tree_widget(self,limit):
        self.thread = ThreadShowMails(self.conn, self.uids,limit, self)
        self.thread.start()


    def show_mail(self,it,col):
        self.mail_window = MailWindow.App(it.contenet)
        self.mail_window.show()

    def closeEvent(self, event):
        self.thread.isStop = True
        self.thread = None
        self.close()
