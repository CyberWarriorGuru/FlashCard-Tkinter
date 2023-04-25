# -*- coding: utf-8 -*-

from PySide6.QtWidgets import (QDialog,
                                QGraphicsScene)
from PySide6.QtCore import Qt, QRectF
import pyqtgraph
from ui.understanding_level import Ui_Dialog
from Database import *
import datetime

class Ui_Understading(QDialog):
    db:Database = None
    bookUuid = ""
    scale = 1.0
    setting = None
    #選択した目次のページリスト
    pageList = []
    def __init__(self, parent=None):
        super(Ui_Understading, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_close.clicked.connect(self.close)
        self.pageList = list()
        
        #databese
        self.db = Database()

    def initialize(self, bookUuid, setting):
        self.bookUuid = bookUuid
        self.setting = setting
        title = self.db.getBookTitleByUuid(self.bookUuid)
        self.ui.label_title.setText(title)
        self.ui.comboBox_graph_x.clear()
        self.ui.comboBox_graph_x.addItems(["X:Time","X:Count"])
        self.ui.comboBox_graph_x.currentIndexChanged.connect(self.onComboGraphXChnaged)
        
    def updateScreenInfo(self, numOfQuesions,numOfWorked, numOfCorrect, numOfUnderstand):
        if numOfQuesions != 0:
            perWork = round(numOfWorked / numOfQuesions * 100.0)
            perUnderstand = round(numOfUnderstand / numOfQuesions * 100.0)
        else:
            perWork = 0
            perUnderstand = 0
        if perWork != 0:
            perCorrct = round(numOfCorrect / numOfWorked * 100.0)
        else:
            perCorrct = 0
        self.ui.label_question_num.setText(str(numOfQuesions)+".")
        self.ui.label_work_num.setText(str(numOfWorked)+".")
        self.ui.label_correct_num.setText(str(numOfCorrect)+".")
        self.ui.label_work_per.setText("(" + str(perWork)+"%)")
        self.ui.label_correct_per.setText("(" + str(perCorrct)+"%)")
        self.ui.label_understand_per.setText(str(perUnderstand)+"%(Remain"+str(100-perUnderstand)+"%)")
        #回目を初期化（1始まりの表記にする）
        self.ui.comboBox.clear()
        maxCount = self.db.getMaxCount(self.bookUuid, self.pageList)
        self.ui.label_work_max.setText(" / " + str(maxCount+1) + "回")
        for i in range(maxCount+1):
            self.ui.comboBox.addItem(str(i+1))

    def update(self, setting, pageList):
        if self.bookUuid == '' or self.bookUuid is None:
            return False
        if self.db is None:
            print("Db is None. Error!!")
            return False
        if setting == "":
            setting = self.setting
        else:
            self.setting = setting
        self.pageList = pageList
        #全.題数
        numOfQuestions = self.db.getNumOfQuestions(self.bookUuid, pageList)
        #取組み結果
        results = self.db.getResultByDate(self.bookUuid, pageList)
        todo = []
        notUnderstand = []
        difficult = []
        plan = []
        x = []
        plan_x = [] #計画線のX軸
        numOfTodo = numOfQuestions
        numOfUndStn = numOfQuestions
        numOfDiff = 0
        numOfCorrect = 0
        numOfTodoPlan = numOfQuestions
        status = [{'uuid':'', 'level':''}]
        x_count = 0
        # if len(results) <= 0:
        #     return

        #計画線（個別に作成）
        if self.ui.comboBox_graph_x.currentText() == "X:Time":
            start = self.timestamp(self.setDatetime(setting['plan']['start']), "day")
            today = self.timestamp(datetime.datetime.now(), "day")
            for _x in range(start, today+86400, 86400):
                if numOfTodoPlan > 0:
                    numOfTodoPlan -= setting['plan']['number']
                    numOfTodoPlan = numOfTodoPlan if numOfTodoPlan > 0 else 0
                else:
                    break
                plan_x.append(_x)
                plan.append(numOfTodoPlan)

        for r in results:
            #label = ['count', 'question_area_uuid', 'datetime', 'result', 'level', 'book_uuid', 'page_number]
            #X軸を回数か時間かによって変える
            # print(self.ui.comboBox_graph_x.currentText())
            if self.ui.comboBox_graph_x.currentText() == "X:Time":
                _time = self.timestamp(r['datetime'], 'day')
                x.append(_time)
            elif self.ui.comboBox_graph_x.currentText() == "X:Count":
                x.append(x_count)
                x_count += 1
            else:
                print("error")

            #すでに取り組んだ.題か確認
            check = self.isExist(status, r['question_area_uuid'])
            if check is None:
                #初めての.題の場合
                #消化数を更新
                numOfTodo = numOfTodo - 1
                todo.append(numOfTodo)
                #理解残を減少
                if r['level'] == 'easy':
                    numOfUndStn = numOfUndStn -1
                notUnderstand.append(numOfUndStn)
                #未理解を増加
                if r['level'] == 'difficult':
                    numOfDiff = numOfDiff + 1
                difficult.append(numOfDiff)
                status.append({'uuid':r['question_area_uuid'], 'level':r['level']})
                if r['result'] == 'correct':
                    numOfCorrect += 1
            else:
                if check == 'standard':
                    #消化数はそのまま
                    todo.append(numOfTodo)
                    #理解残を減少
                    if r['level'] == 'easy':
                        numOfUndStn = numOfUndStn -1
                    notUnderstand.append(numOfUndStn)
                    #未理解を増加
                    if r['level'] == 'difficult':
                        numOfDiff = numOfDiff + 1
                    difficult.append(numOfDiff)
                if check == 'easy':
                    if r['level'] == 'easy':
                        #理解残はそのまま
                        notUnderstand.append(numOfUndStn)
                    else:
                        #理解残を増加（戻す）
                        numOfUndStn += 1
                        notUnderstand.append(numOfUndStn)
                    #消化数はそのまま
                    todo.append(numOfTodo)
                    #未理解を増加
                    if r['level'] == 'difficult':
                        numOfDiff = numOfDiff + 1
                    difficult.append(numOfDiff)
                if check == 'miss':
                    #消化数はそのまま
                    todo.append(numOfTodo)
                    #理解残を減少
                    if r['level'] == 'easy':
                        numOfUndStn = numOfUndStn -1
                    notUnderstand.append(numOfUndStn)
                    #未理解を増加
                    if r['level'] == 'difficult':
                        numOfDiff = numOfDiff + 1
                    difficult.append(numOfDiff)
                if check == 'difficult':
                    #消化数はそのまま
                    todo.append(numOfTodo)
                    #理解残を減少
                    if r['level'] == 'easy':
                        numOfUndStn = numOfUndStn -1
                    notUnderstand.append(numOfUndStn)
                    #Difficultでなければ未理解を減少。Difficultであればそのまま
                    if r['level'] != 'difficult':
                        numOfDiff = numOfDiff - 1
                    difficult.append(numOfDiff)
                if (check == 'miss' or check == 'diffcult') and r['result'] == 'correct':
                    numOfCorrect += 1
                exist = [record for record in status if record.get('uuid')==r['question_area_uuid']]
                if len(exist) == 0:
                    print("error!!!!!!")
                exist[0]['level'] = r['level']
        #画面の指標データを更新
        self.updateScreenInfo(numOfQuestions, numOfQuestions - numOfTodo, numOfCorrect, numOfQuestions - numOfUndStn)
        #グラフを描画
        self.drawGraph(todo, notUnderstand, difficult, x, plan, plan_x)
        return True

    def isExist(self, status, uuid):
        for s in status:
            if s['uuid'] == uuid:
                return s['level']
        return None

    def drawGraph(self, todo, notUnderstand, difficult, x, plan, plan_x):

        # print("x:", x)
        # print("plan_x:", plan_x)
        scene = QGraphicsScene()
        self.ui.graphicsView_graph.setScene(scene)

        self.plotWdgt = pyqtgraph.PlotWidget(
            axisItems = {'bottom':pyqtgraph.DateAxisItem(orientation='bottom')}
        )
        self.plotWdgt.setBackground('w')
        self.plotWdgt.showGrid(x=True, y=True)
        #取組み数
        penWorked = pyqtgraph.mkPen(color=(3, 32, 93), width=2, style=Qt.DashLine)
        penNotUnderstanding = pyqtgraph.mkPen(color=(0, 170, 255), width=5) #(151, 236, 255)
        penDifficult = pyqtgraph.mkPen(color=(255, 116, 35), width=5)
        penPlan = pyqtgraph.mkPen(color=(200, 0, 0), width=2, style=Qt.DashLine)

        # axis = pyqtgraph.DateAxisItem()
        plot_item = self.plotWdgt.plot(x, todo, name="Remains", pen=penWorked, symbol='o', symbolSize=5, symbolPen=(0,0,0), symbolBrush=(3, 32, 93))
        plot_item = self.plotWdgt.plot(x, notUnderstand, name="Not Understanding", pen=penNotUnderstanding, symbol='o', symbolSize=10, symbolPen=(0,0,0), symbolBrush=(0, 170, 255))
        plot_item = self.plotWdgt.plot(x, difficult, name="Difficut", pen=penDifficult, symbol='o', symbolSize=10, symbolPen=(0,0,0), symbolBrush=(255, 116, 35))
        if len(plan) > 1:
            plot_item = self.plotWdgt.plot(plan_x, plan, name="Planned", pen=penPlan, symbol='o', symbolSize=5, symbolPen=(200,0,0), symbolBrush=(3, 32, 93))
        self.plotWdgt.setLabel('left', "<span style=\"color:black;font-size:25px\">Num of Exercises</span>")
        self.plotWdgt.addLegend()
        width = self.plotWdgt.width()
        height = self.plotWdgt.height()
        self.zoomFit(width, height)
        proxy_widget = scene.addWidget(self.plotWdgt)
        #シーンのサイズをリセットしておかないと倍率が正しく設定されない
        scene.setSceneRect(QRectF(0,0,width, height))

    def timestamp(self, timeObj:datetime, type):
        #ミリ秒を整数として扱って計算した場合
        # seconds = int(time.mktime(timeObj.timetuple()))
        # milli = int(timeObj.microsecond/1000)
        # _time = seconds * 1000 + milli
        #Unix Timeで扱う場合（ミリ秒は小数）
        if type == "millisec":
            _time = timeObj.timestamp()
        elif type =="day":
            _date = timeObj.replace(year=timeObj.year,month=timeObj.month, day=timeObj.day,hour=0,minute=0,second=0,microsecond=0, tzinfo=timeObj.tzinfo)
            _time = _date.timestamp()
        return int(_time)
    
    def setDatetime(self, date):
        tmp = date.split('-')
        _date = datetime.datetime(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))
        return _date

    def zoomFit(self, width, height):
        #画像のサイズ（self.pixmapitem.pixmap().width()でも同じ）
        #拡大縮小がサイズに反映されないので、scale係数を乗算
        imageRect = [width*self.scale, height*self.scale]
        print("graph width,height:", width, height)
        print("self.scale:", self.scale, "rects:",width*self.scale, height*self.scale)
        #表示領域のサイズ
        graphicsRect = [self.ui.graphicsView_graph.width(), self.ui.graphicsView_graph.height()]
        widthRatio = graphicsRect[0] / imageRect[0] * 0.99
        heightRatio = graphicsRect[1] / imageRect[1] * 0.99
        if widthRatio > heightRatio:
            scale = heightRatio
        else:
            scale = widthRatio
        self.ui.graphicsView_graph.scale(scale, scale)
        self.scale = scale * self.scale
        print("scale:", scale, "self.scale:",self.scale)

    def onComboGraphXChnaged(self, index):
        self.update(self.setting, self.pageList)

    def resizeEvent(self, event) -> None:
        windowWidth = event.size().width()
        windowHeight = event.size().height()
        print("new window size:", windowWidth, windowHeight)
        y = 0
        spaceY = 10
        spaceX = 50
        #タイトル
        self.ui.label_title.setGeometry(spaceX, spaceY, self.ui.label_title.width(), self.ui.label_title.height())
        #概要グループ
        y += spaceY + self.ui.label_title.height()
        self.ui.groupBox_overview.setGeometry(spaceX, y, self.ui.groupBox_overview.width(), self.ui.groupBox_overview.height())
        #凡例
        edgeOfGraph = windowWidth - spaceX
        self.ui.groupBox_legend.setGeometry(edgeOfGraph-self.ui.groupBox_legend.width(), spaceY*2, self.ui.groupBox_legend.width(), self.ui.groupBox_legend.height())
        #グラフ
        y += self.ui.groupBox_overview.height() + spaceY
        graphWidth = windowWidth - spaceX * 2
        graphHeight = windowHeight - spaceY*5 \
            - self.ui.label_title.height() \
            - self.ui.comboBox_graph_x.height() \
            - self.ui.groupBox_overview.height()
        self.ui.graphicsView_graph.setGeometry(spaceX, y, graphWidth, graphHeight)
        #X軸切り替え
        y += self.ui.graphicsView_graph.height() + spaceY
        self.ui.comboBox_graph_x.setGeometry(spaceX, y, self.ui.comboBox_graph_x.width(), self.ui.comboBox_graph_x.height())
        #閉じるボタン
        closeX = windowWidth/2 - self.ui.pushButton_close.width()
        self.ui.pushButton_close.setGeometry(closeX, y, self.ui.pushButton_close.width(), self.ui.pushButton_close.height())
        #回数設定
        self.ui.groupBox_count.setGeometry(edgeOfGraph-self.ui.groupBox_count.width(), y, self.ui.groupBox_count.width(), self.ui.groupBox_count.height())
        if self.plotWdgt is not None:
            self.zoomFit(self.plotWdgt.width(),self.plotWdgt.height())
        super().resizeEvent(event)