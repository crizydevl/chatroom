# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'F:\PyQt5\PyQt540\ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Form(QWidget):
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(255, 678)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.bt_search = QtWidgets.QToolButton(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon1)
        self.bt_search.setIconSize(QtCore.QSize(32, 32))
        self.bt_search.setAutoRaise(True)
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout.addWidget(self.bt_search)
        self.bt_adduser = QtWidgets.QToolButton(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/adduser.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_adduser.setIcon(icon2)
        self.bt_adduser.setIconSize(QtCore.QSize(32, 32))
        self.bt_adduser.setAutoRaise(True)
        self.bt_adduser.setObjectName("bt_adduser")
        self.horizontalLayout.addWidget(self.bt_adduser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "QQ"))
        self.bt_search.setToolTip(_translate("self", "查找联系人"))
        self.bt_search.setWhatsThis(_translate("self", "查找联系人"))
        self.bt_search.setText(_translate("self", "..."))
        self.bt_adduser.setToolTip(_translate("self", "新增好友"))
        self.bt_adduser.setWhatsThis(_translate("self", "新增好友"))
        self.bt_adduser.setText(_translate("self", "..."))
        self.treeWidget.setWhatsThis(_translate("self", "模拟"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
