# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import (QApplication, 
                                QMainWindow, 
                                QMessageBox)
from ui.kioku import Ui_MainWindow
from Ui_Understanding import *
from Ui_SelectQuestions import *
from Ui_Setting import *
from Ui_Login import *  
from Ui_SelectingContents import *
from CardBase import *
from Database import *
import datetime
from Misc import *

class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    #database connection
    db = None
    #理解度チェックUI
    uiUnderstanding = None
    #問題集選択UI
    uiSelectQuestions= None
    #目次選択UI
    uiContents = None
    #ログイン
    uiLogin = None
    userId = ""
    book_uuid = ""
    #選択された目次のページインデックス（空の場合は全ページが対象）
    pageList= []
    book_title = ""
    cardsMgmt:CardsMgmt = None
    #TODO !!!!!!!!!!!!!!!
    #取組み回目
    count = 0  
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        #databese
        self.db = Database()

        self.login()

        self.initialize()


        self.pushButton_end.clicked.connect(self.close)

        self.pushButton_correct.clicked.connect(self.selectCorrect)
        self.pushButton_easy.clicked.connect(self.selectEasy)
        self.pushButton_wrong.clicked.connect(self.selectWrong)
        self.pushButton_difficult.clicked.connect(self.selectDifficult)
        self.pushButton_skip.clicked.connect(self.selectSkip)

        self.pushButton_understand.clicked.connect(self.understandingLevel)
        self.pushButton_end.clicked.connect(self.end)

        self.pushButton_check.clicked.connect(self.showAnswer)

        self.pushButton_restart.clicked.connect(self.restart)

        self.pushButton_read.clicked.connect(self.showSelectBookUi)
        self.pushButton_setting.clicked.connect(self.showSettingUi)

        self.showSelectBookUi()

    def login(self):
        #ログイン
        self.uiLogin = Ui_Login(self)
        self.uiLogin.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.uiLogin.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.uiLogin.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.uiLogin.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        #ログイン表示
        self.uiLogin.exec()
        #ログイン完了したらユーザIDを取得
        self.userId = self.uiLogin.getUserId()

    #インスタンス生成
    def initialize(self):
        self.comboBox_sorting.addItems(["In Order", "Shuffle"])
        self.comboBox_layout.addItems(["up and down", "side by side"])
        self.comboBox_layout.currentIndexChanged.connect(self.comboLayoutChanged)
        #UI
        #理解度確認画面
        self.uiUnderstanding = Ui_Understading(self)
        #問題集選択画面
        self.uiSelectQuestions = Ui_SelectQuestions(self)
        self.uiSelectQuestions.accepted.connect(self.selectedBookOk)
        self.uiSelectQuestions.rejected.connect(self.selectedBookCancel)
        #目次選択画面
        self.uiContents = Ui_SelectingContents(self)
        self.uiContents.accepted.connect(self.selectedContentsOk)
        #設定画面
        self.uiSetting = Ui_Setting(self)
        self.uiSetting.accepted.connect(self.settingOk)
        self.uiSetting.rejected.connect(self.settingCancel)

        #設定をユーザIDで読込み更新する
        self.uiSetting.setUserId(self.userId)
        self.uiSetting.update()
        self.updateInfo()
    
    #１）問題集選択画面表示
    def showSelectBookUi(self):
        self.uiSelectQuestions.updateBookTitles()
        self.uiSelectQuestions.show()

    #２）問題集を選択してOKを押したら呼ばれる（目次画面表示）
    def selectedBookOk(self):
        book_uuid, book_title = self.uiSelectQuestions.getSelectedBookUuidAndTitle()
        if book_uuid is None:
            QMessageBox.information(None, "Information", "Select exercise book", QMessageBox.Yes)  
            self.uiSelectQuestions.show()
            return
        self.book_uuid = book_uuid
        self.book_title = book_title
        #目次情報読込み
        contents = self.db.readContents(self.userId, self.book_uuid)
        if contents is None:
            self.selectedContentsOk()
            return
        self.uiContents.loadContents(contents)
        self.uiContents.show()

    #３）目次を選択してOKを押したら呼ばれる
    def selectedContentsOk(self):
        pageList = self.uiContents.getPageList()
        #目次が存在しないもしくは選択されていない場合は全ページが対象
        if pageList is None:
            pageList = []
        self.pageList = pageList
        self.label_title.setText(self.book_title)
        self.showCard(self.book_uuid, self.pageList)
        #理解度確認画面生成
        setting = self.uiSetting.getSetting()
        self.uiUnderstanding.initialize(self.book_uuid, setting)
        self.uiUnderstanding.update(setting, self.pageList)

    def selectedBookCancel(self):
        if self.book_uuid is None or self.book_uuid == '':
            # QMessageBox.information(None, "Information", "問題集を選択してください", QMessageBox.Yes) 
            # self.uiSelectQuestions.show()
            return
        print("Cancelled selecting a book")

    def showSettingUi(self):
        self.uiSetting.show()

    def settingOk(self):
        self.uiSetting.clickOk()
        self.updateInfo()

    def settingCancel(self):
        print("Cancelled settingCancel")

    def selectCorrect(self):
        print("selectCorrect")
        self.writeResult("correct", "standard")
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)
    def selectEasy(self):
        print("selectEasy")
        self.writeResult("correct", "easy")
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)
    def selectWrong(self):
        print("selectWrong")
        self.writeResult("wrong", "miss")
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)
    def selectDifficult(self):
        print("selectDifficult")
        self.writeResult("wrong", "difficult")
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)
    def selectSkip(self):
        print("selectSkip")
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)

    
    def showAnswer(self):
        self.cardsMgmt.showAnswer()
    
    def end(self):
        print("end")


    def showCard(self, book_uuid, pageList):
        #cards(問題カード)、ページ画像(pagesQuestions,pagesAnswers)を読込みカード管理インスタンスを作成
        studyCount = self.db.getMaxCount(book_uuid, pageList)
        cards = self.db.readAreas(book_uuid, pageList, studyCount)
        if len(cards) == 0: 
            QMessageBox.information(None, "Information", "Exercise is not set", QMessageBox.Yes)
            return
        imageFolder = [card['q.image_folder'] for card in cards if card['q.image_folder'] is not None]
        pagesQuestions = Misc.getFilePathList(imageFolder[0], 'jpg')
        imageFolder = [card['a.image_folder'] for card in cards if card['a.image_folder'] is not None]
        pagesAnswers = Misc.getFilePathList(imageFolder[0], 'jpg')
        self.cardsMgmt = CardsMgmt(self.graphicsView_page, self.graphicsView_question, self.graphicsView_answer, self.uiSetting, self.restart)
        self.cardsMgmt.setInfo(cards, pagesQuestions, pagesAnswers)
        self.comboLayoutChanged()
        #0番目のカードを表示
        self.cardsMgmt.setSorting("in_order" if self.comboBox_sorting.currentIndex() == 0 else "shuffle")
        self.cardsMgmt.initializeCardIndex()
        prevResultLabel = self.cardsMgmt.nextQuestion()
        self.label_prev_result.setText(prevResultLabel)

    # 最後まで解答した場合(cb_flag="complete")
    # 初めからボタン(cb_flag="")を押したとき
    # 現時点で取り組むカードがない("noTodoCards")場合に呼ばれる
    def restart(self, cb_flag=""):
        if cb_flag == "complete":
            #理解度が100%になったか確認初めから行うか確認
            result = QtWidgets.QMessageBox.question(None,"Confirmation", "You finished all exercises.\n Do you want to restart?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.No:
                return
        if cb_flag == "noTodoCards":
            QMessageBox.information(None, "Information", "There is no outstanding exercise.\nUpdate waiting period at settting if needed.", QMessageBox.Yes)
            self.book_uuid = ""
            self.uiSelectQuestions.show()
            return
        #cards(問題カード)、ページ画像(pagesQuestions,pagesAnswers)を読込みカード管理インスタンスを作成
        studyCount = self.db.getMaxCount(self.book_uuid, self.pageList)
        cards = self.db.readAreas(self.book_uuid, self.pageList, studyCount)
        if len(cards) == 0: return
        if self.checkPerfectUnderstand(cards):
            QMessageBox.information(None, "Information", "The progress of understanding reached 100%!", QMessageBox.Yes)
        pagesQuestions = Misc.getFilePathList(cards[0]['q.image_folder'], 'jpg')
        pagesAnswers = Misc.getFilePathList(cards[0]['a.image_folder'], 'jpg')
        self.cardsMgmt.setInfo(cards, pagesQuestions, pagesAnswers)
        self.cardsMgmt.setSorting("in_order" if self.comboBox_sorting.currentIndex() == 0 else "shuffle")
        self.cardsMgmt.initializeCardIndex()
        self.cardsMgmt.nextQuestion()

    #全てのカードがEasyになっているか確認
    def checkPerfectUnderstand(self, cards):
        for card in cards:
            if card['r.level'] != "easy":
                return False
        return True

    def comboLayoutChanged(self):
        self.cardsMgmt.setLayout(self.comboBox_layout.currentText())
    

    def resizeEvent(self, event) -> None:
        windowWidth = event.size().width()
        windowHeight = event.size().height()
        print("new window size:", windowWidth, windowHeight)
        space = 10
        viewWidthPage = (windowWidth - 10*4) / 3
        viewWidthQuestion = viewWidthPage * (1.4)
        viewWidthAnswer = viewWidthPage * (0.6)
        #groupBox_controllerの上に合わせる下辺
        bottom1 = self.groupBox_controller.height()+space*2
        #pushButton_checkの上に合わせる下辺
        bottom2 = self.pushButton_check.height() + self.groupBox_check.height() + self.groupBox_controller.height()+space*4
        y = 0
        #問題集タイトル
        self.label_title.setGeometry(space*2, space, viewWidthPage-space, self.label_title.height())
        y = space + self.pushButton_read.height() + space
        self.graphicsView_page.setGeometry(space, y, viewWidthPage, windowHeight - y - bottom1)
        self.graphicsView_question.setGeometry(space*2+viewWidthPage, y, viewWidthQuestion, windowHeight - y - bottom2)
        self.graphicsView_answer.setGeometry(space*3+viewWidthPage+viewWidthQuestion, y, viewWidthAnswer, windowHeight - y - bottom2)
        self.label_question.setGeometry(space*2+viewWidthPage, y-self.label_question.height()-space, self.label_question.width(), self.label_question.height())
        self.comboBox_layout.setGeometry(self.label_question.x()+self.label_question.width()+space*5, y-self.label_question.height()-space-5, self.comboBox_layout.width(), self.comboBox_layout.height())
        self.label_answer.setGeometry(space*3+viewWidthPage+viewWidthQuestion, y-self.label_answer.height()-space, self.label_answer.width(), self.label_answer.height())
        delta_x = (windowWidth-viewWidthPage-viewWidthAnswer-space*3)/2-self.pushButton_check.width()/2
        # delta_x = (windowWidth-viewWidthPage-space*3)/2-self.pushButton_check.width()/2
        self.pushButton_check.setGeometry(viewWidthPage+space*2+delta_x, windowHeight-bottom2+space, self.pushButton_check.width(), self.pushButton_check.height())
        #前回結果ラベル
        self.label_prev_result.setGeometry(self.pushButton_check.x()+self.pushButton_check.width()+space*5, windowHeight-bottom2+space, self.label_prev_result.width(), self.label_prev_result.height())
        delta_x = (windowWidth-viewWidthPage-viewWidthAnswer-space*3)/2-self.groupBox_check.width()/2
        # delta_x = (windowWidth-viewWidthPage-space*3)/2-self.groupBox_check.width()/2
        self.groupBox_check.setGeometry(viewWidthPage+space*2+delta_x , windowHeight-bottom2+space+self.pushButton_check.height()+space, self.groupBox_check.width(), self.groupBox_check.height())
        self.groupBox_controller.setGeometry(windowWidth-space-self.groupBox_controller.width(), windowHeight-bottom1+space, self.groupBox_controller.width(), self.groupBox_controller.height())
        self.groupBox_setting.setGeometry(viewWidthPage+space*2+delta_x, windowHeight-bottom1+space, self.groupBox_setting.width(), self.groupBox_setting.height())
        #問題集選択/設定ボタン
        self.pushButton_read.setGeometry(space*3, windowHeight-bottom1+space*2, self.pushButton_read.width(), self.pushButton_read.height())
        self.pushButton_setting.setGeometry(space*6+ self.pushButton_read.width(), windowHeight-bottom1+space*2, self.pushButton_setting.width(), self.pushButton_setting.height())

        if self.cardsMgmt is not None:
            self.cardsMgmt.zoomFitAll()
        
        super().resizeEvent(event)

    def updateInfo(self):
        setting = self.uiSetting.getSetting()
        p = setting['period']
        self.label_standard.setText(str(p['standard_num'])+p['standard_unit'])
        self.label_easy.setText(str(p['easy_num'])+p['easy_unit'])
        self.label_miss.setText(str(p['miss_num'])+p['miss_unit'])
        self.label_difficult.setText(str(p['difficult_num'])+p['difficult_unit'])

    def writeResult(self, result, level):
        currentCard = self.cardsMgmt.getCurrentCard()
        now = datetime.datetime.now()
        nowStr = now.strftime('%Y-%m-%d %H:%M:%S.%f')
        self.db.writeRecords(self.count, currentCard['q.area_uuid'], nowStr, result, level, currentCard['q.book_uuid'])    

    def understandingLevel(self):
        self.uiUnderstanding.showMaximized()
        self.uiUnderstanding.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        self.uiUnderstanding.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.uiUnderstanding.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.uiUnderstanding.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, True)
        setting = self.uiSetting.getSetting()
        if self.uiUnderstanding.update(setting, self.pageList) == False:
            QMessageBox.information(None, "Information", "Select Exercise book.", QMessageBox.Ok)
            return
        self.uiUnderstanding.show()


if __name__ == '__main__':
    argvs = sys.argv
    app = QApplication(argvs)
    ui = Ui_MainWindow()
    ui.showMaximized()
    ui.show()
    sys.exit(app.exec())
