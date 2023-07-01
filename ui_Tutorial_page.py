# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tutorialPage.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_tutorial_page(object):
    def setupUi(self, tutorial_page):
        if not tutorial_page.objectName():
            tutorial_page.setObjectName(u"tutorial_page")
        tutorial_page.resize(863, 699)
        self.centralwidget = QWidget(tutorial_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.about_frame = QFrame(self.centralwidget)
        self.about_frame.setObjectName(u"about_frame")
        self.about_frame.setGeometry(QRect(10, 10, 841, 661))
        self.about_frame.setMaximumSize(QSize(1920, 16777215))
        self.about_frame.setStyleSheet(u"background-color: rgb(252, 252, 252);")
        self.about_frame.setFrameShape(QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.about_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 820, 643))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 20, 10, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(1450, 43))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(800, 500))
        self.scrollArea.setMaximumSize(QSize(850, 500))
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -113, 849, 609))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(750, 16777215))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(750, 16777215))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(5)
        self.label_2.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(750, 16777215))
        self.label_9.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(750, 16777215))
        self.label_8.setFont(font2)
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setMargin(5)
        self.label_8.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.image_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_10.setObjectName(u"image_10")
        self.image_10.setMaximumSize(QSize(320, 180))
        self.image_10.setPixmap(QPixmap(u"calibration_red.png"))
        self.image_10.setScaledContents(True)
        self.image_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.image_10)

        self.image_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_9.setObjectName(u"image_9")
        self.image_9.setMaximumSize(QSize(320, 180))
        self.image_9.setPixmap(QPixmap(u"calibration_green.png"))
        self.image_9.setScaledContents(True)
        self.image_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.image_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(750, 16777215))
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setMargin(5)
        self.label_5.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(750, 16777215))
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(750, 16777215))
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setMargin(5)
        self.label_4.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_4.setObjectName(u"image_4")
        self.image_4.setMaximumSize(QSize(320, 180))
        self.image_4.setPixmap(QPixmap(u"strike_r.png"))
        self.image_4.setScaledContents(True)
        self.image_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_4)

        self.image_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_5.setObjectName(u"image_5")
        self.image_5.setMaximumSize(QSize(320, 180))
        self.image_5.setPixmap(QPixmap(u"strike_g.png"))
        self.image_5.setScaledContents(True)
        self.image_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(750, 16777215))
        self.label_11.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(750, 16777215))
        self.label_10.setFont(font2)
        self.label_10.setTextFormat(Qt.RichText)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setMargin(5)
        self.label_10.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.back_to_main = QPushButton(self.verticalLayoutWidget)
        self.back_to_main.setObjectName(u"back_to_main")
        font3 = QFont()
        font3.setPointSize(14)
        self.back_to_main.setFont(font3)
        self.back_to_main.setStyleSheet(u"background-color: rgb(209, 236, 243);")

        self.verticalLayout.addWidget(self.back_to_main)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        tutorial_page.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(tutorial_page)
        self.statusbar.setObjectName(u"statusbar")
        tutorial_page.setStatusBar(self.statusbar)

        self.retranslateUi(tutorial_page)

        QMetaObject.connectSlotsByName(tutorial_page)
    # setupUi

    def retranslateUi(self, tutorial_page):
        tutorial_page.setWindowTitle(QCoreApplication.translate("tutorial_page", u"Tutorial", None))
        self.label_3.setText(QCoreApplication.translate("tutorial_page", u"Tutorial", None))
        self.label_6.setText(QCoreApplication.translate("tutorial_page", u"Markers", None))
        self.label_2.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">The kulintang is an indigenous instrument native to the Mindanao islands in the </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("tutorial_page", u"Calibration", None))
        self.label_8.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">The kulintang is an indigenous instrument native to the Mindanao islands in the </span></p></body></html>", None))
        self.image_10.setText("")
        self.image_9.setText("")
        self.label_5.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Product Sans'; font-size:14pt;\">The Virtual Kulintang program aims to promote appreciation for the Philippine Indigenous Musical Instruments by making<br />use of computer vision to provide an easily accessible means for users to simulate playing the kulintang instrument.</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("tutorial_page", u"Virtual Kulintang", None))
        self.label_4.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">This program simulates playing of the kulintang instrument through the user's camera (using computer vision). Markers<br />of different colors that are distinct from the background are used as the </span><span style=\" font-family:'Helvetica Neue'; font-size:14pt; font-style:italic;\">basal</span><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">, which will be tracked by the program.<br />A synthesized audio for each of the 8 kulintang gongs will be p"
                        "layed</span><span style=\" font-family:'Product Sans'; font-size:14pt;\"> for every 'hit' detected.</span></p></body></html>", None))
        self.image_4.setText("")
        self.image_5.setText("")
        self.label_11.setText(QCoreApplication.translate("tutorial_page", u"Virtual Kulintang", None))
        self.label_10.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">This program simulates playing of the kulintang instrument through the user's camera (using computer vision). Markers<br />of different colors that are distinct from the background are used as the </span><span style=\" font-family:'Helvetica Neue'; font-size:14pt; font-style:italic;\">basal</span><span style=\" font-family:'Helvetica Neue'; font-size:14pt;\">, which will be tracked by the program.<br />A synthesized audio for each of the 8 kulintang gongs will be p"
                        "layed</span><span style=\" font-family:'Product Sans'; font-size:14pt;\"> for every 'hit' detected.</span></p></body></html>", None))
        self.back_to_main.setText(QCoreApplication.translate("tutorial_page", u"Back to Main Page", None))
    # retranslateUi

