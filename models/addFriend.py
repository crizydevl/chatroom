from view.Ui_additemView import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
class AddFriend(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    # 设定确定时的信号
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        userId = self.lineEdit_add.text()
        if len(userId) == 0:
            QMessageBox.information(self, '提示', '内容不能为空!')
            self.lineEdit_add.setFocus()
        else:
            #　将１返回给主窗口
            self.done(1)

    # 设定拒绝时的信号
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.done(-1)





