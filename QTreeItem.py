from PyQt5 import QtWidgets


class QTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(self,data):
        super(QTreeItem, self).__init__()
        self.data = data