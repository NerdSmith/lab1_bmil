import random

import matplotlib

from widgets.LoginWindow import LoginWindow
from widgets.NUniquePasswordsWindow import NUniquePasswordsWindow
from widgets.SignUpWindow import SignUpWindow

matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow

from core.alphabet import Alphabet
from pyui.ui_main_wnd import Ui_MainWindow
from widgets.FreqWindow import FreqWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.alphabet = Alphabet()
        self.curr_alphabet = []

        self.last_password = []

        self.ui.alphabet_len_inp_2.setMaximum(len(self.alphabet.all_chars))
        self.ui.alphabet_len_inp_2.setMinimum(0)
        self.ui.alphabet_len_inp_2.valueChanged.connect(lambda x: self.update_alphabet(x))
        self.ui.alphabet_len_inp_2.setValue(1)

        self.ui.password_len_inp.setMinimum(1)
        self.ui.password_len_inp.setMaximum(100)

        self.ui.gen_pass_btn.clicked.connect(self.gen_password)
        self.ui.open_dict_btn.clicked.connect(self.open_dict)
        self.ui.signup_btn.clicked.connect(self.open_signup)
        self.ui.list_auth_btn.clicked.connect(self.open_nu_list)
        self.ui.login_btn.clicked.connect(self.open_login_wnd)

    def update_alphabet(self, x):
        self.curr_alphabet = self.alphabet.get_n_symbols(x)

        self.ui.alphabet_list_view.clear()
        self.ui.alphabet_list_view.addItems(self.curr_alphabet)

    def _get_pass_len(self):
        return self.ui.password_len_inp.value()

    def gen_password(self):
        password = []
        for i in range(self._get_pass_len()):
            symbol = random.choice(self.curr_alphabet)
            password.append(symbol)
        self.last_password = password
        self.ui.password_inp.setText("".join(password))

    def open_dict(self):
        if self.last_password:
            self.d = FreqWindow(self.last_password, self.curr_alphabet)
            self.d.exec()

    def open_signup(self):
        self.sup = SignUpWindow()
        self.sup.exec()

    def open_nu_list(self):
        self.l = NUniquePasswordsWindow()
        self.l.exec()

    def open_login_wnd(self):
        self.lw = LoginWindow()
        self.lw.exec()