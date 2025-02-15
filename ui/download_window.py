from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
import os

class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # Titolo della sezione
        self.title = QLabel("Download")
        self.layout().addWidget(self.title)

        # Layout orizzontale per la lista delle immagini
        self.image_list_layout = QVBoxLayout()

        # Aggiungi i bottoni per il download delle immagini
        self.add_download_buttons()

        # Aggiungi il layout della lista delle immagini
        self.layout().addLayout(self.image_list_layout)

    def add_download_buttons(self):
        image_folder = "resources"
        image_files = [f"{i}.png" for i in range(1, 6)]  # Immagini 1.png, 2.png, ...

        for image_file in image_files:
            button = QPushButton(f"Scarica {image_file}")
            button.clicked.connect(lambda checked, file=image_file: self.download_image(file))
            self.image_list_layout.addWidget(button)

    def download_image(self, image_file):
        # Funzione per scaricare il file
        image_path = os.path.join("resources", image_file)
        save_path = os.path.join(os.getcwd(), image_file)  # Percorso di salvataggio

        # Copia il file dalla cartella "resources" alla cartella corrente
        try:
            with open(image_path, "rb") as src_file:
                data = src_file.read()

            with open(save_path, "wb") as dst_file:
                dst_file.write(data)

            print(f"{image_file} scaricato con successo!")
        except Exception as e:
            print(f"Errore nel download di {image_file}: {e}")
