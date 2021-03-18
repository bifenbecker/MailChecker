import App,sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App.App()
    sys.exit(app.exec_())
    # main()