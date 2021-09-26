from dao.ConnectionDataDAO import ConnectionDataDAO
from dao.ProjectDirDAO import ProjectDirDAO

class MainWindowProcessor():
    def __init__(self):
        self.conDAO = ConnectionDataDAO()
        self.projectDirDAO = ProjectDirDAO()

    def refreshConnectionData(self):
        self.conDAO.refresh()
    
    def getConDataFromDAO(self):
        return self.conDAO.getData()

    def getProjectDirDockerComposeTypesFromDAO(self):
        return self.projectDirDAO.getProjectDirDockerComposeTypes()
    
    def saveProjectDirAndDockerComposeTypes(self, projectDir):
        self.projectDirDAO.saveProjectDirAndDockerComposeTypes(projectDir)
