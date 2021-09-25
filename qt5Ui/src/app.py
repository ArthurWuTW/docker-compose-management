import sys
import json
class ConfigParser():
    def __init__(self):
        self.data = {}
    def parseJsonFile(self, file):
        with open(file) as jsonFile:
            self.data = json.load(jsonFile)
    def getDictData(self):
        return self.data
    
class PackagePathImporter():
    def __init__(self):
        self.configParser = ConfigParser()
    def importSubmoduleDependencyPath(self, file):
        self.configParser.parseJsonFile(file)
        for path in self.configParser.getDictData()['packageRelativePath']:
            sys.path.append(path)

if __name__ == "__main__":
    importer = PackagePathImporter()
    importer.importSubmoduleDependencyPath('config.json')

    from views.UiMainWindow import UiMainWindow
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(qWindow)
    qWindow.show()
    sys.exit(app.exec_())