# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_MainWindowBase.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)
        self.actionCreate_Rsa_Key = QtWidgets.QAction(MainWindowBase)
        self.actionCreate_Rsa_Key.setObjectName("actionCreate_Rsa_Key")
        self.menuSettings.addAction(self.actionCreate_Rsa_Key)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindowBase)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
        self.menuSettings.setTitle(_translate("MainWindowBase", "Settings"))
        self.actionCreate_Rsa_Key.setText(_translate("MainWindowBase", "Create SSH Rsa Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowBase = QtWidgets.QMainWindow()
    ui = Ui_MainWindowBase()
    ui.setupUi(MainWindowBase)
    MainWindowBase.show()
    sys.exit(app.exec_())
