from dao.ConnectionDataDAO import ConnectionDataDAO
from dao.ProjectDirDAO import ProjectDirDAO
import subprocess
from model.MachineInfo import MachineInfo
from utils.Const import Const
import threading

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
        self.updateDeployStatus(machineInfo, Const.DEPLOY)
        t = threading.Thread(target = self.job, args=(machineInfo,))
        t.start()
        return "background job running"
    
    def job(self, machineInfo):
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
