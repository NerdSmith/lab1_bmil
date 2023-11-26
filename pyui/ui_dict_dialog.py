# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dict_dialogVKztAz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(597, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.freq_dict_table = QTableWidget(self.frame)
        self.freq_dict_table.setObjectName(u"freq_dict_table")

        self.verticalLayout.addWidget(self.freq_dict_table)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_2.addWidget(self.label_2)

        self.dia_frame = QFrame(self.frame_2)
        self.dia_frame.setObjectName(u"dia_frame")
        self.dia_frame.setMinimumSize(QSize(300, 0))
        self.dia_frame.setFrameShape(QFrame.StyledPanel)
        self.dia_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.dia_frame)

        self.splitter.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441\u0442\u043e\u0442\u043d\u044b\u0439 \u0441\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
    # retranslateUi

