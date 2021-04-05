import sys
from PyQt5 import QtWidgets
from windows import App

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App.App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
