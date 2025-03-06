# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 606)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(10000, 6000))
        self.actionopen_images_folder = QAction(MainWindow)
        self.actionopen_images_folder.setObjectName(u"actionopen_images_folder")
        self.actionopen_label_folder = QAction(MainWindow)
        self.actionopen_label_folder.setObjectName(u"actionopen_label_folder")
        self.actionvit_h = QAction(MainWindow)
        self.actionvit_h.setObjectName(u"actionvit_h")
        self.actionvit_b = QAction(MainWindow)
        self.actionvit_b.setObjectName(u"actionvit_b")
        self.actionvit_l = QAction(MainWindow)
        self.actionvit_l.setObjectName(u"actionvit_l")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(10000, 10000))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 251, 561))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 16))
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 40, 80, 19))
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 70, 80, 19))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 91, 16))
        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 140, 80, 19))
        self.verticalLayoutWidget_3 = QWidget(self.frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 190, 221, 181))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 170, 251, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget_4 = QWidget(self.frame)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 390, 221, 80))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_4.addWidget(self.checkBox_4)

        self.verticalLayoutWidget_5 = QWidget(self.frame)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 480, 221, 70))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout.addWidget(self.checkBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(970, 10, 221, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(970, 280, 221, 271))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.listView_2 = QListView(self.verticalLayoutWidget_2)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_2.addWidget(self.listView_2)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(280, 10, 681, 551))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionopen_images_folder)
        self.menu.addAction(self.actionopen_label_folder)
        self.menu_2.addAction(self.actionvit_h)
        self.menu_2.addAction(self.actionvit_b)
        self.menu_2.addAction(self.actionvit_l)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9b54\u68d2\u5de5\u5177", None))
        self.actionopen_images_folder.setText(QCoreApplication.translate("MainWindow", u"open image folder", None))
        self.actionopen_label_folder.setText(QCoreApplication.translate("MainWindow", u"open label folder", None))
        self.actionvit_h.setText(QCoreApplication.translate("MainWindow", u"vit_h", None))
        self.actionvit_b.setText(QCoreApplication.translate("MainWindow", u"vit_b(\u9ed8\u8ba4)", None))
        self.actionvit_l.setText(QCoreApplication.translate("MainWindow", u"vit_l", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u63d0\u793a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"positive", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"negative", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6846\u63d0\u793a", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"box", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Previous image", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Next image", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u683c\u5f0f\uff1a", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"mask", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u72b6\u6001", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u6807\u6ce8", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u5fae\u8c03", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"image list", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"label list", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
    # retranslateUi

