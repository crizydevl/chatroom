import sys
from multiprocessing import Pipe

from PyQt5 import Qt, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QGridLayout
from register import RegistView

from models.FriendWindow import FriendVeiw
from view.Ui_login import Ui_Form


class LoginWindow(Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        self.isremeber_pwd()
        self.init_ui()


    def init_ui(self):
        self.lineEdit.setPlaceholderText('账号')
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setPlaceholderText("密码6~15位，由字母、数字组成")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)


        grid = QGridLayout()
        # 第x行，第x列开始，占x行、x列
        grid.addWidget(self.label, 0, 0,3, 1)
        grid.addWidget(self.lineEdit,1, 1, 1, 2)
        grid.addWidget(self.lineEdit_2, 2,1,1,2)
        grid.addWidget(self.pushButton, 3,1,1,1)
        grid.addWidget(self.pushButton_2, 3,2,1,1)
        grid.addWidget(self.checkBox, 2,1, 1, 2)
        # grid.addWidget(self.label_3, 2,2,1,1)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)
        grid.setContentsMargins(10,10,10,10)
        self.setLayout(grid)

        font = QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.lineEdit_2.setFont(font)

        # 让窗口固定
        self.setFixedSize(275,179)

        try:
            self.pushButton.clicked.connect(self.user_info)
            self.pushButton_2.clicked.connect(self.register)
        except Exception as e:
            print('4', e)

    # 将登陆信息进行打包、发送
    def user_info(self):
        userId = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.remeber_pwd(userId, password)
        data = {'method':'login', 'usernum': userId, 'passwd':password}
        print(data)
        try:
            self.do_login()
        except Exception as e:
            print('3',e)

        fd1, fd2 = Pipe()
        fd2.send(data)
        recv_info = fd1.recv()
        return userId, password


    # 设置记住密码
    def remeber_pwd(self, userId, password):
        # 设置记住密码
        print('1', userId, password)
        if self.checkBox.checkState() == Qt.Checked:
            data = '1#'+ userId + '#' + password
            # data1 = json.dumps(data)
            print('data2', data)
            with open('users.txt', 'w') as f:
                f.write(data)
        else:
            data = '0#' + userId + '#' + password
            with open('users.txt', 'w') as f:
                f.write(data)


    # 启动时判断是否记住密码
    def isremeber_pwd(self):
        with open('users.txt', 'r') as f:
            data = f.read()
            if data != '':
                data = data.split('#')
                if data[0] == '1':
                    self.checkBox.setChecked(True)
                    self.lineEdit.setText(data[1])
                    self.lineEdit_2.setText(data[2])
                else:
                    self.checkBox.setChecked(False)

    # 跳转至注册界面
    def register(self):
        try:
            Form = QtWidgets.QWidget()
            Form.hide()
            Dialog = QtWidgets.QDialog()
            d = RegistView(Dialog)
            # Dialog.show()
            Dialog.exec_()
        except Exception as e:
            print('2', e)


    def do_login(self):
        try:
            self.hide()
            self.close()
        except Exception as e:
            print('1', e)

def send_ss():
    app = QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    # Form = QtWidgets.QWidget()
    p = LoginWindow()
    app.exec_()
    print(app)

    print('111')
    # app = QApplication(sys.argv)
    ti = FriendVeiw()
    ti.show()
    app.exec_()






if __name__ == "__main__":
    send_ss()