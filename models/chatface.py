import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from view.Ui_chatface import Ui_Dialog
from PyQt5.QtWidgets import QLabel


class ChatFace(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.addEmotionItem()
        self.show()

    def addEmotionItem(self):
        self.setFixedSize(256, 192)

        self.tableWidget.setCellWidget(0, 0)
        self.label_1 = QLabel()
        self.label_1.setPixmap(QPixmap(1 +'.gif'))





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ChatFace()
    sys.exit(app.exec_())



