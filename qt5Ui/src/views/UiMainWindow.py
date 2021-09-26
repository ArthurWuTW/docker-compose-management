from codeGen.Ui_MainWindowBase import Ui_MainWindowBase
from views.UiDialogCreateRsaKey import UiDialogCreateRsaKey
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.MainWindowProcessor import MainWindowProcessor 
from model.MachineInfo import MachineInfo
from utils.Const import Const

class UiMainWindow(Ui_MainWindowBase):
    def __init__(self):
        super().__init__()
        self.qDialogCreateRsaKey = None
        self.processor = MainWindowProcessor()
        self.projectDirData = self.processor.getProjectDirDockerComposeTypesFromDAO()
        self.connectionData = self.processor.getConDataFromDAO()
        self.currentMachineInfo = MachineInfo()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.MessageBox = QtWidgets.QMessageBox()
        self.actionCreate_Rsa_Key.triggered.connect(self.showDialogCreateRsaKeyCallback)
        self.treeWidgetMachineStatus.itemClicked.connect(self.onItemClicked)
        self.pushButtonSave.clicked.connect(self.saveSelectedDockerComposeType)
        self.pushButtonDeploy.clicked.connect(self.deploy)
        self.toolButtonProjectDir.clicked.connect(self.openFileDialog)
        self.lineEditProjectDir.setText(self.projectDirData['projectDir'])
        self.updateCombobox([''])
        self.updateTreeWidget()

    def deploy(self):
        statusMessage = self.processor.deploy(self.currentMachineInfo)
        if(self.isSuccess(statusMessage)):
            self.popUpWindow(Const.INFO, statusMessage)
        else:
            self.popUpWindow(Const.ERROR, statusMessage)
    
    def isSuccess(self, status):
        return True if status == Const.SUCCESS else False
    
    def saveSelectedDockerComposeType(self):
        machineInfo = MachineInfo()
        machineInfo.setMachine(self.lineEditMachineName.text())
        machineInfo.setDockerComposeType(self.comboBox.currentText())
        self.processor.updateDockerComposeType(machineInfo)
        self.connectionData = self.processor.getConDataFromDAO()
        self.updateTreeWidget()

    def updateTreeWidget(self):
        self.treeWidgetMachineStatus.clear()
        for con in self.connectionData['data']:
            item = QtWidgets.QTreeWidgetItem(self.treeWidgetMachineStatus)
            item.setText(0, con['machine'])
            item.setText(1, con['dockerComposeType'])

    def openFileDialog(self):
        self.projectDir = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEditProjectDir.setText(self.projectDir)
        self.processor.saveProjectDirAndDockerComposeTypes(self.projectDir)
        self.projectDirData = self.processor.getProjectDirDockerComposeTypesFromDAO()
        self.updateCombobox([''])

    def showDialogCreateRsaKeyCallback(self):
        self.qDialogCreateRsaKey = QtWidgets.QDialog()
        ui = UiDialogCreateRsaKey()
        ui.setupUi(self.qDialogCreateRsaKey)
        result = self.qDialogCreateRsaKey.exec_()
        if(self.isAccept(result)):
            self.processor.refreshConnectionData()
            print(self.processor.getConDataFromDAO())
    
    def isAccept(self, result):
        return True if result == 1 else False

    def updateCombobox(self, preList):
        self.comboBox.clear()
        self.comboBox.addItems(preList+self.projectDirData['dockerComposeType'])

    def onItemClicked(self, item, column):
        self.lineEditMachineName.setText(item.text(0))
        self.comboBox.setCurrentText(item.text(1))

        self.currentMachineInfo.setMachine(item.text(0))
        self.currentMachineInfo.setDockerComposeType(item.text(1))
        self.currentMachineInfo.setProjectDir(self.projectDirData['projectDir'])

    def popUpWindow(self, title, message):
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(message)
        self.MessageBox.exec_()

