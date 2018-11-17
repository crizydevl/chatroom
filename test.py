# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class MouseEvent(QMainWindow):
    def __init__(self, parent=None):
        super(MouseEvent, self).__init__(parent)
        self.setWindowTitle(self.tr("获得鼠标事件"))

        labelStatus = QLabel();
        labelStatus.setText(self.tr("Mouse Position:"))
        labelStatus.setFixedWidth(100)

        self.labelMousePos = QLabel();
        self.labelMousePos.setText(self.tr(""))
        self.labelMousePos.setFixedWidth(100)

        self.sBar = self.statusBar()
        self.sBar.addPermanentWidget(labelStatus)
        self.sBar.addPermanentWidget(self.labelMousePos)

    def mouseMoveEvent(self, e):
        self.labelMousePos.setText("(" + QString.number(e.x()) + "," + QString.number(e.y()) + ")")

    def mousePressEvent(self, e):
        str = "(" + QString.number(e.x()) + "," + QString.number(e.y()) + ")"
        if e.button() == Qt.LeftButton:
            self.sBar.showMessage(self.tr("Mouse Left Button Pressed:") + str)
        elif e.button() == Qt.RightButton:
            self.sBar.showMessage(self.tr("Mouse Right Button Pressed:") + str)
        elif e.button() == Qt.MidButton:
            self.sBar.showMessage(self.tr("Mouse Middle Button Pressed:") + str)


app = QApplication(sys.argv)
dialog = MouseEvent()
dialog.show()
app.exec_()