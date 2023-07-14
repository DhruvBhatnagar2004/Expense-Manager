# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash screenrMjrGs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 517)
        MainWindow.setStyleSheet(u"border-radius: 20px\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color:#FFF;\n"
"}\n"
"QWidget{\n"
"	background:rgb(9,27,68);\n"
"botder-radius:12px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.app_logo = QFrame(self.centralwidget)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setFrameShape(QFrame.StyledPanel)
        self.app_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_img = QLabel(self.app_logo)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMinimumSize(QSize(150, 150))
        self.logo_img.setMaximumSize(QSize(150, 150))
        self.logo_img.setStyleSheet(u"QLabel{\n"
"	border-radius: 50px;\n"
"}")
        self.logo_img.setPixmap(QPixmap(u"logo.png"))
        self.logo_img.setScaledContents(True)
        self.logo_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logo_img)


        self.verticalLayout.addWidget(self.app_logo)

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_name = QLabel(self.background)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        font.setBold(True)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"color:rgb(254, 121, 199)")
        self.app_name.setPixmap(QPixmap(u"tetx.png"))
        self.app_name.setScaledContents(False)
        self.app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_name)

        self.progress = QFrame(self.background)
        self.progress.setObjectName(u"progress")
        self.progress.setFrameShape(QFrame.StyledPanel)
        self.progress.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progress)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.percentage = QLabel(self.progress)
        self.percentage.setObjectName(u"percentage")
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.percentage.setFont(font1)
        self.percentage.setStyleSheet(u"color:rgb(254, 121, 199)")
        self.percentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.percentage)

        self.progressbar = QProgressBar(self.progress)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setMinimumSize(QSize(0, 0))
        self.progressbar.setMaximumSize(QSize(16777215, 10))
        self.progressbar.setStyleSheet(u"QProgressBar{\n"
"	background: rgba(255, 255, 255,180);\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	color: rgba(200, 200, 200,0);\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius:5px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 255, 255), stop:1 rgba(85, 85, 255, 255))\n"
"}")
        self.progressbar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressbar)


        self.verticalLayout_2.addWidget(self.progress)

        self.footer_2 = QFrame(self.background)
        self.footer_2.setObjectName(u"footer_2")
        self.footer_2.setFrameShape(QFrame.StyledPanel)
        self.footer_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.author = QLabel(self.footer_2)
        self.author.setObjectName(u"author")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.author.setFont(font2)
        self.author.setStyleSheet(u"color:rgb(254, 121, 199)")

        self.horizontalLayout_2.addWidget(self.author)

        self.status = QLabel(self.footer_2)
        self.status.setObjectName(u"status")
        self.status.setFont(font2)
        self.status.setStyleSheet(u"color:rgb(254, 121, 199)")

        self.horizontalLayout_2.addWidget(self.status, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.footer_2)


        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
        self.app_name.setText("")
        self.percentage.setText(QCoreApplication.translate("MainWindow", u"24%", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"Author: HackMasters", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Status: Prototype", None))
    # retranslateUi

