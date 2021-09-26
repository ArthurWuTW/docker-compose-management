from model.SSHConfig import SSHConfig
import subprocess

class DialogCreateRsaKeyProcessor():
    def connectBySshAndGenerateRsaKey(self, sshTarget):
        completedProcess = subprocess.run(['./bin/generateRsaKeyIfExistAndFetchToMachine.sh', sshTarget.getIP(), sshTarget.getPort(), sshTarget.getUsername(), sshTarget.getPassword()])
        return self.getStatusMessage(completedProcess.returncode)

    def getStatusMessage(self, returnCode):
        if(returnCode==1):
            return "generateRsaKeyIfExistAndFetchToMachine.sh failed! Please enter correct arguments"
        if(returnCode==0):
            return "Success"