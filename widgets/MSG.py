from PySide6.QtWidgets import QMessageBox


class MSG(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)

        # self.setIcon(QMessageBox.Information)

        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        self.exec()

