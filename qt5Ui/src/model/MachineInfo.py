class MachineInfo():
    def __init__(self):
        self.machine = None
        self.dockerComposeType = None
    def setMachine(self, machine):
        self.machine = machine
    def setDockerComposeType(self, dockerComposeType):
        self.dockerComposeType = dockerComposeType
    def getMachine(self):
        return self.machine
    def getDockerComposeType(self):
        return self.dockerComposeType