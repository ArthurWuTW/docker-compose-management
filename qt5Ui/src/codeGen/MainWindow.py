# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWIndow(object):
    def setupUi(self, MainWIndow):
        MainWIndow.setObjectName("MainWIndow")
        MainWIndow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWIndow)
        self.centralwidget.setObjectName("centralwidget")
        MainWIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWIndow)
        self.statusbar.setObjectName("statusbar")
        MainWIndow.setStatusBar(self.statusbar)
        self.actionCreate_Rsa_Key = QtWidgets.QAction(MainWIndow)
        self.actionCreate_Rsa_Key.setObjectName("actionCreate_Rsa_Key")
        self.menuSettings.addAction(self.actionCreate_Rsa_Key)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWIndow)
        QtCore.QMetaObject.connectSlotsByName(MainWIndow)

    def retranslateUi(self, MainWIndow):
        _translate = QtCore.QCoreApplication.translate
        MainWIndow.setWindowTitle(_translate("MainWIndow", "MainWindow"))
        self.menuSettings.setTitle(_translate("MainWIndow", "Settings"))
        self.actionCreate_Rsa_Key.setText(_translate("MainWIndow", "Create SSH Rsa Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWIndow = QtWidgets.QMainWindow()
    ui = Ui_MainWIndow()
    ui.setupUi(MainWIndow)
    MainWIndow.show()
    sys.exit(app.exec_())
