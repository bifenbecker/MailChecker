import json,App
import os
import sys

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from gui import settings_window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QUrl, QRect
import PyQt5.QtWebEngineWidgets

class App(QtWidgets.QWidget,settings_window.Ui_Form):
    def __init__(self,main_window):
        super(App, self).__init__()
        self.setupUi(self)
        self.window = main_window
        self.pushButton_Save_Settings.clicked.connect(self.save_settings)
        self.pushButton_Browse.clicked.connect(self.browse)
        self.default_settings()
        self.is_save_path_switched = False

    def default_settings(self):
        self.radioButton_EN.setChecked(True)
        self.radioButton_LightTheme.setChecked(True)
        self.lineEdit_Save_Path.setText("ActiveSession/download")

    def browse(self):
        save_path_download = QFileDialog.getExistingDirectory(self,"Choose")
        self.lineEdit_Save_Path.setText(save_path_download)
        self.is_save_path_switched = True

    def load_theme(self):
        with open('settings.json') as file:
            settings = json.load(file)
        path = "styles/{0}.txt".format(settings['Theme'].replace(' ',''))
        with open(path) as theme:
            style = theme.read()
            self.window.setStyleSheet("")
            self.setStyleSheet("")
            self.window.setStyleSheet(style)
            self.setStyleSheet(style)

    def save_settings(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Do you want to apply the changes?")
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            settings = self.get_settings()
            with open("settings.json", 'w') as json_file:
                json.dump(settings, json_file)
            self.load_theme()



    def get_settings(self):
        settings = {}
        for child in self.children()[0].children():
            if isinstance(child,QtWidgets.QGroupBox):
                for obj in child.children()[0].children():
                    if isinstance(obj,QtWidgets.QRadioButton):
                        if obj.isChecked():
                            settings[obj.parent().parent().title()] = obj.text()
                    if isinstance(obj,QtWidgets.QLineEdit):
                        if self.is_save_path_switched:
                            if os.path.exists(self.lineEdit_Save_Path.text()):
                                settings[obj.parent().parent().title()] = self.lineEdit_Save_Path.text()
                            else:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Information)
                                msgBox.setText("Save path isn't correct")
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                                returnValue = msgBox.exec()
                                settings[obj.parent().parent().title()] = ""
                        else:
                            settings[obj.parent().parent().title()] = ""
        return settings
