import json
from utils.Const import Const

class JsonFileUtil():
    def __init__(self):
        self.const = Const()
    def saveFile(self, data):
        with open(self.const.CONNECTION_DATA_FILE, 'w') as file:
            json.dump(data, file)

    def getConnectionJson(self):
        with open(self.const.CONNECTION_DATA_FILE) as jsonFile:
            return json.load(jsonFile)