from model.SSHConfig import SSHConfig
from model.MachineInfo import MachineInfo
import os
from utils.JsonFileUtil import JsonFileUtil
from utils.Const import Const

class ConnectionDataDAO():
    def __init__(self):
        self.fileUtil = JsonFileUtil()
        self.data = {'data': []}
        if(os.path.isfile(Const.CONNECTION_DATA_FILE)):
            self.data = self.fileUtil.getConnectionJson()
        else:
            self.saveOrUpdate(self.data)

    def saveOrUpdate(self, connectionData):
        self.fileUtil.saveFile(connectionData)

    def addConnectionBySshConfig(self, sshConfig):
        if sshConfig.getUsername()+'@'+sshConfig.getIP() not in self.data['data']:
            self.data['data'].append({
                'machine': sshConfig.getUsername()+'@'+sshConfig.getIP(),
                'dockerComposeType': ''
            })
            self.fileUtil.saveFile(self.data)
            self.data = self.fileUtil.getConnectionJson()
    
    def getData(self):
        return self.data

    def refresh(self):
        self.data = self.fileUtil.getConnectionJson()

    def updateDockerComposeType(self, machineInfo):
        connection = next(x for x in self.data['data'] if x['machine'] == machineInfo.getMachine())
        connection['dockerComposeType'] = machineInfo.getDockerComposeType()

        self.fileUtil.saveFile(self.data)
        self.data = self.fileUtil.getConnectionJson()