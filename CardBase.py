# -*- coding: utf-8 -*-

from distutils.util import subst_vars
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt, QRectF
from Ui_Setting import*
from Misc import *
import datetime
from PIL import Image
from PIL.ImageQt import ImageQt

'''
[Cards Dictionary]
※学習カウントごとに取得(学習カウントが変更になった場合は取得しなおす)
※未学習(結果が登録されていない場合)はr.count, r.datetime, r.result, r.levelはNoneになる
※学習済みの場合は、'r.count','r.datetime','r.result', 'r.level'に最新の結果が入っている
['q.area_uuid', 'q.area_number',  'q.x', 'q.y', 'q.width', 'q.height', 'q.book_uuid', 'q.page_number', 'q.image_folder', \
 'a.area_uuid', 'a.area_number',  'a.x', 'a.y', 'a.width', 'a.height', 'a.book_uuid', 'a.page_number', 'a.image_folder', \
 'r.count',     'r.datetime',     'r.result', 'r.level']
'''

class CardBase():
    #viewの名称（questions, answers)
    viewName = ""
    graphicsView:QtWidgets.QGraphicsView = None
    #画像の絶対拡大・縮小率(全ページ共通)
    scale = 1.0
    pixmapitem = None

    def __init__(self, viewName, graphicsView):
        self.viewName = viewName
        self.graphicsView = graphicsView
        self.scene = QtWidgets.QGraphicsScene()

    def getViewName(self):
        return self.viewName

    def pil2pixmap(self, pilImage):
        qim = ImageQt(pilImage)
        pix = QtGui.QPixmap.fromImage(qim)
        return pix
        # もし上記コードでクラッシュする場合は下記コードを試す
        # if pilImage.mode == "RGB":
        #     r, g, b = pilImage.split()
        #     pilImage = Image.merge("RGB", (b, g, r))
        # elif  pilImage.mode == "RGBA":
        #     r, g, b, a = pilImage.split()
        #     pilImage = Image.merge("RGBA", (b, g, r, a))
        # elif pilImage.mode == "L":
        #     pilImage = pilImage.convert("RGBA")
        # # Bild in RGBA konvertieren, falls nicht bereits passiert
        # im2 = pilImage.convert("RGBA")
        # data = im2.tobytes("raw", "RGBA")
        # qim = QtGui.QImage(data, pilImage.size[0], pilImage.size[1], QtGui.QImage.Format_ARGB32)
        # pixmap = QtGui.QPixmap.fromImage(qim)
        # return pixmap 
        

    def showImageFromPillow(self, pilImage):
        #シーンのアイテムを削除してから画像をセット
        self.clearAllItems()    
        self.pixmapitem = self.scene.addPixmap(self.pil2pixmap(pilImage))
        self.graphicsView.setScene(self.scene)
        self.zoomFit()
        return
    # def showImage(self, pixmapImage):
    #     #シーンのアイテムを削除してから画像をセット
    #     self.clearAllItems()
    #     self.pixmapitem = self.scene.addPixmap(pixmapImage)
    #     self.graphicsView.setScene(self.scene)
    #     self.zoomFit()
    #     return

    def clearAllItems(self):
        items = self.scene.items()
        for item in items:
            self.scene.removeItem(item)

    def showImageFilePath(self, imageFilepath):
        im = Image.open(imageFilepath)
        self.showImageFromPillow(im)
        return
    # def showImageFilePath(self, imageFilepath):
    #     pixmap = QtGui.QPixmap(imageFilepath)
    #     self.showImage(pixmap)
    #     return

    def showRect(self, uuid, x, y, width, height):
        #JSONファイルから読込んだ場合
        areaItem = CreateRectItem([x, y], [x+width, y+height], uuid)
        areaItem.setPenColor(Qt.black)
        areaItem.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable |
                                QtWidgets.QGraphicsItem.ItemIsFocusable)
        self.scene.addItem(areaItem)
        self.scene.update()
        
    def zoomFit(self):
        if self.pixmapitem is None: return
        #シーンのサイズをリセットしておかないと倍率が正しく設定されない
        self.scene.setSceneRect(QRectF(0,0,self.pixmapitem.pixmap().width(), self.pixmapitem.pixmap().height()))
        #画像のサイズ（self.pixmapitem.pixmap().width()でも同じ）
        #拡大縮小がサイズに反映されないので、scale係数を乗算
        print("Image Size:", self.pixmapitem.pixmap().width(), self.pixmapitem.pixmap().height())
        imageRect = [self.scale*self.pixmapitem.pixmap().width(), self.scale*self.pixmapitem.pixmap().height()]
        print("self.scale:", self.scale, "imageRects:",self.scale*self.pixmapitem.pixmap().width(), self.scale*self.pixmapitem.pixmap().height())
        if not self.pixmapitem.pixmap().isNull(): #if not sceneRect.isNull():
            #表示領域のサイズ
            graphicsRect = [self.graphicsView.width(), self.graphicsView.height()]
            print("graphicsRect Size:", self.graphicsView.width(), self.graphicsView.height())
            widthRatio = graphicsRect[0] / imageRect[0] * 0.99
            heightRatio = graphicsRect[1] / imageRect[1] * 0.99
            if widthRatio > heightRatio:
                scale = heightRatio
            else:
                scale = widthRatio
            self.graphicsView.scale(scale, scale)
            self.scale = scale * self.scale
            print("scale:", scale, "self.scale:",self.scale)

    def zoom(self, scale):
        #今の拡大縮小状態に対して、拡大縮小するので、まず1.0倍の状態に戻して絶対倍率を求める
        original_size_scale = 1 / self.scale
        this_time_scale = original_size_scale * scale
        self.graphicsView.scale(this_time_scale, this_time_scale)
        #倍率は絶対倍率を保持する
        self.scale = scale

