from dao.ConnectionDataDAO import ConnectionDataDAO
from dao.ProjectDirDAO import ProjectDirDAO
import subprocess
from model.MachineInfo import MachineInfo
from utils.Const import Const

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
        completedProcess = subprocess.run(['./bin/startContainer.sh', machineInfo.getProjectDir()+'/'+machineInfo.getDockerComposeType(), machineInfo.getMachine()])
        status = self.getStatusMessage(completedProcess.returncode)
        return status
    
    def getStatusMessage(self, returnCode):
        if(returnCode==1):
            return "startContainer.sh failed! Please enter correct arguments"
        if(returnCode==0):
            return Const.SUCCESS
