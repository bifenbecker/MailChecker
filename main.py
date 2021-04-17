import sys
from PyQt5 import QtWidgets,QtGui
from windows import App


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App.App()
    window.setWindowIcon(QtGui.QIcon('icon.ico'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
