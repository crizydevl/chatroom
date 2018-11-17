# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'C:\Users\Python\Desktop\asd\.eric6project\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget

class Ui_Form(QWidget):
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(275, 179)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(110, 80, 71, 31))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 120, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 80, 54, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/user/10.jpg"))
        self.label.setObjectName("label")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "登录"))
        self.checkBox.setText(_translate("self", "记住密码"))
        self.pushButton.setText(_translate("self", "登录"))
        self.pushButton_2.setText(_translate("self", "注册"))
        # self.label_3.setText(_translate("self", "忘记密码？"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

