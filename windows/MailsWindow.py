from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QScrollArea

from threads import ThreadShowMails,ThreadDownload
from QTreeItem import QTreeItem
from Settings import Settings
from gui import mails_window
from windows import MailWindow,App

class Mails(QtWidgets.QWidget, mails_window.Ui_MailsWindow):
    def __init__(self,item: QTreeItem,limit,path_session):
        super(Mails, self).__init__()
        self.setupUi(self)
        self.path_session = path_session
        self.thread = None
        self.thread_download = None
        self.conn = item.conn
        self.uids = item.uids
        self.treeWidget.itemDoubleClicked.connect(self.show_mail)
        self.fill_tree_widget(limit)
        self.pushButton_Download_All.clicked.connect(self.download)
        Settings.setUp(self)

    def download(self):
        pass
        # self.thread_download = ThreadDownload.ThreadDownload(self.path_session)
        # self.thread_download.finished.connect(self.end_download)
        # self.thread_download.start()

    def end_download(self):
        self.thread_download.finished.disconnect(self.end_load)#
        self.thread_download = None
        App.App.show_warning_mes("Mails are loaded")

    def fill_tree_widget(self,limit):
        self.thread = ThreadShowMails.ThreadShowMails(self.conn, self.uids,limit, self)
        self.thread.start()


    def show_mail(self,it,col):
        self.mail_window = MailWindow.App(it.contenet)
        self.mail_window.show()

    def closeEvent(self, event):
        self.thread.isStop = True
        self.thread = None
        self.close()
