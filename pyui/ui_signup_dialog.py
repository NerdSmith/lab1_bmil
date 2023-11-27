# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_dialogXLeUiC.ui'
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
        Form.resize(364, 170)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.final_sign_up = QPushButton(Form)
        self.final_sign_up.setObjectName(u"final_sign_up")

        self.gridLayout.addWidget(self.final_sign_up, 5, 0, 1, 2)

        self.l_3 = QLabel(Form)
        self.l_3.setObjectName(u"l_3")

        self.gridLayout.addWidget(self.l_3, 2, 0, 1, 2)

        self.password_edit = QLineEdit(Form)
        self.password_edit.setObjectName(u"password_edit")

        self.gridLayout.addWidget(self.password_edit, 1, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.username_edit = QLineEdit(Form)
        self.username_edit.setObjectName(u"username_edit")

        self.gridLayout.addWidget(self.username_edit, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.l_4 = QLabel(Form)
        self.l_4.setObjectName(u"l_4")

        self.gridLayout.addWidget(self.l_4, 3, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.final_sign_up.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.l_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.l_4.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

