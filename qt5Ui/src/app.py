import sys
import json
class ConfigJsonParser():
    def __init__(self):
        self.data = {}
    def parse(self, file):
        with open(file) as jsonFile:
            self.data = json.load(jsonFile)
    def getJsonData(self):
        return self.data
    
class SubmodulePackageRelativePathImporter():
    def __init__(self):
        self.parser = ConfigJsonParser()
    def importSubmoduleDependencyPath(self, file):
        self.parser.parse(file)
        print(self.parser.getJsonData())
        for path in self.parser.getJsonData()['packageRelativePath']:
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