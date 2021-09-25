from codeGen.Ui_DialogCreateRsaKeyBase import Ui_DialogCreateRsaKeyBase
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.DialogCreateRsaKeyProcessor import DialogCreateRsaKeyProcessor
from controller.model.SSHConfig import SSHConfig

class UiDialogCreateRsaKey(Ui_DialogCreateRsaKeyBase):

    def __init__(self):
        super().__init__()
        self.processor = DialogCreateRsaKeyProcessor()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.ButtonCreateRsaKey.clicked.connect(lambda: self.clickButtonCreateRsaKey(Dialog))
        self.ButtonExit.clicked.connect(Dialog.reject)
        self.MessageBox = QtWidgets.QMessageBox()

    def clickButtonCreateRsaKey(self, Dialog):
        sshTarget = SSHConfig()
        sshTarget.setIP(self.lineEditIP.text())
        sshTarget.setUsername(self.lineEditUsername.text())
        sshTarget.setPassword(self.lineEditPassword.text())
        sshTarget.setPort(self.lineEditPort.text())

        if(self.connectSuccess(self.processor.connect(sshTarget))):
            Dialog.accept()
        else:
            self.MessageBox.setWindowTitle("Error")
            self.MessageBox.setText("SSH connection failed")
            self.MessageBox.exec_()

    def connectSuccess(self, status):
        if(status=="Success"):
            return True;
        return False;

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qDialog = QtWidgets.QDialog()
    ui = UiDialogCreateRsaKey()
    ui.setupUi(qDialog)
    qDialog.show()
    sys.exit(app.exec_())