class CreateRectItem(QtWidgets.QGraphicsItem):

    uuid = ""

    #矩形開始座標
    startPos = []
    endPos = []

    penWidth = 2
    penColor = Qt.red
    
    def __init__(self, startPos, endPos, pUuid="", parent=None):
        super().__init__(parent)
        self.startPos = startPos
        self.endPos = endPos
        self.uuid = Misc.generateUuid() if pUuid == "" else pUuid
        print(self.uuid)
        
    def setPenColor(self, color):
        self.penColor = color

    def setPos(self, startPos, endPos):
        self.startPos = startPos
        self.endPos = endPos

    def boundingRect(self):
        #この図形を囲む矩形を返す。
        return QRectF(self.startPos[0] - self.penWidth / 2, self.startPos[1] - self.penWidth / 2,
                      self.endPos[0] + self.penWidth, self.endPos[1] + self.penWidth)


    def paint(self, painter, option, widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # ペンとブラシを設定する。
        painter.setPen(
            QtGui.QPen(self.penColor, self.penWidth, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin)
        )   
        # painter.setBrush(Qt.yellow)

        #左上ｘ，ｙ、幅、高さ
        rectangle = QtCore.QRectF(self.startPos[0], self.startPos[1], (self.endPos[0]-self.startPos[0]), (self.endPos[1]-self.startPos[1]))
        painter.drawRect(rectangle)  

        if self.penColor == Qt.black:
            painter.fillRect(self.startPos[0], self.startPos[1], (self.endPos[0]-self.startPos[0]), (self.endPos[1]-self.startPos[1]), QtGui.QColor(255, 0, 0, 50))

    def getUuid(self):
        return self.uuid

#シングルトン（__init__は初回インスタンス生成時しか呼ばれないようにしている）
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Singleton, cls).__new__(cls)
        # else以下は、子クラスの__init__を一度しか実行させなくする
        else:
            def init_pass(self, *args, **kwargs):
                pass
            cls.__init__ = init_pass
        return cls._instance

