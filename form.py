# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1011, 711))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_Load_Data = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Load_Data.setObjectName("groupBox_Load_Data")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_Load_Data)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 10, 241, 221))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Load_Data = QtWidgets.QTabWidget(self.verticalLayoutWidget_6)
        self.Load_Data.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Load_Data.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Load_Data.setTabPosition(QtWidgets.QTabWidget.North)
        self.Load_Data.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Load_Data.setObjectName("Load_Data")
        self.tab_File = QtWidgets.QWidget()
        self.tab_File.setAcceptDrops(True)
        self.tab_File.setObjectName("tab_File")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_File)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 241, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Load_File = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Load_File.setAcceptDrops(True)
        self.pushButton_Load_File.setObjectName("pushButton_Load_File")
        self.gridLayout_2.addWidget(self.pushButton_Load_File, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.Load_Data.addTab(self.tab_File, "")
        self.tab_Proxy_Link = QtWidgets.QWidget()
        self.tab_Proxy_Link.setObjectName("tab_Proxy_Link")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_Proxy_Link)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 231, 161))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.lineEdit_Proxy_Link = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_Proxy_Link.setObjectName("lineEdit_Proxy_Link")
        self.verticalLayout_11.addWidget(self.lineEdit_Proxy_Link)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 2)
        self.Load_Data.addTab(self.tab_Proxy_Link, "")
        self.verticalLayout_8.addWidget(self.Load_Data)
        self.Load_Data_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.Load_Data_Button.setObjectName("Load_Data_Button")
        self.verticalLayout_8.addWidget(self.Load_Data_Button)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_6.addWidget(self.groupBox_Load_Data)
        self.groupBox_Stat = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Stat.setObjectName("groupBox_Stat")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_Stat)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 221, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 4, 5, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_Checked_Mails = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Checked_Mails.setText("")
        self.label_Checked_Mails.setObjectName("label_Checked_Mails")
        self.gridLayout.addWidget(self.label_Checked_Mails, 1, 1, 1, 1)
        self.label_Amount_Mails = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Amount_Mails.setText("")
        self.label_Amount_Mails.setObjectName("label_Amount_Mails")
        self.gridLayout.addWidget(self.label_Amount_Mails, 0, 1, 1, 1)
        self.label_Valid_Mails = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Valid_Mails.setText("")
        self.label_Valid_Mails.setObjectName("label_Valid_Mails")
        self.gridLayout.addWidget(self.label_Valid_Mails, 2, 1, 1, 1)
        self.label_Unvalid_Mails = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Unvalid_Mails.setText("")
        self.label_Unvalid_Mails.setObjectName("label_Unvalid_Mails")
        self.gridLayout.addWidget(self.label_Unvalid_Mails, 3, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_Stat)
        self.groupBox_Direct = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Direct.setObjectName("groupBox_Direct")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_Direct)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 10, 221, 201))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_Start = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.verticalLayout_9.addWidget(self.pushButton_Start)
        self.pushButton_Pause = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_Pause.setObjectName("pushButton_Pause")
        self.verticalLayout_9.addWidget(self.pushButton_Pause)
        self.pushButton_Stop = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.verticalLayout_9.addWidget(self.pushButton_Stop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_7)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        self.verticalLayout_6.addWidget(self.groupBox_Direct)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_Log = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Log.setObjectName("groupBox_Log")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_Log)
        self.treeWidget.setGeometry(QtCore.QRect(0, 20, 481, 531))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setMinimumSectionSize(39)
        self.treeWidget.header().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.groupBox_Log)
        self.groupBox_Message = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_Message.setObjectName("groupBox_Message")
        self.verticalLayout_5.addWidget(self.groupBox_Message)
        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Load_Data.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_Load_Data.setTitle(_translate("MainWindow", "Load"))
        self.pushButton_Load_File.setText(_translate("MainWindow", "Load file or drop here"))
        self.Load_Data.setTabText(self.Load_Data.indexOf(self.tab_File), _translate("MainWindow", "File"))
        self.label_5.setText(_translate("MainWindow", "Link"))
        self.Load_Data.setTabText(self.Load_Data.indexOf(self.tab_Proxy_Link), _translate("MainWindow", "Proxy link"))
        self.Load_Data_Button.setText(_translate("MainWindow", "Load"))
        self.groupBox_Stat.setTitle(_translate("MainWindow", "Statistic"))
        self.label_4.setText(_translate("MainWindow", "Checked Mails"))
        self.label.setText(_translate("MainWindow", "Amount Mails"))
        self.label_3.setText(_translate("MainWindow", "Valid Mails"))
        self.label_2.setText(_translate("MainWindow", "Unvalid Mails"))
        self.groupBox_Direct.setTitle(_translate("MainWindow", "Direct"))
        self.pushButton_Start.setText(_translate("MainWindow", "Start"))
        self.pushButton_Pause.setText(_translate("MainWindow", "Pause"))
        self.pushButton_Stop.setText(_translate("MainWindow", "Stop"))
        self.groupBox_Log.setTitle(_translate("MainWindow", "Log"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Email"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Password"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Request"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Found"))
        self.groupBox_Message.setTitle(_translate("MainWindow", "Message"))
