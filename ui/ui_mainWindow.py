# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1483, 1349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBoxUsers = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxUsers.setObjectName("comboBoxUsers")
        self.horizontalLayout_3.addWidget(self.comboBoxUsers)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEditNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumber.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditNumber.setPlaceholderText("")
        self.lineEditNumber.setObjectName("lineEditNumber")
        self.horizontalLayout_3.addWidget(self.lineEditNumber)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_3.addWidget(self.lineEditPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnOffLineUse = QtWidgets.QPushButton(self.centralwidget)
        self.btnOffLineUse.setObjectName("btnOffLineUse")
        self.horizontalLayout_3.addWidget(self.btnOffLineUse)
        self.checkBoxRememberMe = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxRememberMe.setObjectName("checkBoxRememberMe")
        self.horizontalLayout_3.addWidget(self.checkBoxRememberMe)
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout_3.addWidget(self.btnLogin)
        spacerItem1 = QtWidgets.QSpacerItem(35, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelTip = QtWidgets.QLabel(self.centralwidget)
        self.labelTip.setStyleSheet("color:rgb(0, 0, 255);font: 75 20pt \"Aharoni\";")
        self.labelTip.setObjectName("labelTip")
        self.horizontalLayout_4.addWidget(self.labelTip)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setMinimumSize(QtCore.QSize(0, 0))
        self.labelName.setLineWidth(1)
        self.labelName.setTextFormat(QtCore.Qt.AutoText)
        self.labelName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_4.addWidget(self.labelName)
        self.labelLoginTime = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginTime.setObjectName("labelLoginTime")
        self.horizontalLayout_4.addWidget(self.labelLoginTime)
        self.labelIP = QtWidgets.QLabel(self.centralwidget)
        self.labelIP.setObjectName("labelIP")
        self.horizontalLayout_4.addWidget(self.labelIP)
        self.labelPhone = QtWidgets.QLabel(self.centralwidget)
        self.labelPhone.setObjectName("labelPhone")
        self.horizontalLayout_4.addWidget(self.labelPhone)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 700))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.evaluate = QtWidgets.QWidget()
        self.evaluate.setObjectName("evaluate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.evaluate)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.btnLoadPJ = QtWidgets.QPushButton(self.evaluate)
        self.btnLoadPJ.setEnabled(False)
        self.btnLoadPJ.setObjectName("btnLoadPJ")
        self.horizontalLayout_7.addWidget(self.btnLoadPJ)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.treeWidgetHavePJ = QtWidgets.QTreeWidget(self.evaluate)
        self.treeWidgetHavePJ.setEnabled(True)
        self.treeWidgetHavePJ.setAutoScroll(True)
        self.treeWidgetHavePJ.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidgetHavePJ.setTabKeyNavigation(True)
        self.treeWidgetHavePJ.setDragEnabled(False)
        self.treeWidgetHavePJ.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidgetHavePJ.setColumnCount(5)
        self.treeWidgetHavePJ.setObjectName("treeWidgetHavePJ")
        self.treeWidgetHavePJ.header().setVisible(False)
        self.treeWidgetHavePJ.header().setCascadingSectionResizes(False)
        self.treeWidgetHavePJ.header().setDefaultSectionSize(200)
        self.treeWidgetHavePJ.header().setHighlightSections(False)
        self.treeWidgetHavePJ.header().setMinimumSectionSize(100)
        self.verticalLayout_8.addWidget(self.treeWidgetHavePJ)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.evaluate)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidgetNotPJ = QtWidgets.QTreeWidget(self.tab_5)
        self.treeWidgetNotPJ.setEnabled(True)
        self.treeWidgetNotPJ.setAutoScroll(True)
        self.treeWidgetNotPJ.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidgetNotPJ.setTabKeyNavigation(True)
        self.treeWidgetNotPJ.setDragEnabled(False)
        self.treeWidgetNotPJ.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidgetNotPJ.setColumnCount(5)
        self.treeWidgetNotPJ.setObjectName("treeWidgetNotPJ")
        self.treeWidgetNotPJ.header().setVisible(False)
        self.treeWidgetNotPJ.header().setCascadingSectionResizes(False)
        self.treeWidgetNotPJ.header().setDefaultSectionSize(200)
        self.treeWidgetNotPJ.header().setHighlightSections(False)
        self.treeWidgetNotPJ.header().setMinimumSectionSize(100)
        self.verticalLayout.addWidget(self.treeWidgetNotPJ)
        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.treeWidgetPJInfo = QtWidgets.QTreeWidget(self.tab_6)
        self.treeWidgetPJInfo.setEnabled(True)
        self.treeWidgetPJInfo.setAutoScroll(True)
        self.treeWidgetPJInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidgetPJInfo.setTabKeyNavigation(True)
        self.treeWidgetPJInfo.setDragEnabled(False)
        self.treeWidgetPJInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidgetPJInfo.setColumnCount(6)
        self.treeWidgetPJInfo.setObjectName("treeWidgetPJInfo")
        self.treeWidgetPJInfo.header().setVisible(False)
        self.treeWidgetPJInfo.header().setCascadingSectionResizes(False)
        self.treeWidgetPJInfo.header().setDefaultSectionSize(200)
        self.treeWidgetPJInfo.header().setHighlightSections(False)
        self.treeWidgetPJInfo.header().setMinimumSectionSize(100)
        self.verticalLayout_7.addWidget(self.treeWidgetPJInfo)
        self.tabWidget_4.addTab(self.tab_6, "")
        self.verticalLayout_8.addWidget(self.tabWidget_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.btnPJ = QtWidgets.QPushButton(self.evaluate)
        self.btnPJ.setEnabled(False)
        self.btnPJ.setObjectName("btnPJ")
        self.horizontalLayout_11.addWidget(self.btnPJ)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.evaluate, "")
        self.grabLesson = QtWidgets.QWidget()
        self.grabLesson.setObjectName("grabLesson")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.grabLesson)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.grabLesson)
        self.label_3.setStyleSheet("color:red")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.btnLoadLessonsOnWeb = QtWidgets.QPushButton(self.grabLesson)
        self.btnLoadLessonsOnWeb.setEnabled(False)
        self.btnLoadLessonsOnWeb.setObjectName("btnLoadLessonsOnWeb")
        self.horizontalLayout_5.addWidget(self.btnLoadLessonsOnWeb)
        self.btnLoadInMysql = QtWidgets.QPushButton(self.grabLesson)
        self.btnLoadInMysql.setEnabled(False)
        self.btnLoadInMysql.setObjectName("btnLoadInMysql")
        self.horizontalLayout_5.addWidget(self.btnLoadInMysql)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.grabLesson)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.comboBoxQueryType = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxQueryType.setObjectName("comboBoxQueryType")
        self.comboBoxQueryType.addItem("")
        self.comboBoxQueryType.addItem("")
        self.comboBoxQueryType.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBoxQueryType)
        self.lineEditQueryLessons = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditQueryLessons.setEnabled(False)
        self.lineEditQueryLessons.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditQueryLessons.setObjectName("lineEditQueryLessons")
        self.horizontalLayout_8.addWidget(self.lineEditQueryLessons)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.labelSemester = QtWidgets.QLabel(self.tab_3)
        self.labelSemester.setObjectName("labelSemester")
        self.horizontalLayout_2.addWidget(self.labelSemester)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.treeWigetReadAllLesson = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWigetReadAllLesson.setEnabled(True)
        self.treeWigetReadAllLesson.setMinimumSize(QtCore.QSize(0, 550))
        self.treeWigetReadAllLesson.setAutoScroll(True)
        self.treeWigetReadAllLesson.setRootIsDecorated(False)
        self.treeWigetReadAllLesson.setItemsExpandable(True)
        self.treeWigetReadAllLesson.setAnimated(False)
        self.treeWigetReadAllLesson.setHeaderHidden(False)
        self.treeWigetReadAllLesson.setExpandsOnDoubleClick(True)
        self.treeWigetReadAllLesson.setObjectName("treeWigetReadAllLesson")
        self.treeWigetReadAllLesson.header().setDefaultSectionSize(120)
        self.verticalLayout_2.addWidget(self.treeWigetReadAllLesson)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.treeWidgetQKInfo = QtWidgets.QTreeWidget(self.tab_4)
        self.treeWidgetQKInfo.setObjectName("treeWidgetQKInfo")
        self.treeWidgetQKInfo.header().setDefaultSectionSize(240)
        self.verticalLayout_9.addWidget(self.treeWidgetQKInfo)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget_3)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.grabLesson)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.TreeWidgetLessonsToGrab = QtWidgets.QTreeWidget(self.tab)
        self.TreeWidgetLessonsToGrab.setEnabled(True)
        self.TreeWidgetLessonsToGrab.setAutoScroll(True)
        self.TreeWidgetLessonsToGrab.setRootIsDecorated(False)
        self.TreeWidgetLessonsToGrab.setItemsExpandable(False)
        self.TreeWidgetLessonsToGrab.setAnimated(False)
        self.TreeWidgetLessonsToGrab.setHeaderHidden(False)
        self.TreeWidgetLessonsToGrab.setExpandsOnDoubleClick(True)
        self.TreeWidgetLessonsToGrab.setObjectName("TreeWidgetLessonsToGrab")
        self.TreeWidgetLessonsToGrab.header().setDefaultSectionSize(100)
        self.verticalLayout_4.addWidget(self.TreeWidgetLessonsToGrab)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.btnQK = QtWidgets.QPushButton(self.tab)
        self.btnQK.setEnabled(False)
        self.btnQK.setObjectName("btnQK")
        self.horizontalLayout_10.addWidget(self.btnQK)
        self.btnStopQK = QtWidgets.QPushButton(self.tab)
        self.btnStopQK.setEnabled(False)
        self.btnStopQK.setObjectName("btnStopQK")
        self.horizontalLayout_10.addWidget(self.btnStopQK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TreeWidgetLessonsHaveChosed = QtWidgets.QTreeWidget(self.tab_2)
        self.TreeWidgetLessonsHaveChosed.setEnabled(True)
        self.TreeWidgetLessonsHaveChosed.setAutoScroll(True)
        self.TreeWidgetLessonsHaveChosed.setRootIsDecorated(False)
        self.TreeWidgetLessonsHaveChosed.setItemsExpandable(False)
        self.TreeWidgetLessonsHaveChosed.setAnimated(False)
        self.TreeWidgetLessonsHaveChosed.setHeaderHidden(False)
        self.TreeWidgetLessonsHaveChosed.setExpandsOnDoubleClick(True)
        self.TreeWidgetLessonsHaveChosed.setObjectName("TreeWidgetLessonsHaveChosed")
        self.TreeWidgetLessonsHaveChosed.header().setDefaultSectionSize(100)
        self.verticalLayout_5.addWidget(self.TreeWidgetLessonsHaveChosed)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_6.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.grabLesson, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1483, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menuUser = QtWidgets.QMenu(self.menuBar)
        self.menuUser.setEnabled(False)
        self.menuUser.setTearOffEnabled(False)
        self.menuUser.setSeparatorsCollapsible(False)
        self.menuUser.setToolTipsVisible(False)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menuBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.actionSetDatabase = QtWidgets.QAction(MainWindow)
        self.actionSetDatabase.setObjectName("actionSetDatabase")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setEnabled(True)
        self.actionLogout.setVisible(True)
        self.actionLogout.setObjectName("actionLogout")
        self.actionDeleteThisUserData = QtWidgets.QAction(MainWindow)
        self.actionDeleteThisUserData.setObjectName("actionDeleteThisUserData")
        self.actionDeleteAllUsersData = QtWidgets.QAction(MainWindow)
        self.actionDeleteAllUsersData.setObjectName("actionDeleteAllUsersData")
        self.actionDeleteLessonData = QtWidgets.QAction(MainWindow)
        self.actionDeleteLessonData.setObjectName("actionDeleteLessonData")
        self.menuAbout.addAction(self.help)
        self.menu.addAction(self.actionDeleteAllUsersData)
        self.menu.addSeparator()
        self.menu.addAction(self.actionDeleteLessonData)
        self.menuUser.addAction(self.actionLogout)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionDeleteThisUserData)
        self.menuUser.addSeparator()
        self.menuBar.addAction(self.menuUser.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GrabLesson"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.lineEditNumber.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.lineEditPassword.setText(_translate("MainWindow", ""))
        self.btnOffLineUse.setText(_translate("MainWindow", "离线使用"))
        self.checkBoxRememberMe.setText(_translate("MainWindow", "记住密码"))
        self.btnLogin.setText(_translate("MainWindow", "登录"))
        self.labelTip.setText(_translate("MainWindow", "提示信息"))
        self.labelName.setText(_translate("MainWindow", "姓名"))
        self.labelLoginTime.setText(_translate("MainWindow", "登录时间"))
        self.labelIP.setText(_translate("MainWindow", "IP地址"))
        self.labelPhone.setText(_translate("MainWindow", "手机号"))
        self.btnLoadPJ.setText(_translate("MainWindow", "加载评教信息"))
        self.treeWidgetHavePJ.headerItem().setText(0, _translate("MainWindow", "课程名"))
        self.treeWidgetHavePJ.headerItem().setText(1, _translate("MainWindow", "课程类型"))
        self.treeWidgetHavePJ.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.treeWidgetHavePJ.headerItem().setText(3, _translate("MainWindow", "评教状态"))
        self.treeWidgetHavePJ.headerItem().setText(4, _translate("MainWindow", "rel"))
        self.treeWidgetNotPJ.headerItem().setText(0, _translate("MainWindow", "课程名"))
        self.treeWidgetNotPJ.headerItem().setText(1, _translate("MainWindow", "课程类型"))
        self.treeWidgetNotPJ.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.treeWidgetNotPJ.headerItem().setText(3, _translate("MainWindow", "评教状态"))
        self.treeWidgetNotPJ.headerItem().setText(4, _translate("MainWindow", "rel"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), _translate("MainWindow", "未评教课程"))
        self.treeWidgetPJInfo.headerItem().setText(0, _translate("MainWindow", "课程名"))
        self.treeWidgetPJInfo.headerItem().setText(1, _translate("MainWindow", "课程类型"))
        self.treeWidgetPJInfo.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.treeWidgetPJInfo.headerItem().setText(3, _translate("MainWindow", "评教请求发送时间"))
        self.treeWidgetPJInfo.headerItem().setText(4, _translate("MainWindow", "请求结果"))
        self.treeWidgetPJInfo.headerItem().setText(5, _translate("MainWindow", "状态码"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("MainWindow", "评教信息"))
        self.btnPJ.setText(_translate("MainWindow", "评教"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.evaluate), _translate("MainWindow", "评教"))
        self.label_3.setText(_translate("MainWindow", "注意：开始抢课前，需要输入学号密码！"))
        self.btnLoadLessonsOnWeb.setText(_translate("MainWindow", "导入实时数据并保存进数据库"))
        self.btnLoadInMysql.setText(_translate("MainWindow", "导入数据库中的数据"))
        self.label_8.setText(_translate("MainWindow", "使用查询功能请确保数据库安装正确，具体信息点击“关于”查看帮助信息"))
        self.comboBoxQueryType.setItemText(0, _translate("MainWindow", "课程名"))
        self.comboBoxQueryType.setItemText(1, _translate("MainWindow", "教师"))
        self.comboBoxQueryType.setItemText(2, _translate("MainWindow", "学分"))
        self.lineEditQueryLessons.setPlaceholderText(_translate("MainWindow", "输入后按回车键开始查询"))
        self.labelSemester.setText(_translate("MainWindow", "学期"))
        self.label_4.setText(_translate("MainWindow", "双击课程类别展开所有课程，双击课程添加进抢课列表"))
        self.treeWigetReadAllLesson.setSortingEnabled(False)
        self.treeWigetReadAllLesson.headerItem().setText(0, _translate("MainWindow", "课程类别"))
        self.treeWigetReadAllLesson.headerItem().setText(1, _translate("MainWindow", "课程名"))
        self.treeWigetReadAllLesson.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.treeWigetReadAllLesson.headerItem().setText(3, _translate("MainWindow", "剩余人数"))
        self.treeWigetReadAllLesson.headerItem().setText(4, _translate("MainWindow", "上课时间"))
        self.treeWigetReadAllLesson.headerItem().setText(5, _translate("MainWindow", "学分"))
        self.treeWigetReadAllLesson.headerItem().setText(6, _translate("MainWindow", "url"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "全部课程"))
        self.label_6.setText(_translate("MainWindow", "仅显示50条信息，超过50条之后清空。每三秒发送一次抢课请求。"))
        self.treeWidgetQKInfo.headerItem().setText(0, _translate("MainWindow", "线程编号"))
        self.treeWidgetQKInfo.headerItem().setText(1, _translate("MainWindow", "课程名"))
        self.treeWidgetQKInfo.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.treeWidgetQKInfo.headerItem().setText(3, _translate("MainWindow", "请求发送时间"))
        self.treeWidgetQKInfo.headerItem().setText(4, _translate("MainWindow", "请求结果"))
        self.treeWidgetQKInfo.headerItem().setText(5, _translate("MainWindow", "请求状态码"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "抢课记录"))
        self.label_5.setText(_translate("MainWindow", "双击课程移除该课程"))
        self.TreeWidgetLessonsToGrab.setSortingEnabled(False)
        self.TreeWidgetLessonsToGrab.headerItem().setText(0, _translate("MainWindow", "课程类别"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(1, _translate("MainWindow", "课程名"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(3, _translate("MainWindow", "剩余人数"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(4, _translate("MainWindow", "上课时间"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(5, _translate("MainWindow", "学分"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(6, _translate("MainWindow", "url"))
        self.TreeWidgetLessonsToGrab.headerItem().setText(7, _translate("MainWindow", "flag"))
        self.btnQK.setText(_translate("MainWindow", "开始抢课"))
        self.btnStopQK.setText(_translate("MainWindow", "停止抢课"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "待选课程"))
        self.TreeWidgetLessonsHaveChosed.setSortingEnabled(False)
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(0, _translate("MainWindow", "课程类别"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(1, _translate("MainWindow", "课程名"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(2, _translate("MainWindow", "教师"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(3, _translate("MainWindow", "容量"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(4, _translate("MainWindow", "起止周"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(5, _translate("MainWindow", "新建列"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(6, _translate("MainWindow", "课程类别"))
        self.TreeWidgetLessonsHaveChosed.headerItem().setText(7, _translate("MainWindow", "上课时间"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "已选上的课程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grabLesson), _translate("MainWindow", "选课"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.menuUser.setTitle(_translate("MainWindow", "用户"))
        self.actionHelp.setText(_translate("MainWindow", "help"))
        self.help.setText(_translate("MainWindow", "帮助"))
        self.actionSetDatabase.setText(_translate("MainWindow", "配置数据库"))
        self.actionLogout.setText(_translate("MainWindow", "登出"))
        self.actionDeleteThisUserData.setText(_translate("MainWindow", "清除登录信息"))
        self.actionDeleteAllUsersData.setText(_translate("MainWindow", "建立用户数据表"))
        self.actionDeleteLessonData.setText(_translate("MainWindow", "建立课程数据表"))

