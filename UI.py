#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-17
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from PyQt5 import QtCore, QtWidgets
import sys
import qtawesome
from results import *


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_main()
        self.init_left_widget()
        self.init_right_widget()
        self.init_assemble()

    def init_main(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建窗口主部件网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件网格布局
        self.close = QtWidgets.QPushButton(qtawesome.icon('fa.close', color='white'),'')
        self.close.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.close.setFixedSize(25, 25)
        self.close.setStyleSheet('''
            QPushButton{
                background: #F76677;
                border-radius: 5px;
            }
            QPushButton:hover{
                background: red;
            }
            ''')

    # 创建左侧控件,网格布局
    def init_left_widget(self):
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        # 创建左侧控件内部件
        # 标签
        self.L_lable_1 = QtWidgets.QPushButton('标签1')
        self.L_lable_1.setObjectName('L_lable')
        self.L_lable_2 = QtWidgets.QPushButton('标签2')
        self.L_lable_2.setObjectName('L_lable')
        # 按钮
        self.L_button_1 = QtWidgets.QPushButton('显示成绩')
        self.L_button_1.setObjectName('L_button')
        self.L_button_1.clicked.connect(lambda: self.search())
        self.L_button_2 = QtWidgets.QPushButton('按钮2')
        self.L_button_2.setObjectName('L_button')
        self.L_button_3 = QtWidgets.QPushButton('按钮3')
        self.L_button_3.setObjectName('L_button')
        self.L_button_4 = QtWidgets.QPushButton('按钮4')
        self.L_button_4.setObjectName('L_button')
        self.L_button_5 = QtWidgets.QPushButton('刷新')
        self.L_button_5.setObjectName('L_button')
        self.L_button_5.clicked.connect(lambda: self.clear())
        self.L_x = QtWidgets.QPushButton('')
        # 放置左侧控件内部件
        self.left_layout.addWidget(self.close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.L_lable_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.L_lable_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.L_x, 8, 0, 1, 3)
        # 左侧控件QSS
        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background: #0E1A49;
                border-top: 1px #0E1A49;
                border-bottom: 1px #0E1A49;
                border-left: 1px #0E1A49;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
            QPushButton{
                color: white;
                border: none;
            }
            QPushButton#L_lable{
                border: none;
                border-bottom: 1px solid white;
                font-size: 18px;
                font-weight: 700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#L_button:hover{
                border-left: 4px solid red;
                font-weight: 700;
            }
            ''')

    # 创建右侧控件,网格布局
    def init_right_widget(self):
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)
        # 创建右侧控件内部件
        # 查询栏
        self.search_widget = QtWidgets.QWidget()  # 搜索框
        self.search_layout = QtWidgets.QGridLayout()  # 搜索框布局
        self.search_widget.setLayout(self.search_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.search_widget_text = QtWidgets.QLineEdit()
        self.search_widget_text.setPlaceholderText('Place holder text')

        self.result_widget = QtWidgets.QLabel()
        self.result_layout = QtWidgets.QGridLayout()
        self.result_widget.setLayout(self.result_layout)
        self.result_widget.setText(' ')
        # 放置右侧控件内部件
        # 搜索栏内
        self.search_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.search_layout.addWidget(self.search_widget_text, 0, 1, 1, 8)
        # 放置搜索栏
        self.right_layout.addWidget(self.search_widget, 0, 0, 1, 9)
        self.right_layout.addWidget(self.result_widget, 1, 0, 1, 9)
        # 右侧控件CSS
        self.search_widget_text.setStyleSheet('''
            QLineEdit{
                border: 1px solid gray;
                width: 300px;
                border-radius: 10px;
                padding: 2px 4px;
            }
            ''')
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color: white;
                background: white;
                border-top: 1px solid darkGray;
                border-bottom: 1px solid darkGray;
                border-right: 1px solid darkGray;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            ''')

    def init_assemble(self):
        # 放置控件
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.main_layout.addWidget(self.close, 0, 0, 1, 12)
        # 设置主部件
        self.setCentralWidget(self.main_widget)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置透明窗口背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)
