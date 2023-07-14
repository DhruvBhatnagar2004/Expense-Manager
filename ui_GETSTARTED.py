# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GETSTARTEDFmLezl.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import myresource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 517)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color:rgb(56, 58, 89);\n"
"}\n"
"#widget{\n"
"	background-color:rgb(9,27,68);\n"
"	border-radius:20px;\n"
"}\n"
"QLineEdit{\n"
"	background-color:rgb(9,10,37);\n"
"	padding:5px 3px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color:rgb(9,10,37);\n"
"	padding:10px 5px;\n"
"	border-radius:5px;\n"
"}\n"
"#to_register,#to_login{\n"
"	background-color:transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 450))
        self.widget.setMaximumSize(QSize(250, 450))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Registerpage = QWidget()
        self.Registerpage.setObjectName(u"Registerpage")
        self.verticalLayout_5 = QVBoxLayout(self.Registerpage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.Registerpage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(80, 50))
        self.label.setPixmap(QPixmap(u"pl.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.Registerpage)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(254,121,199);")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.Registerpage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:rgb(254,121,199);")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.Registerpage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.Registerpage)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_5.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.Registerpage)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.to_login = QPushButton(self.Registerpage)
        self.to_login.setObjectName(u"to_login")
        font1 = QFont()
        font1.setUnderline(True)
        self.to_login.setFont(font1)

        self.verticalLayout_5.addWidget(self.to_login, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.Registerpage)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.Registerpage)
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.verticalLayout_7 = QVBoxLayout(self.loginpage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.loginpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 50))
        self.label_7.setMaximumSize(QSize(80, 50))
        self.label_7.setPixmap(QPixmap(u"ti.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.loginpage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color:rgb(254,121,199);")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.loginpage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:rgb(254,121,199);")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.frame_3 = QFrame(self.loginpage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.pushButton_4 = QPushButton(self.loginpage)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.to_register = QPushButton(self.loginpage)
        self.to_register.setObjectName(u"to_register")
        self.to_register.setFont(font1)

        self.verticalLayout_7.addWidget(self.to_register, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.loginpage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.loginpage)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Do you want to sign in?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Already Registered? Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"app name", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.to_register.setText(QCoreApplication.translate("MainWindow", u"Not Registered? Sign Up", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"app name", None))
    # retranslateUi

