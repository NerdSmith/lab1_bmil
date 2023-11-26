from collections import defaultdict

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QVBoxLayout, QLabel

from pyui.ui_dict_dialog import Ui_Form
from widgets.PlotWidget import PlotWidget


class FreqWindow(QDialog):
    def __init__(self, password, alphabet):
        super(FreqWindow, self).__init__()
        self.password = password
        self.alphabet = alphabet

        self.freq_dict = defaultdict(lambda: 0)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.make_dict()
        self.fill_table()
        self.plot_bars()

        self.show()

    def make_dict(self):
        for letter in self.alphabet:
            self.freq_dict[letter] = self.password.count(letter)

    def fill_table(self):
        self.ui.freq_dict_table.setColumnCount(2)
        self.ui.freq_dict_table.setHorizontalHeaderLabels(["Буква", "Частота"])
        self.ui.freq_dict_table.setRowCount(len(self.freq_dict))
        for idx, (k, v) in enumerate(self.freq_dict.items()):
            self.ui.freq_dict_table.setItem(idx, 0, QTableWidgetItem(k))
            self.ui.freq_dict_table.setItem(idx, 1, QTableWidgetItem(str(v)))

    def plot_bars(self):
        layout = QVBoxLayout()
        pw = PlotWidget(self.ui.dia_frame, data={
            "x": self.freq_dict.keys(),
            "y": self.freq_dict.values()
        })
        layout.addWidget(pw.toolbar)
        layout.addWidget(pw)
        self.ui.dia_frame.setLayout(layout)



