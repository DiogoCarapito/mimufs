# pylint: disable=E0611

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    # QToolBar,
    QStatusBar,
    QWidget,
    # QSizePolicy,
    QSplitter,
    # QTextEdit,
    # QSplitterHandle,
    QVBoxLayout,
    # QLabel,
    QPushButton,
    QStackedWidget,
    QSystemTrayIcon,
    QMenu,
    # QListWidget
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize, QEvent

# Update these imports to reflect new structure
from utils.tabler_io_icons import ensure_tabler_icon
from pages import PaginaHome, PaginaDefinicoes, PaginaExtracaoMimuf, PaginaTesteMIMUF

# autogui imports
from autogui import execut_scripts_csv

# class TopToolBar(QToolBar):
#     def __init__(self, parent=None):
#         super().__init__("Main Toolbar", parent)
#         self.setMovable(False)
#         self.setIconSize(QSize(24, 24))  # Reduce toolbar icon size


#         # Spacer to push next actions to the right
#         spacer = QWidget()
#         spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
#         self.addWidget(spacer)

#         # # Dark/Light mode toggle
#         # brightness_icon_path = ensure_tabler_icon("brightness")
#         # self.theme_toggle_action = QAction(QIcon(brightness_icon_path), "Toggle Theme", self)
#         # self.theme_toggle_action.setStatusTip("Toggle Dark/Light Mode")
#         # self.theme_toggle_action.setCheckable(True)
#         # self.theme_toggle_action.triggered.connect(self.toggle_theme)
#         # self.addAction(self.theme_toggle_action)

#         # Right column toggle icon (right)
#         right_icon_path = ensure_tabler_icon("layout-sidebar-right")
#         self.right_toggle_action = QAction(QIcon(right_icon_path), "Toggle Right Column", self)
#         self.right_toggle_action.setStatusTip("Show/Hide Right Column")
#         self.addAction(self.right_toggle_action)

#     # def toggle_theme(self, checked):
#     #     mw = self.parentWidget()
#     #     if checked:
#     #         mw.setStyleSheet("""
#     #             QMainWindow, QToolBar, QStatusBar, QWidget {
#     #                 background: #23272e; color: #e0e0e0;
#     #             }
#     #             QPushButton { background: #23272e; color: #e0e0e0; }
#     #             QLineEdit, QTextEdit { background: #23272e; color: #e0e0e0; }
#     #             QSplitter::handle { background: #444; }
#     #         """)
#     #     else:
#     #         mw.setStyleSheet("""
#     #             QSplitter::handle { background: #ccc; }
#     #         """)


class BottomStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showMessage("Ready")


class ThinSplitter(QSplitter):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setHandleWidth(1)  # Set handle width to 2 pixels

    def createHandle(self):
        handle = super().createHandle()
        # handle.setStyleSheet("background: #ccc;")  # Light gray line
        return handle


class LeftColumn(QWidget):
    def __init__(self, parent=None, center_widget=None):
        super().__init__(parent)
        self.setFixedWidth(40)
        self.center_widget = center_widget

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        icons = ["home", "folder", "test-pipe", "settings"]
        self.buttons = []
        for icon_name in icons:
            icon_path = ensure_tabler_icon(icon_name)
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(36, 36))
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("border: none;")
            btn.clicked.connect(lambda checked, name=icon_name: self.open_menu(name))
            btn.icon_name = icon_name
            btn.installEventFilter(self)
            layout.addWidget(btn)
            self.buttons.append(btn)

        layout.addStretch()

    def open_menu(self, name):
        if self.center_widget:
            self.center_widget.show_menu(name)
        self.show_status(name)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and hasattr(obj, "icon_name"):
            self.show_status(obj.icon_name)
        elif event.type() == QEvent.Leave and hasattr(obj, "icon_name"):
            self.clear_status()
        return super().eventFilter(obj, event)

    def show_status(self, name):
        # Find the main window and set status bar message
        main_win = self.window()
        if hasattr(main_win, "statusBar"):
            main_win.statusBar().showMessage(f"{name.capitalize()}")

    def clear_status(self):
        main_win = self.window()
        if hasattr(main_win, "statusBar"):
            main_win.statusBar().clearMessage()


# class RightColumn(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setFixedWidth(120)
#         self.setMaximumWidth(400)  # Allow resizing up to 400 px

#         layout = QVBoxLayout(self)
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.setSpacing(0)

#         title = QLabel("Right column")
#         layout.addWidget(title)

#         # content = QTextEdit()
#         # layout.addWidget(content)

