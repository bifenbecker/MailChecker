from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton


class QDragPushButton(QPushButton):
    def __init__(self,form):
        super(QDragPushButton, self).__init__(form)
        self.setAcceptDrops(True)
        self.form = form

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        file_name = a0.mimeData().text().split('/')[-1]

        with open(file_name) as file:
            self.form.parent().isFileOpen = True
            self.form.parent().save_json_file(file.readlines(),file_name)


        self.form.parent().label.setText(file_name)
        self.setStyleSheet("")
        self.setStyleSheet("height: 50px;"
                           "background-color: ;"
                           "color: ;")

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        if a0.mimeData().hasText():
            a0.accept()
            self.setStyleSheet("")
            self.setStyleSheet("height: 50px;"
                               "background-color: #b0b0b0;"
                               "color: black;")
        else:
            a0.ignore()

    def dragLeaveEvent(self, a0: QtGui.QDragLeaveEvent) -> None:
        self.setStyleSheet("")
        self.setStyleSheet("height: 50px;"
                           "background-color: ;"
                           "color: ;")

