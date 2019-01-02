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

    def final(self):
        self.final_widget.show()
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

    def doreset(self):
        self.final_widget.hide()
        self.inputbox.hide()
        self.L_x.show()

    def setName(self, id):
        result = self.inputbox.text()
        if (id == 1):
            self.p_1.setText(result)
        elif (id == 2):
            self.p_2.setText(result)
        self.inputbox.clear()

    def _format(self, result):
        time = int(result)
        if (time >= 10000):
            return (result[0] + ":" + result[1:3] + ":" + result[3:5])
        elif (time < 10000 and time >= 1000):
            return (result[0:2] + ":" +result[2:4])
        elif (time < 1000 and time >= 100):
            return (result[0] + ":" + result[1:3])

    def setResult(self, id):
        rresult = self.inputbox.text()
        if rresult and (int(rresult) <= 99999) and (int(rresult) >99):
            result = self._format(rresult)
            if (id == 1):
                self.p_1_1.setText(result)
            elif (id == 2):
                self.p_1_2.setText(result)
            elif (id == 3):
                self.p_1_3.setText(result)
            elif (id == 4):
                self.p_1_4.setText(result)
            elif (id == 5):
                self.p_1_5.setText(result)
            elif (id == 6):
                self.p_2_1.setText(result)
            elif (id == 7):
                self.p_2_2.setText(result)
            elif (id == 8):
                self.p_2_3.setText(result)
            elif (id == 9):
                self.p_2_4.setText(result)
            elif (id == 10):
                self.p_2_5.setText(result)
        else:
            pass
        self.inputbox.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = function()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