class CardsMgmt(Singleton):
    cardQuestion:CardBase
    cardAnswer:CardBase
    pageViewQuestion:CardBase
    setting:Ui_Setting
    original_cards = []
    current_cards = []
    pagesQuestions = []
    pagesAnswers = []
    #現在表示しているカード番号
    currentCardIndex = 0
    #サブエリアがあった場合の並べ方
    layout = "up and down" #"左右に並べる", "上下に並べる"
    #リスタートする時のコールバック
    restart_cb = None

    # #取組み済みの問題の見直し待ち時間（秒単位）
    # waiting = {"standard":60,
    #             "easy":300,
    #             "miss":10,
    #             "difficult":5}

    def __init__(self, graphicsViewPage, graphicsViewQuestion, graphicsViewAnswer, setting, restart_cb):
        self.pageViewQuestion = CardBase("questions", graphicsViewPage)
        self.cardQuestion = CardBase("questions", graphicsViewQuestion)
        self.cardAnswer = CardBase("answers", graphicsViewAnswer)
        self.setting = setting
        self.restart_cb = restart_cb
        #databese
        self.db = Database()
    
    def setInfo(self, cards, pagesQuestions, pagesAnswers):
        self.original_cards = cards
        self.pagesQuestions = pagesQuestions
        self.pagesAnswers = pagesAnswers

    def initializeCardIndex(self):
        self.currentCardIndex = -1

    def setLayout(self, layout):
        self.layout = layout

    def getSubAreaImage(self, imageFilePath, subAreas, mainImage):
        subImage = None
        if len(subAreas) > 0:
            for subArea in subAreas:
                croppedSubImage = self.cropImage(imageFilePath, 
                                                    subArea['x'], 
                                                    subArea['y'], 
                                                    subArea['width'], 
                                                    subArea['height'])
                if self.layout == "side by side":
                    subImage = Misc.imageConcatH(subImage, croppedSubImage)
                else:
                    subImage = Misc.imageConcatV(subImage, croppedSubImage)
        if subImage is not None:
            if self.layout == "side by side":
                return Misc.imageConcatH(mainImage, subImage)
            else:
                return Misc.imageConcatV(mainImage, subImage)
        else:
            return mainImage

    def showQuestion(self, cardIndex):
        #問題カードを表示
        pageIndex = int(self.current_cards[cardIndex]['q.page_number'])
        #カードイメージを作成（画像をクロップ）
        croppedImage = self.cropImage(self.pagesQuestions[pageIndex], 
                        self.current_cards[cardIndex]['q.x'], 
                        self.current_cards[cardIndex]['q.y'], 
                        self.current_cards[cardIndex]['q.width'], 
                        self.current_cards[cardIndex]['q.height'])
        #質問カードのサブエリアを取得
        subAreas = self.db.readQuestionSubAreas(self.current_cards[cardIndex]['q.area_uuid'])
        image = self.getSubAreaImage(self.pagesQuestions[pageIndex], subAreas, croppedImage)
        if image is None: return
        self.cardQuestion.showImageFromPillow(image)
        #答えカードをクリア
        self.cardAnswer.clearAllItems()
        self.currentCardIndex = cardIndex
        #問題ページを表示
        self.pageViewQuestion.showImageFilePath(self.pagesQuestions[pageIndex])
        self.pageViewQuestion.showRect(self.current_cards[cardIndex]['q.area_uuid'],
                        self.current_cards[cardIndex]['q.x'], 
                        self.current_cards[cardIndex]['q.y'], 
                        self.current_cards[cardIndex]['q.width'], 
                        self.current_cards[cardIndex]['q.height'])

    def showAnswer(self):
        #答えカードを表示
        pageIndex = int(self.current_cards[self.currentCardIndex]['a.page_number'])
        #カードイメージを作成（画像をクロップ）
        croppedImage = self.cropImage(self.pagesAnswers[pageIndex], 
                        self.current_cards[self.currentCardIndex]['a.x'], 
                        self.current_cards[self.currentCardIndex]['a.y'], 
                        self.current_cards[self.currentCardIndex]['a.width'], 
                        self.current_cards[self.currentCardIndex]['a.height'])
        #質問カードのサブエリアを取得
        subAreas = self.db.readAnswerSubAreas(self.current_cards[self.currentCardIndex]['a.area_uuid'])
        image = self.getSubAreaImage(self.pagesAnswers[pageIndex], subAreas, croppedImage)
        self.cardAnswer.showImageFromPillow(image)

 
    def nextQuestion(self):
        #最後まで解答した場合
        if (self.currentCardIndex >= len(self.current_cards)-1): 
            self.restart_cb("complete")

        self.currentCardIndex +=1
        for i in range(self.currentCardIndex, len(self.current_cards)):
            #新規の問題の場合
            if self.current_cards[i]['r.datetime'] is None:
                self.currentCardIndex = i
                print("New card. card index is set to:", i)
                self.showQuestion(i)
                prevResultLebel = "First exercise"
                return prevResultLebel
            else:
                #以前取組み済みの場合は、指定経過時間を過ぎているか判定
                waitSetting = self.setting.getSetting()
                deltaSec = waitSetting['period'][self.current_cards[i]['r.level']]
                cardDatetime = datetime.datetime.strptime(self.current_cards[i]['r.datetime'], '%Y-%m-%d %H:%M:%S.%f')
                targetDateTime = cardDatetime + datetime.timedelta(seconds=deltaSec)
                now = datetime.datetime.now()
                if now > targetDateTime:
                    self.currentCardIndex = i
                    print("card[",self.current_cards[i]['r.level'], "] is on study. card index is set to:", i)
                    self.showQuestion(i)    
                    word = {"standard":"Correct", "easy":"Easy","miss":"Mistake","difficult":"Difficult"}
                    prevResultLebel = "Previous: " + word[self.current_cards[i]['r.level']] + " (" + cardDatetime.strftime("%Y/%m/%d %H:%M") + ")"
                    return prevResultLebel
        #取組みが必要なカードがない場合
        self.restart_cb("noTodoCards")


    def cropImage(self, imageFilePath, top, left, width, height):
        im = Image.open(imageFilePath)
        croppedIm = im.crop((top, left, top+width, left+height))
        # croppedPixmap = QtGui.QPixmap(imageFilePath).copy(top, left, width, height)
        return croppedIm
    
    def zoomFitAll(self):
        self.cardQuestion.zoomFit()
        self.cardAnswer.zoomFit()
        self.pageViewQuestion.zoomFit()

    def setSorting(self, type):
        if self.original_cards is None: return False
        if type == "shuffle":
            self.current_cards = Misc.shuffle(self.original_cards)
            return True
        elif type == "in_order":
            self.current_cards = self.original_cards
            return True
        else:
            print("error type")
            return False
        
    def getCurrentCard(self):
        return self.current_cards[self.currentCardIndex]
    
    