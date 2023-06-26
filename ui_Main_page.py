# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_page.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(681, 515)
        MainPage.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(252, 252, 252);\n"
"}")
        self.centralwidget = QWidget(MainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(35)
        self.verticalSpacer = QSpacerItem(26, 176, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.tutorial = QPushButton(self.centralwidget)
        self.tutorial.setObjectName(u"tutorial")
        font = QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.tutorial.setFont(font)
        self.tutorial.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(209, 236, 243);\n"
"}")

        self.gridLayout_13.addWidget(self.tutorial, 5, 2, 1, 1, Qt.AlignVCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(252, 252, 252);\n"
"	border-color: rgba(252, 252, 252, 0);\n"
"	font: 700 36pt \"Product Sans\";\n"
"}")

        self.gridLayout_13.addWidget(self.label, 1, 0, 1, 3, Qt.AlignHCenter|Qt.AlignVCenter)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setFont(font)
        self.about.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(209, 236, 243);\n"
"}")

        self.gridLayout_13.addWidget(self.about, 5, 0, 1, 1, Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.start.setFont(font1)
        self.start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(247, 200, 131);\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"}")

        self.gridLayout_13.addWidget(self.start, 5, 1, 1, 1, Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_3, 6, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        MainPage.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainPage)
        self.statusbar.setObjectName(u"statusbar")
        MainPage.setStatusBar(self.statusbar)

        self.retranslateUi(MainPage)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"Virtual Kulintang", None))
        self.tutorial.setText(QCoreApplication.translate("MainPage", u"Tutorial", None))
        self.label.setText(QCoreApplication.translate("MainPage", u"Virtual Kulintang", None))
        self.about.setText(QCoreApplication.translate("MainPage", u"About", None))
        self.start.setText(QCoreApplication.translate("MainPage", u"START", None))
    # retranslateUi

