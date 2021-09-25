from codeGen.DialogCreateRsaKeyBase import Ui_DialogCreateRsaKeyBase
from PyQt5 import QtCore, QtGui, QtWidgets



class UiDialogCreateRsaKey(Ui_DialogCreateRsaKeyBase):
    def setupUi(self, UiDialogCreateRsaKey):
        super().setupUi(UiDialogCreateRsaKey)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qDialog = QtWidgets.QDialog()
    ui = UiDialogCreateRsaKey()
    ui.setupUi(qDialog)
    qDialog.show()
    sys.exit(app.exec_())