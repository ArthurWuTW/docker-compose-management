from codeGen.Ui_DialogCreateRsaKeyBase import Ui_DialogCreateRsaKeyBase
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.DialogCreateRsaKeyProcessor import DialogCreateRsaKeyProcessor

class UiDialogCreateRsaKey(Ui_DialogCreateRsaKeyBase):

    def __init__(self):
        super().__init__()
        self.processor = DialogCreateRsaKeyProcessor()

    def setupUi(self, UiDialogCreateRsaKey):
        super().setupUi(UiDialogCreateRsaKey)
        self.ButtonCreateRsaKey.clicked.connect(self.clickButtonCreateRsaKey)

    def clickButtonCreateRsaKey(self):
        print(self.lineEditIP.text())
        print(self.lineEditUsername.text())
        print(self.lineEditPassword.text())
        print(self.lineEditPort.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qDialog = QtWidgets.QDialog()
    ui = UiDialogCreateRsaKey()
    ui.setupUi(qDialog)
    qDialog.show()
    sys.exit(app.exec_())