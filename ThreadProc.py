import threading
import time,asyncio
from PyQt5.QtCore import QThread, pyqtSignal
import MailData


class TreadProc(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,*args):
        super().__init__()
        self.args = args[0]

    def run(self):
        proc = 100/len(self.args)
        chv = proc
        for i in range(len(self.args)):
            MailData.MailData.add_to_data_base(self.args[i].strip())
            # threading.Thread(target=MailData.MailData.add_to_data_base,args=self.args[i].strip(), daemon=True).start()
            QThread.msleep(10)
            self.change_value.emit(chv)
            chv += proc