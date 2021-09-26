from model.SSHConfig import SSHConfig
import subprocess
from dao.ConnectionDataDAO import ConnectionDataDAO
from utils.Const import Const

class DialogCreateRsaKeyProcessor():
    def __init__(self):
        self.conDAO = ConnectionDataDAO()
    def connectBySshAndGenerateRsaKey(self, sshTarget):
        completedProcess = subprocess.run(['./bin/generateRsaKeyIfExistAndFetchToMachine.sh', sshTarget.getIP(), sshTarget.getPort(), sshTarget.getUsername(), sshTarget.getPassword()])
        status = self.getStatusMessage(completedProcess.returncode)
        if(self.isSuccess(status)):
            self.conDAO.addConnectionBySshConfig(sshTarget)

        return status

    def getStatusMessage(self, returnCode):
        if(returnCode==1):
            return "generateRsaKeyIfExistAndFetchToMachine.sh failed! Please enter correct arguments"
        if(returnCode==0):
            return Const.SUCCESS
    
    def isSuccess(self, status):
        return True if status == Const.SUCCESS else False