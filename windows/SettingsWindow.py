import json
import os
import sys
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from windows import App
from Settings import Settings
from gui import settings_window
from PyQt5 import QtWidgets, QtGui

class App(QtWidgets.QWidget,settings_window.Ui_SettingsWindow):
    def __init__(self,main_window):
        super(App, self).__init__()
        self.setupUi(self)
        self.window = main_window
        self.pushButton_Save_Settings.clicked.connect(self.save_settings)
        self.pushButton_BrowseCurrentSession.clicked.connect(self.browse_current_session)
        self.pushButton_Browse.clicked.connect(self.browse)
        self.default_settings()
        Settings.setUp(self)
        self.is_save_path_switched = False

    def browse_current_session(self):
        if self.window.path_session is None:
            App.App.show_warning_mes("Select session")
        else:
            self.lineEdit_Save.setText(self.window.path_session)

    def default_settings(self):
        with open('settings.json') as file:
            settings = json.load(file)
            for key in settings:
                name = "radioButton_" + settings[key].replace(' ','')
                name2 = "lineEdit_" + key
                try:
                    rb = self.findChild(QtWidgets.QRadioButton,name)
                    rb.setChecked(True)
                except:
                    le = self.findChild(QtWidgets.QLineEdit, name2)
                    if settings[key] == "":
                        le.setText("ActiveSession/")
                    else:
                        le.setText(settings[key])


    def browse(self):
        save_path_download = QFileDialog.getExistingDirectory(self,"Choose")
        self.lineEdit_Save.setText(save_path_download)
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
            with open("settings.json", 'w',encoding='utf-8') as json_file:
                json.dump(settings, json_file)
            Settings.setUp(self)
            Settings.setUp(self.window)
            self.window.setup()


    def get_settings(self):
        settings = {}
        for child in self.children()[0].children():
            if isinstance(child,QtWidgets.QGroupBox):
                for obj in child.children()[0].children():
                    if isinstance(obj,QtWidgets.QRadioButton):
                        if obj.isChecked():
                            settings[obj.parent().parent().objectName().split("_")[-1]] = obj.objectName().split("_")[-1]
                    if isinstance(obj,QtWidgets.QLineEdit):
                        if self.is_save_path_switched:
                            if os.path.exists(self.lineEdit_Save.text()):
                                settings[obj.parent().parent().objectName().split("_")[-1]] = self.lineEdit_Save.text()
                            else:
                                msgBox = QMessageBox()
                                msgBox.setIcon(QMessageBox.Information)
                                msgBox.setText("Save path isn't correct")
                                msgBox.setWindowTitle("Warning")
                                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                                returnValue = msgBox.exec()
                                settings[obj.parent().parent().objectName().split("_")[-1]] = ""
                        else:
                            settings[obj.parent().parent().objectName().split("_")[-1]] = ""
        return settings
