import sys

from PySide6.QtWidgets import QApplication, QWidget

from db.db_engine import engine
from db.models.base import Base
from widgets.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
