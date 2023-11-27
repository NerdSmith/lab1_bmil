from PySide6.QtWidgets import QDialog, QTableWidgetItem

from db.user_rep import UserRepository
from pyui.ui_nunique_pass import Ui_Form


class NUniquePasswordsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.u_rep = UserRepository()

        nu_list = self.u_rep.get_non_unique()
        self.fill_table(nu_list)

    def fill_table(self, nulist):
        self.ui.non_unique_passwords_table.setColumnCount(2)
        self.ui.non_unique_passwords_table.setHorizontalHeaderLabels(["Имя", "Пароль"])
        self.ui.non_unique_passwords_table.setRowCount(len(nulist))
        for idx, user in enumerate(nulist):
            self.ui.non_unique_passwords_table.setItem(idx, 0, QTableWidgetItem(user.name))
            self.ui.non_unique_passwords_table.setItem(idx, 1, QTableWidgetItem(user.password))
