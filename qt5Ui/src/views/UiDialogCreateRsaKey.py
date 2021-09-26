from codeGen.Ui_DialogCreateRsaKeyBase import Ui_DialogCreateRsaKeyBase
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.DialogCreateRsaKeyProcessor import DialogCreateRsaKeyProcessor
from model.SSHConfig import SSHConfig
from utils.Const import Const

class UiDialogCreateRsaKey(Ui_DialogCreateRsaKeyBase):

    def __init__(self):
        super().__init__()
        self.processor = DialogCreateRsaKeyProcessor()
        self.const = Const()

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

        statusMessage = self.processor.connectBySshAndGenerateRsaKey(sshTarget)
        if(self.isSuccess(statusMessage)):
            self.popUpWindow(self.const.INFO, statusMessage)
            Dialog.accept()
        else:
            self.popUpWindow(self.const.ERROR, statusMessage)
            
    def isSuccess(self, status):
        if(status=="Success"):
            return True
        return False
    
    def popUpWindow(self, title, message):
        self.MessageBox.setWindowTitle("Error")
        self.MessageBox.setText(message)
        self.MessageBox.exec_()