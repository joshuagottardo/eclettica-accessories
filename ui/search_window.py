import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QListWidget, QListWidgetItem
)
from db.db_manager import DatabaseManager
from ui.result_item_widget import ResultItemWidget

tags_list = ["------", "Laccio", "Soletta", "Pad in gel", "Plantare ortopedici", "Cinturino", "Intersuola", "Raffreddatore", "Tacco", "Copritacco", "Spazzola", "Lucido", "Borsa"]

class Search(QWidget):
    def __init__(self, db_manager: DatabaseManager):
        super().__init__()

        self.db_manager = db_manager  # Salva il riferimento al DatabaseManager
        self.cache = []  # Cache locale dei nomi e dei tipi

        # Layout principale
        layout = QVBoxLayout()

        # Campo NOME
        name_layout = QHBoxLayout()
        name_label = QLabel("NOME")
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(300)  # Imposta la larghezza fissa
        self.name_input.textChanged.connect(lambda text: self.update_results(text))  # Connettiti al metodo di aggiornamento
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()  # Aggiungi spazio vuoto
        layout.addLayout(name_layout)

        # Campo TIPO
        type_layout = QHBoxLayout()
        type_label = QLabel("TIPO")
        self.type_combobox = QComboBox()    
        self.type_combobox.addItems(tags_list)  # Aggiungi i tipi qui
        self.type_combobox.setFixedWidth(200)  # Imposta la larghezza fissa
        self.type_combobox.currentTextChanged.connect(lambda _: self.update_results(self.name_input.text()))  # Connessione al cambiamento del tag
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combobox)
        type_layout.addStretch()  # Aggiungi spazio vuoto
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

        # Imposta il layout principale
        self.setLayout(layout)

        # Carica inizialmente i dati nella cache
        self.load_cache()

    def load_cache(self):
        """Carica tutti i nomi e i tipi nella cache locale e visualizzali subito."""
        self.cache = self.db_manager.get_all_names_and_types()  # Ora è una lista di tuple (nome, tipo)

        # Visualizza tutti i risultati iniziali
        self.display_all_results()

    def update_results(self, text=""):
        """Aggiorna i risultati della ricerca dinamicamente in base al nome e al tag."""
        selected_tag = self.type_combobox.currentText().strip()

        # Se non c'è testo nel campo NOME
        if not text:
            filtered_items = [
                (name, type_) 
                for name, type_ in self.cache
                if (selected_tag == "------" or selected_tag.lower() in type_.lower())
            ]
        else:
            filtered_items = [
                (name, type_)
                for name, type_ in self.cache if text.lower() in name.lower()
            ]
            if selected_tag != "------":
                filtered_items = [
                    (name, type_) for name, type_ in filtered_items
                    if selected_tag.lower() in type_.lower()
                ]

        # Pulizia lista risultati
        self.result_list.clear()

        # Aggiunta dei nuovi elementi personalizzati
        for name, type_ in filtered_items:
            item_widget = ResultItemWidget(name, type_)
            item = QListWidgetItem(self.result_list)
            item.setSizeHint(item_widget.sizeHint())  # Imposta la dimensione del widget
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)  # Assegna il widget personalizzato

    def display_all_results(self):
        """Mostra tutti i risultati disponibili al caricamento con i widget personalizzati."""
        self.result_list.clear()  # Pulisce la lista

        for name, type_ in self.cache:
            item_widget = ResultItemWidget(name, type_)
            item = QListWidgetItem(self.result_list)
            item.setSizeHint(item_widget.sizeHint())  # Imposta la dimensione del widget
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, item_widget)  # Assegna il widget personalizzato
