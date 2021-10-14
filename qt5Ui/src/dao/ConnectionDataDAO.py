from model.SSHConfig import SSHConfig
from model.MachineInfo import MachineInfo
import os
from utils.JsonFileUtil import JsonFileUtil
from utils.Const import Const


class ConnectionDataDAO():

    def __init__(self):
        self.fileUtil = JsonFileUtil()
        self.data = {Const.DATA: []}
        if(os.path.isfile(Const.CONNECTION_DATA_FILE)):
            self.data = self.fileUtil.getConnectionJson()
        else:
            self.saveOrUpdate(self.data)

    def saveOrUpdate(self, connectionData):
        self.fileUtil.saveFile(connectionData)

    def addConnectionBySshConfig(self, sshConfig):
        if sshConfig.getUsername() + '@' + sshConfig.getIP() not in self.data[Const.DATA]:
            self.data[Const.DATA].append({
                Const.MACHINE: sshConfig.getUsername() + '@' + sshConfig.getIP(),
                Const.DOCKER_COMPOSE_TYPE: '',
                Const.DEPLOY_STATUS: ''
            })
            self.fileUtil.saveFile(self.data)
            self.data = self.fileUtil.getConnectionJson()
    
    def getData(self):
        return self.data

    def refresh(self):
        self.data = self.fileUtil.getConnectionJson()

    def updateDockerComposeType(self, machineInfo):
        connection = next(x for x in self.data[Const.DATA] if x[Const.MACHINE] == machineInfo.getMachine())
        connection[Const.DOCKER_COMPOSE_TYPE] = machineInfo.getDockerComposeType()

        self.fileUtil.saveFile(self.data)
        self.data = self.fileUtil.getConnectionJson()

    def updateDeployStatus(self, machineInfo):
        connection = next(x for x in self.data[Const.DATA] if x[Const.MACHINE] == machineInfo.getMachine())
        connection[Const.DEPLOY_STATUS] = machineInfo.getDeployStatus()

        self.fileUtil.saveFile(self.data)
        self.data = self.fileUtil.getConnectionJson()
