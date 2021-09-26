class MachineInfo():
    def __init__(self):
        self.machine = None
        self.dockerComposeType = None
        self.projectDir = None
    def setMachine(self, machine):
        self.machine = machine
    def setDockerComposeType(self, dockerComposeType):
        self.dockerComposeType = dockerComposeType
    def setProjectDir(self, projectDir):
        self.projectDir = projectDir
    def getMachine(self):
        return self.machine
    def getDockerComposeType(self):
        return self.dockerComposeType
    def getProjectDir(self):
        return self.projectDir