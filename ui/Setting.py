# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QDialogButtonBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog_setting(object):
    def setupUi(self, Dialog_setting):
        if not Dialog_setting.objectName():
            Dialog_setting.setObjectName(u"Dialog_setting")
        Dialog_setting.resize(910, 544)
        self.buttonBox = QDialogButtonBox(Dialog_setting)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(540, 490, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(Dialog_setting)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 861, 462))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_miss = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_miss.setObjectName(u"spinBox_miss")
        self.spinBox_miss.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_miss.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_miss, 5, 2, 1, 1)

        self.spinBox_standard = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_standard.setObjectName(u"spinBox_standard")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_standard.sizePolicy().hasHeightForWidth())
        self.spinBox_standard.setSizePolicy(sizePolicy)
        self.spinBox_standard.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_standard.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_standard, 2, 2, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 12pt \"Yu Gothic UI\";")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.spinBox_easy = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_easy.setObjectName(u"spinBox_easy")
        self.spinBox_easy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_easy.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_easy, 4, 2, 1, 1)

        self.comboBox_easy_unit = QComboBox(self.verticalLayoutWidget)
        self.comboBox_easy_unit.addItem("")
        self.comboBox_easy_unit.addItem("")
        self.comboBox_easy_unit.addItem("")
        self.comboBox_easy_unit.addItem("")
        self.comboBox_easy_unit.setObjectName(u"comboBox_easy_unit")

        self.gridLayout.addWidget(self.comboBox_easy_unit, 4, 3, 1, 1)

        self.comboBox_miss_unit = QComboBox(self.verticalLayoutWidget)
        self.comboBox_miss_unit.addItem("")
        self.comboBox_miss_unit.addItem("")
        self.comboBox_miss_unit.addItem("")
        self.comboBox_miss_unit.addItem("")
        self.comboBox_miss_unit.setObjectName(u"comboBox_miss_unit")

        self.gridLayout.addWidget(self.comboBox_miss_unit, 5, 3, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.spinBox_difficult = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_difficult.setObjectName(u"spinBox_difficult")
        self.spinBox_difficult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_difficult.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_difficult, 6, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 4, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 6, 4, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        self.comboBox_standard_unit = QComboBox(self.verticalLayoutWidget)
        self.comboBox_standard_unit.addItem("")
        self.comboBox_standard_unit.addItem("")
        self.comboBox_standard_unit.addItem("")
        self.comboBox_standard_unit.addItem("")
        self.comboBox_standard_unit.setObjectName(u"comboBox_standard_unit")

        self.gridLayout.addWidget(self.comboBox_standard_unit, 2, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 4, 1, 1)

        self.comboBox_difficult_unit = QComboBox(self.verticalLayoutWidget)
        self.comboBox_difficult_unit.addItem("")
        self.comboBox_difficult_unit.addItem("")
        self.comboBox_difficult_unit.addItem("")
        self.comboBox_difficult_unit.addItem("")
        self.comboBox_difficult_unit.setObjectName(u"comboBox_difficult_unit")

        self.gridLayout.addWidget(self.comboBox_difficult_unit, 6, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.pushButton_reset = QPushButton(self.verticalLayoutWidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.gridLayout.addWidget(self.pushButton_reset, 0, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_wed = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_wed.setObjectName(u"checkBox_wed")

        self.gridLayout_2.addWidget(self.checkBox_wed, 5, 3, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 12pt \"Yu Gothic UI\";")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.checkBox_sat = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_sat.setObjectName(u"checkBox_sat")

        self.gridLayout_2.addWidget(self.checkBox_sat, 5, 6, 1, 1)

        self.checkBox_fri = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_fri.setObjectName(u"checkBox_fri")

        self.gridLayout_2.addWidget(self.checkBox_fri, 5, 5, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.checkBox_tue = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_tue.setObjectName(u"checkBox_tue")

        self.gridLayout_2.addWidget(self.checkBox_tue, 5, 2, 1, 1)

        self.spinBox_perday = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_perday.setObjectName(u"spinBox_perday")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_perday.sizePolicy().hasHeightForWidth())
        self.spinBox_perday.setSizePolicy(sizePolicy1)
        self.spinBox_perday.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_perday.setMaximum(999)

        self.gridLayout_2.addWidget(self.spinBox_perday, 3, 1, 1, 1)

        self.checkBox_thu = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_thu.setObjectName(u"checkBox_thu")

        self.gridLayout_2.addWidget(self.checkBox_thu, 5, 4, 1, 1)

        self.dateEdit_startdate = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_startdate.setObjectName(u"dateEdit_startdate")

        self.gridLayout_2.addWidget(self.dateEdit_startdate, 12, 1, 1, 1)

        self.checkBox_mon = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_mon.setObjectName(u"checkBox_mon")

        self.gridLayout_2.addWidget(self.checkBox_mon, 5, 1, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 12, 0, 1, 1)

        self.checkBox_sun = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_sun.setObjectName(u"checkBox_sun")

        self.gridLayout_2.addWidget(self.checkBox_sun, 5, 7, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 8, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_rewards_pt = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_rewards_pt.setObjectName(u"spinBox_rewards_pt")
        sizePolicy1.setHeightForWidth(self.spinBox_rewards_pt.sizePolicy().hasHeightForWidth())
        self.spinBox_rewards_pt.setSizePolicy(sizePolicy1)
        self.spinBox_rewards_pt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_rewards_pt.setMaximum(999)

        self.gridLayout_3.addWidget(self.spinBox_rewards_pt, 1, 1, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 700 12pt \"Yu Gothic UI\";")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog_setting)
        self.buttonBox.accepted.connect(Dialog_setting.accept)
        self.buttonBox.rejected.connect(Dialog_setting.reject)

        QMetaObject.connectSlotsByName(Dialog_setting)
    # setupUi

    def retranslateUi(self, Dialog_setting):
        Dialog_setting.setWindowTitle(QCoreApplication.translate("Dialog_setting", u"Setting", None))
        self.label.setText(QCoreApplication.translate("Dialog_setting", u"Waiting period for looking back", None))
        self.comboBox_easy_unit.setItemText(0, QCoreApplication.translate("Dialog_setting", u"weeks", None))
        self.comboBox_easy_unit.setItemText(1, QCoreApplication.translate("Dialog_setting", u"days", None))
        self.comboBox_easy_unit.setItemText(2, QCoreApplication.translate("Dialog_setting", u"hours", None))
        self.comboBox_easy_unit.setItemText(3, QCoreApplication.translate("Dialog_setting", u"minutes", None))

        self.comboBox_miss_unit.setItemText(0, QCoreApplication.translate("Dialog_setting", u"weeks", None))
        self.comboBox_miss_unit.setItemText(1, QCoreApplication.translate("Dialog_setting", u"days", None))
        self.comboBox_miss_unit.setItemText(2, QCoreApplication.translate("Dialog_setting", u"hours", None))
        self.comboBox_miss_unit.setItemText(3, QCoreApplication.translate("Dialog_setting", u"minutes", None))

        self.label_3.setText(QCoreApplication.translate("Dialog_setting", u"Correct(Easy)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_setting", u"Correct(Not difficut)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_setting", u"Wrong(Mistake)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_setting", u"Wrong(Difficut)", None))
        self.comboBox_standard_unit.setItemText(0, QCoreApplication.translate("Dialog_setting", u"weeks", None))
        self.comboBox_standard_unit.setItemText(1, QCoreApplication.translate("Dialog_setting", u"days", None))
        self.comboBox_standard_unit.setItemText(2, QCoreApplication.translate("Dialog_setting", u"hours", None))
        self.comboBox_standard_unit.setItemText(3, QCoreApplication.translate("Dialog_setting", u"minutes", None))

        self.comboBox_difficult_unit.setItemText(0, QCoreApplication.translate("Dialog_setting", u"weeks", None))
        self.comboBox_difficult_unit.setItemText(1, QCoreApplication.translate("Dialog_setting", u"days", None))
        self.comboBox_difficult_unit.setItemText(2, QCoreApplication.translate("Dialog_setting", u"hours", None))
        self.comboBox_difficult_unit.setItemText(3, QCoreApplication.translate("Dialog_setting", u"minutes", None))

        self.pushButton_reset.setText(QCoreApplication.translate("Dialog_setting", u"Reset progress", None))
        self.checkBox_wed.setText(QCoreApplication.translate("Dialog_setting", u"Wed", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_setting", u"Planning", None))
        self.checkBox_sat.setText(QCoreApplication.translate("Dialog_setting", u"Sat", None))
        self.checkBox_fri.setText(QCoreApplication.translate("Dialog_setting", u"Fri", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_setting", u"Number of exercises per day", None))
        self.checkBox_tue.setText(QCoreApplication.translate("Dialog_setting", u"\u706b", None))
        self.checkBox_thu.setText(QCoreApplication.translate("Dialog_setting", u"Thu", None))
        self.checkBox_mon.setText(QCoreApplication.translate("Dialog_setting", u"Mon", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_setting", u"Start day of exercise", None))
        self.checkBox_sun.setText(QCoreApplication.translate("Dialog_setting", u"Sun", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_setting", u"Day of exercise", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_setting", u"pt", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_setting", u"Points", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_setting", u"Rewards", None))
    # retranslateUi

