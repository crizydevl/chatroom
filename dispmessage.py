import sys

from PyQt5.QtGui import QIcon

from view.Ui_newForm import Ui_Form
from PyQt5.QtWidgets import QTextEdit, QWidget, QApplication, QTextBrowser, QMainWindow
from PyQt5 import QtWidgets


class ChatItem(QWidget, Ui_Form):
    def __init__(self, Form ,parent=None):
        super().__init__()
        self.form = Form
        self.setupUi(self.form)
        print('1',Form)
        self.pushButton.clicked.connect(self.send_text)
        # self.do_init()
        self.form.show()

    def setupUi(self, Form):
        super().setupUi(Form)


    def send_text(self):
        print('dddd')
        print('33', self)
        send_info = self.textEdit.toPlainText()
        # print(send_info + QIcon())
        # path = QString()
        # send_info =
        # self.textBrowser.setHtml(send_info)
        # self.textBrowser.append(send_info)
        self.textBrowser.insertHtml(send_info + '<img src="images/chat.jpg">')
        self.textEdit.clear()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    s = ChatItem(Form)
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # s.show()
    sys.exit(app.exec_())
        

