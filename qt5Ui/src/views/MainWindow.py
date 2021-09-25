from codeGen.MainWindowBase import Ui_MainWindowBase
from PyQt5 import QtCore, QtGui, QtWidgets

class UiMainWindow(Ui_MainWindowBase):
    def setupUi(self, UiMainWindow):
        super().setupUi(UiMainWindow)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(qWindow)
    qWindow.show()
    sys.exit(app.exec_())