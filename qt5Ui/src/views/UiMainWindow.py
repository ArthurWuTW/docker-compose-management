from codeGen.Ui_MainWindowBase import Ui_MainWindowBase
from UiDialogCreateRsaKey import UiDialogCreateRsaKey
from PyQt5 import QtCore, QtGui, QtWidgets

class UiMainWindow(Ui_MainWindowBase):
    def __init__(self):
        super().__init__()
        self.qDialogCreateRsaKey = None

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.actionCreate_Rsa_Key.triggered.connect(self.showDialogCreateRsaKeyCallback)

    def showDialogCreateRsaKeyCallback(self):
        self.qDialogCreateRsaKey = QtWidgets.QDialog()
        ui = UiDialogCreateRsaKey()
        ui.setupUi(self.qDialogCreateRsaKey)
        self.qDialogCreateRsaKey.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(qWindow)
    qWindow.show()
    sys.exit(app.exec_())