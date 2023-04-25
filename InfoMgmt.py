# -*- coding: utf-8 -*-

from Misc import *
import json, uuid

class InfoMgmtBase:
    __jsonFilePath = ""
    __book = None

    def __init__( self ) :
        self.__book = dict({"uuid":"", "file_name":"", "image_folder":"", "contents":[], "page":[]})

    def initialize(self, jsonFilePath, pdfFilePath, imageFolder):
        self.__jsonFilePath = jsonFilePath
        self.__book['file_name'] = Misc.extractFileNameWoExtention(pdfFilePath)
        self.__book['image_folder'] = imageFolder
        self.__book['uuid'] = str(uuid.uuid4())

    def addUpdatePage(self, pageNumber, width, height):
        existPage = [d for d in self.__book["page"] if d.get('pageNumber') == pageNumber]
        if len(existPage) == 0:
            self.__book["page"].append({'pageNumber':pageNumber, "width":width, "height":height})
        else:
            existPage[0]['width'] = width
            existPage[0]['height'] = height
    
    def setContents(self, contents):
        self.__book["contents"] = contents

    def getContents(self):
        if "contents" in self.__book:
            return self.__book["contents"]
        else:
            return []

    '''
        areaInfo: {uuid:"xxx", linkedUuid:"yyy", areaNumber:0, x:0, y:0, width:10, height:10}
    '''
    def addUpdateArea(self, pageNumber, areaInfo):#uuid, linkedUuid, areaNumber, x, y, width, height):
        x = areaInfo['x'] #float(x)
        y = areaInfo['y'] #float(y)
        width = areaInfo['width'] #float(width)
        height = areaInfo['height'] #float(height)
        page = [page for page in self.__book["page"] if page.get('pageNumber') == pageNumber]
        if len(page) == 0 :
            return False
        if not "area" in page[0]:
            page[0]['area'] = [{'uuid':areaInfo['uuid'], 'linked-uuid':areaInfo['linkedUuid'], 'areaNumber':areaInfo['areaNumber'], "x":x, "y":y, "width":width, "height":height}]
        else:
            existArea = [area for area in page[0].get("area") if area.get('uuid') == areaInfo['uuid']]
            if len(existArea) == 0:
                page[0]['area'].append({'uuid':areaInfo['uuid'], 'linked-uuid':areaInfo['linkedUuid'], 'areaNumber':areaInfo['areaNumber'], "x":x, "y":y, "width":width, "height":height})
            else:
                existArea[0]['linked-uuid'] = areaInfo['linkedUuid']
                existArea[0]['areaNumber'] = areaInfo['areaNumber']
                existArea[0]['x'] = x
                existArea[0]['y'] = y
                existArea[0]['width'] = width
                existArea[0]['height'] = height
        return True

    '''
        subAreaInfo: {uuid:"xxx", 
                    subAreas:[{
                        subUuid:"ccc", subNum:"fff", x:0, y:0, width:10, height:10
                    }]}
    '''
    def addUpdateSubArea(self, pageNumber, subAreaInfo):
        pageIndex = [i for i, page in enumerate(self.__book["page"]) if page.get('pageNumber') == pageNumber]
        if len(pageIndex) == 0 :
            return False
        #main Areaが無ければ追加しない
        if not "area" in self.__book["page"][pageIndex[0]]:
            return False
        areas = self.__book["page"][pageIndex[0]]["area"]
        if len(areas) == 0:
            return False
        #対象のエリアのインデックスを抽出
        areaIndex = [i for i, area in enumerate(areas) if area.get('uuid') == subAreaInfo['uuid']]
        if len(areaIndex) == 0:
            return False
        if not 'subAreas' in areas[areaIndex[0]]:
            areas[areaIndex[0]]['subAreas'] = subAreaInfo['subAreas']
            return True
        subAreas = areas[areaIndex[0]]['subAreas']
        subAreaIndex = [i for i, subArea in enumerate(subAreas) if subArea.get('subUuid') == subAreaInfo['subAreas'][0]['subUuid']]
        if len(subAreaIndex) == 0:
            subAreas.append(subAreaInfo['subAreas'][0])
        else:
            subAreas[subAreaIndex[0]]['subNum'] = subAreaInfo['subAreas'][0]['subNum']
            subAreas[subAreaIndex[0]]['x'] = subAreaInfo['subAreas'][0]['x']
            subAreas[subAreaIndex[0]]['y'] = subAreaInfo['subAreas'][0]['y']
            subAreas[subAreaIndex[0]]['width'] = subAreaInfo['subAreas'][0]['width']
            subAreas[subAreaIndex[0]]['height'] = subAreaInfo['subAreas'][0]['height']
        return True

    def deleteMainAndSubArea(self, pageNumber, uuid):
         #対象のページのリストのインデックスを抽出
        pageIndex = [i for i, page in enumerate(self.__book["page"]) if page.get('pageNumber') == pageNumber]
        if len(pageIndex) == 0 :
            return False
        #リストのインデックスが[]リスト形式で戻ってきているので、0番目を指定
        if not "area" in self.__book["page"][pageIndex[0]]:
            return False
        #対象ページのエリアリストを抽出
        areas = self.__book["page"][pageIndex[0]]["area"]
        #対象のエリアのインデックスを抽出
        areaIndex = [i for i, area in enumerate(areas) if area.get('uuid') == uuid]
        if len(areaIndex) == 0:
            return False
        #対象エリアを削除
        del areas[areaIndex[0]]
        return True

    def deleteSubArea(self, pageNumber, mainUuid, subUuid):
        #対象のページのリストのインデックスを抽出
        pageIndex = [i for i, page in enumerate(self.__book["page"]) if page.get('pageNumber') == pageNumber]
        if len(pageIndex) == 0 :
            return False
        #リストのインデックスが[]リスト形式で戻ってきているので、0番目を指定
        if not "area" in self.__book["page"][pageIndex[0]]:
            return False
        #対象ページのエリアリストを抽出
        areas = self.__book["page"][pageIndex[0]]["area"]
        #対象のエリアのインデックスを抽出
        areaIndex = [i for i, area in enumerate(areas) if area.get('uuid') == mainUuid]
        if len(areaIndex) == 0:
            return False
        subAreas = areas[areaIndex[0]]['subAreas']
        subAreaIndex = [i for i, subArea in enumerate(subAreas) if subArea.get('subUuid') == subUuid]
        if len(subAreaIndex) == 0:
            return False
        #対象エリアを削除
        del subAreas[subAreaIndex[0]]
        return True


    def deleteArea(self, pageNumber, uuid, subUuid):
        if subUuid is None:
            self.deleteMainAndSubArea(pageNumber, uuid)
        else:
            self.deleteSubArea(pageNumber, uuid, subUuid)

    def getAreas(self, pageNumber):
        areas = [page.get('area') for page in self.__book["page"] if page.get('pageNumber') == pageNumber]
        if len(areas) != 0:
            return areas[0]
        else:
            return []

    def saveToJson(self):
        try:
            with open(f'{self.__jsonFilePath}', 'w', encoding='utf-8') as fp:
                jsonBook = json.dump(self.__book, fp, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
                print(e)
                return False

    def loadFromJson(self, filePath):
        try:
            with open(filePath, 'r', encoding='utf-8') as fp:
                self.__book = json.load(fp)
                self.__jsonFilePath = filePath
        except Exception as e:
            print(e)

    def getImageFolder(self):
        return self.__book['image_folder']

    def getBooks(self):
        return self.__book
    
    def getUuid(self):
        return self.__book['uuid']

    def getLinkedAreaUuid(self, linkedUuid):
        #LinkedUuidを指定するとAnswersの対象エリアの情報を返す(ページをまたがって全文検索する)
        for page in self.__book["page"]:
            if "area" in page:
                #対象ページのエリアリストを抽出
                areas = page["area"]
                #対象のエリアのインデックスを抽出
                areaIndex = [i for i, area in enumerate(areas) if area.get('linked-uuid') == linkedUuid]
                if len(areaIndex) == 0:
                    continue
                return page['pageNumber'], areas[areaIndex[0]]['uuid'], areas[areaIndex[0]]['x'],areas[areaIndex[0]]['y']
        return None, None, None, None


    '''
    [
        {
            file_name:"title",
            image_folder:"",
            uuid:"", 
            content:[{
                title:"xxx",
                pageNumber:1,
                parts:[{
                    title:"xxx",
                    pageNumber:1
                }]
            }]
            page:[
                {
                    pageNumber:1,
                    width:500,
                    height:1000,
                    area:[
                        {
                            uuid:"xxx",
                            linked-uuid:"yyy",
                            areaNumber:1,
                            x:10,
                            y:10,
                            width:100,
                            height:30,
                            subAreas[
                                {
                                    subUuid:"",
                                    subNum:1,
                                    x:10,
                                    y:10,
                                    width:10
                                }
                            ]
                        },
                        {
                            areaNumber:2,
                            x:10,
                            y:10,
                            width:100,
                            height:30
                        }
                    ]
                },
                {
                    pageNumber:2,
                    width:500,
                    height:1000,
                    area:[
                        {
                            areaNumber:1,
                            x:10,
                            y:10,
                            width:100,
                            height:30
                        },
                        {
                            areaNumber:2,
                            x:10,
                            y:10,
                            width:100,
                            height:30
                        }
                    ]
                }
        ]}
    ]

    '''
    