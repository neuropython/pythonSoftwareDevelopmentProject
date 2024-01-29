# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"pyABP")
            MainWindow.setWindowTitle(u"pyABP")
        MainWindow.resize(800, 765)
        MainWindow.setStyleSheet("""
            QMainWindow {
                border-radius: 10px;
            }
        """)

        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave_to_file = QAction(MainWindow)
        self.actionSave_to_file.setObjectName(u"actionSave_to_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setEnabled(True)
        self.title.setGeometry(QRect(30, 10, 731, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setMidLineWidth(0)
        self.title.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 330, 731, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 729, 379))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(370, 80, 391, 221))
        self.specifyValuesFor = QLabel(self.centralwidget)
        self.specifyValuesFor.setObjectName(u"label_2")
        self.specifyValuesFor.setGeometry(QRect(100, 70, 111, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setBold(True)
        self.specifyValuesFor.setFont(font1)
        self.time_checkbox = QCheckBox(self.centralwidget)
        self.time_checkbox.setObjectName(u"time_checkbox")
        self.time_checkbox.setGeometry(QRect(30, 220, 101, 21))
        self.frequency_checkbox = QCheckBox(self.centralwidget)
        self.frequency_checkbox.setObjectName(u"frequency_checkbox")
        self.frequency_checkbox.setGeometry(QRect(200, 220, 140, 21))
        self.samplingRate = QLabel(self.centralwidget)
        self.samplingRate.setObjectName(u"samplingRate")
        self.samplingRate.setGeometry(QRect(30, 100, 91, 16))
        self.samplingRateEditTxt = QTextEdit(self.centralwidget)
        self.samplingRateEditTxt.setObjectName(u"samplingRateEditTxt")
        self.samplingRateEditTxt.setGeometry(QRect(170, 98, 171, 25))
        self.fileNames = QLabel(self.centralwidget)
        self.fileNames.setObjectName(u"fileNames")
        self.fileNames.setGeometry(QRect(30, 130, 120, 16))
        self.fileNamesEditTxt = QTextEdit(self.centralwidget)
        self.fileNamesEditTxt.setObjectName(u"fileNamesEditTxt")
        self.fileNamesEditTxt.setGeometry(QRect(170, 128, 171, 25))
        self.windowSize = QLabel(self.centralwidget)
        self.windowSize.setObjectName(u"label_5")
        self.windowSize.setGeometry(QRect(30, 160, 101, 16))
        self.windowSizeEditTxt = QTextEdit(self.centralwidget)
        self.windowSizeEditTxt.setObjectName(u"windowSizeEditTxt")
        self.windowSizeEditTxt.setGeometry(QRect(170, 158, 171, 25))
        self.overlapEditTxt = QTextEdit(self.centralwidget)
        self.overlapEditTxt.setObjectName(u"overlapEditTxt")
        self.overlapEditTxt.setGeometry(QRect(170, 188, 171, 25))
        self.overlapTxt = QLabel(self.centralwidget)
        self.overlapTxt.setObjectName(u"label_6")
        self.overlapTxt.setGeometry(QRect(30, 190, 101, 16))
        self.analyze_button = QPushButton(self.centralwidget)
        self.analyze_button.setObjectName(u"pushButton")
        self.analyze_button.setGeometry(QRect(30, 250, 321, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAnalize = QMenu(self.menubar)
        self.menuAnalize.setObjectName(u"menuAnalize")
        self.menuHow_to_use = QMenu(self.menubar)
        self.menuHow_to_use.setObjectName(u"menuHow_to_use")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAnalize.menuAction())
        self.menubar.addAction(self.menuHow_to_use.menuAction())
        self.menuAnalize.addAction(self.actionClose)
        self.menuAnalize.addAction(self.actionSave_to_file)

        self.retranslateUi(MainWindow)

        self.samplingRateEditTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.samplingRateEditTxt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.fileNamesEditTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.fileNamesEditTxt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.windowSizeEditTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.windowSizeEditTxt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.overlapEditTxt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.overlapEditTxt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        font = QFont("Cascadia Code", 9)  # Specify the font size here

        self.time_checkbox.setFont(font)
        self.time_checkbox.setStyleSheet("""        
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
                border: 1px solid #565C63; /* Add border */
            }
            QCheckBox::indicator:unchecked {
                background-color: #1B1D1F;
            }
            QCheckBox::indicator:checked {
                background-color: #246ED9;
            }
            QCheckBox {
                color: #565C63; /* Adjust text color */
            }       
        """)

        self.frequency_checkbox.setFont(font)
        self.frequency_checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
                border: 1px solid #565C63; /* Add border */
            }
            QCheckBox::indicator:unchecked {
                background-color: #1B1D1F;
            }
            QCheckBox::indicator:checked {
                background-color: #246ED9;
            }
            QCheckBox {
                color: #565C63; /* Adjust text color */
            }
        """)

        MainWindow.setFont(font)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #1B1D1F;
                border: 1px solid;
                border-radius: 10px;
                color: #DDDDDD;
            }
        """)

        font1 = QFont()
        font1.setFamilies("Poppins")
        font1.setBold(True)

        font1.setPointSize(12)
        self.analyze_button.setFont(font1)
        self.analyze_button.setStyleSheet("""
        background-color: #246ED9;
        color: #DDDDDD;
        border: 1px solid;
        border-radius: 10px;
        """)

        font = QFont("Cascadia Code")
        font1.setPointSize(12)

        self.samplingRateEditTxt.setFont(font)
        self.samplingRateEditTxt.setStyleSheet("color: #665C63;")

        self.fileNamesEditTxt.setFont(font)
        self.fileNamesEditTxt.setStyleSheet("color: #665C63;")

        self.windowSizeEditTxt.setFont(font)
        self.windowSizeEditTxt.setStyleSheet("color: #665C63;")

        self.overlapEditTxt.setFont(font)
        self.overlapEditTxt.setStyleSheet("color: #565C63;")

        self.title.setFont(font)
        self.title.setStyleSheet("color: #565C63;")

        self.specifyValuesFor.setFont(font)
        self.specifyValuesFor.setStyleSheet("color: #565C63;")

        self.samplingRate.setFont(font)
        self.samplingRate.setStyleSheet("color: #565C63;")

        self.fileNames.setFont(font)
        self.fileNames.setStyleSheet("color: #565C63;")

        self.windowSize.setFont(font)
        self.windowSize.setStyleSheet("color: #565C63;")

        self.overlapTxt.setFont(font)
        self.overlapTxt.setStyleSheet("color: #565C63;")

        self.samplingRateEditTxt.setStyleSheet("background-color: #1B1D1F;")
        self.fileNamesEditTxt.setStyleSheet("background-color: #1B1D1F;")
        self.windowSizeEditTxt.setStyleSheet("background-color: #1B1D1F;")
        self.overlapEditTxt.setStyleSheet("background-color: #1B1D1F;")

        font = QFont("Cascadia Code")
        font.setBold(True)
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u' Drag and Drop paths here ', None))
        self.plainTextEdit.setStyleSheet("""
            color: #00ff00;
            background-color: #17191B;
        """)

        self.scrollArea.setStyleSheet("background-color: #17191B;")

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyABP", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSave_to_file.setText(QCoreApplication.translate("MainWindow", u"Save to file ", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Brain Lab ABP analysis Software", None))
        self.plainTextEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Drag and Drop paths here ", None))
        self.specifyValuesFor.setText(QCoreApplication.translate("MainWindow", u"Specify values for:", None))
        self.time_checkbox.setText(QCoreApplication.translate("MainWindow", u"Time Domain", None))
        self.frequency_checkbox.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain", None))
        self.samplingRate.setText(QCoreApplication.translate("MainWindow", u"Sampling rate", None))
        self.fileNames.setText(QCoreApplication.translate("MainWindow", u"Names of the rows", None))
        self.windowSize.setText(QCoreApplication.translate("MainWindow", u"Window size", None))
        self.overlapTxt.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
        self.analyze_button.setText(QCoreApplication.translate("MainWindow", u"Analize", None))
        self.menuAnalize.setTitle(QCoreApplication.translate("MainWindow", u"Analize", None))
        self.menuHow_to_use.setTitle(QCoreApplication.translate("MainWindow", u"How to use", None))
    # retranslateUi

