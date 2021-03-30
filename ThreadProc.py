import threading
import time,asyncio
from PyQt5.QtCore import QThread, pyqtSignal
from multiprocessing import Process,Lock
import MailData


class TreadProc(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path,args):
        super().__init__()
        self.args = args
        self.path = path

    def run(self):
        proc = 100 / len(self.args)
        chv = proc
        preccess = [Process(target=MailData.MailData.get_mails, args=(arg.strip(),self.path,)) for arg in self.args]
        for process in preccess:
            process.start()
            self.change_value.emit(chv)
            chv += proc
        for process in preccess:
            process.join()

    def stop(self):
        self.exec_()

