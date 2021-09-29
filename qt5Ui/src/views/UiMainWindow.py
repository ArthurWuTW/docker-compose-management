from codeGen.Ui_MainWindowBase import Ui_MainWindowBase
from views.UiDialogCreateRsaKey import UiDialogCreateRsaKey
from PyQt5 import QtCore, QtGui, QtWidgets
from controller.MainWindowProcessor import MainWindowProcessor 
from model.MachineInfo import MachineInfo
from utils.Const import Const
from model.EnterShellConfig import EnterShellConfig

class UiMainWindow(Ui_MainWindowBase):
    def __init__(self):
        super().__init__()
        self.qDialogCreateRsaKey = None
        self.processor = MainWindowProcessor()
        self.projectDirData = self.processor.getProjectDirDockerComposeTypesFromDAO()
        self.currentMachineInfo = MachineInfo()
        self.containerName = None

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.MessageBox = QtWidgets.QMessageBox()
        self.actionCreate_Rsa_Key.triggered.connect(self.showDialogCreateRsaKeyCallback)
        self.treeWidgetMachineStatus.itemClicked.connect(self.onItemClicked)
        self.treeWidgetDockerContainerStatus.itemClicked.connect(self.onContainerClicked)
        self.pushButtonDeployRefresh.clicked.connect(self.refreshDeployStatus)
        self.pushButtonSave.clicked.connect(self.saveSelectedDockerComposeType)
        self.pushButtonEnterContainer.clicked.connect(self.enterContainer)
        self.pushButtonDeployStop.clicked.connect(self.stopContainer)
        self.pushButtonDeploy.clicked.connect(self.deploy)
        self.toolButtonProjectDir.clicked.connect(self.openFileDialog)
        self.lineEditProjectDir.setText(self.projectDirData[Const.PROJECT_DIR])
        self.updateCombobox([''])
        self.updateTreeWidget()

    def enterContainer(self):
        enterShellConfig = EnterShellConfig()
        enterShellConfig.setMachine(self.lineEditMachineName.text())
        enterShellConfig.setContainer(self.containerName)
        enterShellConfig.setLoginUser(self.lineEditUserName.text())
        self.processor.enterContainer(enterShellConfig)
    
    def onContainerClicked(self, item, column):
        self.containerName = item.text(0)

    def stopContainer(self):
        statusMessage = self.processor.stopContainer(self.currentMachineInfo)
        self.popUpWindow(Const.INFO, statusMessage)
        self.refreshDeployStatus()
    
    def refreshDeployStatus(self):
        self.processor.refreshConnectionData()
        self.updateTreeWidget()
        self.treeWidgetDockerContainerStatus.clear()

    def deploy(self):
        statusMessage = self.processor.deploy(self.currentMachineInfo)
        self.popUpWindow(Const.INFO, statusMessage)
        self.refreshDeployStatus()
    
    def saveSelectedDockerComposeType(self):
        machineInfo = MachineInfo()
        machineInfo.setMachine(self.lineEditMachineName.text())
        machineInfo.setDockerComposeType(self.comboBox.currentText())
        self.processor.updateDockerComposeType(machineInfo)
        self.processor.refreshConnectionData()
        self.updateTreeWidget()

    def updateTreeWidget(self):
        self.treeWidgetMachineStatus.clear()
        for con in self.processor.getConDataFromDAO()[Const.DATA]:
            item = QtWidgets.QTreeWidgetItem(self.treeWidgetMachineStatus)
            item.setText(0, con[Const.MACHINE])
            item.setText(1, con[Const.DOCKER_COMPOSE_TYPE])
            item.setText(2, con[Const.DEPLOY_STATUS])

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
            self.updateTreeWidget()
            print(self.processor.getConDataFromDAO())
    
    def isAccept(self, result):
        return True if result == 1 else False

    def updateCombobox(self, preList):
        self.comboBox.clear()
        self.comboBox.addItems(preList+self.projectDirData[Const.DOCKER_COMPOSE_TYPE])

    def onItemClicked(self, item, column):
        self.lineEditMachineName.setText(item.text(0))
        self.comboBox.setCurrentText(item.text(1))

        self.currentMachineInfo.setMachine(item.text(0))
        self.currentMachineInfo.setDockerComposeType(item.text(1))
        self.currentMachineInfo.setDeployStatus(item.text(2))
        self.currentMachineInfo.setProjectDir(self.projectDirData[Const.PROJECT_DIR])
        
        self.refreshDockerContainerProcess(self.currentMachineInfo)

    def popUpWindow(self, title, message):
        self.MessageBox.setWindowTitle(title)
        self.MessageBox.setText(message)
        self.MessageBox.exec_()
    
    def refreshDockerContainerProcess(self, machineInfo):
        self.treeWidgetDockerContainerStatus.clear()
        stringArrayOfArray = self.processor.refreshDockerContainerProcess(machineInfo)
        if self.isNotNone(stringArrayOfArray):
            for out in stringArrayOfArray:
                if self.isMatchTreeWidgetColumnSize(out, 4):
                    item = QtWidgets.QTreeWidgetItem(self.treeWidgetDockerContainerStatus)
                    item.setText(0, out[0])
                    item.setText(1, out[1])
                    item.setText(2, out[2])
                    item.setText(3, out[3])
    
    def isNotNone(self, resultObject):
        return True if resultObject != None else False
    
    def isMatchTreeWidgetColumnSize(self, arr, size):
        return True if len(arr) >= size else False
    
    def isNotEmpty(self, text):
        return True if text != Const.EMPTY else False


