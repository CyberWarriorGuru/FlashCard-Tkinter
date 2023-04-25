# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'understanding_level.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGraphicsView,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1058, 676)
        font = QFont()
        font.setFamilies([u"\u30e1\u30a4\u30ea\u30aa"])
        font.setPointSize(20)
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.graphicsView_graph = QGraphicsView(Dialog)
        self.graphicsView_graph.setObjectName(u"graphicsView_graph")
        self.graphicsView_graph.setGeometry(QRect(40, 160, 991, 451))
        self.pushButton_close = QPushButton(Dialog)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(410, 620, 91, 41))
        self.pushButton_close.setStyleSheet(u"font: 12pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(30, 20, 851, 41))
        self.label_title.setStyleSheet(u"font: 700 20pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.groupBox_legend = QGroupBox(Dialog)
        self.groupBox_legend.setObjectName(u"groupBox_legend")
        self.groupBox_legend.setGeometry(QRect(850, 50, 201, 101))
        self.groupBox_legend.setStyleSheet(u"background-color: rgb(255, 224, 199);")
        self.label_6 = QLabel(self.groupBox_legend)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 221, 21))
        self.label_7 = QLabel(self.groupBox_legend)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 50, 211, 21))
        self.label_8 = QLabel(self.groupBox_legend)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 70, 171, 21))
        self.label_9 = QLabel(self.groupBox_legend)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 171, 21))
        self.comboBox_graph_x = QComboBox(Dialog)
        self.comboBox_graph_x.setObjectName(u"comboBox_graph_x")
        self.comboBox_graph_x.setGeometry(QRect(40, 620, 121, 31))
        self.comboBox_graph_x.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.groupBox_overview = QGroupBox(Dialog)
        self.groupBox_overview.setObjectName(u"groupBox_overview")
        self.groupBox_overview.setGeometry(QRect(40, 70, 791, 81))
        self.groupBox_overview.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.label_understand_per = QLabel(self.groupBox_overview)
        self.label_understand_per.setObjectName(u"label_understand_per")
        self.label_understand_per.setGeometry(QRect(540, 40, 251, 31))
        self.label_understand_per.setStyleSheet(u"font: 700 18pt \"\u30e1\u30a4\u30ea\u30aa\";\n"
"color: rgb(0, 170, 255);")
        self.label_5 = QLabel(self.groupBox_overview)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 40, 211, 31))
        self.label_work_per = QLabel(self.groupBox_overview)
        self.label_work_per.setObjectName(u"label_work_per")
        self.label_work_per.setGeometry(QRect(240, 40, 81, 31))
        self.label_work_per.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label = QLabel(self.groupBox_overview)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 31))
        self.label_question_num = QLabel(self.groupBox_overview)
        self.label_question_num.setObjectName(u"label_question_num")
        self.label_question_num.setGeometry(QRect(180, 10, 51, 31))
        self.label_question_num.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_3 = QLabel(self.groupBox_overview)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 10, 161, 31))
        self.label_work_num = QLabel(self.groupBox_overview)
        self.label_work_num.setObjectName(u"label_work_num")
        self.label_work_num.setGeometry(QRect(180, 40, 51, 31))
        self.label_work_num.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_2 = QLabel(self.groupBox_overview)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 161, 31))
        self.label_correct_num = QLabel(self.groupBox_overview)
        self.label_correct_num.setObjectName(u"label_correct_num")
        self.label_correct_num.setGeometry(QRect(470, 10, 41, 31))
        self.label_correct_num.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_correct_per = QLabel(self.groupBox_overview)
        self.label_correct_per.setObjectName(u"label_correct_per")
        self.label_correct_per.setGeometry(QRect(520, 10, 81, 31))
        self.label_correct_per.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.groupBox_count = QGroupBox(Dialog)
        self.groupBox_count.setObjectName(u"groupBox_count")
        self.groupBox_count.setGeometry(QRect(830, 620, 181, 51))
        self.comboBox = QComboBox(self.groupBox_count)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 121, 31))
        self.comboBox.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")
        self.label_work_max = QLabel(self.groupBox_count)
        self.label_work_max.setObjectName(u"label_work_max")
        self.label_work_max.setGeometry(QRect(140, 10, 41, 31))
        self.label_work_max.setStyleSheet(u"font: 14pt \"\u30e1\u30a4\u30ea\u30aa\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Progress", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">\u6559\u79d1\u66f8\u30ef\u30fc\u30af</span></p></body></html>", None))
        self.groupBox_legend.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Dotted Black: Remains</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Blue Line: Not Understanding</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Red Line: Difficult</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Dotted Red: Planned</span></p></body></html>", None))
        self.groupBox_overview.setTitle("")
        self.label_understand_per.setText(QCoreApplication.translate("Dialog", u"75%(Remain 25%)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Understanding Progress:</span></p></body></html>", None))
        self.label_work_per.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">(33%)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Num of Exercises:</span></p></body></html>", None))
        self.label_question_num.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">100</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Num of Corrects:</span></p></body></html>", None))
        self.label_work_num.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">30</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Num of Answers:</span></p></body></html>", None))
        self.label_correct_num.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:700;\">25</span></p></body></html>", None))
        self.label_correct_per.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">(75%)</span></p></body></html>", None))
        self.groupBox_count.setTitle("")
        self.label_work_max.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">/3</span></p></body></html>", None))
    # retranslateUi

