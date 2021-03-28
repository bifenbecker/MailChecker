import App,sys,asyncio,PrevLoadWindow,DialogWindow
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App.App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
