# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_DialogCreateRsaKeyBase.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCreateRsaKeyBase(object):
    def setupUi(self, DialogCreateRsaKeyBase):
        DialogCreateRsaKeyBase.setObjectName("DialogCreateRsaKeyBase")
        DialogCreateRsaKeyBase.resize(440, 299)
        self.labelUsername = QtWidgets.QLabel(DialogCreateRsaKeyBase)
        self.labelUsername.setGeometry(QtCore.QRect(60, 110, 71, 17))
        self.labelUsername.setObjectName("labelUsername")
        self.labelIP = QtWidgets.QLabel(DialogCreateRsaKeyBase)
        self.labelIP.setGeometry(QtCore.QRect(110, 30, 16, 17))
        self.labelIP.setObjectName("labelIP")
        self.labelPort = QtWidgets.QLabel(DialogCreateRsaKeyBase)
        self.labelPort.setGeometry(QtCore.QRect(100, 70, 31, 17))
        self.labelPort.setObjectName("labelPort")
        self.labelPassword = QtWidgets.QLabel(DialogCreateRsaKeyBase)
        self.labelPassword.setGeometry(QtCore.QRect(60, 150, 67, 17))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditIP = QtWidgets.QLineEdit(DialogCreateRsaKeyBase)
        self.lineEditIP.setGeometry(QtCore.QRect(130, 30, 113, 27))
        self.lineEditIP.setObjectName("lineEditIP")
        self.lineEditPort = QtWidgets.QLineEdit(DialogCreateRsaKeyBase)
        self.lineEditPort.setGeometry(QtCore.QRect(130, 70, 113, 27))
        self.lineEditPort.setObjectName("lineEditPort")
        self.lineEditUsername = QtWidgets.QLineEdit(DialogCreateRsaKeyBase)
        self.lineEditUsername.setGeometry(QtCore.QRect(130, 110, 113, 27))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(DialogCreateRsaKeyBase)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 150, 113, 27))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.ButtonExit = QtWidgets.QPushButton(DialogCreateRsaKeyBase)
        self.ButtonExit.setGeometry(QtCore.QRect(90, 240, 99, 27))
        self.ButtonExit.setObjectName("ButtonExit")
        self.CreateRsaKeyButton = QtWidgets.QPushButton(DialogCreateRsaKeyBase)
        self.CreateRsaKeyButton.setGeometry(QtCore.QRect(240, 240, 171, 27))
        self.CreateRsaKeyButton.setObjectName("CreateRsaKeyButton")

        self.retranslateUi(DialogCreateRsaKeyBase)
        QtCore.QMetaObject.connectSlotsByName(DialogCreateRsaKeyBase)

    def retranslateUi(self, DialogCreateRsaKeyBase):
        _translate = QtCore.QCoreApplication.translate
        DialogCreateRsaKeyBase.setWindowTitle(_translate("DialogCreateRsaKeyBase", "Dialog"))
        self.labelUsername.setText(_translate("DialogCreateRsaKeyBase", "Username"))
        self.labelIP.setText(_translate("DialogCreateRsaKeyBase", "IP"))
        self.labelPort.setText(_translate("DialogCreateRsaKeyBase", "Port"))
        self.labelPassword.setText(_translate("DialogCreateRsaKeyBase", "Password"))
        self.ButtonExit.setText(_translate("DialogCreateRsaKeyBase", "Exit"))
        self.CreateRsaKeyButton.setText(_translate("DialogCreateRsaKeyBase", "Create RSA key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCreateRsaKeyBase = QtWidgets.QDialog()
    ui = Ui_DialogCreateRsaKeyBase()
    ui.setupUi(DialogCreateRsaKeyBase)
    DialogCreateRsaKeyBase.show()
    sys.exit(app.exec_())
