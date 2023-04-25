# -*- coding: utf-8 -*-

from PySide6 import QtWidgets
from pathlib import Path
import os, re, random, glob, uuid
from PIL import Image

class Misc:

    '''
    ファイル操作関連
    '''
    #ファイルのパスから拡張子を除いたファイル名を返す
    @staticmethod
    def extractFileNameWoExtention(filePath):
        return os.path.splitext(os.path.basename(filePath))[0]

    #ファイルのパスから拡張子を付けたファイル名を返す
    @staticmethod
    def extractFileName(filePath):
        return os.path.basename(filePath)
    
    #ファイルのパスからフォルダ部分を返す
    @staticmethod
    def extractFolder(filePath):
        return os.path.dirname(filePath)

    #ファイルかフォルダが存在するか確認
    @staticmethod
    def isExistPath(path):
        return os.path.exists(path)
    

    #ファイルパスのリストをファイル名でソーティングする
    @staticmethod
    def sortingFilePathList(file_path_list):
        if len(file_path_list) == 0:
            return []
        file_name_list = [os.path.basename(file_path) for file_path in file_path_list]
        #for debug (re.searchの動作確認。ファイル名から0-9にピリオドが続くものを見つけて、0-9のGroupを取り出す)
        # file_name_list_sorted = Misc.sort_filenames(file_name_list)
        # for file in file_name_list:
        #     tmp = re.search(r"([0-9]+)\.", file).group(1)
        #     print (tmp1)
        #拡張子のピリオドの直前の数字で並び替える
        file_name_list_sorted = sorted(file_name_list, key=lambda x:int((re.search(r"([0-9]+)\.", x)).group(1)))
        # file_name_list_sorted = sorted(file_name_list, key=lambda x:int((re.search(r"[0-9]+", x)).group(0)))
        dir_path = os.path.dirname(file_path_list[0])
        new_file_path_list = [os.path.join(dir_path, file) for file in file_name_list_sorted]
        return new_file_path_list
   
    pattern = re.compile(r'\d+')
    @staticmethod
    def find_max_digit(texts):
        result = 0
        for text in texts:
            numbers = Misc.pattern.findall(text)
            sorted_digits = sorted([str(number) for number in numbers], key=lambda text: len(text))
            result = len(sorted_digits[-1]) if result < len(sorted_digits[-1]) else result
        return result

    @staticmethod
    def sort_filenames(file_names):
        # 1. 数字の最大桁数を取得する
        max_digit = Misc.find_max_digit(file_names)
        # 2. 最大桁数に合わせて数字を置換する
        zero_pad_file_names = []
        for file_name in file_names:
            zero_pad_file_name = file_name
            matches = Misc.pattern.finditer(zero_pad_file_name)
            for match in reversed(list(matches)):
                start_pos = match.span()[0]
                end_pos = match.span()[1]
                sub_target = match.string[start_pos:end_pos]
                zero_pad_text = '0' * (max_digit - len(sub_target)) + sub_target
                zero_pad_file_name = zero_pad_file_name[:start_pos] + zero_pad_text + zero_pad_file_name[end_pos:]
            zero_pad_file_names.append({
                'original': file_name,
                'zero_pad': zero_pad_file_name,
            })
        # 3. すべての数字を連結した値を使ってソートする
        s = sorted(zero_pad_file_names, key=lambda x: x.get('zero_pad'))
        return s


    #folder内の指定した拡張子のファイルをファイル名で並び替えてリストとして返す
    # folder:フルパス（'c:/aaa/ccc'）
    # extention:拡張子（'jpg'） 
    @staticmethod
    def getFilePathList(folder, extension):
        pathList = []
        for x in glob.glob(f'{folder}/*.{extension}'):
            pathList.append(Path(x))
        pathList = Misc.sortingFilePathList(pathList)
        return pathList

    #ファイルダイアログを表示して選択したファイル名を返す
    #拡張子の指定例："*.pdf *.json"
    @staticmethod
    def selectFileDialog(extention):
        filters = f'Image files ({extention});;Any files (*)'
        filename = QtWidgets.QFileDialog.getOpenFileName(filter=filters)#ファイルダイアログで、パスを取得。
        if len(filename) > 0:
            return filename[0]
        else:
            return None

    @staticmethod
    def generateUuid():
        return str(uuid.uuid4())

    @staticmethod
    def shuffle(list):
        return random.sample(list, len(list))

    #KeyのリストとListデータを渡すとDict形式で戻す
    #Key = ['aaa', 'bbb']
    #list = [(123, 234),(456, 678)]
    #return [['aaa':123, 'bbb':234], ['aaa':456, 'bbb':678]]
    @staticmethod
    def fromListToDict(keys, list):
        outList = []
        for data in list:
            outList.append(dict(zip(keys, data)))
        return outList

    @staticmethod
    def imageConcatH(im1, im2, color=(255, 255, 255)):
        if im1 is None:
            return im2
        if im2 is None:
            return im1
        dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    @staticmethod
    def imageConcatV(im1, im2, color=(255, 255, 255)):
        if im1 is None:
            return im2
        if im2 is None:
            return im1
        dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst