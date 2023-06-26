# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calib_prompt.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(503, 207)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 459, 163))
        self.Calib_prompt = QVBoxLayout(self.gridLayoutWidget)
        self.Calib_prompt.setSpacing(0)
        self.Calib_prompt.setObjectName(u"Calib_prompt")
        self.Calib_prompt.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Calib_prompt.addItem(self.verticalSpacer_3)

        self.calibration = QLabel(self.gridLayoutWidget)
        self.calibration.setObjectName(u"calibration")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.calibration.setFont(font)

        self.Calib_prompt.addWidget(self.calibration, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Calib_prompt.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	text-align: justify;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}")

        self.Calib_prompt.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Calib_prompt.addItem(self.verticalSpacer_2)

        self.calibration_start = QPushButton(self.gridLayoutWidget)
        self.calibration_start.setObjectName(u"calibration_start")
        font2 = QFont()
        font2.setBold(True)
        self.calibration_start.setFont(font2)

        self.Calib_prompt.addWidget(self.calibration_start)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calibration.setText(QCoreApplication.translate("MainWindow", u"Calibration Instruction", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Place the main color of the marker within the circle on the screen <br/>and click anywhere on the frame to capture the image for calibration.</p></body></html>", None))
        self.calibration_start.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
    # retranslateUi

