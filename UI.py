#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-17
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from PyQt5 import QtCore, QtWidgets
import qtawesome


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_main()
        self.init_left_widget()
        self.init_final_widget()
        self.init_rank_list()
        self.init_stacked_widget()
        self.init_assemble()

    def init_main(self):
        self.setFixedSize(960, 720)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建窗口主部件网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件网格布局
        self.close = QtWidgets.QPushButton(qtawesome.icon('fa.close', color='white'), '')
        self.close.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.close.setFixedSize(30, 30)
        self.close.setStyleSheet('''
            QPushButton{
                background: #FF6F61;
                border-radius: 10px;
            }
            QPushButton:hover{
                background: red;
            }
            ''')
        self.reset = QtWidgets.QPushButton(qtawesome.icon('fa.refresh', color='white'), '')
        self.reset.clicked.connect(lambda: self.doReset())
        self.reset.setFixedSize(30, 30)
        self.reset.setStyleSheet('''
            QPushButton{
                background: #FF6F61;
                border-radius: 10px;
            }
            QPushButton:hover{
                background: green;
            }
            ''')

    # 创建左侧控件,网格布局
    def init_left_widget(self):
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        self.left_widget.setFixedWidth(150)
        # 创建左侧控件内部件
        # 标签
        self.L_lable_1 = QtWidgets.QPushButton('成绩栏')
        self.L_lable_1.setObjectName('L_lable')
        self.L_lable_2 = QtWidgets.QPushButton('选手资料')
        self.L_lable_2.setObjectName('L_lable')
        # 按钮
        # ,lable 1
        self.L_button_1 = QtWidgets.QPushButton('1V1成绩栏')
        self.L_button_1.setObjectName('L_button')
        self.L_button_1.clicked.connect(lambda: self.final())
        self.L_button_2 = QtWidgets.QPushButton('晋级成绩栏')
        self.L_button_2.setObjectName('L_button')
        self.L_button_2.clicked.connect(lambda: self.listRank())
        # ,lable 2
        self.L_button_3 = QtWidgets.QPushButton('个人')
        self.L_button_3.setObjectName('L_button')
        self.L_button_4 = QtWidgets.QPushButton('参赛经历')
        self.L_button_4.setObjectName('L_button')
        self.L_button_5 = QtWidgets.QPushButton('刷新')
        self.L_button_5.setObjectName('L_button')
        self.L_button_5.clicked.connect(lambda: self.clear())
        self.L_x = QtWidgets.QPushButton('')
        # 输入框
        self.inputbox = QtWidgets.QLineEdit()
        self.inputbox.setPlaceholderText('无符号成绩')
        self.inputbox.hide()
        # 放置左侧控件内部件
        self.left_layout.addWidget(self.close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.L_lable_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.L_lable_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.L_x, 7, 0, 1, 3)
        self.left_layout.addWidget(self.inputbox, 8, 0, 1, 3)
        self.left_layout.addWidget(self.L_button_5, 9, 0, 1, 3)
        # 左侧控件QSS
        self.L_x.setFixedHeight(30)
        self.inputbox.setFixedHeight(30)
        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background: #FF6F61;
                border-radius: 10px;

            }
            QPushButton{
                color: white;
                border: none;
                font-size: 18px;
                font-weight: 700;
                font-family: "微软雅黑";
            }
            QPushButton#L_lable{
                border: none;
                border-bottom: 1px solid white;
                font-size: 22px;
                font-weight: 900;
                font-family: "微软雅黑";
            }
            QPushButton#L_button:hover{
                border-left: 4px solid white;
                font-weight: 900;
                font-size: 20px;
            }
            QLineEdit{
                border-radius: 5px;
            }
            ''')

    # 创建窗口堆栈容器
    def init_stacked_widget(self):
        self.stacked_Widget = QtWidgets.QStackedWidget()

    # 创建决赛成绩栏,网格布局,,堆栈 0
    def init_final_widget(self):
        self.final_widget = QtWidgets.QWidget()
        self.final_widget.setObjectName('final_widget')
        self.final_layout = QtWidgets.QGridLayout()
        self.final_widget.setLayout(self.final_layout)
        self.final_widget.setFixedHeight(150)
        # 创建决赛成绩栏内部件
        # 第一行================================================
        self.p_1 = QtWidgets.QPushButton()
        self.p_1.setObjectName('player_L')
        self.p_1_layout = QtWidgets.QGridLayout()
        self.p_1.setLayout(self.p_1_layout)
        self.p_1.setText('-')
        self.p_1.clicked.connect(lambda: self.setName(1))
        # r1
        self.p_1_1 = QtWidgets.QPushButton()
        self.p_1_1.setObjectName('upper')
        self.p_1_1_layout = QtWidgets.QGridLayout()
        self.p_1_1.setLayout(self.p_1_1_layout)
        self.p_1_1.setText('-')
        self.p_1_1.clicked.connect(lambda: self.setTime(1))
        # r2
        self.p_1_2 = QtWidgets.QPushButton()
        self.p_1_2.setObjectName('upper')
        self.p_1_2_layout = QtWidgets.QGridLayout()
        self.p_1_2.setLayout(self.p_1_2_layout)
        self.p_1_2.setText('-')
        self.p_1_2.clicked.connect(lambda: self.setTime(2))
        # r3
        self.p_1_3 = QtWidgets.QPushButton()
        self.p_1_3.setObjectName('upper')
        self.p_1_3_layout = QtWidgets.QGridLayout()
        self.p_1_3.setLayout(self.p_1_3_layout)
        self.p_1_3.setText('-')
        self.p_1_3.clicked.connect(lambda: self.setTime(3))
        # r4
        self.p_1_4 = QtWidgets.QPushButton()
        self.p_1_4.setObjectName('upper')
        self.p_1_4_layout = QtWidgets.QGridLayout()
        self.p_1_4.setLayout(self.p_1_4_layout)
        self.p_1_4.setText('-')
        self.p_1_4.clicked.connect(lambda: self.setTime(4))
        # r5
        self.p_1_5 = QtWidgets.QPushButton()
        self.p_1_5.setObjectName('upper')
        self.p_1_5_layout = QtWidgets.QGridLayout()
        self.p_1_5.setLayout(self.p_1_5_layout)
        self.p_1_5.setText('-')
        self.p_1_5.clicked.connect(lambda: self.setTime(5))
        self.p_1_5.clicked.connect(lambda: self.AVG(1))
        # r6 AVG
        self.p_1_AVG = QtWidgets.QPushButton()
        self.p_1_AVG.setObjectName('upper_last')
        self.p_1_AVG_layout = QtWidgets.QGridLayout()
        self.p_1_AVG.setLayout(self.p_1_AVG_layout)
        self.p_1_AVG.setText('-')
        # 第二行================================================
        self.p_2 = QtWidgets.QPushButton()
        self.p_2.setObjectName('player_R')
        self.p_2_layout = QtWidgets.QGridLayout()
        self.p_2.setLayout(self.p_2_layout)
        self.p_2.setText('-')
        self.p_2.clicked.connect(lambda: self.setName(2))
        # r1
        self.p_2_1 = QtWidgets.QPushButton()
        self.p_2_1.setObjectName('lower')
        self.p_2_1_layout = QtWidgets.QGridLayout()
        self.p_2_1.setLayout(self.p_2_1_layout)
        self.p_2_1.setText('-')
        self.p_2_1.clicked.connect(lambda: self.setTime(6))
        # r2
        self.p_2_2 = QtWidgets.QPushButton()
        self.p_2_2.setObjectName('lower')
        self.p_2_2_layout = QtWidgets.QGridLayout()
        self.p_2_2.setLayout(self.p_2_2_layout)
        self.p_2_2.setText('-')
        self.p_2_2.clicked.connect(lambda: self.setTime(7))
        # r3
        self.p_2_3 = QtWidgets.QPushButton()
        self.p_2_3.setObjectName('lower')
        self.p_2_3_layout = QtWidgets.QGridLayout()
        self.p_2_3.setLayout(self.p_2_3_layout)
        self.p_2_3.setText('-')
        self.p_2_3.clicked.connect(lambda: self.setTime(8))
        # r4
        self.p_2_4 = QtWidgets.QPushButton()
        self.p_2_4.setObjectName('lower')
        self.p_2_4_layout = QtWidgets.QGridLayout()
        self.p_2_4.setLayout(self.p_2_4_layout)
        self.p_2_4.setText('-')
        self.p_2_4.clicked.connect(lambda: self.setTime(9))
        # r5
        self.p_2_5 = QtWidgets.QPushButton()
        self.p_2_5.setObjectName('lower')
        self.p_2_5_layout = QtWidgets.QGridLayout()
        self.p_2_5.setLayout(self.p_2_5_layout)
        self.p_2_5.setText('-')
        self.p_2_5.clicked.connect(lambda: self.setTime(10))
        self.p_2_5.clicked.connect(lambda: self.AVG(2))
        # r6 AVG
        self.p_2_AVG = QtWidgets.QPushButton()
        self.p_2_AVG.setObjectName('lower_last')
        self.p_2_AVG_layout = QtWidgets.QGridLayout()
        self.p_2_AVG.setLayout(self.p_2_AVG_layout)
        self.p_2_AVG.setText('-')
        # 放置决赛成绩栏内部件
        self.final_layout.addWidget(self.p_1, 1, 0, 1, 1)
        self.final_layout.addWidget(self.p_1_1, 1, 1, 1, 1)
        self.final_layout.addWidget(self.p_1_2, 1, 2, 1, 1)
        self.final_layout.addWidget(self.p_1_3, 1, 3, 1, 1)
        self.final_layout.addWidget(self.p_1_4, 1, 4, 1, 1)
        self.final_layout.addWidget(self.p_1_5, 1, 5, 1, 1)
        self.final_layout.addWidget(self.p_1_AVG, 1, 6, 1, 1)
        self.final_layout.addWidget(self.p_2, 2, 0, 1, 1)
        self.final_layout.addWidget(self.p_2_1, 2, 1, 1, 1)
        self.final_layout.addWidget(self.p_2_2, 2, 2, 1, 1)
        self.final_layout.addWidget(self.p_2_3, 2, 3, 1, 1)
        self.final_layout.addWidget(self.p_2_4, 2, 4, 1, 1)
        self.final_layout.addWidget(self.p_2_5, 2, 5, 1, 1)
        self.final_layout.addWidget(self.p_2_AVG, 2, 6, 1, 1)
        self.final_layout.setSpacing(0)
        # final控件QSS
        self.final_widget.setStyleSheet('''
            QWidget#final_widget{
                color: white;
                background: #0E1A49;
                border-radius: 10px;
            }
            QPushButton{
                color: white;
                border: none;
                font-size: 25px;
                font-weight: 700;
                font-family: "微软雅黑";
                height: 100px
            }
            QPushButton#player_L{
                font-size: 28px;
                border: 2px solid darkGray;
                border-left: none;
                border-top: none;
            }
            QPushButton#upper{
                border: 2px solid darkGray;
                border-top: none;
            }
            QPushButton#upper:hover{
                color: red;
                font-size: 30px;
                font-weight: 900;
            }
            QPushButton#upper_last{
                border: 2px solid darkGray;
                border-top: none;
                border-right: none;
                color: red;
            }
            QPushButton#player_R{
                font-size: 28px;
                border: 2px solid darkGray;
                border-left: none;
                border-bottom: none;
            }
            QPushButton#lower{
                border: 2px solid darkGray;
                border-bottom: none;
            }
            QPushButton#lower:hover{
                color: red;
                font-size: 30px;
                font-weight: 900;
            }
            QPushButton#lower_last{
                border: 2px solid darkGray;
                border-bottom: none;
                border-right: none;
                color: red
            }
            ''')

    # 创建晋级成绩栏,网格布局,,堆栈 1
    def init_rank_list(self):
        self.list = QtWidgets.QWidget()
        self.list.setObjectName('list')
        self.list_layout = QtWidgets.QGridLayout()
        self.list.setLayout(self.list_layout)
        # line head
        self.line_h = QtWidgets.QPushButton()
        self.line_h.setObjectName('header')
        self.line_h_layout = QtWidgets.QGridLayout()
        self.line_h.setLayout(self.line_h_layout)
        self.line_h.setFixedHeight(50)
        # name
        self.line_h_name = QtWidgets.QLabel()
        self.line_h_name.setObjectName('cell')
        self.line_h_name.setText("姓名")
        self.line_h_name_layout = QtWidgets.QGridLayout()
        self.line_h_name.setLayout(self.line_h_name_layout)
        # 1
        self.line_h_1 = QtWidgets.QLabel()
        self.line_h_1.setObjectName('cell')
        self.line_h_1.setText("1")
        self.line_h_1_layout = QtWidgets.QGridLayout()
        self.line_h_1.setLayout(self.line_h_1_layout)
        # 2
        self.line_h_2 = QtWidgets.QLabel()
        self.line_h_2.setObjectName('cell')
        self.line_h_2.setText("2")
        self.line_h_2_layout = QtWidgets.QGridLayout()
        self.line_h_2.setLayout(self.line_h_2_layout)
        # 3
        self.line_h_3 = QtWidgets.QLabel()
        self.line_h_3.setObjectName('cell')
        self.line_h_3.setText("3")
        self.line_h_3_layout = QtWidgets.QGridLayout()
        self.line_h_3.setLayout(self.line_h_3_layout)
        # 4
        self.line_h_4 = QtWidgets.QLabel()
        self.line_h_4.setObjectName('cell')
        self.line_h_4.setText("4")
        self.line_h_4_layout = QtWidgets.QGridLayout()
        self.line_h_4.setLayout(self.line_h_4_layout)
        # 5
        self.line_h_5 = QtWidgets.QLabel()
        self.line_h_5.setObjectName('cell')
        self.line_h_5.setText("5")
        self.line_h_5_layout = QtWidgets.QGridLayout()
        self.line_h_5.setLayout(self.line_h_5_layout)
        # AVG
        self.line_h_AVG = QtWidgets.QLabel()
        self.line_h_AVG.setObjectName('cell')
        self.line_h_AVG.setText("AVG")
        self.line_h_AVG_layout = QtWidgets.QGridLayout()
        self.line_h_AVG.setLayout(self.line_h_AVG_layout)
        # assemble line head
        self.line_h_layout.addWidget(self.line_h_name, 0, 0, 1, 1)
        self.line_h_layout.addWidget(self.line_h_1, 0, 1, 1, 1)
        self.line_h_layout.addWidget(self.line_h_2, 0, 2, 1, 1)
        self.line_h_layout.addWidget(self.line_h_3, 0, 3, 1, 1)
        self.line_h_layout.addWidget(self.line_h_4, 0, 4, 1, 1)
        self.line_h_layout.addWidget(self.line_h_5, 0, 5, 1, 1)
        self.line_h_layout.addWidget(self.line_h_AVG, 0, 6, 1, 1)
        # line 1
        self.line_1 = QtWidgets.QPushButton()
        self.line_1.setObjectName('line')
        self.line_1_layout = QtWidgets.QGridLayout()
        self.line_1.setLayout(self.line_1_layout)
        self.line_1.setFixedHeight(50)
        # name
        self.line_1_name = QtWidgets.QLabel()
        self.line_1_name.setObjectName('cell')
        self.line_1_name.setText("-")
        self.line_1_name_layout = QtWidgets.QGridLayout()
        self.line_1_name.setLayout(self.line_1_name_layout)
        # 1
        self.line_1_1 = QtWidgets.QLabel()
        self.line_1_1.setObjectName('cell')
        self.line_1_1.setText("-")
        self.line_1_1_layout = QtWidgets.QGridLayout()
        self.line_1_1.setLayout(self.line_1_1_layout)
        # 2
        self.line_1_2 = QtWidgets.QLabel()
        self.line_1_2.setObjectName('cell')
        self.line_1_2.setText("-")
        self.line_1_2_layout = QtWidgets.QGridLayout()
        self.line_1_2.setLayout(self.line_1_2_layout)
        # 3
        self.line_1_3 = QtWidgets.QLabel()
        self.line_1_3.setObjectName('cell')
        self.line_1_3.setText("-")
        self.line_1_3_layout = QtWidgets.QGridLayout()
        self.line_1_3.setLayout(self.line_1_3_layout)
        # 4
        self.line_1_4 = QtWidgets.QLabel()
        self.line_1_4.setObjectName('cell')
        self.line_1_4.setText("-")
        self.line_1_4_layout = QtWidgets.QGridLayout()
        self.line_1_4.setLayout(self.line_1_4_layout)
        # 5
        self.line_1_5 = QtWidgets.QLabel()
        self.line_1_5.setObjectName('cell')
        self.line_1_5.setText("-")
        self.line_1_5_layout = QtWidgets.QGridLayout()
        self.line_1_5.setLayout(self.line_1_5_layout)
        # AVG
        self.line_1_AVG = QtWidgets.QLabel()
        self.line_1_AVG.setObjectName('cell')
        self.line_1_AVG.setText("-")
        self.line_1_AVG_layout = QtWidgets.QGridLayout()
        self.line_1_AVG.setLayout(self.line_1_AVG_layout)
        # assemble line 1
        self.line_1_layout.addWidget(self.line_1_name, 0, 0, 1, 1)
        self.line_1_layout.addWidget(self.line_1_1, 0, 1, 1, 1)
        self.line_1_layout.addWidget(self.line_1_2, 0, 2, 1, 1)
        self.line_1_layout.addWidget(self.line_1_3, 0, 3, 1, 1)
        self.line_1_layout.addWidget(self.line_1_4, 0, 4, 1, 1)
        self.line_1_layout.addWidget(self.line_1_5, 0, 5, 1, 1)
        self.line_1_layout.addWidget(self.line_1_AVG, 0, 6, 1, 1)
        # line 2
        self.line_2 = QtWidgets.QPushButton()
        self.line_2.setObjectName('line')
        self.line_2_layout = QtWidgets.QGridLayout()
        self.line_2.setLayout(self.line_2_layout)
        self.line_2.setFixedHeight(50)
        # name
        self.line_2_name = QtWidgets.QLabel()
        self.line_2_name.setObjectName('cell')
        self.line_2_name.setText("-")
        self.line_2_name_layout = QtWidgets.QGridLayout()
        self.line_2_name.setLayout(self.line_2_name_layout)
        # 1
        self.line_2_1 = QtWidgets.QLabel()
        self.line_2_1.setObjectName('cell')
        self.line_2_1.setText("-")
        self.line_2_1_layout = QtWidgets.QGridLayout()
        self.line_2_1.setLayout(self.line_2_1_layout)
        # 2
        self.line_2_2 = QtWidgets.QLabel()
        self.line_2_2.setObjectName('cell')
        self.line_2_2.setText("-")
        self.line_2_2_layout = QtWidgets.QGridLayout()
        self.line_2_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_2_3 = QtWidgets.QLabel()
        self.line_2_3.setObjectName('cell')
        self.line_2_3.setText("-")
        self.line_2_3_layout = QtWidgets.QGridLayout()
        self.line_2_3.setLayout(self.line_2_3_layout)
        # 4
        self.line_2_4 = QtWidgets.QLabel()
        self.line_2_4.setObjectName('cell')
        self.line_2_4.setText("-")
        self.line_2_4_layout = QtWidgets.QGridLayout()
        self.line_2_4.setLayout(self.line_2_4_layout)
        # 5
        self.line_2_5 = QtWidgets.QLabel()
        self.line_2_5.setObjectName('cell')
        self.line_2_5.setText("-")
        self.line_2_5_layout = QtWidgets.QGridLayout()
        self.line_2_5.setLayout(self.line_2_5_layout)
        # AVG
        self.line_2_AVG = QtWidgets.QLabel()
        self.line_2_AVG.setObjectName('cell')
        self.line_2_AVG.setText("-")
        self.line_2_AVG_layout = QtWidgets.QGridLayout()
        self.line_2_AVG.setLayout(self.line_2_AVG_layout)
        # assemble line 2
        self.line_2_layout.addWidget(self.line_2_name, 0, 0, 1, 1)
        self.line_2_layout.addWidget(self.line_2_1, 0, 1, 1, 1)
        self.line_2_layout.addWidget(self.line_2_2, 0, 2, 1, 1)
        self.line_2_layout.addWidget(self.line_2_3, 0, 3, 1, 1)
        self.line_2_layout.addWidget(self.line_2_4, 0, 4, 1, 1)
        self.line_2_layout.addWidget(self.line_2_5, 0, 5, 1, 1)
        self.line_2_layout.addWidget(self.line_2_AVG, 0, 6, 1, 1)
        # line 3
        self.line_3 = QtWidgets.QPushButton()
        self.line_3.setObjectName('line')
        self.line_3_layout = QtWidgets.QGridLayout()
        self.line_3.setLayout(self.line_3_layout)
        self.line_3.setFixedHeight(50)
        # name
        self.line_3_name = QtWidgets.QLabel()
        self.line_3_name.setObjectName('cell')
        self.line_3_name.setText("-")
        self.line_3_name_layout = QtWidgets.QGridLayout()
        self.line_3_name.setLayout(self.line_3_name_layout)
        # 1
        self.line_3_1 = QtWidgets.QLabel()
        self.line_3_1.setObjectName('cell')
        self.line_3_1.setText("-")
        self.line_3_1_layout = QtWidgets.QGridLayout()
        self.line_3_1.setLayout(self.line_3_1_layout)
        # 2
        self.line_3_2 = QtWidgets.QLabel()
        self.line_3_2.setObjectName('cell')
        self.line_3_2.setText("-")
        self.line_3_2_layout = QtWidgets.QGridLayout()
        self.line_3_2.setLayout(self.line_3_2_layout)
        # 3
        self.line_3_3 = QtWidgets.QLabel()
        self.line_3_3.setObjectName('cell')
        self.line_3_3.setText("-")
        self.line_3_3_layout = QtWidgets.QGridLayout()
        self.line_3_3.setLayout(self.line_3_3_layout)
        # 4
        self.line_3_4 = QtWidgets.QLabel()
        self.line_3_4.setObjectName('cell')
        self.line_3_4.setText("-")
        self.line_3_4_layout = QtWidgets.QGridLayout()
        self.line_3_4.setLayout(self.line_3_4_layout)
        # 5
        self.line_3_5 = QtWidgets.QLabel()
        self.line_3_5.setObjectName('cell')
        self.line_3_5.setText("-")
        self.line_3_5_layout = QtWidgets.QGridLayout()
        self.line_3_5.setLayout(self.line_3_5_layout)
        # AVG
        self.line_3_AVG = QtWidgets.QLabel()
        self.line_3_AVG.setObjectName('cell')
        self.line_3_AVG.setText("-")
        self.line_3_AVG_layout = QtWidgets.QGridLayout()
        self.line_3_AVG.setLayout(self.line_3_AVG_layout)
        # assemble line 3
        self.line_3_layout.addWidget(self.line_3_name, 0, 0, 1, 1)
        self.line_3_layout.addWidget(self.line_3_1, 0, 1, 1, 1)
        self.line_3_layout.addWidget(self.line_3_2, 0, 2, 1, 1)
        self.line_3_layout.addWidget(self.line_3_3, 0, 3, 1, 1)
        self.line_3_layout.addWidget(self.line_3_4, 0, 4, 1, 1)
        self.line_3_layout.addWidget(self.line_3_5, 0, 5, 1, 1)
        self.line_3_layout.addWidget(self.line_3_AVG, 0, 6, 1, 1)
        # line 4
        self.line_4 = QtWidgets.QPushButton()
        self.line_4.setObjectName('line')
        self.line_4_layout = QtWidgets.QGridLayout()
        self.line_4.setLayout(self.line_4_layout)
        self.line_4.setFixedHeight(50)
        # name
        self.line_4_name = QtWidgets.QLabel()
        self.line_4_name.setObjectName('cell')
        self.line_4_name.setText("-")
        self.line_4_name_layout = QtWidgets.QGridLayout()
        self.line_4_name.setLayout(self.line_4_name_layout)
        # 1
        self.line_4_1 = QtWidgets.QLabel()
        self.line_4_1.setObjectName('cell')
        self.line_4_1.setText("-")
        self.line_4_1_layout = QtWidgets.QGridLayout()
        self.line_4_1.setLayout(self.line_4_1_layout)
        # 2
        self.line_4_2 = QtWidgets.QLabel()
        self.line_4_2.setObjectName('cell')
        self.line_4_2.setText("-")
        self.line_4_2_layout = QtWidgets.QGridLayout()
        self.line_4_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_4_3 = QtWidgets.QLabel()
        self.line_4_3.setObjectName('cell')
        self.line_4_3.setText("-")
        self.line_4_3_layout = QtWidgets.QGridLayout()
        self.line_4_3.setLayout(self.line_4_3_layout)
        # 4
        self.line_4_4 = QtWidgets.QLabel()
        self.line_4_4.setObjectName('cell')
        self.line_4_4.setText("-")
        self.line_4_4_layout = QtWidgets.QGridLayout()
        self.line_4_4.setLayout(self.line_4_4_layout)
        # 5
        self.line_4_5 = QtWidgets.QLabel()
        self.line_4_5.setObjectName('cell')
        self.line_4_5.setText("-")
        self.line_4_5_layout = QtWidgets.QGridLayout()
        self.line_4_5.setLayout(self.line_4_5_layout)
        # AVG
        self.line_4_AVG = QtWidgets.QLabel()
        self.line_4_AVG.setObjectName('cell')
        self.line_4_AVG.setText("-")
        self.line_4_AVG_layout = QtWidgets.QGridLayout()
        self.line_4_AVG.setLayout(self.line_4_AVG_layout)
        # assemble line 4
        self.line_4_layout.addWidget(self.line_4_name, 0, 0, 1, 1)
        self.line_4_layout.addWidget(self.line_4_1, 0, 1, 1, 1)
        self.line_4_layout.addWidget(self.line_4_2, 0, 2, 1, 1)
        self.line_4_layout.addWidget(self.line_4_3, 0, 3, 1, 1)
        self.line_4_layout.addWidget(self.line_4_4, 0, 4, 1, 1)
        self.line_4_layout.addWidget(self.line_4_5, 0, 5, 1, 1)
        self.line_4_layout.addWidget(self.line_4_AVG, 0, 6, 1, 1)
        # line 5
        self.line_5 = QtWidgets.QPushButton()
        self.line_5.setObjectName('line')
        self.line_5_layout = QtWidgets.QGridLayout()
        self.line_5.setLayout(self.line_5_layout)
        self.line_5.setFixedHeight(50)
        # name
        self.line_5_name = QtWidgets.QLabel()
        self.line_5_name.setObjectName('cell')
        self.line_5_name.setText("-")
        self.line_5_name_layout = QtWidgets.QGridLayout()
        self.line_5_name.setLayout(self.line_5_name_layout)
        # 1
        self.line_5_1 = QtWidgets.QLabel()
        self.line_5_1.setObjectName('cell')
        self.line_5_1.setText("-")
        self.line_5_1_layout = QtWidgets.QGridLayout()
        self.line_5_1.setLayout(self.line_5_1_layout)
        # 2
        self.line_5_2 = QtWidgets.QLabel()
        self.line_5_2.setObjectName('cell')
        self.line_5_2.setText("-")
        self.line_5_2_layout = QtWidgets.QGridLayout()
        self.line_5_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_5_3 = QtWidgets.QLabel()
        self.line_5_3.setObjectName('cell')
        self.line_5_3.setText("-")
        self.line_5_3_layout = QtWidgets.QGridLayout()
        self.line_5_3.setLayout(self.line_5_3_layout)
        # 4
        self.line_5_4 = QtWidgets.QLabel()
        self.line_5_4.setObjectName('cell')
        self.line_5_4.setText("-")
        self.line_5_4_layout = QtWidgets.QGridLayout()
        self.line_5_4.setLayout(self.line_5_4_layout)
        # 5
        self.line_5_5 = QtWidgets.QLabel()
        self.line_5_5.setObjectName('cell')
        self.line_5_5.setText("-")
        self.line_5_5_layout = QtWidgets.QGridLayout()
        self.line_5_5.setLayout(self.line_5_5_layout)
        # AVG
        self.line_5_AVG = QtWidgets.QLabel()
        self.line_5_AVG.setObjectName('cell')
        self.line_5_AVG.setText("-")
        self.line_5_AVG_layout = QtWidgets.QGridLayout()
        self.line_5_AVG.setLayout(self.line_5_AVG_layout)
        # assemble line 5
        self.line_5_layout.addWidget(self.line_5_name, 0, 0, 1, 1)
        self.line_5_layout.addWidget(self.line_5_1, 0, 1, 1, 1)
        self.line_5_layout.addWidget(self.line_5_2, 0, 2, 1, 1)
        self.line_5_layout.addWidget(self.line_5_3, 0, 3, 1, 1)
        self.line_5_layout.addWidget(self.line_5_4, 0, 4, 1, 1)
        self.line_5_layout.addWidget(self.line_5_5, 0, 5, 1, 1)
        self.line_5_layout.addWidget(self.line_5_AVG, 0, 6, 1, 1)
        # line 6
        self.line_6 = QtWidgets.QPushButton()
        self.line_6.setObjectName('line')
        self.line_6_layout = QtWidgets.QGridLayout()
        self.line_6.setLayout(self.line_6_layout)
        self.line_6.setFixedHeight(50)
        # name
        self.line_6_name = QtWidgets.QLabel()
        self.line_6_name.setObjectName('cell')
        self.line_6_name.setText("-")
        self.line_6_name_layout = QtWidgets.QGridLayout()
        self.line_6_name.setLayout(self.line_6_name_layout)
        # 1
        self.line_6_1 = QtWidgets.QLabel()
        self.line_6_1.setObjectName('cell')
        self.line_6_1.setText("-")
        self.line_6_1_layout = QtWidgets.QGridLayout()
        self.line_6_1.setLayout(self.line_6_1_layout)
        # 2
        self.line_6_2 = QtWidgets.QLabel()
        self.line_6_2.setObjectName('cell')
        self.line_6_2.setText("-")
        self.line_6_2_layout = QtWidgets.QGridLayout()
        self.line_6_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_6_3 = QtWidgets.QLabel()
        self.line_6_3.setObjectName('cell')
        self.line_6_3.setText("-")
        self.line_6_3_layout = QtWidgets.QGridLayout()
        self.line_6_3.setLayout(self.line_6_3_layout)
        # 4
        self.line_6_4 = QtWidgets.QLabel()
        self.line_6_4.setObjectName('cell')
        self.line_6_4.setText("-")
        self.line_6_4_layout = QtWidgets.QGridLayout()
        self.line_6_4.setLayout(self.line_6_4_layout)
        # 5
        self.line_6_5 = QtWidgets.QLabel()
        self.line_6_5.setObjectName('cell')
        self.line_6_5.setText("-")
        self.line_6_5_layout = QtWidgets.QGridLayout()
        self.line_6_5.setLayout(self.line_6_5_layout)
        # AVG
        self.line_6_AVG = QtWidgets.QLabel()
        self.line_6_AVG.setObjectName('cell')
        self.line_6_AVG.setText("-")
        self.line_6_AVG_layout = QtWidgets.QGridLayout()
        self.line_6_AVG.setLayout(self.line_6_AVG_layout)
        # assemble line 6
        self.line_6_layout.addWidget(self.line_6_name, 0, 0, 1, 1)
        self.line_6_layout.addWidget(self.line_6_1, 0, 1, 1, 1)
        self.line_6_layout.addWidget(self.line_6_2, 0, 2, 1, 1)
        self.line_6_layout.addWidget(self.line_6_3, 0, 3, 1, 1)
        self.line_6_layout.addWidget(self.line_6_4, 0, 4, 1, 1)
        self.line_6_layout.addWidget(self.line_6_5, 0, 5, 1, 1)
        self.line_6_layout.addWidget(self.line_6_AVG, 0, 6, 1, 1)
        # line 7
        self.line_7 = QtWidgets.QPushButton()
        self.line_7.setObjectName('line')
        self.line_7_layout = QtWidgets.QGridLayout()
        self.line_7.setLayout(self.line_7_layout)
        self.line_7.setFixedHeight(50)
        # name
        self.line_7_name = QtWidgets.QLabel()
        self.line_7_name.setObjectName('cell')
        self.line_7_name.setText("-")
        self.line_7_name_layout = QtWidgets.QGridLayout()
        self.line_7_name.setLayout(self.line_7_name_layout)
        # 1
        self.line_7_1 = QtWidgets.QLabel()
        self.line_7_1.setObjectName('cell')
        self.line_7_1.setText("-")
        self.line_7_1_layout = QtWidgets.QGridLayout()
        self.line_7_1.setLayout(self.line_7_1_layout)
        # 2
        self.line_7_2 = QtWidgets.QLabel()
        self.line_7_2.setObjectName('cell')
        self.line_7_2.setText("-")
        self.line_7_2_layout = QtWidgets.QGridLayout()
        self.line_7_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_7_3 = QtWidgets.QLabel()
        self.line_7_3.setObjectName('cell')
        self.line_7_3.setText("-")
        self.line_7_3_layout = QtWidgets.QGridLayout()
        self.line_7_3.setLayout(self.line_7_3_layout)
        # 4
        self.line_7_4 = QtWidgets.QLabel()
        self.line_7_4.setObjectName('cell')
        self.line_7_4.setText("-")
        self.line_7_4_layout = QtWidgets.QGridLayout()
        self.line_7_4.setLayout(self.line_7_4_layout)
        # 5
        self.line_7_5 = QtWidgets.QLabel()
        self.line_7_5.setObjectName('cell')
        self.line_7_5.setText("-")
        self.line_7_5_layout = QtWidgets.QGridLayout()
        self.line_7_5.setLayout(self.line_7_5_layout)
        # AVG
        self.line_7_AVG = QtWidgets.QLabel()
        self.line_7_AVG.setObjectName('cell')
        self.line_7_AVG.setText("-")
        self.line_7_AVG_layout = QtWidgets.QGridLayout()
        self.line_7_AVG.setLayout(self.line_7_AVG_layout)
        # assemble line 7
        self.line_7_layout.addWidget(self.line_7_name, 0, 0, 1, 1)
        self.line_7_layout.addWidget(self.line_7_1, 0, 1, 1, 1)
        self.line_7_layout.addWidget(self.line_7_2, 0, 2, 1, 1)
        self.line_7_layout.addWidget(self.line_7_3, 0, 3, 1, 1)
        self.line_7_layout.addWidget(self.line_7_4, 0, 4, 1, 1)
        self.line_7_layout.addWidget(self.line_7_5, 0, 5, 1, 1)
        self.line_7_layout.addWidget(self.line_7_AVG, 0, 6, 1, 1)
        # line 8
        self.line_8 = QtWidgets.QPushButton()
        self.line_8.setObjectName('line')
        self.line_8_layout = QtWidgets.QGridLayout()
        self.line_8.setLayout(self.line_8_layout)
        self.line_8.setFixedHeight(50)
        # name
        self.line_8_name = QtWidgets.QLabel()
        self.line_8_name.setObjectName('cell')
        self.line_8_name.setText("-")
        self.line_8_name_layout = QtWidgets.QGridLayout()
        self.line_8_name.setLayout(self.line_8_name_layout)
        # 1
        self.line_8_1 = QtWidgets.QLabel()
        self.line_8_1.setObjectName('cell')
        self.line_8_1.setText("-")
        self.line_8_1_layout = QtWidgets.QGridLayout()
        self.line_8_1.setLayout(self.line_8_1_layout)
        # 2
        self.line_8_2 = QtWidgets.QLabel()
        self.line_8_2.setObjectName('cell')
        self.line_8_2.setText("-")
        self.line_8_2_layout = QtWidgets.QGridLayout()
        self.line_8_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_8_3 = QtWidgets.QLabel()
        self.line_8_3.setObjectName('cell')
        self.line_8_3.setText("-")
        self.line_8_3_layout = QtWidgets.QGridLayout()
        self.line_8_3.setLayout(self.line_8_3_layout)
        # 4
        self.line_8_4 = QtWidgets.QLabel()
        self.line_8_4.setObjectName('cell')
        self.line_8_4.setText("-")
        self.line_8_4_layout = QtWidgets.QGridLayout()
        self.line_8_4.setLayout(self.line_8_4_layout)
        # 5
        self.line_8_5 = QtWidgets.QLabel()
        self.line_8_5.setObjectName('cell')
        self.line_8_5.setText("-")
        self.line_8_5_layout = QtWidgets.QGridLayout()
        self.line_8_5.setLayout(self.line_8_5_layout)
        # AVG
        self.line_8_AVG = QtWidgets.QLabel()
        self.line_8_AVG.setObjectName('cell')
        self.line_8_AVG.setText("-")
        self.line_8_AVG_layout = QtWidgets.QGridLayout()
        self.line_8_AVG.setLayout(self.line_8_AVG_layout)
        # assemble line 8
        self.line_8_layout.addWidget(self.line_8_name, 0, 0, 1, 1)
        self.line_8_layout.addWidget(self.line_8_1, 0, 1, 1, 1)
        self.line_8_layout.addWidget(self.line_8_2, 0, 2, 1, 1)
        self.line_8_layout.addWidget(self.line_8_3, 0, 3, 1, 1)
        self.line_8_layout.addWidget(self.line_8_4, 0, 4, 1, 1)
        self.line_8_layout.addWidget(self.line_8_5, 0, 5, 1, 1)
        self.line_8_layout.addWidget(self.line_8_AVG, 0, 6, 1, 1)
        # line 9
        self.line_9 = QtWidgets.QPushButton()
        self.line_9.setObjectName('line')
        self.line_9_layout = QtWidgets.QGridLayout()
        self.line_9.setLayout(self.line_9_layout)
        self.line_9.setFixedHeight(50)
        # name
        self.line_9_name = QtWidgets.QLabel()
        self.line_9_name.setObjectName('cell')
        self.line_9_name.setText("-")
        self.line_9_name_layout = QtWidgets.QGridLayout()
        self.line_9_name.setLayout(self.line_9_name_layout)
        # 1
        self.line_9_1 = QtWidgets.QLabel()
        self.line_9_1.setObjectName('cell')
        self.line_9_1.setText("-")
        self.line_9_1_layout = QtWidgets.QGridLayout()
        self.line_9_1.setLayout(self.line_9_1_layout)
        # 2
        self.line_9_2 = QtWidgets.QLabel()
        self.line_9_2.setObjectName('cell')
        self.line_9_2.setText("-")
        self.line_9_2_layout = QtWidgets.QGridLayout()
        self.line_9_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_9_3 = QtWidgets.QLabel()
        self.line_9_3.setObjectName('cell')
        self.line_9_3.setText("-")
        self.line_9_3_layout = QtWidgets.QGridLayout()
        self.line_9_3.setLayout(self.line_9_3_layout)
        # 4
        self.line_9_4 = QtWidgets.QLabel()
        self.line_9_4.setObjectName('cell')
        self.line_9_4.setText("-")
        self.line_9_4_layout = QtWidgets.QGridLayout()
        self.line_9_4.setLayout(self.line_9_4_layout)
        # 5
        self.line_9_5 = QtWidgets.QLabel()
        self.line_9_5.setObjectName('cell')
        self.line_9_5.setText("-")
        self.line_9_5_layout = QtWidgets.QGridLayout()
        self.line_9_5.setLayout(self.line_9_5_layout)
        # AVG
        self.line_9_AVG = QtWidgets.QLabel()
        self.line_9_AVG.setObjectName('cell')
        self.line_9_AVG.setText("-")
        self.line_9_AVG_layout = QtWidgets.QGridLayout()
        self.line_9_AVG.setLayout(self.line_9_AVG_layout)
        # assemble line 9
        self.line_9_layout.addWidget(self.line_9_name, 0, 0, 1, 1)
        self.line_9_layout.addWidget(self.line_9_1, 0, 1, 1, 1)
        self.line_9_layout.addWidget(self.line_9_2, 0, 2, 1, 1)
        self.line_9_layout.addWidget(self.line_9_3, 0, 3, 1, 1)
        self.line_9_layout.addWidget(self.line_9_4, 0, 4, 1, 1)
        self.line_9_layout.addWidget(self.line_9_5, 0, 5, 1, 1)
        self.line_9_layout.addWidget(self.line_9_AVG, 0, 6, 1, 1)
        # line 10
        self.line_10 = QtWidgets.QPushButton()
        self.line_10.setObjectName('line')
        self.line_10_layout = QtWidgets.QGridLayout()
        self.line_10.setLayout(self.line_10_layout)
        self.line_10.setFixedHeight(50)
        # name
        self.line_10_name = QtWidgets.QLabel()
        self.line_10_name.setObjectName('cell')
        self.line_10_name.setText("-")
        self.line_10_name_layout = QtWidgets.QGridLayout()
        self.line_10_name.setLayout(self.line_10_name_layout)
        # 1
        self.line_10_1 = QtWidgets.QLabel()
        self.line_10_1.setObjectName('cell')
        self.line_10_1.setText("-")
        self.line_10_1_layout = QtWidgets.QGridLayout()
        self.line_10_1.setLayout(self.line_10_1_layout)
        # 2
        self.line_10_2 = QtWidgets.QLabel()
        self.line_10_2.setObjectName('cell')
        self.line_10_2.setText("-")
        self.line_10_2_layout = QtWidgets.QGridLayout()
        self.line_10_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_10_3 = QtWidgets.QLabel()
        self.line_10_3.setObjectName('cell')
        self.line_10_3.setText("-")
        self.line_10_3_layout = QtWidgets.QGridLayout()
        self.line_10_3.setLayout(self.line_10_3_layout)
        # 4
        self.line_10_4 = QtWidgets.QLabel()
        self.line_10_4.setObjectName('cell')
        self.line_10_4.setText("-")
        self.line_10_4_layout = QtWidgets.QGridLayout()
        self.line_10_4.setLayout(self.line_10_4_layout)
        # 5
        self.line_10_5 = QtWidgets.QLabel()
        self.line_10_5.setObjectName('cell')
        self.line_10_5.setText("-")
        self.line_10_5_layout = QtWidgets.QGridLayout()
        self.line_10_5.setLayout(self.line_10_5_layout)
        # AVG
        self.line_10_AVG = QtWidgets.QLabel()
        self.line_10_AVG.setObjectName('cell')
        self.line_10_AVG.setText("-")
        self.line_10_AVG_layout = QtWidgets.QGridLayout()
        self.line_10_AVG.setLayout(self.line_10_AVG_layout)
        # assemble line 10
        self.line_10_layout.addWidget(self.line_10_name, 0, 0, 1, 1)
        self.line_10_layout.addWidget(self.line_10_1, 0, 1, 1, 1)
        self.line_10_layout.addWidget(self.line_10_2, 0, 2, 1, 1)
        self.line_10_layout.addWidget(self.line_10_3, 0, 3, 1, 1)
        self.line_10_layout.addWidget(self.line_10_4, 0, 4, 1, 1)
        self.line_10_layout.addWidget(self.line_10_5, 0, 5, 1, 1)
        self.line_10_layout.addWidget(self.line_10_AVG, 0, 6, 1, 1)
        # line 11
        self.line_11 = QtWidgets.QPushButton()
        self.line_11.setObjectName('line')
        self.line_11_layout = QtWidgets.QGridLayout()
        self.line_11.setLayout(self.line_11_layout)
        self.line_11.setFixedHeight(50)
        # name
        self.line_11_name = QtWidgets.QLabel()
        self.line_11_name.setObjectName('cell')
        self.line_11_name.setText("-")
        self.line_11_name_layout = QtWidgets.QGridLayout()
        self.line_11_name.setLayout(self.line_11_name_layout)
        # 1
        self.line_11_1 = QtWidgets.QLabel()
        self.line_11_1.setObjectName('cell')
        self.line_11_1.setText("-")
        self.line_11_1_layout = QtWidgets.QGridLayout()
        self.line_11_1.setLayout(self.line_11_1_layout)
        # 2
        self.line_11_2 = QtWidgets.QLabel()
        self.line_11_2.setObjectName('cell')
        self.line_11_2.setText("-")
        self.line_11_2_layout = QtWidgets.QGridLayout()
        self.line_11_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_11_3 = QtWidgets.QLabel()
        self.line_11_3.setObjectName('cell')
        self.line_11_3.setText("-")
        self.line_11_3_layout = QtWidgets.QGridLayout()
        self.line_11_3.setLayout(self.line_11_3_layout)
        # 4
        self.line_11_4 = QtWidgets.QLabel()
        self.line_11_4.setObjectName('cell')
        self.line_11_4.setText("-")
        self.line_11_4_layout = QtWidgets.QGridLayout()
        self.line_11_4.setLayout(self.line_11_4_layout)
        # 5
        self.line_11_5 = QtWidgets.QLabel()
        self.line_11_5.setObjectName('cell')
        self.line_11_5.setText("-")
        self.line_11_5_layout = QtWidgets.QGridLayout()
        self.line_11_5.setLayout(self.line_11_5_layout)
        # AVG
        self.line_11_AVG = QtWidgets.QLabel()
        self.line_11_AVG.setObjectName('cell')
        self.line_11_AVG.setText("-")
        self.line_11_AVG_layout = QtWidgets.QGridLayout()
        self.line_11_AVG.setLayout(self.line_11_AVG_layout)
        # assemble line 11
        self.line_11_layout.addWidget(self.line_11_name, 0, 0, 1, 1)
        self.line_11_layout.addWidget(self.line_11_1, 0, 1, 1, 1)
        self.line_11_layout.addWidget(self.line_11_2, 0, 2, 1, 1)
        self.line_11_layout.addWidget(self.line_11_3, 0, 3, 1, 1)
        self.line_11_layout.addWidget(self.line_11_4, 0, 4, 1, 1)
        self.line_11_layout.addWidget(self.line_11_5, 0, 5, 1, 1)
        self.line_11_layout.addWidget(self.line_11_AVG, 0, 6, 1, 1)
        # line 12
        self.line_12 = QtWidgets.QPushButton()
        self.line_12.setObjectName('line')
        self.line_12_layout = QtWidgets.QGridLayout()
        self.line_12.setLayout(self.line_12_layout)
        self.line_12.setFixedHeight(50)
        # name
        self.line_12_name = QtWidgets.QLabel()
        self.line_12_name.setObjectName('cell')
        self.line_12_name.setText("-")
        self.line_12_name_layout = QtWidgets.QGridLayout()
        self.line_12_name.setLayout(self.line_12_name_layout)
        # 1
        self.line_12_1 = QtWidgets.QLabel()
        self.line_12_1.setObjectName('cell')
        self.line_12_1.setText("-")
        self.line_12_1_layout = QtWidgets.QGridLayout()
        self.line_12_1.setLayout(self.line_12_1_layout)
        # 2
        self.line_12_2 = QtWidgets.QLabel()
        self.line_12_2.setObjectName('cell')
        self.line_12_2.setText("-")
        self.line_12_2_layout = QtWidgets.QGridLayout()
        self.line_12_2.setLayout(self.line_2_2_layout)
        # 3
        self.line_12_3 = QtWidgets.QLabel()
        self.line_12_3.setObjectName('cell')
        self.line_12_3.setText("-")
        self.line_12_3_layout = QtWidgets.QGridLayout()
        self.line_12_3.setLayout(self.line_12_3_layout)
        # 4
        self.line_12_4 = QtWidgets.QLabel()
        self.line_12_4.setObjectName('cell')
        self.line_12_4.setText("-")
        self.line_12_4_layout = QtWidgets.QGridLayout()
        self.line_12_4.setLayout(self.line_12_4_layout)
        # 5
        self.line_12_5 = QtWidgets.QLabel()
        self.line_12_5.setObjectName('cell')
        self.line_12_5.setText("-")
        self.line_12_5_layout = QtWidgets.QGridLayout()
        self.line_12_5.setLayout(self.line_12_5_layout)
        # AVG
        self.line_12_AVG = QtWidgets.QLabel()
        self.line_12_AVG.setObjectName('cell')
        self.line_12_AVG.setText("-")
        self.line_12_AVG_layout = QtWidgets.QGridLayout()
        self.line_12_AVG.setLayout(self.line_12_AVG_layout)
        # assemble line 12
        self.line_12_layout.addWidget(self.line_12_name, 0, 0, 1, 1)
        self.line_12_layout.addWidget(self.line_12_1, 0, 1, 1, 1)
        self.line_12_layout.addWidget(self.line_12_2, 0, 2, 1, 1)
        self.line_12_layout.addWidget(self.line_12_3, 0, 3, 1, 1)
        self.line_12_layout.addWidget(self.line_12_4, 0, 4, 1, 1)
        self.line_12_layout.addWidget(self.line_12_5, 0, 5, 1, 1)
        self.line_12_layout.addWidget(self.line_12_AVG, 0, 6, 1, 1)
        #
        # assemble list
        self.list_layout.addWidget(self.line_h, 0, 0, 1, 1)
        self.list_layout.addWidget(self.line_1, 1, 0, 1, 1)
        self.list_layout.addWidget(self.line_2, 2, 0, 1, 1)
        self.list_layout.addWidget(self.line_3, 3, 0, 1, 1)
        self.list_layout.addWidget(self.line_4, 4, 0, 1, 1)
        self.list_layout.addWidget(self.line_5, 5, 0, 1, 1)
        self.list_layout.addWidget(self.line_6, 6, 0, 1, 1)
        self.list_layout.addWidget(self.line_7, 7, 0, 1, 1)
        self.list_layout.addWidget(self.line_8, 8, 0, 1, 1)
        self.list_layout.addWidget(self.line_9, 9, 0, 1, 1)
        self.list_layout.addWidget(self.line_10, 10, 0, 1, 1)
        self.list_layout.addWidget(self.line_11, 11, 0, 1, 1)
        self.list_layout.addWidget(self.line_12, 12, 0, 1, 1)
        self.list_layout.setSpacing(2)
        self.list.setStyleSheet('''
            QPushButton#header{
                border: none;
                border-bottom: 2px solid white;
                background-color: #0E1A49;
                border-radius: 10px;
            }
            QPushButton#line{
                border: none;
                background-color: #0E1A49;
                border-radius: 10px;
            }
            QPushButton#line:hover{
                border: none;
                border-left: 4px solid white;
                background-color: #0E1A49;
                border-radius: 10px;
            }
            QLabel{
                color: white;
                border: none;
                font-size: 18px;
                font-weight: 700;
                font-family: "微软雅黑";
            }
            ''')

    def init_assemble(self):
        # 堆栈控件
        self.stacked_Widget.addWidget(self.final_widget)
        self.stacked_Widget.addWidget(self.list)
        # 放置控件
        self.main_layout.addWidget(self.left_widget, 0, 0, 11, 2)
        self.main_layout.addWidget(self.stacked_Widget, 0, 2, 11, 13)
        self.main_layout.addWidget(self.close, 0, 0, 1, 1)
        self.main_layout.addWidget(self.reset, 0, 1, 1, 12)
        # 设置主部件
        self.setCentralWidget(self.main_widget)
        self.setWindowOpacity(1)  # 设置窗口透明度
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置透明窗口背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(5)
