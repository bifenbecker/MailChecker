from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl

from Settings import Settings
from gui import mails_window
from windows import MailWindow

class App(QtWidgets.QWidget, mails_window.Ui_MailsWindow):
    def __init__(self,search_result):
        super(App, self).__init__()
        self.setupUi(self)
        self.search_result = search_result
        self.treeWidget.itemDoubleClicked.connect(self.show_mail)
        self.fill_tree_widget()
        Settings.setUp(self)

    def fill_tree_widget(self):
        for mail in self.search_result:
            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, str(mail[1]))
            item.setText(1, mail[3])
            item.setText(2, mail[2])
            item.setText(3, mail[5])
            self.treeWidget.addTopLevelItem(item)
            self.treeWidget.expandAll()

    def show_mail(self,it,col):
        indexes = self.treeWidget.selectionModel().selectedRows(col)
        for index in sorted(indexes):
            i = index.row()
            content = self.search_result[i][4]
        self.mail_window = MailWindow.App(content)
        self.mail_window.show()
