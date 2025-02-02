from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QGridLayout, QFileDialog, QMessageBox
)
from db.db_manager import DatabaseManager

tags_list = ["Laccio", "Soletta", "Pad in gel", "Plantare ortopedici", "Cinturino", "Intersuola", "Raffreddatore", "Tacco", "Copritacco", "Spazzola", "Lucido", "Borsa"]

class Add(QWidget):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()  # Istanzia il gestore del database

        # Layout principale
        layout = QVBoxLayout()

        # Campo NOME
        name_layout = QHBoxLayout()
        name_label = QLabel("NOME")
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(300)
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()
        layout.addLayout(name_layout)

        # Campo TIPO
        type_layout = QHBoxLayout()
        type_label = QLabel("TIPO")
        self.type_combobox = QComboBox()
        self.type_combobox.addItems(tags_list)
        self.type_combobox.setFixedWidth(200)
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combobox)
        type_layout.addStretch()
        layout.addLayout(type_layout)

        # Campo TAG (12 checkbox in griglia)
        """
        tag_container = QHBoxLayout()
        tag_label = QLabel("TAG")
        layout.addWidget(tag_label)

        self.tag_layout = QGridLayout()
        self.tags = []
        for i in range(12):
            tag_checkbox = QCheckBox(tags_list[i])
            self.tags.append(tag_checkbox)
            self.tag_layout.addWidget(tag_checkbox, i // 4, i % 4)

        self.tag_layout.setSpacing(25)
        tag_container.addLayout(self.tag_layout)
        tag_container.addStretch()
        layout.addLayout(tag_container)
        """

        # Selezione immagine
        image_layout = QHBoxLayout()
        image_label = QLabel("Seleziona Immagine")
        self.image_path = QLineEdit()
        self.image_path.setReadOnly(True)
        self.image_path.setFixedWidth(300)
        self.image_button = QPushButton("Scegli")
        self.image_button.clicked.connect(self.choose_image)

        image_layout.addWidget(image_label)
        image_layout.addWidget(self.image_path)
        image_layout.addWidget(self.image_button)
        image_layout.addStretch()
        layout.addLayout(image_layout)

        # Bottone Conferma
        self.confirm_button = QPushButton("AGGIUNGI")
        self.confirm_button.setStyleSheet(
            """
            QPushButton {
                background-color: green;
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #008000;
            }
            """
        )
        self.confirm_button.clicked.connect(self.add_accessory)  # Collega il pulsante alla funzione
        layout.addWidget(self.confirm_button)

        layout.addStretch()

        # Imposta il layout principale
        self.setLayout(layout)

    def choose_image(self):
        """Apre un file dialog per scegliere un'immagine."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleziona un'immagine", "", "Immagini (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.image_path.setText(file_path)

    def add_accessory(self):
        """Gestisce l'inserimento di un nuovo accessorio nel database."""
        nome = self.name_input.text()
        tipo = self.type_combobox.currentText()
        immagine_path = self.image_path.text()

        if not nome or not tipo or not immagine_path:
            QMessageBox.warning(self, "Errore", "Tutti i campi sono obbligatori!")
            return

        try:
            # Leggi l'immagine come binario
            with open(immagine_path, "rb") as file:
                immagine_data = file.read()

            # Inserisci i dati nel database
            self.db_manager.insert_accessory(nome, tipo, immagine_data)
            QMessageBox.information(self, "Successo", "Accessorio aggiunto con successo!")

            # Resetta i campi
            self.name_input.clear()
            self.type_combobox.setCurrentIndex(0)
            self.image_path.clear()

        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore durante l'inserimento: {str(e)}")
