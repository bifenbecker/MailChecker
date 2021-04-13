from threading import *
import os, json
from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class TreadProc(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path):
        super().__init__()
        self.path_session = path


    def run(self):
        with open(os.path.join(self.path_session, "users.json")) as json_file:
            users = json.load(json_file)
        proc = 100 / len(users)
        chv = proc
        tasks = [Thread(target=Connections.get_connection, args=(user,)) for user in users]
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
            self.change_value.emit(chv)
            chv += proc


    def stop(self):
        self.exec_()

