from utils.JsonFileUtil import JsonFileUtil
from utils.Const import Const
import os


class ProjectDirDAO():

    def __init__(self):
        self.fileUtil = JsonFileUtil()
        self.data = {'dockerComposeType':[], 'projectDir':''}
        if(os.path.isfile(Const.PROJECT_DIR_FILE)):
            self.data = self.fileUtil.getProjectDirAndDockerComposeTypes()
        else:
            self.saveOrUpdate(self.data)
    
    def getProjectDirDockerComposeTypes(self):
        return self.data
    
    def saveOrUpdate(self, data):
        self.fileUtil.saveProjectDir(data)
    
    def saveProjectDirAndDockerComposeTypes(self, projectDir):
        self.data['projectDir'] = projectDir
        self.data['dockerComposeType'] = []
        self.data['dockerComposeType'].extend(self.fileUtil.getDockerComposeTypesByPrefix("machine-*", projectDir))
        self.fileUtil.saveProjectDir(self.data)

