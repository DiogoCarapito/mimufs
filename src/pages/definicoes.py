# pylint: disable=E0611

from PySide6.QtWidgets import (
    # QApplication,
    # QMainWindow,
    # QToolBar,
    # QStatusBar,
    QWidget,
    # QSizePolicy,
    # QSplitter,
    # QTextEdit,
    # QSplitterHandle,
    QVBoxLayout,
    QLabel,
    QPushButton,
    # QStackedWidget,
    # QListWidget,
)


class PaginaDefinicoes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("<h2>Settings</h2>"))
        layout.addWidget(QPushButton("Change Theme"))
        layout.addStretch()
