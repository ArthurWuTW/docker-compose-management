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
        MainWindowBase.resize(788, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidgetMachineStatus = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidgetMachineStatus.setGeometry(QtCore.QRect(40, 100, 681, 192))
        self.treeWidgetMachineStatus.setObjectName("treeWidgetMachineStatus")
        self.toolButtonProjectDir = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonProjectDir.setGeometry(QtCore.QRect(630, 50, 24, 25))
        self.toolButtonProjectDir.setObjectName("toolButtonProjectDir")
        self.lineEditProjectDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProjectDir.setGeometry(QtCore.QRect(90, 50, 531, 27))
        self.lineEditProjectDir.setReadOnly(True)
        self.lineEditProjectDir.setObjectName("lineEditProjectDir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 321, 17))
        self.label.setObjectName("label")
        self.treeWidgetDockerContainerStatus = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidgetDockerContainerStatus.setGeometry(QtCore.QRect(40, 310, 681, 192))
        self.treeWidgetDockerContainerStatus.setObjectName("treeWidgetDockerContainerStatus")
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 25))
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
        self.treeWidgetMachineStatus.headerItem().setText(0, _translate("MainWindowBase", "Machine"))
        self.treeWidgetMachineStatus.headerItem().setText(1, _translate("MainWindowBase", "Docker-compose Type"))
        self.treeWidgetMachineStatus.headerItem().setText(2, _translate("MainWindowBase", "SSH status"))
        self.toolButtonProjectDir.setText(_translate("MainWindowBase", "..."))
        self.label.setText(_translate("MainWindowBase", "Project Directory"))
        self.treeWidgetDockerContainerStatus.headerItem().setText(0, _translate("MainWindowBase", "Docker Container Status"))
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
