import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QToolBar, QLabel
)
from PySide6.QtGui import QIcon, QAction

from db.db_manager import DatabaseManager
from ui.gallery_window import GalleryWindow
from ui.download_window import DownloadWindow
from ui.search_window import Search
from ui.add_window import AddWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Applicazione con due sezioni")
        self.setMinimumSize(1366, 768)

        # Crezione riferimento alle classi utilizzate
        self.db_manager = DatabaseManager()
        self.gallery_window = GalleryWindow()
        self.download_window = DownloadWindow()
        self.search_window = Search(self.db_manager, self.gallery_window, self.download_window)
        self.add_window = AddWindow()
        
        # Collegamento segnale "accessory_added" al metodo "load_cache" di Search"
        self.add_window.accessory_added.connect(self.search_window.load_cache)

        # Creazione widget per tutta la finestra
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Toolbar
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

        # Creazione layout per le due sezione (cerca/aggiungi e immagine/download)
        main_layout = QHBoxLayout()

        # PARTE SINISTRA: stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.add_window)
        self.stacked_widget.addWidget(self.search_window)
        main_layout.addWidget(self.stacked_widget, 1)

        # PARTE DESTRA: layout verticale
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.gallery_window, 2)
        self.download_widget = DownloadWindow()  # Crea l'istanza del widget per il download
        right_layout.addWidget(self.download_widget, 1)
        main_layout.addLayout(right_layout, 1)
        
        central_widget.setLayout(main_layout)
        
        self.stacked_widget.setCurrentIndex(1)


    def show_add_widget(self):
        """Mostra la sezione 'Aggiungi'"""
        self.stacked_widget.setCurrentIndex(0)

    def show_search_widget(self):
        """Mostra la sezione 'Cerca'"""
        self.stacked_widget.setCurrentIndex(1)
