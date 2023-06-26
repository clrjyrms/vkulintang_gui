# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loading_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QStatusBar, QWidget)

class Ui_LoadingPage(object):
    def setupUi(self, LoadingPage):
        if not LoadingPage.objectName():
            LoadingPage.setObjectName(u"LoadingPage")
        LoadingPage.resize(492, 245)
        self.centralwidget = QWidget(LoadingPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Loading = QFrame(self.centralwidget)
        self.Loading.setObjectName(u"Loading")
        self.Loading.setGeometry(QRect(10, 10, 471, 211))
        self.Loading.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(252, 252, 252);\n"
"	border-radius: 10px;\n"
"	border-style: none;\n"
"}")
        self.Loading.setFrameShape(QFrame.StyledPanel)
        self.Loading.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.Loading)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 471, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.Loading)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 110, 471, 20))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(0)
        self.progressBar = QProgressBar(self.Loading)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 150, 391, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(247, 200, 131);\n"
"}")
        self.progressBar.setValue(20)
        LoadingPage.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoadingPage)
        self.statusbar.setObjectName(u"statusbar")
        LoadingPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoadingPage)

        QMetaObject.connectSlotsByName(LoadingPage)
    # setupUi

    def retranslateUi(self, LoadingPage):
        LoadingPage.setWindowTitle(QCoreApplication.translate("LoadingPage", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoadingPage", u"Virtual Kulintang", None))
        self.label_2.setText(QCoreApplication.translate("LoadingPage", u"Loading...", None))
    # retranslateUi

