from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
import base64

class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.title = QLabel("Download")
        self.layout().addWidget(self.title)

        # Pulsante per il download dell'immagine
        self.download_button = QPushButton("Scarica Immagine")
        #self.download_button.setEnabled(False)
        self.download_button.clicked.connect(self.download_image)
        self.layout().addWidget(self.download_button)

        self.image_data = None

    def set_image_data(self, image_data):
        """Aggiorna l'immagine da scaricare e abilita il pulsante."""
        self.image_data = image_data
        self.download_button.setEnabled(True)
        print("DownloadWindow: set_image_data chiamato. Pulsante abilitato.")

    def download_image(self):
        """Salva l'immagine su file quando l'utente clicca sul pulsante."""
        if self.image_data is not None:
            print("sono nel primo if")
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Salva Immagine",
                "immagine.png",
                "Immagini (*.png *.jpg *.jpeg)"
            )
            if file_path:
                try:
                    # Se image_data è una stringa, assumiamo sia in base64 e la decodifichiamo
                    data_to_write = self.image_data
                    if isinstance(self.image_data, str):
                        data_to_write = base64.b64decode(self.image_data)
                    with open(file_path, "wb") as f:
                        f.write(data_to_write)
                    print(f"Immagine salvata in {file_path}")
                except Exception as e:
                    print(f"Errore nel salvataggio dell'immagine: {e}")
