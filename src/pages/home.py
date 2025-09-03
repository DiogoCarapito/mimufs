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
    # QPushButton,
    # QStackedWidget,
)


class PaginaHome(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("<h2>Welcome Home</h2>"))
        layout.addWidget(QLabel("This is your dashboard."))
        layout.addStretch()
