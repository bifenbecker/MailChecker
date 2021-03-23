from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from design import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import os


class Second(QtWidgets.QMainWindow):
    accounts = []

    def __init__(self):
        super(Second, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.load_path)
        self.ui.pushButton_2.clicked.connect(self.load_file)

    # def hide_fields(self):
    #     self.ui.pushButton.hide()
    #     self.ui.pushButton_2.hide()
    #     self.ui.lineEdit.hide()
    #
    # def show_fields(self):
    #     self.ui.pushButton.show()
    #     self.ui.pushButton_2.show()
    #     self.ui.lineEdit.show()

    def read_file(self, file_path):
        with open(file_path, encoding="utf-8") as file:
            # self.hide_fields()
            return file.read()

    def load_path(self):
        file_path = self.ui.lineEdit.text()

        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            self.mails = self.read_file(file_path)
        else:
            self.ui.lineEdit.setText("Wrong file path")

    def load_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', '.', '(*.txt*)')[0]

        if file_path:
            Second.accounts = self.read_file(file_path).split('\n')
            self.close()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.accounts = ""
        # self.ui.centralwidget.setstyleSheet("background-image: url(https://ustroim-prazdnik.info/_pu/13/14095692.jpg);")

        self.ui.pushButton.clicked.connect(self.load_path)
        self.ui.pushButton_2.clicked.connect(self.load_file)

        # def hide_fields(self):
        #     self.ui.pushButton.hide()
        #     self.ui.pushButton_2.hide()
        #     self.ui.lineEdit.hide()
        #
        # def show_fields(self):
        #     self.ui.pushButton.show()
        #     self.ui.pushButton_2.show()
        #     self.ui.lineEdit.show()

    def change_page(self):
        self.ui.page.hide()
        self.ui.page_2.show()

    def load_accounts(self):
        pass

    def read_file(self, file_path):
        with open(file_path, encoding="utf-8") as file:
            # self.hide_fields()
            return file.read()

    def load_path(self):
        file_path = self.ui.lineEdit.text()

        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            self.accounts = self.read_file(file_path).split('\n')
            self.change_page()
        else:
            self.ui.lineEdit.setText("Wrong file path")

    def load_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', '.', '(*.txt*)')[0]

        if file_path:
            self.accounts = self.read_file(file_path).split('\n')
            self.change_page()


app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())
