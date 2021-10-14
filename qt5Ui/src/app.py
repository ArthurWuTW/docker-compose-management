import sys

if __name__ == "__main__":

    from views.UiMainWindow import UiMainWindow
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(qWindow)
    qWindow.show()
    sys.exit(app.exec_())
