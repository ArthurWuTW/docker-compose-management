# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogCreateRsaKey.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCreateRsaKey(object):
    def setupUi(self, DialogCreateRsaKey):
        DialogCreateRsaKey.setObjectName("DialogCreateRsaKey")
        DialogCreateRsaKey.resize(440, 299)
        self.labelUsername = QtWidgets.QLabel(DialogCreateRsaKey)
        self.labelUsername.setGeometry(QtCore.QRect(60, 110, 71, 17))
        self.labelUsername.setObjectName("labelUsername")
        self.labelIP = QtWidgets.QLabel(DialogCreateRsaKey)
        self.labelIP.setGeometry(QtCore.QRect(110, 30, 16, 17))
        self.labelIP.setObjectName("labelIP")
        self.labelPort = QtWidgets.QLabel(DialogCreateRsaKey)
        self.labelPort.setGeometry(QtCore.QRect(100, 70, 31, 17))
        self.labelPort.setObjectName("labelPort")
        self.labelPassword = QtWidgets.QLabel(DialogCreateRsaKey)
        self.labelPassword.setGeometry(QtCore.QRect(60, 150, 67, 17))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditIP = QtWidgets.QLineEdit(DialogCreateRsaKey)
        self.lineEditIP.setGeometry(QtCore.QRect(130, 30, 113, 27))
        self.lineEditIP.setObjectName("lineEditIP")
        self.lineEditPort = QtWidgets.QLineEdit(DialogCreateRsaKey)
        self.lineEditPort.setGeometry(QtCore.QRect(130, 70, 113, 27))
        self.lineEditPort.setObjectName("lineEditPort")
        self.lineEditUsername = QtWidgets.QLineEdit(DialogCreateRsaKey)
        self.lineEditUsername.setGeometry(QtCore.QRect(130, 110, 113, 27))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(DialogCreateRsaKey)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 150, 113, 27))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.ButtonExit = QtWidgets.QPushButton(DialogCreateRsaKey)
        self.ButtonExit.setGeometry(QtCore.QRect(90, 240, 99, 27))
        self.ButtonExit.setObjectName("ButtonExit")
        self.CreateRsaKeyButton = QtWidgets.QPushButton(DialogCreateRsaKey)
        self.CreateRsaKeyButton.setGeometry(QtCore.QRect(240, 240, 171, 27))
        self.CreateRsaKeyButton.setObjectName("CreateRsaKeyButton")

        self.retranslateUi(DialogCreateRsaKey)
        QtCore.QMetaObject.connectSlotsByName(DialogCreateRsaKey)

    def retranslateUi(self, DialogCreateRsaKey):
        _translate = QtCore.QCoreApplication.translate
        DialogCreateRsaKey.setWindowTitle(_translate("DialogCreateRsaKey", "Dialog"))
        self.labelUsername.setText(_translate("DialogCreateRsaKey", "Username"))
        self.labelIP.setText(_translate("DialogCreateRsaKey", "IP"))
        self.labelPort.setText(_translate("DialogCreateRsaKey", "Port"))
        self.labelPassword.setText(_translate("DialogCreateRsaKey", "Password"))
        self.ButtonExit.setText(_translate("DialogCreateRsaKey", "Exit"))
        self.CreateRsaKeyButton.setText(_translate("DialogCreateRsaKey", "Create RSA key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCreateRsaKey = QtWidgets.QDialog()
    ui = Ui_DialogCreateRsaKey()
    ui.setupUi(DialogCreateRsaKey)
    DialogCreateRsaKey.show()
    sys.exit(app.exec_())
