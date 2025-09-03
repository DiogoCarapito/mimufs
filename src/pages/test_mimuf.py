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
    QGridLayout,
    QLineEdit,  # Add this import
)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, Qt


class PaginaTesteMIMUF(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: #fff;")  # Pure white background
        layout = QVBoxLayout(self)

        # Title image at the top
        title_image = QLabel()
        pixmap = QPixmap("assets/autogui/mimuf_top_bar.jpg")
        max_width = 800  # Set your desired max width
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaledToWidth(max_width, Qt.SmoothTransformation)
            title_image.setPixmap(scaled_pixmap)
        title_image.setAlignment(Qt.AlignCenter)
        title_image.setMaximumWidth(max_width)
        layout.addWidget(title_image)
        # layout.addWidget(QLabel("<h2>TESTE MIMUF</h2>"))

        # List of image paths
        self.image_paths = [
            "assets/autogui/p01_btn.jpg",
            "assets/autogui/p02_btn.jpg",
            "assets/autogui/p03_btn.jpg",
            "assets/autogui/p04_btn.jpg",
            "assets/autogui/p05_btn.jpg",
            "assets/autogui/p06_btn.jpg",
            "assets/autogui/p07_btn.jpg",
            "assets/autogui/p09_btn.jpg",
            "assets/autogui/p10_btn.jpg",
            "assets/autogui/p11_btn.jpg",
            "assets/autogui/p15_btn.jpg",
        ]

        # Grid of buttons (2 columns)
        grid = QGridLayout()
        for idx, img_path in enumerate(self.image_paths):
            btn = QPushButton()
            btn.setIcon(QIcon(img_path))
            btn.setIconSize(QSize(400, 64))
            btn.setFixedSize(400, 64)
            btn.setStyleSheet("border: none;")
            row = idx // 2
            col = idx % 2
            grid.addWidget(btn, row, col)
            btn.clicked.connect(lambda checked, i=idx: self.show_text(i))

        layout.addLayout(grid)

        # Label to display text below the grid
        self.info_label = QLabel("")
        layout.addWidget(self.info_label)

        # Add a text input below the label (hidden by default)
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter text here...")
        self.text_input.setVisible(False)
        layout.addWidget(self.text_input)

        layout.addStretch()

    def show_text(self, idx):
        main_win = self.window()
        if hasattr(main_win, "statusBar"):
            main_win.statusBar().showMessage(self.image_paths[idx])
        self.info_label.setText(self.image_paths[idx])
        self.text_input.setVisible(True)
