from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class GalleryWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # Creazione dell'etichetta per l'immagine
        self.image_label = QLabel(self)  
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Aggiungi l'etichetta al layout
        self.layout.addWidget(self.image_label)
        
        self.setLayout(self.layout)

    def update_image(self, image_data):
        """Metodo per aggiornare l'immagine nella galleria"""
        
        if image_data:  # Verifica che i dati dell'immagine non siano vuoti
            # Converte i dati binari in un QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            
            # Imposta l'immagine nell'etichetta
            self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
        else:
            # Se non ci sono dati dell'immagine, imposta un'immagine di default o vuota
            self.image_label.clear()
