from dao.ConnectionDataDAO import ConnectionDataDAO

class MainWindowProcessor():
    def __init__(self):
        self.conDAO = ConnectionDataDAO()

    def refreshConnectionData(self):
        self.conDAO.refresh()
    
    def getConDataFromDAO(self):
        return self.conDAO.getData()