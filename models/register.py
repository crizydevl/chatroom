from view.Ui_register import Ui_Dialog
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit,QMessageBox
from PyQt5.QtGui import QPixmap


class RegistView(Ui_Dialog):
    def __init__(self, Dialog):
        super(RegistView, self).__init__()
        try:
            self.setupUi(Dialog)
            Dialog.show()
        except Exception as e:
            print(e)
        self.init_ui()
        self.pushButton.clicked.connect(self.do_regist)
        self.pushButton_2.clicked.connect(self.send_email)

    def init_ui(self):
        # 设置密码输入框格式
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_3.setPlaceholderText("密码由6~15位，由字母、数字组成")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.lineEdit_6.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_6.setPlaceholderText("密码由6~15位，由字母、数字组成")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)

        self.lineEdit_3.setMaxLength(15)
        self.lineEdit_6.setMaxLength(15)

        self.lineEdit_6.cursorPositionChanged.connect(self.pwd_juage)



    def do_regist(self):
        uname = self.lineEdit.text()
        uage = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        email = self.lineEdit_2.text()
        print('1'+ uname, '2'+uage, '3'+password, '4'+email)

    def pwd_juage(self):

        try:
            pwd = self.lineEdit_3.text()
            pwd1 = self.lineEdit_6.text()
            if pwd1 != pwd:
                # QMessageBox.warning(Dialog, '提示', '两次输入的密码不一致')
                self.label_5.setText('密码不一致')
            else:
                self.label_5.setText(' ^_^ ')
                # self.label_5.setPixmap(QPixmap('../images/tim.jpeg'))
        except Exception as e:
            print(e)


    def send_email(self):
        pass


