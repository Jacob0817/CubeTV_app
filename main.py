#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-31
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from UI import *
from results import *
import sys


class function(MainUi):
    def __init__(self):
        super().__init__()
    # 决赛PK，成绩栏开关

    def final(self):
        self.stacked_Widget.setCurrentIndex(0)
        self.inputbox.show()
        self.L_x.hide()

    def clear(self):
        self.p_1.setText('-')
        self.p_1_1.setText('-')
        self.p_1_2.setText('-')
        self.p_1_3.setText('-')
        self.p_1_4.setText('-')
        self.p_1_5.setText('-')
        self.p_2.setText('-')
        self.p_2_1.setText('-')
        self.p_2_2.setText('-')
        self.p_2_3.setText('-')
        self.p_2_4.setText('-')
        self.p_2_5.setText('-')

    # 关闭功能窗口
    def doReset(self):
        self.inputbox.hide()
        self.L_x.show()

    # 检查输入框是否为空
    def isInput(setFuc):
        def check(self, boxId):
            boxInput = self.inputbox.text()
            if boxInput:
                return setFuc(self, boxId)
            else:
                pass
        return check

    # 决赛成绩栏，设置选手姓名
    @isInput
    def setName(self, boxId):
        result = self.inputbox.text()
        if (boxId == 1):
            self.p_1.setText(result)
        elif (boxId == 2):
            self.p_2.setText(result)
        self.inputbox.clear()

    # 决赛成绩栏，调整成绩显示格式
    def _format(self, result):
        time = int(result)
        if (time >= 10000):
            return (result[0] + ":" + result[1:3] + "." + result[3:5])
        elif (time < 10000 and time >= 1000):
            return (result[0:2] + "." + result[2:4])
        elif (time < 1000 and time >= 100):
            return (result[0] + "." + result[1:3])
        elif (time <= 99):
            return ("0." + str(time))

    # 决赛成绩栏，设置成绩显示
    @isInput
    def setTime(self, boxId):
        rresult = self.inputbox.text()
        if (int(rresult) <= 99999):
            result = self._format(rresult)
            if (boxId == 1):
                self.p_1_1.setText(result)
            elif (boxId == 2):
                self.p_1_2.setText(result)
            elif (boxId == 3):
                self.p_1_3.setText(result)
            elif (boxId == 4):
                self.p_1_4.setText(result)
            elif (boxId == 5):
                self.p_1_5.setText(result)
            elif (boxId == 6):
                self.p_2_1.setText(result)
            elif (boxId == 7):
                self.p_2_2.setText(result)
            elif (boxId == 8):
                self.p_2_3.setText(result)
            elif (boxId == 9):
                self.p_2_4.setText(result)
            elif (boxId == 10):
                self.p_2_5.setText(result)
        self.inputbox.clear()

    # 决赛成绩栏，平均成绩
    def addt(self, timeList):
        summ = 0
        for time in timeList:
            if (time < 100):
                summ = summ + time
            else:
                sec = int(time / 100) * 60 + time % 100
                summ = summ + sec
        avg = float(("%.2f" % (summ / 5)))
        if (avg >= 60):
            tmin = int(avg / 60)
            tsec = avg % 60
            timmm = str(tmin) + ":" + str(tsec)
        else:
            timmm = str(avg)
        return timmm

    def AVG(self, line):
        if (line == 1):
            P1r = self.p_1_1.text()
            P1 = P1r.replace(':', '')
            P2r = self.p_1_2.text()
            P2 = P2r.replace(':', '')
            P3r = self.p_1_3.text()
            P3 = P3r.replace(':', '')
            P4r = self.p_1_4.text()
            P4 = P4r.replace(':', '')
            P5r = self.p_1_5.text()
            P5 = P5r.replace(':', '')
            timeList = [float(P1), float(P2), float(P3), float(P4), float(P5)]
            AVG = self.addt(timeList)
            self.p_1_AVG.setText(AVG)
            print(timeList)
        else:
            P1r = self.p_2_1.text()
            P1 = P1r.replace(':', '')
            P2r = self.p_2_2.text()
            P2 = P2r.replace(':', '')
            P3r = self.p_2_3.text()
            P3 = P3r.replace(':', '')
            P4r = self.p_2_4.text()
            P4 = P4r.replace(':', '')
            P5r = self.p_2_5.text()
            P5 = P5r.replace(':', '')
            timeList = [float(P1), float(P2), float(P3), float(P4), float(P5)]
            AVG = self.addt(timeList)
            self.p_2_AVG.setText(str(AVG))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = function()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
