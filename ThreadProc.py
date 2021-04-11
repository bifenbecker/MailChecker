import os
import threading
import time,asyncio
from PyQt5.QtCore import QThread, pyqtSignal
from logic import app
from multiprocessing import Process,Lock

from logic.database.database import SQLiteDB


class TreadProc(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path,args,fname):
        super().__init__()
        self.file_name = fname
        self.args = args
        self.path = path

    def run(self):
        proc = 100 / len(self.args)
        chv = proc
        db_location = os.path.join(self.path, 'database.db')
        create_db = True
        create_tables = True
        sqlite_db = SQLiteDB(db_location, create_db, create_tables)
        # preccess = [Process(target=MailData.MailData.get_mails, args=(arg.strip(),self.path,)) for arg in self.args]
        # for process in preccess:
        #     process.start()
        #     self.change_value.emit(chv)
        #     chv += proc
        # for process in preccess:
        #     process.join()

        try:
            for arg in self.args:
                user = {"login": arg.strip().split(":")[0], "password": arg.strip().split(":")[1]}

                print(user)
                app.run(user, self.path, self.file_name, sqlite_db)

                self.change_value.emit(chv)
                chv += proc
        except:
            self.stop()


    def stop(self):
        self.exec_()

