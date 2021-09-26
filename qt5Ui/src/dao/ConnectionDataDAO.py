from model.SSHConfig import SSHConfig
import os
from utils.JsonFileUtil import JsonFileUtil
from utils.Const import Const

class ConnectionDataDAO():
    def __init__(self):
        self.const = Const()
        self.fileUtil = JsonFileUtil()
        self.data = {'data': []}
        if(not os.path.isfile(self.const.CONNECTION_DATA_FILE)):
            self.saveOrUpdate(self.data)
        else:
            self.data = self.fileUtil.getConnectionJson()
    
    def saveOrUpdate(self, connectionData):
        self.fileUtil.saveFile(connectionData)

    def addConnectionBySshConfig(self, sshConfig):
        if sshConfig.getUsername()+'@'+sshConfig.getIP() not in self.data['data']:
            self.data['data'].append(sshConfig.getUsername()+'@'+sshConfig.getIP())
            self.fileUtil.saveFile(self.data)
            self.data = self.fileUtil.getConnectionJson()