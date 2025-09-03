# pylint: disable=E0611

import os
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QTextEdit,
)
from PySide6.QtCore import Qt


class PaginaExtracaoMimuf(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        main_layout = QHBoxLayout(self)

        # --- Left column: scripts list ---
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("<h2>Available Scripts</h2>"))

        scripts_folder = "src/autogui/scripts/"
        script_files = [
            f
            for f in os.listdir(scripts_folder)
            if f.endswith(".csv") and f != "__init__.py"
        ]

        self.list_widget = QListWidget()
        for script in script_files:
            item = QListWidgetItem(script)
            item.setFlags(
                item.flags()
                | Qt.ItemIsUserCheckable
                | Qt.ItemIsSelectable
                | Qt.ItemIsEnabled
            )
            item.setCheckState(Qt.Unchecked)
            self.list_widget.addItem(item)
        left_layout.addWidget(self.list_widget)
        left_layout.addStretch()

        # --- Right column: CSV content ---
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("<h2>Script Content</h2>"))
        self.content_box = QTextEdit()
        self.content_box.setReadOnly(True)
        right_layout.addWidget(self.content_box)
        right_layout.addStretch()

        # Add columns to main layout
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(right_widget, 2)

        # Connect selection
        self.list_widget.itemClicked.connect(self.on_script_clicked)

    def on_script_clicked(self, item):
        script_path = os.path.join("src/autogui/scripts/", item.text())
        if os.path.exists(script_path):
            with open(script_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.content_box.setPlainText(content)
        else:
            self.content_box.setPlainText("File not found.")

    def get_selected_files(self):
        selected_files = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.Checked:
                selected_files.append(item.text())
        return selected_files
