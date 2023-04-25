# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (QDialog,
                                QMessageBox)
from ui.select_questions import *
from InfoMgmt import *
from Database import *

class Ui_SelectQuestions(QDialog):
    #database connection
    db = None
    infoMgmtQuestions:InfoMgmtBase = None
    infoMgmtAnswers:InfoMgmtBase = None
    #["book_uuid", "タイトル"]
    titlesInfo = []

    def __init__(self, parent=None):
        super(Ui_SelectQuestions, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #databese
        self.db = Database()

        #json設定ファイル管理
        if self.infoMgmtQuestions is None:
            self.infoMgmtQuestions = InfoMgmtBase()
        if self.infoMgmtAnswers is None:
            self.infoMgmtAnswers = InfoMgmtBase()

        self.ui.pushButton_read.clicked.connect(self.selectfile)

        self.updateBookTitles()

        #for Debug
        # jsonFileQuestions = r'C:\coding\pyside\image_file\教科書ワーク 社会歴史\questions_book.json'
        # jsonFileAnswers = r'C:\coding\pyside\image_file\教科書ワーク 社会歴史\answers_book.json'


    def updateBookTitles(self):
        self.ui.listWidget_select_questions.clear()
        self.titlesInfo = self.db.getBookTitles()
        if len(self.titlesInfo) == 0:
            QMessageBox.information(None, "Information", "Import an exercise book.", QMessageBox.Yes)
            return
        for uuid, title in self.titlesInfo:
            self.ui.listWidget_select_questions.addItem(title)

    def selectfile(self):
        questionFilePath = Misc.selectFileDialog("*.json")
        if questionFilePath == "" or questionFilePath == None: return
        folder = Misc.extractFolder(questionFilePath)
        questionFileName = Misc.extractFileName(questionFilePath)
        answersFileName = questionFileName.replace('questions', 'answers')
        answersFilePath = folder + "/" + answersFileName
        if answersFileName == questionFileName or Misc.isExistPath(answersFilePath) == False:
            QMessageBox.information(None, "Information", "Answers cabnot be found. Please save answers information in the same folder of the exercise information.", QMessageBox.Yes)
            return

        #指定されたJSONファイルを読込みDBに書き込む
        self.infoMgmtQuestions.loadFromJson(questionFilePath)
        questionsBook = self.infoMgmtQuestions.getBooks()
        bookUuid = self.infoMgmtQuestions.getUuid()
        self.db.deleteBook("questions",bookUuid)
        self.db.writeJsonToDb("questions", questionsBook)

        self.infoMgmtAnswers.loadFromJson(answersFilePath)
        answersBook = self.infoMgmtAnswers.getBooks()
        bookUuid = self.infoMgmtAnswers.getUuid()
        self.db.deleteBook("answers",bookUuid)
        self.db.writeJsonToDb("answers", answersBook)

    def getSelectedBookUuidAndTitle(self):
        row = self.ui.listWidget_select_questions.currentRow()
        #選択されていない場合
        if row < 0:
            return None
        return self.titlesInfo[row][0], self.titlesInfo[row][1]
