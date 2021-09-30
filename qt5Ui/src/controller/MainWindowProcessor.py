from dao.ConnectionDataDAO import ConnectionDataDAO
from dao.ProjectDirDAO import ProjectDirDAO
import subprocess
from model.MachineInfo import MachineInfo
from model.EnterShellConfig import EnterShellConfig
from utils.Const import Const
import threading
import re

class MainWindowProcessor():
    def __init__(self):
        self.conDAO = ConnectionDataDAO()
        self.projectDirDAO = ProjectDirDAO()

    def refreshConnectionData(self):
        self.conDAO.refresh()
    
    def getConDataFromDAO(self):
        return self.conDAO.getData()

    def getProjectDirDockerComposeTypesFromDAO(self):
        return self.projectDirDAO.getProjectDirDockerComposeTypes()
    
    def saveProjectDirAndDockerComposeTypes(self, projectDir):
        self.projectDirDAO.saveProjectDirAndDockerComposeTypes(projectDir)
    
    def updateDockerComposeType(self, machineInfo):
        self.conDAO.updateDockerComposeType(machineInfo)
    
    def deploy(self, machineInfo):
        self.updateDeployStatus(machineInfo, Const.EMPTY)
        self.updateDeployStatus(machineInfo, Const.DEPLOY)
        t = threading.Thread(target = self.startJob, args=(machineInfo,))
        t.start()
        return Const.BACKGROUND_JOB_RUNNING
    
    def stopContainer(self, machineInfo):
        self.updateDeployStatus(machineInfo, Const.CLOSING)
        t = threading.Thread(target = self.closeJob, args=(machineInfo,))
        t.start()
        return Const.BACKGROUND_JOB_RUNNING
    
    def enterJob(self, enterShellConfig):
        _ = subprocess.run(['./bin/openAnotherTerminalAndRun.sh', enterShellConfig.getMachine(), enterShellConfig.getLoginUser(), enterShellConfig.getContainer()])
    
    def enterContainer(self, enterShellConfig):
        t = threading.Thread(target = self.enterJob, args=(enterShellConfig,))
        t.start()

    def closeJob(self, machineInfo):
        completedProcess = subprocess.run(['./bin/stopContainer.sh', machineInfo.getProjectDir()+'/'+machineInfo.getDockerComposeType(), machineInfo.getMachine()])
        status = self.getStatusMessage(completedProcess.returncode)
        self.updateDeployStatus(machineInfo, Const.SLEEPING if self.isSuccess(status) else Const.FAILED)
    
    def startJob(self, machineInfo):
        completedProcess = subprocess.run(['./bin/startContainer.sh', machineInfo.getProjectDir()+'/'+machineInfo.getDockerComposeType(), machineInfo.getMachine()])
        status = self.getStatusMessage(completedProcess.returncode)
        self.updateDeployStatus(machineInfo, Const.SUCCESS if self.isSuccess(status) else Const.FAILED)
    
    def isSuccess(self, status):
        return True if status == Const.SUCCESS else False

    def getStatusMessage(self, returnCode):
        if(returnCode==1):
            return Const.FAILED
        if(returnCode==0):
            return Const.SUCCESS
    
    def updateDeployStatus(self, machineInfo, status):
        machineInfo.setDeployStatus(status)
        self.conDAO.updateDeployStatus(machineInfo)
    
    def refreshDockerContainerProcess(self, machineInfo):
        print(machineInfo.getDeployStatus())
        if(self.isSuccess(machineInfo.getDeployStatus())):
            completedProcess = subprocess.Popen(['./bin/checkContainerStatus.sh', machineInfo.getProjectDir()+'/'+machineInfo.getDockerComposeType(), machineInfo.getMachine()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = completedProcess.communicate()
            outArray = out.decode('utf-8').split('\n')
            stringArray = []
            for row in outArray:
                stringArray.append(re.split(Const.TWO_SPACE_OR_MORE,row))
            return stringArray
        
    def checkConnection(self, machineInfo):
        completedProcess = subprocess.run(['./bin/checkConnection.sh', machineInfo.getMachine()])
        status = self.getStatusMessage(completedProcess.returncode)
        self.updateDeployStatus(machineInfo, machineInfo.getDeployStatus() if self.isSuccess(status) else Const.LOST_CONNECTION)
    
