# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_contents.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHeaderView, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_SelectContents(object):
    def setupUi(self, SelectContents):
        if not SelectContents.objectName():
            SelectContents.setObjectName(u"SelectContents")
        SelectContents.resize(518, 403)
        self.gridLayoutWidget = QWidget(SelectContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 501, 331))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.gridLayoutWidget)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(SelectContents)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(340, 360, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.retranslateUi(SelectContents)
        self.buttonBox.accepted.connect(SelectContents.accept)

        QMetaObject.connectSlotsByName(SelectContents)
    # setupUi

    def retranslateUi(self, SelectContents):
        SelectContents.setWindowTitle(QCoreApplication.translate("SelectContents", u"Select Contents", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("SelectContents", u"Page Number", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SelectContents", u"End index", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SelectContents", u"Start index", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SelectContents", u"Section", None));
    # retranslateUi

