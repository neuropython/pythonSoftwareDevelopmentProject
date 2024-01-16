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
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave_to_file = QAction(MainWindow)
        self.actionSave_to_file.setObjectName(u"actionSave_to_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(30, 10, 731, 61))
        font = QFont()
        font.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 70, 111, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.time_checkbox = QCheckBox(self.centralwidget)
        self.time_checkbox.setObjectName(u"checkBox")
        self.time_checkbox.setGeometry(QRect(30, 220, 101, 21))
        self.frequency_checkbox = QCheckBox(self.centralwidget)
        self.frequency_checkbox.setObjectName(u"checkBox_2")
        self.frequency_checkbox.setGeometry(QRect(210, 220, 131, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 100, 91, 16))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 100, 171, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 130, 101, 16))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(170, 130, 171, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 160, 101, 16))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(170, 160, 171, 21))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(170, 190, 171, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 190, 101, 16))
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyABP", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSave_to_file.setText(QCoreApplication.translate("MainWindow", u"Save to file ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Brain Lab ABP analysis Software", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Drag and Drop paths here ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Specify values for:", None))
        self.time_checkbox.setText(QCoreApplication.translate("MainWindow", u"Time Domain", None))
        self.frequency_checkbox.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sampling rate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Names of the files", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"window_size", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"overlap", None))
        self.analyze_button.setText(QCoreApplication.translate("MainWindow", u"Analize", None))
        self.menuAnalize.setTitle(QCoreApplication.translate("MainWindow", u"Analize", None))
        self.menuHow_to_use.setTitle(QCoreApplication.translate("MainWindow", u"How to use", None))
    # retranslateUi

