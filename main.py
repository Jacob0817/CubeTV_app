#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-31
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from UI import *


class function(MainUi):
    def __init__(self):
        super().__init__()

    def search(self):
        try:
            results = n_results('2011ZHAN24', 444)[0]
            self.result_widget.setText(str(results))
        except:
            self.result_widget.setText('未找到匹配项或未连接到数据库')

    def clear(self):
        self.result_widget.setText(' ')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = function()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
