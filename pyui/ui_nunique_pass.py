# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nunique_passPiGLVZ.ui'
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
        Form.resize(365, 307)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.non_unique_passwords_table = QTableWidget(Form)
        self.non_unique_passwords_table.setObjectName(u"non_unique_passwords_table")

        self.gridLayout.addWidget(self.non_unique_passwords_table, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u043d\u0435\u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
    # retranslateUi

