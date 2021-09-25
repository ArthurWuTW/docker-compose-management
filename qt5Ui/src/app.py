import sys
import json
class ConfigJsonParser():
    def __init__(self):
        self.data = {}
    def parse(self, file):
        with open(file) as jsonFile:
            self.data = json.load(jsonFile)
    def getDictData(self):
        return self.data
    
class SubmodulePackageRelativePathImporter():
    def __init__(self):
        self.jsonParser = ConfigJsonParser()
    def importSubmoduleDependencyPath(self, file):
        self.jsonParser.parse(file)
        for path in self.jsonParser.getDictData()['packageRelativePath']:
            sys.path.append(path)

if __name__ == "__main__":
    importer = SubmodulePackageRelativePathImporter()
    importer.importSubmoduleDependencyPath('config.json')

    from views.UiMainWindow import UiMainWindow
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(qWindow)
    qWindow.show()
    sys.exit(app.exec_())