import threading
import time,asyncio
from PyQt5.QtCore import QThread, pyqtSignal
from multiprocessing import Process,Lock
import Connections


class TreadProc(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path,args):
        super().__init__()
        self.args = args
        self.path = path

    def run(self):
        proc = 100 / len(self.args)
        chv = proc
        preccess = [Process(target=Connections.Connections.get_connections, args=(arg.split(":")[0],arg.split(":")[1].strip(),)) for arg in self.args]
        for process in preccess:
            process.start()
            self.change_value.emit(chv)
            chv += proc
        for process in preccess:
            process.join()
        # asyncio.run(self.go())

    async def go(self):
        proc = 100 / len(self.args)
        chv = proc
        for arg in self.args:
            mail = arg.split(":")[0]
            passwd = arg.split(":")[-1].strip()
            await Connections.Connections.get_connections(mail,passwd)
            self.change_value.emit(chv)
            chv += proc


    def stop(self):
        self.exec_()

