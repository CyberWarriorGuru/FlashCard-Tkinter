# -*- coding: utf-8 -*-
from asyncio import constants
import MySQLdb
import json
from Misc import *

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

class Database(Singleton):
    
    def __init__(self, parent=None): 
        '''
            Questions Book Table:
                uuid(PK)
                file_name
                image_folder
                contents
            Questions pages Table:
                uuid(PK)
                page number(PK)
                width
                height
            Questions areas Table
                area_uuid(PK)
                linked_uuid
                areaNumber
                x
                y
                width
                height
                book_uuid
                page_number
            records table
                count(pk)                (取組み回数：取組み回数(問題数の対する一通りの実施回数)と各問題の解答回数は別)
                question_area_uuid(pk)
                datetime(pk)            （日時）
                result                   (正解、不正解)
                level                    (普通、簡単、ミス、難しい)
                book_uuid
            setting table
                data (json)
        '''
        #-は使用できないので_に変更
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute("create table if not exists user_info(user_id varchar(256), password varchar(256), primary key (user_id))")
        cursor.execute("create table if not exists questions_book(uuid varchar(36), file_name varchar(2048), image_folder varchar(2048), contents json, primary key (uuid))")
        cursor.execute("create table if not exists questions_pages(uuid varchar(36), page_number varchar(128), width double, height double, primary key (uuid, page_number))")
        cursor.execute("create table if not exists questions_areas(area_uuid varchar(36), linked_uuid varchar(36), area_number varchar(128), x double, y double, width double, height double, book_uuid varchar(36), page_number varchar(128), primary key (area_uuid))")
        cursor.execute("create table if not exists questions_sub_areas(sub_area_uuid varchar(36), sub_area_number varchar(128), x double, y double, width double, height double, book_uuid varchar(36), page_number varchar(128), main_uuid varchar(36), primary key (sub_area_uuid))")
        cursor.execute("create table if not exists answers_book(uuid varchar(36), file_name varchar(2048), image_folder varchar(2048), contents json, primary key (uuid))")
        cursor.execute("create table if not exists answers_pages(uuid varchar(36), page_number varchar(128), width double, height double, primary key (uuid, page_number))")
        cursor.execute("create table if not exists answers_areas(area_uuid varchar(36), linked_uuid varchar(36), area_number varchar(128), x double, y double, width double, height double, book_uuid varchar(36), page_number varchar(128), primary key (area_uuid))")
        cursor.execute("create table if not exists answers_sub_areas(sub_area_uuid varchar(36), sub_area_number int signed, x double, y double, width double, height double, book_uuid varchar(36), page_number varchar(128), main_uuid varchar(36), primary key (sub_area_uuid))")
        cursor.execute("create table if not exists records(count int unsigned, question_area_uuid varchar(36), datetime datetime(6), result varchar(32), level varchar(32), book_uuid varchar(36), primary key (count, question_area_uuid, datetime))")
        cursor.execute("create or replace view records_latest_date as \
                                select T1.count, T1.question_area_uuid, T1.datetime, T1.result, T1.level, T1.book_uuid from records as T1 \
                                inner join ( \
                                    select count, question_area_uuid, Max(datetime) as latest \
                                    from records group by count, question_area_uuid) as T2 \
                                on T1.count = T2.count and T1.question_area_uuid = T2.question_area_uuid and T1.datetime = T2.latest;")
        cursor.execute("create table if not exists setting(user_id varchar(128), data json, primary key (user_id))")
        #commit不要
        #  self.connection.commit()
        cursor.close()
        conn.close()

    def getConnection(self):
        try:
            conn = MySQLdb.connect(
                                host='gotit.smagai.com',
                                user='usersql',
                                passwd='20220622',
                                db='kioku_db',
                                charset='utf8')
            return conn
        except Exception as e:
            print(e)
            return None

    #JSONを読込んでDBに書き込む
    # questions_book, questions_pages, questions_areas
    # answers_book, answers_pages, answers_areas
    def writeJsonToDb(self, source, json_data):
        bookTable = "questions_book"
        pageTable = "questions_pages"
        areaTable = "questions_areas"
        subAreaTable = "questions_sub_areas"
        if source == "questions":
            print("source type:", source)
        elif source == "answers":
            print("source type:", source)
            bookTable = "answers_book"
            pageTable = "answers_pages"
            areaTable = "answers_areas"
            subAreaTable = "answers_sub_areas"
        else:
            print("Error:unrecognize source type.", source)
            return False
        #questions_book
        if 'contents' in json_data:
            contentsJson = json.dumps(json_data['contents'], ensure_ascii=False)
        else:
            contentsJson = json.dumps([], ensure_ascii=False)
        sql = "INSERT INTO "+bookTable+" (uuid, file_name, image_folder, contents) VALUES ('" + json_data['uuid'] + "','" + json_data['file_name'] + "','" + json_data['image_folder'] + "', '" + contentsJson + "') ON DUPLICATE KEY UPDATE file_name = VALUES (file_name), image_folder = VALUES (image_folder), contents = VALUES (contents);"
        # print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        #questions_pages
        for data in json_data['page']:
            sql = "INSERT INTO " + pageTable+ " VALUES ('" + json_data['uuid'] + "','" + str(data['pageNumber']) + "'," + str(data['width']) + "," + str(data['height']) + ") ON DUPLICATE KEY UPDATE width = VALUES(width), height = VALUES(height);"
            # print(sql)
            cursor.execute(sql)
        #questions_areas
        for page in json_data['page']:
            if 'area' not in page: continue
            for areas in page['area']:
                if areas is None: continue
                sql = "INSERT INTO " + areaTable + " VALUES ('" + str(areas['uuid']) + "','" + str(areas['linked-uuid']) + "','" + str(areas['areaNumber']) + "'," + str(areas['x']) + "," + str(areas['y']) + "," + str(areas['width']) + "," + str(areas['height']) + ",'" + str(json_data['uuid']) + "','" + str(page['pageNumber']) + "') ON DUPLICATE KEY UPDATE linked_uuid = VALUES(linked_uuid), area_number = VALUES(area_number), x = VALUES(x), y = VALUES(y), width = VALUES(width), height = VALUES(height), book_uuid = VALUES(book_uuid), page_number = VALUES(page_number);"
                # print(sql)
                cursor.execute(sql)
        #questions_sub_areas
        for page in json_data['page']:
            if 'area' not in page: continue
            for areas in page['area']:
                if areas is None: continue
                if 'subAreas' not in areas: continue
                for subArea in areas['subAreas']:
                    sql = "INSERT INTO " + subAreaTable + " VALUES ('" + str(subArea['subUuid']) + "'," + str(subArea['subNum']) + "," + str(subArea['x']) + "," + str(subArea['y']) + "," + str(subArea['width']) + "," + str(subArea['height']) + ",'" + str(json_data['uuid']) + "','" + str(page['pageNumber']) + "', '" + str(areas['uuid']) + "') ON DUPLICATE KEY UPDATE sub_area_uuid = VALUES(sub_area_uuid), sub_area_number = VALUES(sub_area_number), x = VALUES(x), y = VALUES(y), width = VALUES(width), height = VALUES(height), book_uuid = VALUES(book_uuid), page_number = VALUES(page_number), main_uuid = VALUES(main_uuid);"
                    #print(sql)
                    cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()


    def checkPassword(self, userId, password):
        sql = f'select password from user_info where user_id = "{userId}";'
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if data is not None:
            #パスワードが一致
            if data[0] == password:
                return True
            else:
                #パスワードが不一致
                return False
        else:
            #ユーザが見つからない
            return False


    #指定した学習カウントの問題取組み内容を取得(countは0始まり)
    def readAreas(self, book_uuid, pageList, count):
        ''' [View]
            Questions areas Table
                area_uuid(PK) -- answer linked_uuid
                linked_uuid
                areaNumber
                x
                y
                width
                height
                book_uuid
                page_number
                image_folder
                -----------------------------------------------
                answer  area_uuid
                        areaNumber
                        x
                        y
                        width
                        height
                        book_uuid
                        page_number
                        image_folder
                -----------------------------------------------
                record  count
                        datetime
                        result
                        level

        '''
        # sql = f'select q.area_uuid, q.area_number,  q.x, q.y, q.width, q.height, q.book_uuid, q.page_number, qb.image_folder, \
        #                a.area_uuid, a.area_number,  a.x, a.y, a.width, a.height, a.book_uuid, a.page_number, ab.image_folder,  \
        #                r.count,     date_format(r.datetime,"%Y-%m-%d %H:%i:%s.%f"), r.result, r.level \
        #                 from questions_areas as q \
        #                 left join answers_areas as a on q.area_uuid = a.linked_uuid and q.book_uuid = "{book_uuid}" \
        #                 left join questions_book as qb on q.book_uuid = qb.uuid \
        #                 left join answers_book as ab on a.book_uuid = ab.uuid \
        #                 left join records_latest_date as r on q.area_uuid = r.question_area_uuid and r.count ={count}\
        #                 order by cast(q.page_number as signed) asc, cast(q.area_number as signed) asc;'
        if len(pageList) > 0:
            sql = 'select q.area_uuid, q.area_number,  q.x, q.y, q.width, q.height, q.book_uuid, q.page_number, qb.image_folder, \
                       a.area_uuid, a.area_number,  a.x, a.y, a.width, a.height, a.book_uuid, a.page_number, ab.image_folder,  \
                       r.count,     date_format(r.datetime,"%Y-%m-%d %H:%i:%s.%f"), r.result, r.level \
                        from questions_areas as q \
                        left join answers_areas as a on q.area_uuid = a.linked_uuid \
                        left join questions_book as qb on q.book_uuid = qb.uuid \
                        left join answers_book as ab on a.book_uuid = ab.uuid \
                        left join records_latest_date as r on q.area_uuid = r.question_area_uuid and r.count ={0} \
                        where q.book_uuid = "{1}" and q.page_number in ({2}) \
                        order by cast(q.page_number as signed) asc, cast(q.area_number as signed) asc;'.format(count, book_uuid, ', '.join('{}'.format(pageList[i]) for i in range(len(pageList))))
        else:
            sql = 'select q.area_uuid, q.area_number,  q.x, q.y, q.width, q.height, q.book_uuid, q.page_number, qb.image_folder, \
                       a.area_uuid, a.area_number,  a.x, a.y, a.width, a.height, a.book_uuid, a.page_number, ab.image_folder,  \
                       r.count,     date_format(r.datetime,"%Y-%m-%d %H:%i:%s.%f"), r.result, r.level \
                        from questions_areas as q \
                        left join answers_areas as a on q.area_uuid = a.linked_uuid \
                        left join questions_book as qb on q.book_uuid = qb.uuid \
                        left join answers_book as ab on a.book_uuid = ab.uuid \
                        left join records_latest_date as r on q.area_uuid = r.question_area_uuid and r.count ={0} \
                        where q.book_uuid = "{1}" \
                        order by cast(q.page_number as signed) asc, cast(q.area_number as signed) asc;'.format(count, book_uuid)

        print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        areas = cursor.fetchall()
        cursor.close()
        conn.close()
        label = ['q.area_uuid', 'q.area_number',  'q.x', 'q.y', 'q.width', 'q.height', 'q.book_uuid', 'q.page_number', 'q.image_folder', \
                 'a.area_uuid', 'a.area_number',  'a.x', 'a.y', 'a.width', 'a.height', 'a.book_uuid', 'a.page_number', 'a.image_folder', \
                 'r.count',     'r.datetime',     'r.result', 'r.level']
        areas_dict = Misc.fromListToDict(label, areas)
        #ページリストに含まれるページのエリアのみ抽出する
        # if len(pageList) > 0:
        #     areas_dict1 = []
        #     for page in pageList:
        #         areas = [area for area in areas_dict if area.get('q.page_number') == page]
        #         areas_dict1.extend(areas)
        #     return areas_dict1
        # else:
        #     return areas_dict
        return areas_dict

    def readQuestionSubAreas(self, main_uuid):
        sql = f'select sub_area_uuid, sub_area_number, x, y, width, height, book_uuid, page_number, main_uuid \
                        from questions_sub_areas \
                        where main_uuid = "{main_uuid}" \
                        order by sub_area_number asc;'
        print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        areas = cursor.fetchall()
        cursor.close()
        conn.close()
        label = ['sub_area_uuid', 'sub_area_number', 'x', 'y', 'width', 'height', 'book_uuid', 'page_number', 'main_uuid']
        areas_dict = Misc.fromListToDict(label, areas)
        return areas_dict

    def readAnswerSubAreas(self, main_uuid):
        sql = f'select sub_area_uuid, sub_area_number, x, y, width, height, book_uuid, page_number, main_uuid \
                        from answers_sub_areas \
                        where main_uuid = "{main_uuid}" \
                        order by sub_area_number asc;'
        print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        areas = cursor.fetchall()
        cursor.close()
        conn.close()
        label = ['sub_area_uuid', 'sub_area_number', 'x', 'y', 'width', 'height', 'book_uuid', 'page_number', 'main_uuid']
        areas_dict = Misc.fromListToDict(label, areas)
        return areas_dict

    def writeRecords(self, count, question_area_uuid, datetime, result, level, book_uuid):
        sql = f'insert into records values ({count},"{question_area_uuid}","{datetime}","{result}","{level}", "{book_uuid}");'
        # print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def getBookTitleByUuid(self, book_uuid):
        sql = f'select file_name from questions_book where uuid = "{book_uuid}";'
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if len(data) > 0:
            return data[0]
        else:
            return ""

    def getBookTitles(self):
        sql = f'select uuid, file_name from questions_book group by uuid;'
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def getMaxCount(self, book_uuid, pageList):
        if len(pageList) > 0:
            sql = 'select max(r.count) from records as r \
                    left join questions_areas as q on r.question_area_uuid = q.area_uuid \
                    where r.book_uuid = "{0}" and q.page_number in ({1});'.format(book_uuid, ', '.join('{}'.format(pageList[i]) for i in range(len(pageList))))
        else:
            sql = 'select max(count) from records where book_uuid = "{0}"'.format(book_uuid)
        # sql = 'select area_uuid from questions_areas where book_uuid = "{0}" and page_number in ({1});'.format(book_uuid, ', '.join('{}'.format(pageList[i]) for i in range(len(pageList))))
        print(sql)
        print(pageList)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if len(data) == 0:
            return data[0]
        else:
            return 0

    def getNumOfQuestions(self, book_uuid, pageList):
        # sql = f'select area_uuid from questions_areas where book_uuid = "{book_uuid}";'
        if len(pageList) > 0:
            sql = 'select area_uuid from questions_areas where book_uuid = "{0}" and page_number in ({1});'.format(book_uuid, ', '.join('{}'.format(pageList[i]) for i in range(len(pageList))))
        else:
            sql = 'select area_uuid from questions_areas where book_uuid = "{0}";'.format(book_uuid)
        # print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        areasUuid = cursor.fetchall()
        cursor.close()
        conn.close()
        return len(areasUuid)
 
    def getResultByDate(self, book_uuid, pageList):
        # sql = f'select * from records where book_uuid = "{book_uuid}" order by datetime asc;'
        if len(pageList) > 0:
            sql = 'select r.count, r.question_area_uuid, r.datetime, r.result, r.level, r.book_uuid, q.page_number \
                from records as r \
                left join questions_areas as q on r.question_area_uuid = q.area_uuid \
                where r.book_uuid = "{0}" and q.page_number in ({1}) \
                order by r.datetime asc;'.format(book_uuid, ', '.join('{}'.format(pageList[i]) for i in range(len(pageList))))
        else:
            sql = 'select r.count, r.question_area_uuid, r.datetime, r.result, r.level, r.book_uuid, q.page_number \
                from records as r \
                left join questions_areas as q on r.question_area_uuid = q.area_uuid \
                where r.book_uuid = "{0}" \
                order by r.datetime asc;'.format(book_uuid)
        # print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        label = ['count', 'question_area_uuid', 'datetime', 'result', 'level', 'book_uuid', 'page_number']
        records_dict = Misc.fromListToDict(label, records)
        return records_dict

    #とりあえずuser_idは"1"で固定
    def readSetting(self, userId):
        sql = f'select data from setting where user_id = "{userId}";'
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row is not None:
            return json.loads(row[0])
        return None

    def writeSetting(self, userId, setting):
        json_data = json.dumps(setting, ensure_ascii=False)
        sql = "insert into setting (user_id, data) values (\'%s\', \'%s\') on duplicate key update user_id = values (user_id), data = values (data);" % (userId, json_data)
        print(sql)
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def readContents(self, userId, bookUuid):
        #TODO userId
        sql = f'select contents from questions_book where uuid = "{bookUuid}";'
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row[0] is not None:
            return json.loads(row[0])
        return None

    def deleteBook(self, source, bookUuid):
        bookTable = "questions_book"
        pageTable = "questions_pages"
        areaTable = "questions_areas"
        subAreaTable = "questions_sub_areas"
        if source == "questions":
            print("source type:", source)
        elif source == "answers":
            print("source type:", source)
            bookTable = "answers_book"
            pageTable = "answers_pages"
            areaTable = "answers_areas"
            subAreaTable = "answers_sub_areas"
        else:
            print("Error:unrecognize source type.", source)
            return False
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = 'delete from ' + bookTable + ' where uuid = "{}"'.format(bookUuid)
        print(sql)
        cursor.execute(sql)
        sql = 'delete from ' + pageTable + ' where uuid = "{}"'.format(bookUuid)
        print(sql)
        cursor.execute(sql)
        sql = 'delete from ' + areaTable + ' where book_uuid = "{}"'.format(bookUuid)
        print(sql)
        cursor.execute(sql)
        sql = 'delete from ' + subAreaTable + ' where book_uuid = "{}"'.format(bookUuid)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True


    def deleteRecordsTable(self):
        sql = "delete from records;"
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    # def getResult(self, book_uuid, sql):
    #     self.cursor.execute(sql)
    #     records = self.cursor.fetchall()
    #     label = ['count', 'question_area_uuid', 'datetime', 'result', 'level', 'book_uuid']
    #     records_dict = Misc.fromListToDict(label, records)
    #     # print(records_dict)
    #     correct_records = []
    #     for record in records_dict:
    #         if record['result'] == 'correct':
    #             correct_records.append(record)
    #     numOfQuestions = self.getNumOfQuestions(book_uuid)
    #     numOfCorrect = self.getNumOfCorrect(book_uuid)
    #     return {'book_uuid':book_uuid, 'num_of_questions':numOfQuestions, 'num_of_correct':numOfCorrect, 'num_of_records':len(records), 'records':records_dict}

    # #取り組んだ問題数を抽出
    # def getResultWorked(self, book_uuid):
    #     #recordsテーブルに記録された最も古い日付のレコードを取り出す（最初に取り組んだ日）
    #     sql = f'select T1.count, T1.question_area_uuid, date_format(T1.datetime,"%Y-%m-%d %H:%i:%s.%f"), T1.result, T1.level, T1.book_uuid \
    #             from records T1 \
    #             inner join (select count, question_area_uuid, Min(datetime) as latest from records group by count, question_area_uuid) as T2 \
    #             on T1.book_uuid = "{book_uuid}" \
    #             where T1.datetime = T2.latest order by T1.datetime asc;'
    #     # print(sql)
    #     return self.getResult(book_uuid, sql)

    # #理解した問題数を抽出
    # def getResultEasy(self, book_uuid):
    #     #recordsテーブルに記録された最も古い日付のレコードを取り出す（最初に取り組んだ日）
    #     sql = f'select T1.count, T1.question_area_uuid, date_format(T1.datetime,"%Y-%m-%d %H:%i:%s.%f"), T1.result, T1.level, T1.book_uuid \
    #             from records T1 \
    #             inner join (select count, question_area_uuid, Min(datetime) as latest from records group by count, question_area_uuid) as T2 \
    #             on T1.book_uuid = "{book_uuid}" and T1.level = "easy" \
    #             where T1.datetime = T2.latest order by T1.datetime asc;'
    #     # print(sql)
    #     return self.getResult(book_uuid, sql)

    # #理解できていない問題数を抽出
    # def getResultDifficult(self, book_uuid):
    #     #recordsテーブルに記録された最も古い日付のレコードを取り出す（最初に取り組んだ日）
    #     sql = f'select T1.count, T1.question_area_uuid, date_format(T1.datetime,"%Y-%m-%d %H:%i:%s.%f"), T1.result, T1.level, T1.book_uuid \
    #             from records T1 \
    #             inner join (select count, question_area_uuid, Min(datetime) as latest from records group by count, question_area_uuid) as T2 \
    #             on T1.book_uuid = "{book_uuid}" and T1.level = "difficult" \
    #             where T1.datetime = T2.latest order by T1.datetime asc;'
    #     # print(sql)
    #     return self.getResult(book_uuid, sql)

    # def getNumOfCorrect(self, book_uuid):
    #     sql = f'select * from records where book_uuid = "{book_uuid}" and result = "correct";'
    #     self.cursor.execute(sql)
    #     data = self.cursor.fetchall()
    #     return len(data)



    # def readDb(self, source):
    #     self.cursor.execute(f'select * from {source}_book;')
    #     # self.cursor.execute("select data, `data`->'$.page[*].area' from "+table)
    #     # self.cursor.execute("select data from "+table+" where `data`->'$.page[*].area' is not NULL")
    #     # self.cursor.execute("select `data`->'$.page[*].pageNumber', `data`->'$.page[*].area' from "+table+" where JSON_TYPE(`data`->'$.page[*].area') <> NULL")
    #     rows = self.cursor.fetchall()
    #     for row in rows:
    #         if row is None: continue
    #         # data = json.loads(row[0])
    #         # print(row)