#     def update_content(self, context):
#         # Clear and update layout with new contextual info
#         # For example, show components if present
#         for i in reversed(range(self.layout().count())):
#             widget = self.layout().itemAt(i).widget()
#             if widget:
#                 widget.deleteLater()
#         if "components" in context:
#             self.layout().addWidget(QLabel("<h2>Components</h2>"))
#             list_widget = QListWidget()
#             list_widget.addItems(context["components"])
#             self.layout().addWidget(list_widget)


class CenterColumn(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: #fff;")  # Pure white background
        # Use imported page classes
        self.pages = {
            "home": PaginaHome(self),
            "folder": PaginaExtracaoMimuf(self),
            "test-pipe": PaginaTesteMIMUF(self),
            "settings": PaginaDefinicoes(self),
        }
        for page in self.pages.values():
            self.addWidget(page)

    def show_menu(self, name):
        if name in self.pages:
            self.setCurrentWidget(self.pages[name])

    # def get_context(self, name):
    #     # Return context data for the right column based on the page
    #     if name == "folder":
    #         _, components = load_script_csv("src/autogui/scripts/test_script.csv")
    #         return {"components": components}
    #     # Add more cases for other pages as needed
    #     return {}


class SystemTrayMenu:
    def __init__(self, main_window, main_app, extracao_page=None):
        self.tray_icon = QSystemTrayIcon(QIcon("assets/logo/logo.ico"), main_window)
        self.tray_menu = QMenu()
        show_action = QAction("Show", main_window)
        show_action.triggered.connect(main_window.show)
        self.tray_menu.addAction(show_action)

        # Add "Executar Extração" action
        extracao_action = QAction("Executar Extração", main_window)
        extracao_action.triggered.connect(lambda: self.executar_extracao(extracao_page))
        self.tray_menu.addAction(extracao_action)

        quit_action = QAction("Quit", main_window)
        quit_action.triggered.connect(main_app.quit)
        self.tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

    def executar_extracao(self, extracao_page):
        print("click")
        if extracao_page is not None:
            selected_files = extracao_page.get_selected_files()
            execut_scripts_csv(selected_files)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mimufs")
        self.resize(800, 600)
        self.setWindowIcon(QIcon("src/assets/logo/logo.ico"))  # Set app icon

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        # help_menu = menubar.addMenu("Help")
        # about_action = QAction("About", self)
        # about_action.triggered.connect(self.show_about)
        # help_menu.addAction(about_action)

        # # Add top toolbar
        # toolbar = TopToolBar(self)
        # self.addToolBar(toolbar)

        # Add bottom status bar
        status_bar = BottomStatusBar(self)
        self.setStatusBar(status_bar)

        # Use ThinSplitter for columns
        self.splitter = ThinSplitter(Qt.Horizontal)

        # Center column as QStackedWidget
        self.center_col = CenterColumn(self)

        # Left column, pass center_col reference
        self.left_col = LeftColumn(self, center_widget=self.center_col)

        # Right column
        # self.right_col = RightColumn(self)

        self.splitter.addWidget(self.left_col)
        self.splitter.addWidget(self.center_col)
        # self.splitter.addWidget(self.right_col)

        self.splitter.setSizes([120, 560, 120])

        self.setCentralWidget(self.splitter)

        # Connect toggle actions
        # toolbar.left_toggle_action.triggered.connect(self.toggle_left_column)
        # toolbar.right_toggle_action.triggered.connect(self.toggle_right_column)

        # State for toggling
        # self.left_expanded = True
        self.right_expanded = True

    # def toggle_left_column(self):
    #     sizes = self.splitter.sizes()
    #     if self.left_expanded:
    #         # Collapse left column
    #         self.splitter.setSizes([0, sizes[1] + sizes[0], sizes[2]])
    #     else:
    #         # Expand left column to 120px
    #         self.splitter.setSizes([120, sizes[1] - 120 if sizes[1] > 120 else sizes[1], sizes[2]])
    #     self.left_expanded = not self.left_expanded

    def toggle_right_column(self):
        sizes = self.splitter.sizes()
        if self.right_expanded:
            # Collapse right column
            self.splitter.setSizes([sizes[0], sizes[1] + sizes[2], 0])
        else:
            # Expand right column to 120px
            self.splitter.setSizes(
                [sizes[0], sizes[1] - 120 if sizes[1] > 120 else sizes[1], 120]
            )
        self.right_expanded = not self.right_expanded

    # def show_about(self):
    #     from PySide6.QtWidgets import QMessageBox
    #     QMessageBox.about(self, "About Mimufs", "Mimufs Pro\nA modern file manager.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    tray_menu = SystemTrayMenu(window, app, window.center_col.pages.get("folder"))
    sys.exit(app.exec())
