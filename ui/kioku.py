# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kioku_smallfont.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGroupBox,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1225, 734)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView_question = QGraphicsView(self.centralwidget)
        self.graphicsView_question.setObjectName(u"graphicsView_question")
        self.graphicsView_question.setGeometry(QRect(410, 70, 481, 321))
        self.graphicsView_question.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.graphicsView_answer = QGraphicsView(self.centralwidget)
        self.graphicsView_answer.setObjectName(u"graphicsView_answer")
        self.graphicsView_answer.setGeometry(QRect(900, 70, 311, 192))
        self.graphicsView_answer.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.groupBox_check = QGroupBox(self.centralwidget)
        self.groupBox_check.setObjectName(u"groupBox_check")
        self.groupBox_check.setGeometry(QRect(490, 500, 711, 81))
        self.groupBox_check.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.pushButton_correct = QPushButton(self.groupBox_check)
        self.pushButton_correct.setObjectName(u"pushButton_correct")
        self.pushButton_correct.setGeometry(QRect(10, 10, 121, 31))
        self.pushButton_correct.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(0, 170, 255);\n"
"color:rgb(0, 0, 127);\n"
"")
        self.label_standard = QLabel(self.groupBox_check)
        self.label_standard.setObjectName(u"label_standard")
        self.label_standard.setGeometry(QRect(30, 40, 81, 31))
        self.label_standard.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_standard.setAlignment(Qt.AlignCenter)
        self.pushButton_easy = QPushButton(self.groupBox_check)
        self.pushButton_easy.setObjectName(u"pushButton_easy")
        self.pushButton_easy.setGeometry(QRect(150, 10, 121, 31))
        self.pushButton_easy.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(151, 236, 255);\n"
"color: rgb(0, 0, 127);\n"
"")
        self.label_easy = QLabel(self.groupBox_check)
        self.label_easy.setObjectName(u"label_easy")
        self.label_easy.setGeometry(QRect(160, 40, 101, 31))
        self.label_easy.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_easy.setAlignment(Qt.AlignCenter)
        self.pushButton_wrong = QPushButton(self.groupBox_check)
        self.pushButton_wrong.setObjectName(u"pushButton_wrong")
        self.pushButton_wrong.setGeometry(QRect(300, 10, 121, 31))
        self.pushButton_wrong.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(255, 170, 127);\n"
"color: rgb(74, 0, 0);\n"
"")
        self.label_miss = QLabel(self.groupBox_check)
        self.label_miss.setObjectName(u"label_miss")
        self.label_miss.setGeometry(QRect(310, 40, 101, 31))
        self.label_miss.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_miss.setAlignment(Qt.AlignCenter)
        self.pushButton_difficult = QPushButton(self.groupBox_check)
        self.pushButton_difficult.setObjectName(u"pushButton_difficult")
        self.pushButton_difficult.setGeometry(QRect(440, 10, 121, 31))
        self.pushButton_difficult.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(255, 116, 35);\n"
"color: rgb(74, 0, 0);\n"
"")
        self.label_difficult = QLabel(self.groupBox_check)
        self.label_difficult.setObjectName(u"label_difficult")
        self.label_difficult.setGeometry(QRect(450, 40, 101, 31))
        self.label_difficult.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_difficult.setAlignment(Qt.AlignCenter)
        self.pushButton_skip = QPushButton(self.groupBox_check)
        self.pushButton_skip.setObjectName(u"pushButton_skip")
        self.pushButton_skip.setGeometry(QRect(610, 10, 91, 31))
        self.pushButton_skip.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(212, 212, 212);\n"
"color: rgb(74, 0, 0);\n"
"")
        self.label_standard.raise_()
        self.label_easy.raise_()
        self.label_miss.raise_()
        self.label_difficult.raise_()
        self.pushButton_easy.raise_()
        self.pushButton_difficult.raise_()
        self.pushButton_correct.raise_()
        self.pushButton_wrong.raise_()
        self.pushButton_skip.raise_()
        self.label_answer = QLabel(self.centralwidget)
        self.label_answer.setObjectName(u"label_answer")
        self.label_answer.setGeometry(QRect(910, 40, 81, 21))
        self.label_question = QLabel(self.centralwidget)
        self.label_question.setObjectName(u"label_question")
        self.label_question.setGeometry(QRect(420, 40, 81, 21))
        self.groupBox_controller = QGroupBox(self.centralwidget)
        self.groupBox_controller.setObjectName(u"groupBox_controller")
        self.groupBox_controller.setGeometry(QRect(840, 620, 291, 51))
        self.pushButton_understand = QPushButton(self.groupBox_controller)
        self.pushButton_understand.setObjectName(u"pushButton_understand")
        self.pushButton_understand.setGeometry(QRect(10, 10, 151, 31))
        self.pushButton_understand.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(3, 32, 93);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_end = QPushButton(self.groupBox_controller)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setGeometry(QRect(190, 10, 91, 31))
        self.pushButton_end.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(3, 32, 93);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_check = QPushButton(self.centralwidget)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setGeometry(QRect(690, 410, 211, 41))
        self.pushButton_check.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(3, 32, 93);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_read = QPushButton(self.centralwidget)
        self.pushButton_read.setObjectName(u"pushButton_read")
        self.pushButton_read.setGeometry(QRect(10, 630, 121, 31))
        self.pushButton_read.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color: rgb(218, 218, 218);\n"
