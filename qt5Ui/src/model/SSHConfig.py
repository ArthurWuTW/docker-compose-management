class SSHConfig():
    def __init__(self):
        self.ip = None
        self.port = None
        self.username = None
        self.password = None
    def setIP(self, ip):
        self.ip = ip
    def setPort(self, port):
        self.port = port
    def setUsername(self, username):
        self.username = username
    def setPassword(self, password):
        self.password = password
    def getIP(self):
        return self.ip
    def getPort(self):
        return self.port
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password