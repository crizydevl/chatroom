import sys

import datetime
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFontDialog, QColorDialog, QComboBox, QDialog
from .chatface import ChatFace
from view.Ui_chatView import Ui_Dialog

class ChatForm(Ui_Dialog):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.init_ui()
        try:
            self.setupUi()
            self.pushButton.clicked.connect(self.send_text)
            self.toolButton_2.clicked.connect(self.clear)
            self.toolButton_3.clicked.connect(self.italic)
            self.toolButton_5.clicked.connect(self.select_color)
            self.toolButton_4.clicked.connect(self.select_chatface)
        except Exception as e:
            print(e)

    # 处理、发送信息
    def send_text(self):
        chat_msg = self.textBrowser.toPlainText()
        send_info = self.textEdit.toPlainText()
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_info = '小强 ' + time + ':'
        color = self.select_color()
        self.textBrowser.insertHtml('<p style="font-size:15px;">%s</p>' % user_info + '<P style="color:%s">%s</P>' % (color ,send_info)+'<br>')
        self.textEdit.clear()

    # 将好友信息显示到窗口
    def init_ui(self):
        # print('init_ui', self.name)
        return self.setWindowTitle(self.name)

    # 清除聊天记录
    def clear(self):
        self.textEdit.clear()

    # 设置字体
    def italic(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textBrowser.setFont(font)

    # 设置字体颜色
    def select_color(self):
        color = 'black'
        list = ['red', 'blue', 'yellow', 'gray', 'green', 'black','orange']
        for i in list:
            combo = self.comboBox.addItem(i)
        color = self.comboBox.currentText()
        return color

    def select_chatface(self):
        chat = ChatFace()
        chat.show()

    # 设置键盘事件
    def keyPressEvent(self, event):
        self.textEdit.popup(self.mapToGlobal(event.pos()))
        keyevent = QKeyEvent(event)
        if keyevent.key() in (Qt.Key_Enter, Qt.key_Return):
            print('111111111')
            self.pushButton.clicked.emit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ch = ChatForm()
    ch.show()
    sys.exit(app.exec_())