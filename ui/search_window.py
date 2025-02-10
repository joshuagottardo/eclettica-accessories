import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#tags_list = ["------", ]

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt
from db.db_manager import DatabaseManager
from ui.result_item_widget import ResultItemWidget
import ui.gallery_window as gallery_window

class Search(QWidget):
    def __init__(self, db_manager: DatabaseManager, gallery_window: gallery_window.GalleryWindow):
        super().__init__()

        self.db_manager = db_manager  # Salva il riferimento al DatabaseManager
        self.gallery_window = gallery_window  # Riferimento alla GalleryWindow per aggiornare l'immagine
        self.cache = []  # Cache locale dei nomi e dei tipi
        self.tags_list = self.db_manager.get_tags()
        self.tags_list.insert(0, "------")  # Aggiungi "------" come opzione di default


        # Layout principale
        layout = QVBoxLayout()

        # Campo NOME
        name_layout = QHBoxLayout()
        name_label = QLabel("NOME")
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(300)
        self.name_input.textChanged.connect(lambda text: self.update_results(text))  # Connettiti al metodo di aggiornamento
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
        self.type_combobox.currentTextChanged.connect(lambda _: self.update_results(self.name_input.text()))  # Connessione al cambiamento del tag
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combobox)
        type_layout.addStretch()
        layout.addLayout(type_layout)

        # Sezione dei risultati
        results_label = QLabel("Risultati:")
        layout.addWidget(results_label)

        # Lista dei risultati
        self.result_list = QListWidget()
        """
        self.result_list.setStyleSheet(
        
            QListWidget {
                background-color: #323232;
                border: none;
                font-size: 15px;
                font-style: italic;
            }
            QListWidget::item {
                background-color: #3a3a3a;
                margin: 2px;
                padding: 5px;
                border-radius: 4px;
                font-style: italic;
                margin-bottom: 10px;
                padding: 13px;
            }
            QListWidget::item:selected {
                background-color: #007BFF;
                color: #ffffff;
            }
        )
        """

        layout.addWidget(self.result_list)
        
        self.setLayout(layout)
        
        self.load_cache()
        
        self.result_list.itemClicked.connect(self.on_item_clicked)
                

    def load_cache(self):
        """Carica tutti i nomi e i tipi nella cache locale e visualizzali subito."""
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
            # Salva l'intero oggetto Accessory nell'item
            item.setData(Qt.UserRole, accessory)
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)
            
    def on_item_clicked(self, item: QListWidgetItem):
        """
        Quando l'utente clicca su un item, recupera l'oggetto Accessory associato
        e aggiorna la GalleryWindow con l'immagine.
        """
        accessory = item.data(Qt.UserRole)
        if accessory and hasattr(accessory, "immagine"):
            self.gallery_window.update_image(accessory.immagine)

    def display_all_results(self):
        
        self.result_list.clear()

        for accessory in self.cache:
            item_widget = ResultItemWidget(accessory.nome, accessory.tipo)
            item = QListWidgetItem(self.result_list)
            item.setSizeHint(item_widget.sizeHint())
            item.setData(Qt.UserRole, accessory)
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)
