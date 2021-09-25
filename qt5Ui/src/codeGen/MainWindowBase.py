# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindowBase.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWIndowBase(object):
    def setupUi(self, MainWIndowBase):
        MainWIndowBase.setObjectName("MainWIndowBase")
        MainWIndowBase.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWIndowBase)
        self.centralwidget.setObjectName("centralwidget")
        MainWIndowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWIndowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWIndowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWIndowBase)
        self.statusbar.setObjectName("statusbar")
        MainWIndowBase.setStatusBar(self.statusbar)
        self.actionCreate_Rsa_Key = QtWidgets.QAction(MainWIndowBase)
        self.actionCreate_Rsa_Key.setObjectName("actionCreate_Rsa_Key")
        self.menuSettings.addAction(self.actionCreate_Rsa_Key)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWIndowBase)
        QtCore.QMetaObject.connectSlotsByName(MainWIndowBase)

    def retranslateUi(self, MainWIndowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWIndowBase.setWindowTitle(_translate("MainWIndowBase", "MainWindow"))
        self.menuSettings.setTitle(_translate("MainWIndowBase", "Settings"))
        self.actionCreate_Rsa_Key.setText(_translate("MainWIndowBase", "Create SSH Rsa Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWIndowBase = QtWidgets.QMainWindow()
    ui = Ui_MainWIndowBase()
    ui.setupUi(MainWIndowBase)
    MainWIndowBase.show()
    sys.exit(app.exec_())
