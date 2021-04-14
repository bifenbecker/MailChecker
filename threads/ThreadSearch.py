from PyQt5.QtCore import QThread, pyqtSignal
from Connections import *


class ThreadSearch(QThread):
    change_value = pyqtSignal(float)

    def __init__(self,requests = (),table_requset = ""):
        super().__init__()
        self.table_request = table_requset
        self.requests = requests

    def run(self):
        Connections.get_result_filter(self.table_request, self.requests)

    def stop(self):
        self.exec_()