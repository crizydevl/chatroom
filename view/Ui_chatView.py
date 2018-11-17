# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Python\Desktop\asd\.eric6project\chatView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(512, 466)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 7)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/chat/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 1, 3, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/chat/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 1, 4, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/chat/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 5, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/chat/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon3)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout.addWidget(self.toolButton_5, 1, 6, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 7)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("self", "self"))
        self.toolButton_4.setText(_translate("self", "..."))
        self.toolButton_3.setText(_translate("self", "..."))
        self.toolButton_2.setText(_translate("self", "..."))
        self.toolButton_5.setText(_translate("self", "..."))
        self.pushButton.setText(_translate("self", "发送>>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#
#     ui = Ui_Dialog()
#     ui.setupUi(self)
#     ui.show()
#     sys.exit(app.exec_())

