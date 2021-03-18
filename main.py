import App,sys,asyncio
from PyQt5 import QtWidgets

async def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App.App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    asyncio.run(main())
