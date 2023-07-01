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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_tutorial_page(object):
    def setupUi(self, tutorial_page):
        if not tutorial_page.objectName():
            tutorial_page.setObjectName(u"tutorial_page")
        tutorial_page.resize(863, 715)
        self.centralwidget = QWidget(tutorial_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.about_frame = QFrame(self.centralwidget)
        self.about_frame.setObjectName(u"about_frame")
        self.about_frame.setGeometry(QRect(10, 10, 841, 681))
        self.about_frame.setMaximumSize(QSize(1920, 16777215))
        self.about_frame.setStyleSheet(u"background-color: rgb(252, 252, 252);")
        self.about_frame.setFrameShape(QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.about_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 820, 666))
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

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(800, 500))
        self.scrollArea.setMaximumSize(QSize(850, 1000))
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 780, 749))
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

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

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

        self.image_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_9.setObjectName(u"image_9")
        sizePolicy.setHeightForWidth(self.image_9.sizePolicy().hasHeightForWidth())
        self.image_9.setSizePolicy(sizePolicy)
        self.image_9.setMinimumSize(QSize(320, 160))
        self.image_9.setMaximumSize(QSize(320, 160))
        self.image_9.setPixmap(QPixmap(u"calibration_green.png"))
        self.image_9.setScaledContents(True)
        self.image_9.setAlignment(Qt.AlignCenter)
        self.image_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.image_9)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

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

        self.image_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.image_4.setObjectName(u"image_4")
        sizePolicy.setHeightForWidth(self.image_4.sizePolicy().hasHeightForWidth())
        self.image_4.setSizePolicy(sizePolicy)
        self.image_4.setMinimumSize(QSize(320, 160))
        self.image_4.setMaximumSize(QSize(320, 160))
        self.image_4.setPixmap(QPixmap(u"strike_r.png"))
        self.image_4.setScaledContents(True)
        self.image_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.image_4)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

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

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(750, 16777215))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_2.addWidget(self.label_16)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

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
        self.label_3.setText(QCoreApplication.translate("tutorial_page", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Tutorial</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("tutorial_page", u"Markers", None))
        self.label_2.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">The markers must have a spherical tip with different colors, preferrably contrasting. It is also adivsed that the<br />markers should be contrasting with the background for a more accurate detection and tracking.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("tutorial_page", u"Calibration", None))
        self.label_8.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Place the tip of the marker within the circle on the screen. Once inside the area, click anywhere on the frame to<br />capture the image. The left marker will be calibrated first, then afterwards, the right marker will be calibrated next.</span></p></body></html>", None))
        self.image_9.setText("")
        self.label_7.setText(QCoreApplication.translate("tutorial_page", u"Playing the Virtual Kulintang", None))
        self.label_4.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Product Sans'; font-size:14pt;\">The centroid of the marker will be marked by a blue dot, which will be the basis for the hit detection. To be considered as a<br />&quot;hit&quot; action, the blue dot must cross the upper bound of the boxes, from above the line to anywhere below the line. </span></p></body></html>", None))
        self.image_4.setText("")
        self.label_11.setText(QCoreApplication.translate("tutorial_page", u"Closing the Program", None))
        self.label_10.setText(QCoreApplication.translate("tutorial_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Product Sans'; font-size:14pt;\">To close the program, press the </span><span style=\" font-family:'Product Sans'; font-size:14pt; font-weight:700;\">ESC </span><span style=\" font-family:'Product Sans'; font-size:14pt;\">key on your keyboard.</span></p></body></html>", None))
        self.label_16.setText("")
        self.back_to_main.setText(QCoreApplication.translate("tutorial_page", u"Back to Main Page", None))
    # retranslateUi

