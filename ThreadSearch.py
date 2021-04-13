from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class ThreadSearch(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,requests = ()):
        super().__init__()
        self.requests = requests

    def run(self):
        Connections.get_result_filter(self.requests)


    def stop(self):
        self.exec_()