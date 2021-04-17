# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1149, 810)
        MainWindow.setMinimumSize(QtCore.QSize(1149, 810))
        MainWindow.setMaximumSize(QtCore.QSize(1149, 810))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1151, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 5, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_Statistic = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_Statistic.setFont(font)
        self.groupBox_Statistic.setObjectName("groupBox_Statistic")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_Statistic)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 361, 471))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(4, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_Checked = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Checked.setText("")
        self.label_Checked.setObjectName("label_Checked")
        self.gridLayout_3.addWidget(self.label_Checked, 4, 1, 1, 1)
        self.label_Accounts = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Accounts.setText("")
        self.label_Accounts.setObjectName("label_Accounts")
        self.gridLayout_3.addWidget(self.label_Accounts, 2, 1, 1, 1)
        self.label_unvalid = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_unvalid.setObjectName("label_unvalid")
        self.gridLayout_3.addWidget(self.label_unvalid, 8, 0, 1, 1)
        self.label_valid = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_valid.setObjectName("label_valid")
        self.gridLayout_3.addWidget(self.label_valid, 6, 0, 1, 1)
        self.label_checked = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_checked.setObjectName("label_checked")
        self.gridLayout_3.addWidget(self.label_checked, 4, 0, 1, 1)
        self.label_accounts = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Seb Neue Light")
        self.label_accounts.setFont(font)
        self.label_accounts.setStyleSheet("font-family: \"Seb Neue Light\";")
        self.label_accounts.setLineWidth(1)
        self.label_accounts.setTextFormat(QtCore.Qt.AutoText)
        self.label_accounts.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_accounts.setObjectName("label_accounts")
        self.gridLayout_3.addWidget(self.label_accounts, 2, 0, 1, 1)
        self.label_Valid = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Valid.setText("")
        self.label_Valid.setObjectName("label_Valid")
        self.gridLayout_3.addWidget(self.label_Valid, 6, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 5, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 3, 0, 1, 1)
        self.label_Unvalid = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Unvalid.setText("")
        self.label_Unvalid.setObjectName("label_Unvalid")
        self.gridLayout_3.addWidget(self.label_Unvalid, 8, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 5, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_3.addWidget(self.line_8, 1, 1, 1, 1)
        self.label_active_session = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_active_session.setObjectName("label_active_session")
        self.gridLayout_3.addWidget(self.label_active_session, 0, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_3.addWidget(self.line_7, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 7, 0, 1, 1)
        self.label_Active_Session = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Active_Session.setText("")
        self.label_Active_Session.setObjectName("label_Active_Session")
        self.gridLayout_3.addWidget(self.label_Active_Session, 0, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 7, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Connections = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Connections.setFont(font)
        self.label_Connections.setObjectName("label_Connections")
        self.horizontalLayout_3.addWidget(self.label_Connections)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setStyleSheet("height: 17px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.label_status = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_3.addWidget(self.label_status)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 9, 0, 1, 2)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.horizontalLayout.addWidget(self.groupBox_Statistic)
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Seb Neue Light")
        font.setPointSize(12)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_Filter = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Filter.setStyleSheet("")
        self.groupBox_Filter.setObjectName("groupBox_Filter")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_Filter)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 656, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_Date = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Date.setEnabled(False)
        self.checkBox_Date.setObjectName("checkBox_Date")
        self.gridLayout.addWidget(self.checkBox_Date, 2, 0, 1, 1)
        self.dateEdit_date = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_date.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(16)
        self.dateEdit_date.setFont(font)
        self.dateEdit_date.setObjectName("dateEdit_date")
        self.gridLayout.addWidget(self.dateEdit_date, 2, 1, 1, 1)
        self.spinBox_Amount_letters = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_Amount_letters.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(16)
        self.spinBox_Amount_letters.setFont(font)
        self.spinBox_Amount_letters.setStyleSheet("")
        self.spinBox_Amount_letters.setObjectName("spinBox_Amount_letters")
        self.gridLayout.addWidget(self.spinBox_Amount_letters, 0, 1, 1, 1)
        self.checkBox_Only_Seen = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Only_Seen.setEnabled(False)
        self.checkBox_Only_Seen.setObjectName("checkBox_Only_Seen")
        self.gridLayout.addWidget(self.checkBox_Only_Seen, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_display_letters_from = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_display_letters_from.setObjectName("label_display_letters_from")
        self.gridLayout.addWidget(self.label_display_letters_from, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_Filter)
        self.groupBox_Requests = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Requests.setObjectName("groupBox_Requests")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_Requests)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 17, 571, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(10, 5, 0, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Search = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Search.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue ExtBd")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setStyleSheet("")
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.gridLayout_2.addWidget(self.pushButton_Search, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.checkBox_Search = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_Search.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_Search.setFont(font)
        self.checkBox_Search.setObjectName("checkBox_Search")
        self.gridLayout_2.addWidget(self.checkBox_Search, 0, 0, 1, 1)
        self.label_subject = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Seb Neue Light")
        font.setPointSize(10)
        self.label_subject.setFont(font)
        self.label_subject.setObjectName("label_subject")
        self.gridLayout_2.addWidget(self.label_subject, 3, 0, 1, 1)
        self.label_body = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Seb Neue Light")
        font.setPointSize(10)
        self.label_body.setFont(font)
        self.label_body.setObjectName("label_body")
        self.gridLayout_2.addWidget(self.label_body, 5, 0, 1, 1)
        self.label_from = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Seb Neue Light")
        font.setPointSize(10)
        self.label_from.setFont(font)
        self.label_from.setObjectName("label_from")
        self.gridLayout_2.addWidget(self.label_from, 1, 0, 1, 1)
        self.lineEdit_From = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_From.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(13)
        self.lineEdit_From.setFont(font)
        self.lineEdit_From.setObjectName("lineEdit_From")
        self.gridLayout_2.addWidget(self.lineEdit_From, 2, 0, 1, 2)
        self.lineEdit_Subject = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Subject.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(13)
        self.lineEdit_Subject.setFont(font)
        self.lineEdit_Subject.setObjectName("lineEdit_Subject")
        self.gridLayout_2.addWidget(self.lineEdit_Subject, 4, 0, 1, 2)
        self.lineEdit_Body = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Body.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Seb Neue")
        font.setPointSize(13)
        self.lineEdit_Body.setFont(font)
        self.lineEdit_Body.setObjectName("lineEdit_Body")
        self.gridLayout_2.addWidget(self.lineEdit_Body, 6, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 11)
        self.horizontalLayout_2.addWidget(self.groupBox_Requests)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 21))
        self.menubar.setObjectName("menubar")
        self.menuLoad = QtWidgets.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        self.menuChoose_session = QtWidgets.QMenu(self.menubar)
        self.menuChoose_session.setObjectName("menuChoose_session")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_mails = QtWidgets.QAction(MainWindow)
        self.actionLoad_mails.setObjectName("actionLoad_mails")
        self.actionAdd_Session = QtWidgets.QAction(MainWindow)
        self.actionAdd_Session.setObjectName("actionAdd_Session")
        self.actionDelete_Session = QtWidgets.QAction(MainWindow)
        self.actionDelete_Session.setObjectName("actionDelete_Session")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionLoad_file = QtWidgets.QAction(MainWindow)
        self.actionLoad_file.setObjectName("actionLoad_file")
        self.actionLoad_link = QtWidgets.QAction(MainWindow)
        self.actionLoad_link.setObjectName("actionLoad_link")
        self.menuLoad.addAction(self.actionLoad_file)
        self.menuLoad.addAction(self.actionLoad_link)
        self.menuChoose_session.addAction(self.actionAdd_Session)
        self.menuChoose_session.addAction(self.actionDelete_Session)
        self.menuChoose_session.addSeparator()
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuLoad.menuAction())
        self.menubar.addAction(self.menuChoose_session.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mail Checker"))
        self.groupBox_Statistic.setTitle(_translate("MainWindow", "Statistic"))
        self.label_unvalid.setText(_translate("MainWindow", "Unvalid:"))
        self.label_valid.setText(_translate("MainWindow", "Valid:"))
        self.label_checked.setText(_translate("MainWindow", "Checked:"))
        self.label_accounts.setText(_translate("MainWindow", "Accounts:"))
        self.label_active_session.setText(_translate("MainWindow", "Active session"))
        self.label_Connections.setText(_translate("MainWindow", "Connections"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Email"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Password"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Request"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Amount"))
        self.groupBox_Filter.setTitle(_translate("MainWindow", "Filters"))
        self.checkBox_Date.setText(_translate("MainWindow", "Date"))
        self.dateEdit_date.setDisplayFormat(_translate("MainWindow", "dd.mm.yyyy"))
        self.checkBox_Only_Seen.setText(_translate("MainWindow", "Only seen"))
        self.label_display_letters_from.setText(_translate("MainWindow", "Display letters from"))
        self.groupBox_Requests.setTitle(_translate("MainWindow", "Requests"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))
        self.checkBox_Search.setText(_translate("MainWindow", "Search in letters"))
        self.label_subject.setText(_translate("MainWindow", "Subject"))
        self.label_body.setText(_translate("MainWindow", "Body"))
        self.label_from.setText(_translate("MainWindow", "From"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
        self.menuChoose_session.setTitle(_translate("MainWindow", "Select session"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionLoad_mails.setText(_translate("MainWindow", "Load mails"))
        self.actionAdd_Session.setText(_translate("MainWindow", "Add Session"))
        self.actionDelete_Session.setText(_translate("MainWindow", "Delete Session"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionLoad_file.setText(_translate("MainWindow", "Load file"))
        self.actionLoad_link.setText(_translate("MainWindow", "Load link"))
