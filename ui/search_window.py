import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt, Signal
from db.db_manager import DatabaseManager
from ui.result_item_widget import ResultItemWidget
import ui.gallery_window as gallery_window
import ui.download_window as download_window

class Search(QWidget):
    
    def __init__(self, db_manager: DatabaseManager, gallery_window: gallery_window.GalleryWindow, download_window: download_window.DownloadWindow):
        super().__init__()

        self.db_manager = db_manager  # Riferimento al DatabaseManager
        self.gallery_window = gallery_window  # Riferimento alla GalleryWindow per aggiornare l'immagine
        self.download_window = download_window  # Istanza di DownloadWindow
        self.cache = []  # Cache locale dei dati
        self.tags_list = self.db_manager.get_tags()
        self.tags_list.insert(0, "------")  # Aggiungi "------" come opzione di default
        
        # Layout principale
        layout = QVBoxLayout()

        # Campo NOME
        name_layout = QHBoxLayout()
        name_label = QLabel("NOME")
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(300)
        self.name_input.textChanged.connect(lambda text: self.update_results(text))
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()
        layout.addLayout(name_layout)

        # Campo TIPO
        type_layout = QHBoxLayout()
        type_label = QLabel("TIPO")
        self.type_combobox = QComboBox()    
        self.type_combobox.addItems(self.tags_list)
        self.type_combobox.setFixedWidth(200)
        self.type_combobox.currentTextChanged.connect(lambda _: self.update_results(self.name_input.text()))
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combobox)
        type_layout.addStretch()
        layout.addLayout(type_layout)

        # Sezione dei risultati
        results_label = QLabel("Risultati:")
        layout.addWidget(results_label)

        # Lista dei risultati
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)
        
        self.setLayout(layout)
        
        self.load_cache()
        
        self.result_list.itemClicked.connect(self.on_item_clicked)
                

    def load_cache(self):
        """Carica i dati dal database e visualizza i risultati."""
        self.cache = self.db_manager.get_all_names_and_types()
        self.display_all_results()

    def update_results(self, text=""):
        selected_tag = self.type_combobox.currentText().strip()

        if not text:
            filtered_items = [
                accessory for accessory in self.cache 
                if selected_tag == "------" or selected_tag.lower() in accessory.tipo.lower()
            ]
        else:
            filtered_items = [
                accessory for accessory in self.cache if text.lower() in accessory.nome.lower()
            ]
            if selected_tag != "------":
                filtered_items = [
                    accessory for accessory in filtered_items if selected_tag.lower() in accessory.tipo.lower()
                ]

        self.result_list.clear()
        
        for accessory in filtered_items:
            item_widget = ResultItemWidget(accessory.nome, accessory.tipo)
            item = QListWidgetItem(self.result_list)
            item.setSizeHint(item_widget.sizeHint())
            # Associa l'intero oggetto accessory all'item
            item.setData(Qt.UserRole, accessory)
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)
            
    def on_item_clicked(self, item: QListWidgetItem):
        """
        Quando l'utente clicca un item, recupera l'oggetto Accessory e,
        se presente l'attributo 'immagine' (BLOB), aggiorna la GalleryWindow
        e invia i dati al DownloadWindow.
        """
        accessory = item.data(Qt.UserRole)
        if accessory is not None and getattr(accessory, "immagine", None) is not None:
            self.gallery_window.update_image(accessory.immagine)
            self.download_window.set_image_data(accessory.immagine)

    def display_all_results(self):
        self.result_list.clear()

        for accessory in self.cache:
            item_widget = ResultItemWidget(accessory.nome, accessory.tipo)
            item = QListWidgetItem(self.result_list)
            item.setSizeHint(item_widget.sizeHint())
            item.setData(Qt.UserRole, accessory)
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)
