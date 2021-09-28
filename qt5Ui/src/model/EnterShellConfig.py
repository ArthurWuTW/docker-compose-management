class EnterShellConfig():
    def __init__(self):
        self.machine = None
        self.container = None
        self.loginUser = None
    def setMachine(self, machine):
        self.machine = machine
    def setContainer(self, container):
        self.container = container
    def setLoginUser(self, loginUser):
        self.loginUser = loginUser
    def getMachine(self):
        return self.machine
    def getContainer(self):
        return self.container
    def getLoginUser(self):
        return self.loginUser
