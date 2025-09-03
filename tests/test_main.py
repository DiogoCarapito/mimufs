# pylint: disable=E0611
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from PySide6.QtWidgets import QApplication
from src.main import MainWindow


def test_main_window_title():
    app = QApplication([])  # pylint: disable=unused-variable
    window = MainWindow()
    assert window.windowTitle() == "Mimufs"
