from statistics import mean

from PySide6.QtCore import QEvent, QDateTime
from PySide6.QtWidgets import QDialog

from core.biometric import Biometric
from pyui.ui_signup_dialog import Ui_Form


class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.key_pressed_time = None
        self.last_key_release_time = None

        self.ui.password_edit.installEventFilter(self)

        self.bio = Biometric()

        self.ui.final_sign_up.clicked.connect(self.handle_submit)

    def eventFilter(self, obj, event):
        if obj == self.ui.password_edit and event.type() == QEvent.KeyPress:
            if event.isAutoRepeat():
                # Клавиша удерживается
                pass
            else:
                # Новое нажатие клавиши
                self.handle_key_press()
        elif obj == self.ui.password_edit and event.type() == QEvent.KeyRelease:
            if not event.isAutoRepeat():
                # Клавиша была отпущена
                self.handle_key_release()

        return super().eventFilter(obj, event)

    def handle_key_press(self):
        current_time = QDateTime.currentDateTime()

        if self.key_pressed_time is not None:
            interval = self.key_pressed_time.msecsTo(current_time)
            print(f"Time between key presses: {interval} ms")
            self.bio.current_metric.press_time.append(interval)
            self.ui.l_3.setText(str(mean(self.bio.current_metric.press_time)))

        self.key_pressed_time = current_time

    def handle_key_release(self):
        current_time = QDateTime.currentDateTime()

        if self.last_key_release_time is not None:
            interval = self.last_key_release_time.msecsTo(current_time)
            print(f"Time between key releases: {interval} ms")
            self.bio.current_metric.release_time.append(interval)
            self.ui.l_4.setText(str(mean(self.bio.current_metric.release_time)))

        self.last_key_release_time = current_time

    def handle_submit(self):
        if self.ui.username_edit.text() and self.ui.password_edit.text():
            self.bio.submit_metric(self.ui.username_edit.text(), self.ui.password_edit.text())
            self.close()
