# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_session.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 160)
        Form.setMinimumSize(QtCore.QSize(300, 160))
        Form.setMaximumSize(QtCore.QSize(380, 160))
        self.comboBox_Sessions = QtWidgets.QComboBox(Form)
        self.comboBox_Sessions.setGeometry(QtCore.QRect(40, 70, 221, 22))
        self.comboBox_Sessions.setObjectName("comboBox_Sessions")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Cancel = QtWidgets.QPushButton(Form)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(170, 120, 91, 23))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.pushButton_Delete = QtWidgets.QPushButton(Form)
        self.pushButton_Delete.setGeometry(QtCore.QRect(70, 120, 91, 23))
        self.pushButton_Delete.setObjectName("pushButton_Delete")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete session"))
        self.label.setText(_translate("Form", "Select the session to be deleted"))
        self.pushButton_Cancel.setText(_translate("Form", "Cancel"))
        self.pushButton_Delete.setText(_translate("Form", "Delete"))
