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
                border-radius: 5px;
            }
            QPushButton:hover{
                background: red;
            }
            ''')
        self.reset = QtWidgets.QPushButton(qtawesome.icon('fa.refresh', color='white'), '')
        self.reset.clicked.connect(lambda: self.doreset())
        self.reset.setFixedSize(30, 30)
        self.reset.setStyleSheet('''
            QPushButton{
                background: #FF6F61;
                border-radius: 5px;
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
        self.L_lable_1 = QtWidgets.QPushButton('决赛')
        self.L_lable_1.setObjectName('L_lable')
        self.L_lable_2 = QtWidgets.QPushButton('选手资料')
        self.L_lable_2.setObjectName('L_lable')
        # 按钮
        # ,lable 1
        self.L_button_1 = QtWidgets.QPushButton('1V1')
        self.L_button_1.setObjectName('L_button')
        self.L_button_1.clicked.connect(lambda: self.final())
        self.L_button_2 = QtWidgets.QPushButton('成绩栏')
        self.L_button_2.setObjectName('L_button')
        # ,lable 2
        self.L_button_3 = QtWidgets.QPushButton('按钮3')
        self.L_button_3.setObjectName('L_button')
        self.L_button_4 = QtWidgets.QPushButton('按钮4')
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
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;

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

    # 创建右侧控件,决赛成绩栏,网格布局
    def init_final_widget(self):
        self.final_widget = QtWidgets.QWidget()
        self.final_widget.setObjectName('final_widget')
        self.final_layout = QtWidgets.QGridLayout()
        self.final_widget.setLayout(self.final_layout)
        self.final_widget.setFixedHeight(200)
        self.final_widget.hide()
        # 创建右侧控件内部件
        # 第一行
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
        self.p_1_1.clicked.connect(lambda: self.setResult(1))
        # r2
        self.p_1_2 = QtWidgets.QPushButton()
        self.p_1_2.setObjectName('upper')
        self.p_1_2_layout = QtWidgets.QGridLayout()
        self.p_1_2.setLayout(self.p_1_2_layout)
        self.p_1_2.setText('-')
        self.p_1_2.clicked.connect(lambda: self.setResult(2))
        # r3
        self.p_1_3 = QtWidgets.QPushButton()
        self.p_1_3.setObjectName('upper')
        self.p_1_3_layout = QtWidgets.QGridLayout()
        self.p_1_3.setLayout(self.p_1_3_layout)
        self.p_1_3.setText('-')
        self.p_1_3.clicked.connect(lambda: self.setResult(3))
        # r4
        self.p_1_4 = QtWidgets.QPushButton()
        self.p_1_4.setObjectName('upper')
        self.p_1_4_layout = QtWidgets.QGridLayout()
        self.p_1_4.setLayout(self.p_1_4_layout)
        self.p_1_4.setText('-')
        self.p_1_4.clicked.connect(lambda: self.setResult(4))
        # r5
        self.p_1_5 = QtWidgets.QPushButton()
        self.p_1_5.setObjectName('upper_last')
        self.p_1_5_layout = QtWidgets.QGridLayout()
        self.p_1_5.setLayout(self.p_1_5_layout)
        self.p_1_5.setText('-')
        self.p_1_5.clicked.connect(lambda: self.setResult(5))
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
        self.p_2_1.clicked.connect(lambda: self.setResult(6))
        # r2
        self.p_2_2 = QtWidgets.QPushButton()
        self.p_2_2.setObjectName('lower')
        self.p_2_2_layout = QtWidgets.QGridLayout()
        self.p_2_2.setLayout(self.p_2_2_layout)
        self.p_2_2.setText('-')
        self.p_2_2.clicked.connect(lambda: self.setResult(7))
        # r3
        self.p_2_3 = QtWidgets.QPushButton()
        self.p_2_3.setObjectName('lower')
        self.p_2_3_layout = QtWidgets.QGridLayout()
        self.p_2_3.setLayout(self.p_2_3_layout)
        self.p_2_3.setText('-')
        self.p_2_3.clicked.connect(lambda: self.setResult(8))
        # r4
        self.p_2_4 = QtWidgets.QPushButton()
        self.p_2_4.setObjectName('lower')
        self.p_2_4_layout = QtWidgets.QGridLayout()
        self.p_2_4.setLayout(self.p_2_4_layout)
        self.p_2_4.setText('-')
        self.p_2_4.clicked.connect(lambda: self.setResult(9))
        # r5
        self.p_2_5 = QtWidgets.QPushButton()
        self.p_2_5.setObjectName('lower_last')
        self.p_2_5_layout = QtWidgets.QGridLayout()
        self.p_2_5.setLayout(self.p_2_5_layout)
        self.p_2_5.setText('-')
        self.p_2_5.clicked.connect(lambda: self.setResult(10))
        # 放置右侧控件内部件
        # 放置结果输出，临时组件
        self.final_layout.addWidget(self.p_1, 1, 0, 1, 1)
        self.final_layout.addWidget(self.p_1_1, 1, 1, 1, 1)
        self.final_layout.addWidget(self.p_1_2, 1, 2, 1, 1)
        self.final_layout.addWidget(self.p_1_3, 1, 3, 1, 1)
        self.final_layout.addWidget(self.p_1_4, 1, 4, 1, 1)
        self.final_layout.addWidget(self.p_1_5, 1, 5, 1, 1)
        self.final_layout.addWidget(self.p_2, 2, 0, 1, 1)
        self.final_layout.addWidget(self.p_2_1, 2, 1, 1, 1)
        self.final_layout.addWidget(self.p_2_2, 2, 2, 1, 1)
        self.final_layout.addWidget(self.p_2_3, 2, 3, 1, 1)
        self.final_layout.addWidget(self.p_2_4, 2, 4, 1, 1)
        self.final_layout.addWidget(self.p_2_5, 2, 5, 1, 1)
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
            }
            QPushButton#upper_last:hover{
                color: red;
                font-size: 30px;
                font-weight: 900;
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
            }
            QPushButton#lower_last:hover{
                color: red;
                font-size: 30px;
                font-weight: 900;
            }
            ''')

    def init_assemble(self):
        # 放置控件
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.final_widget, 0, 2, 12, 10)
        self.main_layout.addWidget(self.close, 0, 0, 1, 1)
        self.main_layout.addWidget(self.reset, 0, 1, 1, 12)
        # 设置主部件
        self.setCentralWidget(self.main_widget)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置透明窗口背景
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(5)
