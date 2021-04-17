import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QScrollArea, QAbstractItemView
import json
from threads import ThreadShowMails,ThreadDownload
from QTreeItem import QTreeItem
from Settings import Settings
from gui import mails_window
from windows import MailWindow,App

class Mails(QtWidgets.QWidget, mails_window.Ui_MailsWindow):
    def __init__(self,item: QTreeItem,uids,path_session):
        super(Mails, self).__init__()
        self.setupUi(self)
        self.path_session = path_session
        self.thread = None
        self.thread_download = None
        self.uids = uids
        self.item = item
        self.treeWidget.itemDoubleClicked.connect(self.show_mail)
        self.fill_tree_widget()
        self.pushButton_Download_All.clicked.connect(self.download)
        self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        Settings.setUp(self)

    def download(self):
        with open("settings.json") as json_file:
            settings = json.load(json_file)
        download_path = settings['Save']
        if download_path == "":
            download_path = os.path.join(self.path_session,'download emails',self.item.text(0))
        else:
            download_path = os.path.join(download_path,'download emails',self.item.text(0))

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        if self.thread_download is None:
            self.thread_download = ThreadDownload.ThreadDownload(download_path,self.item.conn,self.uids)
            self.thread_download.change_value.connect(self.setProgressBar)
            self.thread_download.finished.connect(self.end_download)
            self.thread_download.start()


    def setProgressBar(self,value):
        self.progressBar.setValue(value)

    def end_download(self):
        self.thread_download.finished.disconnect(self.end_download)#
        self.thread_download = None
        App.App.show_warning_mes("Mails are loaded")

    def fill_tree_widget(self):
        self.thread = ThreadShowMails.ThreadShowMails(self.item.conn, self.uids, self)
        self.thread.start()


    def show_mail(self,it,col):
        self.mail_window = MailWindow.App(it.contenet)
        self.mail_window.show()

    def closeEvent(self, event):
        self.thread.isStop = True
        self.thread = None
        self.close()
