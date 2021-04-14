from threading import *
import os, json
from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class ThreadDownload(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,path):
        super().__init__()
        self.path = path


    def run(self):
        with open("settings.json") as json_file:
            settings = json.load(json_file)
        download_path = settings['Save']
        if download_path == "":
            download_path = self.path
        for i in range(5):
            print(download_path)


    def stop(self):
        self.exec_()

