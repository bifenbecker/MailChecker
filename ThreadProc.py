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
        asyncio.run(self.load_mails())

    async def load_mails(self):
        proc = 100 / len(self.args)
        chv = proc
        for i in range(len(self.args)):
            start = time.time()
            await MailData.MailData.load_imap(self.args[i].strip())
            print(time.time() - start)
            self.change_value.emit(chv)
            chv += proc