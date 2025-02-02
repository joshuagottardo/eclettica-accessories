from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar, QMenuBar, QLabel, QDockWidget, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Esempio di QMainWindow")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Benvenuto nel central widget"))
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("CERCA")
        edit_menu = menu_bar.addMenu("AGGIUNGI")

        # Toolbar
        toolbar = QToolBar("Toolbar principale")
        toolbar.addAction("Azione 1")
        toolbar.addAction("Azione 2")
        self.addToolBar(toolbar)

        # Status bar
        status_bar = QStatusBar()
        status_bar.showMessage("Pronto")
        self.setStatusBar(status_bar)

        # Dock widget
        dock_widget = QDockWidget("Dock Widget")
        dock_widget.setWidget(QLabel("Contenuto del dock widget"))
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
