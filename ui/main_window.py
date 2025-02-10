import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QToolBar, QLabel
)

from PySide6.QtGui import QIcon, QAction
from ui.add_window import Add
from ui.search_window import Search
from ui.gallery_window import GalleryWindow
from ui.download_window import DownloadWindow

from db.db_manager import DatabaseManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Applicazione con due sezioni")
        self.setMinimumSize(1366, 768)

        # Crea il database manager
        self.db_manager = DatabaseManager()

        # Crea un'unica istanza della GalleryWindow
        self.gallery_window = GalleryWindow()

        # Passa la stessa istanza della gallery a Search
        self.search_window = Search(self.db_manager, self.gallery_window)
        add_window = Add()
        add_window.accessory_added.connect(self.search_window.load_cache)

        # Crea il central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # TOOLBAR
        toolbar = QToolBar("toolbar")
        
        icon = QIcon("resources/search-icon.png")
        icon_search = icon.pixmap(20, 20)
        search_action = QAction(icon_search, "CERCA", self)
        search_action.setText("CERCA")
        search_action.setToolTip("Cerca accessorio")
        search_action.triggered.connect(self.show_search_widget)
        toolbar.addAction(search_action)
        
        add_action = QAction("AGGIUNGI ACCESSORIO", self)
        add_action.triggered.connect(self.show_add_widget)
        toolbar.addAction(add_action)

        self.addToolBar(toolbar)

        # Crea il layout principale (orizzontale)
        main_layout = QHBoxLayout()

        # PARTE SINISTRA: lo stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(add_window)
        self.stacked_widget.addWidget(self.search_window)
        main_layout.addWidget(self.stacked_widget, 1)

        # PARTE DESTRA: layout verticale
        right_layout = QVBoxLayout()

        # Utilizza la stessa GalleryWindow creata in precedenza
        right_layout.addWidget(self.gallery_window, 2)

        # Sezione inferiore con il DownloadWidget
        self.download_widget = DownloadWindow()  # Crea l'istanza del widget per il download
        right_layout.addWidget(self.download_widget, 1)

        # Aggiungi il layout verticale alla parte destra
        main_layout.addLayout(right_layout, 1)

        # Imposta il layout del central widget
        central_widget.setLayout(main_layout)
        
        self.stacked_widget.setCurrentIndex(1)


    def show_add_widget(self):
        self.stacked_widget.setCurrentIndex(0)  # Mostra la sezione "Aggiungi"

    def show_search_widget(self):
        self.stacked_widget.setCurrentIndex(1)  # Mostra la sezione "Cerca"
