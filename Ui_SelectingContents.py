from PySide6.QtWidgets import (QDialog,
                                QMessageBox)
from PySide6 import QtCore

from ui.select_contents import *

class Ui_SelectingContents(QDialog):
    def __init__(self, parent=None):
        super(Ui_SelectingContents, self).__init__(parent)
        self.ui = Ui_SelectContents()
        self.ui.setupUi(self)
        self.setDesign()

    def initialize(self, contents):
        self.loadContents(contents)

    def setDesign(self):    
        self.ui.treeWidget.setColumnWidth(0, 400)
        self.ui.treeWidget.hideColumn(1)
        self.ui.treeWidget.hideColumn(2)
        self.ui.treeWidget.setColumnWidth(3, 50)
        self.ui.treeWidget.setStyleSheet(
            "QTreeWidget {"
                "alternate-background-color:lightyellow;"
            "}"
            "QTreeWidget::item {"
                "border:1px solid #d9d9d9;"
                "border-top-color:transparent; border-bottom-color:transparent;"
            "}"
            "QTreeWidget::item:hover {"
                "background:qlineargradient(x1:0, y1:0, x2:0, y2:1,"
                    "stop:0 #e7effd, stop:1 #cbdaf1);"
                "border:1px solid #bfcde4;"
            "}"
            "QTreeWidget::item:selected {"
                "background:qlineargradient(x1:0, y1:0, x2:0, y2:1,"
                    "stop:0 #e7effd, stop:1 #cbdaf1);"
                "border:1px solid #567dbc;"
            "}"
            "QTreeWidget::item:selected:active {"
                "background:qlineargradient(x1:0, y1:0, x2:0, y2:1,"
                    "stop:0 #7eb1ff, stop:1 #668dcc);"
            "}"
            "QTreeWidget::item:selected:!active {"
                "background:qlineargradient(x1:0, y1:0, x2:0, y2:1,"
                    "stop:0 #5b8bd8, stop:1 #476faf);"
            "}"
        )

    #index(0始まり)の場所にトップツリーを追加
    def addTopPart(self, index, section, startIndex, endIndex, actualPageNum):
        item = QTreeWidgetItem([section, str(startIndex), str(endIndex), str(actualPageNum)], 0) #第二引数はTypeで0:parent
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsAutoTristate | Qt.ItemIsSelectable)
        #フラッシュカード画面のみ追加
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        if index == 0:
            self.ui.treeWidget.addTopLevelItem(item)
        else:
            self.ui.treeWidget.insertTopLevelItem(index, item)
        self.ui.treeWidget.setCurrentItem(item)
        return self.ui.treeWidget.currentItem()

    def addChildPart(self, parentItem, index, section, startPage, endPage, actualPageNum):
        item = QTreeWidgetItem([section, str(startPage), str(endPage), str(actualPageNum)], 1) #1:child
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsAutoTristate | Qt.ItemIsSelectable)
        #フラッシュカード画面のみ追加
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(0, Qt.Unchecked)
        if index == 0:
            parentItem.addChild(item)
        else:
            parentItem.insertChild(index, item)
        parentItem.setExpanded(True)
        self.ui.treeWidget.setCurrentItem(item)
        return self.ui.treeWidget.currentItem()


    def loadContents(self, contents):
        def recursion(_part, _parentItem, _parts):
            d = { key:_part[key] for key in _part if not 'parts' == key }
            if _parentItem is None:
                item = self.addTopPart(0, d['section'], d['startPage'], d['endPage'], d['actualPageNum'])
            else:
                item = self.addChildPart(_parentItem, 0, d['section'], d['startPage'], d['endPage'], d['actualPageNum'])
            if 'parts' in _part:
                for child in _part['parts']:
                    recursion(child, item, _parts)
        self.ui.treeWidget.clear()
        if contents is None:return
        for topPart in contents:
            recursion(topPart, None, contents)
    
    def getPageList(self):
        def recursion(item):
            _pageList = []
            #チェックされていない場合
            if item.checkState(0) == Qt.Unchecked: return []
            #全チェックされている場合
            if item.checkState(0) == Qt.Checked:
                _page = list(range(int(item.text(1)), int(item.text(2))+1))
                return _page
            #部分チェックされている場合は再帰検索
            if item.childCount() > 0:
                for i in range(item.childCount()):
                    _pageList.extend(recursion(item.child(i)))
            return _pageList
        
        pageList = []
        for ti in range(self.ui.treeWidget.topLevelItemCount()):
            item = self.ui.treeWidget.topLevelItem(ti)
            #カラム0にstateが付く（checked, PartiallyChecked, Unchecked)
            if item.checkState(0) == Qt.Unchecked: continue
            if item.checkState(0) == Qt.Checked:
                _page = list(range(int(item.text(1)), int(item.text(2))+1))
                pageList.extend(_page)
                continue
            #PartiallyCheckedの場合
            if item.childCount() > 0:
                for i in range(item.childCount()):
                    pageList.extend(recursion(item.child(i)))
        return pageList
