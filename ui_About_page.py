# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_about_page(object):
    def setupUi(self, about_page):
        if not about_page.objectName():
            about_page.setObjectName(u"about_page")
        about_page.resize(811, 478)
        self.centralwidget = QWidget(about_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.about_frame = QFrame(self.centralwidget)
        self.about_frame.setObjectName(u"about_frame")
        self.about_frame.setGeometry(QRect(10, 10, 791, 441))
        self.about_frame.setMaximumSize(QSize(1920, 16777215))
        self.about_frame.setStyleSheet(u"background-color: rgb(252, 252, 252);")
        self.about_frame.setFrameShape(QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.about_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 771, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 20, 10, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(1450, 16777215))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1450, 16777215))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(5)
        self.label_2.setIndent(5)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(1450, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setMargin(5)
        self.label_4.setIndent(5)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(1450, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setMargin(5)
        self.label_5.setIndent(5)

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.back_to_main = QPushButton(self.verticalLayoutWidget)
        self.back_to_main.setObjectName(u"back_to_main")
        font2 = QFont()
        font2.setPointSize(14)
        self.back_to_main.setFont(font2)
        self.back_to_main.setStyleSheet(u"background-color: rgb(209, 236, 243);")

        self.verticalLayout.addWidget(self.back_to_main)

        about_page.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(about_page)
        self.statusbar.setObjectName(u"statusbar")
        about_page.setStatusBar(self.statusbar)

        self.retranslateUi(about_page)

        QMetaObject.connectSlotsByName(about_page)
    # setupUi

    def retranslateUi(self, about_page):
        about_page.setWindowTitle(QCoreApplication.translate("about_page", u"About", None))
        self.label_3.setText(QCoreApplication.translate("about_page", u"<html><head/><body><p><span style=\" text-decoration: underline;\">About Virtual Kulintang</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("about_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">The kulintang is an indigenous instrument native to the Mindanao islands in the southern part of the country. It is a set<br />of 8 embossed gongs suspended horizontally on two parallel strings arranged from largest to smallest, left to right.<br />The gongs are knobbed at the center and played using a pair of soft wooden sticks called the </span><span style=\" font-size:14pt; font-style:italic;\">basal</span><span style=\" font-size:14pt;\">.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("about_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">This program simulates playing of the kulintang instrument through the user's camera (using computer vision). Markers<br />of different colors that are distinct from the background are used as the </span><span style=\" font-family:'Helvetica Neue'; font-size:14pt; font-style:italic;\">basal</span><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">, which will be tracked by the program.<br />A synthesized audio for each of the 8 kulintang gongs will be p"
                        "layed</span><span style=\" font-family:'Product Sans'; font-size:14pt;\"> for every 'hit' detected.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("about_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Product Sans'; font-size:14pt;\">The Virtual Kulintang program aims to promote appreciation for the Philippine Indigenous Musical Instruments by making<br />use of computer vision to provide an easily accessible means for users to simulate playing the kulintang instrument.</span></p></body></html>", None))
        self.back_to_main.setText(QCoreApplication.translate("about_page", u"Back to Main Page", None))
    # retranslateUi

