# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialogWhwRVP.ui'
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
        Form.resize(366, 366)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.username_edit = QLineEdit(Form)
        self.username_edit.setObjectName(u"username_edit")

        self.gridLayout.addWidget(self.username_edit, 0, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.id_edit = QLineEdit(Form)
        self.id_edit.setObjectName(u"id_edit")

        self.gridLayout.addWidget(self.id_edit, 0, 4, 1, 1)

        self.password_edit = QLineEdit(Form)
        self.password_edit.setObjectName(u"password_edit")

        self.gridLayout.addWidget(self.password_edit, 3, 2, 1, 3)

        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")

        self.gridLayout.addWidget(self.login_btn, 5, 0, 1, 5)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Id", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

