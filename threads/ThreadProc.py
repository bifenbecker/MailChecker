import datetime
import shutil
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
        files = os.listdir(self.path_session)
        file_name = ""
        for file in files:
            if file.split(".")[-1] == "json":
                file_name = file.split('.')[0]
            if re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}.[0-9]{2}.[0-9]{2}',str(file)):
                shutil.rmtree(os.path.join(self.path_session,file))

        path = os.path.join(self.path_session,file_name + "_" + str(datetime.datetime.now()).split(".")[0].replace(":","."))
        os.makedirs(path)
        f_good = open(os.path.join(path,'GOOD.txt'),'w+')
        f_bad = open(os.path.join(path,'BAD.txt'),'w+')
        f_remain = open(os.path.join(path,'REMAIN.txt'),'w+')
        f_error = open(os.path.join(path,'ERROR.txt'),'w+')
        f_good.close()
        f_bad.close()
        f_remain.close()
        f_error.close()

        with open(os.path.join(self.path_session, "{0}.json".format(file_name))) as json_file:
            users = json.load(json_file)
        proc = 100 / len(users)
        chv = proc
        tasks = [Thread(target=Connections.get_connection, args=(user,path,)) for user in users]
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
            self.change_value.emit(chv)
            chv += proc



    def stop(self):
        self.exec_()

