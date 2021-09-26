import json
from utils.Const import Const
import glob
import os

class JsonFileUtil():
    def saveFile(self, data):
        with open(Const.CONNECTION_DATA_FILE, 'w') as file:
            json.dump(data, file)

    def getConnectionJson(self):
        with open(Const.CONNECTION_DATA_FILE) as jsonFile:
            return json.load(jsonFile)
    
    def getProjectDirAndDockerComposeTypes(self):
        with open(Const.PROJECT_DIR_FILE) as jsonFile:
            return json.load(jsonFile)
    
    def saveProjectDir(self, data):
        with open(Const.PROJECT_DIR_FILE, 'w') as file:
            json.dump(data, file)

    def getDockerComposeTypesByPrefix(self, regex, projectDir):
        return [os.path.basename(x) for x in glob.glob(projectDir+'/'+regex)]