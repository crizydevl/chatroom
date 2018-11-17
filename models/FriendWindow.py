# -*- coding: utf-8 -*-

import re
# from view.Ui_newForm import Ui_Form
# from Dialog_additem import Dialog_additem
import sys
from threading import Thread

from PyQt5.QtCore import Qt, QSize, pyqtSlot, QVariant
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTreeWidgetItem, QMenu, QAction, \
    QInputDialog, QMessageBox, QAbstractItemView, QCompleter

from models.chat_view import ChatForm
from view.Ui_ui import Ui_Form
from .addFriend import AddFriend


class FriendVeiw(Ui_Form):

    #分组信息存储
    grouplist = []
    #用户信息存储
    userlist = []


    def __init__(self, parent=None):
        super(FriendVeiw, self).__init__(parent)
        print('sss')
        self.setupUi()
        # self.show()
        self.Ui_init()


    def Ui_init(self):
        # 设置好友图标大小等
        # print('3', self, '4', self.form)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setColumnWidth(0, 50)
        self.treeWidget.setHeaderLabels(['好友'])
        self.treeWidget.setIconSize(QSize(50, 50))


        # 搜索时自动填充，创建一个缓存空间, 0行1列
        self.add_model = QStandardItemModel(0, 1, self)
        add_completer = QCompleter(self.add_model, self)
        self.lineEdit.setCompleter(add_completer)
        add_completer.activated[str].connect(self.onUsernameChoosed)


        self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        # print('t1')
        self.treeWidget.itemSelectionChanged.connect(self.getListitems)
        self.treeWidget.itemDoubleClicked.connect(self.open_chatview)
        # print('t2')
        # self.treeWidget.currentItemChanged.connect(self.restatistic)
        # self.treeWidget.itemClicked.connect(self.isclick)

        # 样式的设置
        # with codecs.open('./qss/treeWidget.qss', 'r', 'utf-8') as f:
        #     style = f.read()
        #     print(style)
        # self.treeWidget.setStyleSheet(style)

        # 添加好友分组
        root = self.createGroup('我的好友')
        # root1 = self.createGroup('我的群组')
        root.setExpanded(True)
        # root1.setExpanded(True)

    # 创建好友分组
    def createGroup(self, groupname):
        onlinenum = 0
        group = QTreeWidgetItem(self.treeWidget)
        groupdic = {'group':group, 'groupname': groupname, 'childcount':0, 'childstatus':0}

        # 给分组设置小图标
        icon = self.searchicon(groupname)
        group.setIcon(0, icon)
    #
    #     # with codecs.open('friend_info', 'r', 'utf-8') as f:
    #     #     fre_info = f.read()
    #     # print(fre_info.split('\r\n'))
        fre_info = [['小李','1001','0','../images/user/0.jpg'],['小强','1002','1','../images/user/0.jpg'],['小明','1003','1','../images/user/0.jpg']]
        for item in fre_info:
            child = QTreeWidgetItem()
            uname = item[0]
            chatID = item[1]
            status = item[2]
            icon_path = QIcon(item[3])
            name = uname + '(%s)' % chatID
            # name, chatID, icon_path, font, status = self.createUser(item)
            font = QFont()
            font.setPointSize(9)

            userdic = {'user': child, 'username': name, 'userID': chatID, 'status': status}
            self.userlist.append(userdic)
            child.setFont(0, font)
            child.setIcon(0, icon_path)
            # 离线、在线判断
            onlinenum, name = self.judge_online(status, onlinenum, name, child)
            group.addChild(child)

        # 判断在线、总人数
        childnum = group.childCount()
        print('childnum:', childnum, 'online:', onlinenum)
        off_line_num = childnum - onlinenum
        groupdic['childcount'] = childnum
        groupdic['childstatus'] = onlinenum
        groupname += ' ' + str(onlinenum) + '/' + str(childnum)
        group.setText(0, groupname)
        self.grouplist.append(groupdic)
        # print('grouplist:', self.grouplist)
        return group

    # 在线、离线判断
    def judge_online(self,status, onlinenum, name, child):
        if status == '1':
            onlinenum += 1
            name += ' 在线'
            child.setText(0, name)
        else:
            name += ' 离线'
            child.setText(0, name)
        return onlinenum, name

    # 设置菜单
    def contextMenuEvent(self, event):
        hititem = self.treeWidget.currentItem()
        print('event', event, 'hititem', hititem)
        if hititem:
            # 当root是 None 时，此时节点在分组上
            root = hititem.parent()
            if root is None:
                pgroupmenu = QMenu(self)
                pAddgroupAct = QAction('添加分组',self.treeWidget)
                pRenameAct = QAction('重命名',self.treeWidget)
                pDeleteAct = QAction('删除该组',self.treeWidget)
                pgroupmenu.addAction(pAddgroupAct)
                pgroupmenu.addAction(pRenameAct)
                pgroupmenu.addAction(pDeleteAct)
                pAddgroupAct.triggered.connect(self.addgroup)
                pRenameAct.triggered.connect(self.renamegroup)
                if self.treeWidget.itemAbove(hititem) is None:
                    pDeleteAct.setEnabled(False)
                else:
                    pDeleteAct.triggered.connect(self.deletegroup)
                pgroupmenu.popup(self.mapToGlobal(event.pos()))
            # 此时节点在联系人上
            elif root.childCount() > 0:
                pItemmenu = QMenu(self)       
                pDeleteItemAct = QAction('删除联系人',pItemmenu)
                pRenameItemAct = QAction('添加备注', pItemmenu)
                pItemmenu.addAction(pDeleteItemAct)
                pItemmenu.addAction(pRenameItemAct)
                pDeleteItemAct.triggered.connect(self.delete)
                pRenameItemAct.triggered.connect(self.renameItem)
                print('font', hititem.text(0))
                # 左键点击事件


                # self.treeWidget.itemDoubleClicked(hititem).connect(self.click_event)
                # 当联系人大于 1时，可以转移
                if len(self.grouplist) > 1:
                    pSubMenu = QMenu('转移联系人至' ,pItemmenu)
                    pItemmenu.addMenu(pSubMenu)
                    for item_dic in self.grouplist:
                        if item_dic['group'] is not root:
                            pMoveAct = QAction(item_dic['groupname'] ,pItemmenu)
                            pSubMenu.addAction(pMoveAct)
                            pMoveAct.triggered.connect(self.moveItem)
                pItemmenu.popup(self.mapToGlobal(event.pos()))
    # 添加分组
    def addgroup(self):
        gname, ok = QInputDialog.getText(self,'提示信息','请输入分组名称')
        if ok:
            if len(gname) == 0:
                QMessageBox.information(self,'提示','分组名称不能为空哦')
            else:
                self.createGroup(gname)
    # 重命名
    def renamegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gnewname, ok = QInputDialog.getText(self,'提示信息','请输入分组的新名称')
        if ok:
            if len(gnewname) == 0:
                QMessageBox.information(self,'提示','分组名称不能为空哦')
            else:
                hitgroup.setText(0, gnewname)
                newicon = self.searchicon(hitgroup.text(0))
                hitgroup.setIcon(0, newicon)
                gindex = self.searchgroup(hitgroup)
                self.grouplist[gindex]['groupname'] = gnewname
                self.treeWidget.setCurrentItem(hitgroup.child(0))
    # 给联系人添加备注
    def renameItem(self):
        hituser = self.treeWidget.currentItem()
        uindex = self.searchuser(hituser)
        unewname, ok = QInputDialog.getText(self,'提示信息','请输入备注名称')
        if ok:
            if len(unewname) == 0:
                QMessageBox.information(self,'提示','备注名称不能为空哦')
            else:
                hituser.setText(0,unewname)
                self.userslist[uindex]['username'] = unewname
     # 删除分组
    def deletegroup(self):
        hitgroup = self.treeWidget.currentItem()
        gindex = self.searchgroup(hitgroup)
        reply = QMessageBox.question(self,'警告','确定要删除这个分组及其联系人吗？', QMessageBox.Yes | QMessageBox.No , QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.treeWidget.takeTopLevelItem(gindex)
            del self.grouplist[gindex]
    # 移动联系人
    def moveItem(self):
        movelist = self.getListitems(self.menuflag)
        togroupname = self.sender().text()
        mindex = self.searchgroup(togroupname)
        togroup = self.grouplist[mindex]['group']
        self.deleteItems(movelist, flag = 0)
        self.add(togroup, movelist)
        self.tmpuseritem.clear()

    def delete(self):
        delitems = self.getListitems(self.menuflag)
        self.deleteItems(delitems)
        self.tmpuseritem.clear()

    def deleteItems(self, items, flag = 1):
        for delitem in items:
            delitem.setData(0, Qt.CheckStateRole, QVariant())#取消删除item的复选框
            pindex = delitem.parent().indexOfChild(delitem)
            dindex = self.searchuser(delitem)
            ishide = self.userslist[dindex]['ishide']
            if flag == 1:
                del self.userslist[dindex]
            fathergroup = delitem.parent()
            findex = self.searchgroup(fathergroup)
            if ishide == 1:
                self.grouplist[findex]['childishide'] -= 1
                self.grouplist[findex]['childcount'] -= 1
            else:
                self.grouplist[findex]['childcount'] -= 1

            delitem.parent().takeChild(pindex)

    def add(self, group, items):
        gindex = self.searchgroup(group)
        for item in items:
            aindex = self.searchuser(item)
            ishide = self.userslist[aindex]['ishide']
            if ishide == 1:
                self.grouplist[gindex]['childishide'] += 1
                self.grouplist[gindex]['childcount'] += 1
            else:
                self.grouplist[gindex]['childcount'] += 1
            group.addChild(item)
            self.treeWidget.setCurrentItem(item)

    def Batchoperation(self):
        self.menuflag *= -1

        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setCheckState(0, Qt.Unchecked)

    def CancelBatchoperation(self):
        self.menuflag *= -1
        group = self.getListitems()[0].parent()
        childnum = group.childCount()
        for c in range(childnum):
            child = group.child(c)
            child.setData(0, Qt.CheckStateRole, QVariant())

    def isclick(self, item):
        if item.checkState(0) == Qt.Checked:
            if self.tmpuseritem.count(item) == 0:
                self.tmpuseritem.append(item)
        else:
            if len(self.tmpuseritem) > 0:
                if self.tmpuseritem.count(item) != 0:
                    i = self.tmpuseritem.index(item)
                    del self.tmpuseritem[i]

    # 查找分组
    def searchgroup(self, hitgroup):
        if isinstance(hitgroup,str):
            for i,g in enumerate(self.grouplist):
                if g['groupname'] == hitgroup:
                    return i
        else:
            for i,g in enumerate(self.grouplist):
                if g['group'] == hitgroup:
                    return i

    def searchuser(self, hituser):
        if isinstance(hituser, str):
            for i,u in enumerate(self.userlist):
                if u['userID'] == hituser:
                    return i
        else:
            for i,u in enumerate(self.userslist):
                if u['user'] == hituser:
                    return i

    def searchicon(self, gpname2):
        if gpname2.find('好友') >= 0:
            return QIcon('../iamges/list_images/buddy.ico')
        elif gpname2.find('同事') >= 0:
            return QIcon('../images/list_images/partner.ico')
        elif gpname2.find('黑名单') >= 0:
            return QIcon('../images/list_images/blacklist.ico')
        else:
            return QIcon('../images/list_images/buddy_default.ico')

    # 返回当前对象
    def getListitems(self, flag = 1):
        if flag > 0:
            return self.treeWidget.selectedItems()

    def restatistic(self, item, preitem):
        if item:
            fathergroup = item.parent() 
            if fathergroup:
                self.restatistic_op(fathergroup)
            else:
                self.restatistic_op(item)
        elif preitem.parent().childCount() == 1:
            lastgroupname = preitem.parent().text(0).split()[0] + ' 0/0'
            preitem.parent().setText(0, lastgroupname)
            self.menuflag = 1

    def restatistic_op(self, itemorgroup):
        gindex = self.searchgroup(itemorgroup)
        totalcount = self.grouplist[gindex]['childcount']
        hidecount = self.grouplist[gindex]['childishide']
        fathergroupname = self.grouplist[gindex]['groupname']
        fathergroupname += ' ' + str(totalcount - hidecount) + '/' + str(totalcount)    
        itemorgroup.setText(0, fathergroupname)



    def open_chatview(self):
        t = Thread()
        print('2222')

        user_id, user_name = self.handle_info()

        try:
            # app = QApplication(sys.argv)
            self.hide()
            ch = ChatForm(user_id, user_name)
            ch.show()
            ch.exec_()
            # sys.exit(app.exec_())
        except Exception as e:
            print(e)

        t.start()
        t.join()


    # 双击时获取好友信息
    def handle_info(self):
        hititem = self.treeWidget.currentItem()
        text = hititem.text(0)

        partern = '\d+'
        user_id = re.findall(partern, text)

        partern1 = '^\w+'
        user_name = re.findall(partern1, text)
        print('11', user_id[0], user_name[0])
        return user_id[0], user_name[0]

    # 添加好友
    @pyqtSlot()
    def on_bt_adduser_clicked(self):
        addUser = AddFriend()
        for gro in self.grouplist:
            addUser.comboBox.addItem(gro['groupname'])
        r = addUser.exec_()
        if r >0:
            newItem = QTreeWidgetItem()
            newId = addUser.lineEdit_add.text()
            print('newId', newId)
            # 设置一个接口　获取　id 对应的信息
            newUser = ['小李', '1006', '1', '../images/user/7.jpg']
            newName = newUser[0]
            newStatus = newUser[2]
            newPath = QIcon(newUser[3])

            name = newName + '(%s)' % newId
            font = QFont()
            font.setPointSize(9)

            userdic = {'user': newItem, 'username': name, 'userID': newId, 'status': newStatus}
            self.userlist.append(userdic)
            newItem.setFont(0, font)
            newItem.setIcon(0, newPath)
            newItem.setText(0, name)

            comboInfo = addUser.comboBox.currentText()
            conboIndex = self.searchgroup(comboInfo)
            group = self.grouplist[conboIndex]['group']
            self.grouplist[conboIndex]['childcount'] += 1

            group.addChild(newItem)
            self.treeWidget.setCurrentItem(newItem)

    # 获取lineEdit的输入信息
    def onUsernameChoosed(self, name):
        self.lineEdit.setText(name)

    # 查找好友
    @pyqtSlot()
    def on_bt_search_clicked(self):
        userId = self.lineEdit.text()
        if len(userId) > 0:
            user_index = self.searchuser(userId)
            print('user', user_index)
            userItem = self.userlist[user_index]['user']
            self.treeWidget.setCurrentItem(userItem)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        unameList = []
        for i in self.userlist:
            userName = i['username']
            if userName.find(text) > 0:
                unameList.append(userName)
            self.add_model.removeRows(0, self.add_model.rowCount())

            for n in range(0, len(unameList)):
                self.add_model.insertRow(0)
                self.add_model.setData(self.add_model.index(0, 0), unameList[n])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    tim = FriendVeiw()
    tim.show()
    sys.exit(app.exec_())