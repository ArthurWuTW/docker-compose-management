from codeGen.Ui_DialogCreateRsaKeyBase import Ui_DialogCreateRsaKeyBase
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.DialogCreateRsaKeyProcessor import DialogCreateRsaKeyProcessor
from model.SSHConfig import SSHConfig
from utils.Const import Const

class UiDialogCreateRsaKey(Ui_DialogCreateRsaKeyBase):

    def __init__(self):
        super().__init__()
        self.processor = DialogCreateRsaKeyProcessor()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.ButtonCreateRsaKey.clicked.connect(lambda: self.clickButtonCreateRsaKeyAndPassKeyToTarget(Dialog))
        self.ButtonExit.clicked.connect(Dialog.reject)
        self.MessageBox = QtWidgets.QMessageBox()

    def clickButtonCreateRsaKeyAndPassKeyToTarget(self, Dialog):
        sshTarget = SSHConfig()
        sshTarget.setIP(self.lineEditIP.text())
        sshTarget.setUsername(self.lineEditUsername.text())
        sshTarget.setPassword(self.lineEditPassword.text())
        sshTarget.setPort(self.lineEditPort.text())

        statusMessage = self.processor.connectBySshAndGenerateRsaKey(sshTarget)
        if(self.isSuccess(statusMessage)):
            self.popUpWindow(Const.INFO, statusMessage)
            Dialog.accept()
        else:
            self.popUpWindow(Const.ERROR, statusMessage)
            
    def isSuccess(self, status):
        if(status == Const.SUCCESS):
            return True
        return False
    
    def popUpWindow(self, title, message):
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(message)
        self.MessageBox.exec_()