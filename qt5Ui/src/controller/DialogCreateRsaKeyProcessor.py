from model.SSHConfig import SSHConfig
import subprocess
from dao.ConnectionDataDAO import ConnectionDataDAO
from utils.Const import Const

class DialogCreateRsaKeyProcessor():
    def __init__(self):
        self.conDAO = ConnectionDataDAO()
        self.const = Const()
    def connectBySshAndGenerateRsaKey(self, sshTarget):
        completedProcess = subprocess.run(['./bin/generateRsaKeyIfExistAndFetchToMachine.sh', sshTarget.getIP(), sshTarget.getPort(), sshTarget.getUsername(), sshTarget.getPassword()])
        status = self.getStatusMessage(completedProcess.returncode)
        if(self.isSuccess(status)):
            print(self.const.SUCCESS+"sadasdf")
            self.conDAO.addConnectionBySshConfig(sshTarget)

        return status

    def getStatusMessage(self, returnCode):
        if(returnCode==1):
            return "generateRsaKeyIfExistAndFetchToMachine.sh failed! Please enter correct arguments"
        if(returnCode==0):
            return self.const.SUCCESS
    
    def isSuccess(self, status):
        return True if status == self.const.SUCCESS else False