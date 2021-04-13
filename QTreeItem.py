from PyQt5 import QtWidgets


class QTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(self,uids,conn,content = None):
        super(QTreeItem, self).__init__()
        self.uids = uids
        self.conn = conn
        self.contenet = content