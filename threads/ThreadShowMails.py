from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class ThreadShowMails(QThread):

    def __init__(self,conn,uids,window):
        super().__init__()
        self.isStop = False
        self.conn = conn
        self.uids = uids
        self.window = window


    def run(self):
        for uid in self.uids:
            try:
                mail = Connections.get_mail(self.conn, uid)
            except OSError:
                break
            if mail is not None:
                item = QTreeItem.QTreeItem(self.uids,self.conn,mail['content'])
                item.setText(0, mail['data'])
                item.setText(1, mail['subject'])
                item.setText(2, mail['from'])
                item.setText(3, mail['type'])
                self.window.treeWidget.addTopLevelItem(item)
            if self.isStop:
                break


    def stop(self):
        self.exec_()