from threading import *
import os, json
from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class ThreadDownload(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path,conn,uids):
        super().__init__()
        self.path = path
        self.conn = conn
        self.uids = uids

    def run(self):
        proc = 100 / len(self.uids)
        chv = proc
        # download process
        for uid in self.uids:

            Connections.download_mail(self.conn,uid,self.path)
            self.change_value.emit(chv)
            chv += proc

    def stop(self):
        self.exec_()

