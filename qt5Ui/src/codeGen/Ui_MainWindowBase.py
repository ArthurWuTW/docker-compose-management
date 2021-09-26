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
        self.treeWidgetMachineStatus.setGeometry(QtCore.QRect(40, 100, 461, 192))
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
        self.treeWidgetDockerContainerStatus.setGeometry(QtCore.QRect(40, 320, 681, 192))
        self.treeWidgetDockerContainerStatus.setObjectName("treeWidgetDockerContainerStatus")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(540, 190, 171, 27))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 170, 161, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 110, 161, 17))
        self.label_3.setObjectName("label_3")
        self.lineEditMachineName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMachineName.setGeometry(QtCore.QRect(540, 130, 171, 27))
        self.lineEditMachineName.setReadOnly(True)
        self.lineEditMachineName.setObjectName("lineEditMachineName")
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(540, 240, 171, 27))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonDeploy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDeploy.setGeometry(QtCore.QRect(550, 530, 171, 27))
        self.pushButtonDeploy.setObjectName("pushButtonDeploy")
        self.pushButtonDeloyAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDeloyAll.setGeometry(QtCore.QRect(550, 580, 171, 27))
        self.pushButtonDeloyAll.setObjectName("pushButtonDeloyAll")
        self.pushButtonRebuildDeploy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRebuildDeploy.setGeometry(QtCore.QRect(340, 530, 171, 27))
        self.pushButtonRebuildDeploy.setObjectName("pushButtonRebuildDeploy")
        self.pushButtonDeployStopAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDeployStopAll.setGeometry(QtCore.QRect(340, 580, 171, 27))
        self.pushButtonDeployStopAll.setObjectName("pushButtonDeployStopAll")
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
        self.label_2.setText(_translate("MainWindowBase", "Docker-compose Type"))
        self.label_3.setText(_translate("MainWindowBase", "Machine"))
        self.pushButtonSave.setText(_translate("MainWindowBase", "Save"))
        self.pushButtonDeploy.setText(_translate("MainWindowBase", "Deploy"))
        self.pushButtonDeloyAll.setText(_translate("MainWindowBase", "Deploy ALL"))
        self.pushButtonRebuildDeploy.setText(_translate("MainWindowBase", "Rebuild and Deploy"))
        self.pushButtonDeployStopAll.setText(_translate("MainWindowBase", "Stop ALL"))
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