"\n"
"")
        self.graphicsView_page = QGraphicsView(self.centralwidget)
        self.graphicsView_page.setObjectName(u"graphicsView_page")
        self.graphicsView_page.setGeometry(QRect(10, 70, 381, 541))
        self.graphicsView_page.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.groupBox_setting = QGroupBox(self.centralwidget)
        self.groupBox_setting.setObjectName(u"groupBox_setting")
        self.groupBox_setting.setGeometry(QRect(490, 620, 301, 51))
        self.pushButton_restart = QPushButton(self.groupBox_setting)
        self.pushButton_restart.setObjectName(u"pushButton_restart")
        self.pushButton_restart.setGeometry(QRect(10, 10, 121, 31))
        self.pushButton_restart.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color:rgb(3, 32, 93);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.comboBox_sorting = QComboBox(self.groupBox_setting)
        self.comboBox_sorting.setObjectName(u"comboBox_sorting")
        self.comboBox_sorting.setGeometry(QRect(150, 10, 141, 31))
        self.comboBox_sorting.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"")
        self.pushButton_setting = QPushButton(self.centralwidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setGeometry(QRect(150, 630, 121, 31))
        self.pushButton_setting.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"background-color: rgb(218, 218, 218);\n"
"\n"
"")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 10, 791, 21))
        self.label_title.setStyleSheet(u"font: 700 14pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"")
        self.label_prev_result = QLabel(self.centralwidget)
        self.label_prev_result.setObjectName(u"label_prev_result")
        self.label_prev_result.setGeometry(QRect(940, 410, 281, 31))
        self.label_prev_result.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.comboBox_layout = QComboBox(self.centralwidget)
        self.comboBox_layout.setObjectName(u"comboBox_layout")
        self.comboBox_layout.setGeometry(QRect(560, 30, 141, 31))
        self.comboBox_layout.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView_question.raise_()
        self.graphicsView_answer.raise_()
        self.label_answer.raise_()
        self.label_question.raise_()
        self.groupBox_controller.raise_()
        self.pushButton_check.raise_()
        self.pushButton_read.raise_()
        self.graphicsView_page.raise_()
        self.groupBox_setting.raise_()
        self.groupBox_check.raise_()
        self.pushButton_setting.raise_()
        self.label_title.raise_()
        self.label_prev_result.raise_()
        self.comboBox_layout.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"gotit", None))
        self.groupBox_check.setTitle("")
        self.pushButton_correct.setText(QCoreApplication.translate("MainWindow", u" Correct", None))
        self.label_standard.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\uff11\u65e5\u5f8c</span></p></body></html>", None))
        self.pushButton_easy.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.label_easy.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\uff11\u9031\u9593\u5f8c</span></p></body></html>", None))
        self.pushButton_wrong.setText(QCoreApplication.translate("MainWindow", u"Mistake", None))
        self.label_miss.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\uff11\u6642\u9593\u5f8c</span></p></body></html>", None))
        self.pushButton_difficult.setText(QCoreApplication.translate("MainWindow", u"Difficult", None))
        self.label_difficult.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\uff110\u5206\u5f8c</span></p></body></html>", None))
        self.pushButton_skip.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30ad\u30c3\u30d7", None))
        self.label_answer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#03205d;\">Answer</span></p></body></html>", None))
        self.label_question.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#03205d;\">Exercise</span></p></body></html>", None))
        self.groupBox_controller.setTitle("")
        self.pushButton_understand.setText(QCoreApplication.translate("MainWindow", u"Check Progress", None))
        self.pushButton_end.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"Check Answer", None))
        self.pushButton_read.setText(QCoreApplication.translate("MainWindow", u"Select Exercise ", None))
        self.groupBox_setting.setTitle("")
        self.pushButton_restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.pushButton_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_title.setText("")
        self.label_prev_result.setText(QCoreApplication.translate("MainWindow", u"Previous:Correct", None))
    # retranslateUi

