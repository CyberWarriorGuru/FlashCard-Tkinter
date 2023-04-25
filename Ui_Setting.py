# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from ui.Setting import *
from InfoMgmt import *
from Database import *

class Ui_Setting(QDialog):
    #database connection
    db = None
    #設定（Default）
    settingDefault = {"period":{
                            "standard_num":1,
                            "standard_unit":"days",
                            "standard":2678400,
                            "easy_num":10,
                            "easy_unit":"days",
                            "easy":26784000,
                            "miss_num":10,
                            "miss_unit":"hours",
                            "miss":36000,
                            "difficult_num":10,
                            "difficult_unit":"minutes",
                            "difficult":600
                        },
                "plan":{
                            "number":1,
                            "unit":"日",
                            "monday":1,
                            "tuesday":1,
                            "wednesday":1,
                            "thursday":1,
                            "friday":1,
                            "saturday":1,
                            "sunday":1,
                            "start":"2022-05-28"
                        },
                "reward":{
                            "point":50
                }
    }
    setting = settingDefault
    userId = ""
    def __init__(self, parent=None):
        super(Ui_Setting, self).__init__(parent)
        self.ui = Ui_Dialog_setting()
        self.ui.setupUi(self)
        self.ui.pushButton_reset.clicked.connect(self.resetProgress)
        #databese
        self.db = Database()


    def setUserId(self, userId):
        self.userId = userId

    def update(self):
        self.readSetting()
        self.ui.spinBox_standard.setValue(int(self.setting['period']['standard_num']))
        self.ui.comboBox_standard_unit.setCurrentText(self.setting['period']['standard_unit'])
        self.ui.spinBox_easy.setValue(int(self.setting['period']['easy_num']))
        self.ui.comboBox_easy_unit.setCurrentText(self.setting['period']['easy_unit'])
        self.ui.spinBox_miss.setValue(int(self.setting['period']['miss_num']))
        self.ui.comboBox_miss_unit.setCurrentText(self.setting['period']['miss_unit'])
        self.ui.spinBox_difficult.setValue(int(self.setting['period']['difficult_num']))
        self.ui.comboBox_difficult_unit.setCurrentText(self.setting['period']['difficult_unit'])

        self.ui.spinBox_perday.setValue(int(self.setting['plan']['number']))
        self.ui.checkBox_mon.setChecked(True if self.setting['plan']['monday'] == 1 else False)
        self.ui.checkBox_tue.setChecked(True if self.setting['plan']['tuesday'] == 1 else False)
        self.ui.checkBox_wed.setChecked(True if self.setting['plan']['wednesday'] == 1 else False)
        self.ui.checkBox_thu.setChecked(True if self.setting['plan']['thursday'] == 1 else False)
        self.ui.checkBox_fri.setChecked(True if self.setting['plan']['friday'] == 1 else False)
        self.ui.checkBox_sat.setChecked(True if self.setting['plan']['saturday'] == 1 else False)
        self.ui.checkBox_sun.setChecked(True if self.setting['plan']['sunday'] == 1 else False)

        _date =  self.setting['plan']['start'].split('-')
        self.ui.dateEdit_startdate.setDate(QDate(int(_date[0]), int(_date[1]), int(_date[2])))

        self.ui.spinBox_rewards_pt.setValue(int(self.setting['reward']['point']))

    def getSetting(self):
        return self.setting

    def readSetting(self):
        setting = self.db.readSetting(self.userId)
        if setting is not None:
            if "period" in setting and "plan" in setting and  ("reward" in setting): 
                self.setting = setting
                return self.setting
        self.setting = self.settingDefault
        return self.setting

    def writeSetting(self):
        self.setting['period']['standard_num'] = self.ui.spinBox_standard.value()
        self.setting['period']['standard_unit'] = self.ui.comboBox_standard_unit.currentText()
        self.setting['period']['standard'] = self.calculateSeconds(self.setting['period']['standard_num'], self.setting['period']['standard_unit'])

        self.setting['period']['easy_num'] = self.ui.spinBox_easy.value()
        self.setting['period']['easy_unit'] = self.ui.comboBox_easy_unit.currentText()
        self.setting['period']['easy'] = self.calculateSeconds(self.setting['period']['easy_num'], self.setting['period']['easy_unit'])

        self.setting['period']['miss_num'] = self.ui.spinBox_miss.value()
        self.setting['period']['miss_unit'] = self.ui.comboBox_miss_unit.currentText()
        self.setting['period']['miss'] = self.calculateSeconds(self.setting['period']['miss_num'], self.setting['period']['miss_unit'])

        self.setting['period']['difficult_num'] = self.ui.spinBox_difficult.value()
        self.setting['period']['difficult_unit'] = self.ui.comboBox_difficult_unit.currentText()
        self.setting['period']['difficult'] = self.calculateSeconds(self.setting['period']['difficult_num'], self.setting['period']['difficult_unit'])

        self.setting['plan']['number'] = self.ui.spinBox_perday.value()
        self.setting['plan']['monday'] = 1 if self.ui.checkBox_mon.isChecked() == True else 0
        self.setting['plan']['tuesday'] = 1 if self.ui.checkBox_tue.isChecked() == True else 0
        self.setting['plan']['wednesday'] = 1 if self.ui.checkBox_wed.isChecked() == True else 0
        self.setting['plan']['thursday'] = 1 if self.ui.checkBox_thu.isChecked() == True else 0
        self.setting['plan']['friday'] = 1 if self.ui.checkBox_fri.isChecked() == True else 0
        self.setting['plan']['saturday'] = 1 if self.ui.checkBox_sat.isChecked() == True else 0
        self.setting['plan']['sunday'] = 1 if self.ui.checkBox_sun.isChecked() == True else 0

        self.setting['plan']['start'] = self.ui.dateEdit_startdate.date().toString("yyyy-MM-dd")

        self.setting['reward']['point'] = self.ui.spinBox_rewards_pt.value()

        return self.db.writeSetting(self.userId, self.setting)

    def calculateSeconds(self, number, unit):
        unit_second = 0
        if unit == "weeks":
            unit_second = 60 * 60 * 24 * 7
        elif unit == "days":
            unit_second = 60 * 60* 24
        elif unit == "hours":
            unit_second = 60 * 60
        elif unit == "minutes":
            unit_second = 60
        else:
            print("Errro!!!!")
        periodSeconds = number * unit_second
        # print("見返し経過時間(数値、単位、秒)",number, unit, periodSeconds)
        return periodSeconds

    def clickOk(self):
        self.writeSetting()
        return self.readSetting()

    def resetProgress(self):
        result = QtWidgets.QMessageBox.question(None,"Confirmation", "Do you wanto to clear the progress?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.No:
            return
        self.db.deleteRecordsTable()
        return