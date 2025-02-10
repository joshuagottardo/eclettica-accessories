from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

class GalleryWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        image_label = QLabel()
        pixmap = QPixmap("resources/background.png")
        pixmap = pixmap.scaled(400, 400)
        image_label.setPixmap(pixmap)
        image_label.setFixedSize(400, 400)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        self.setLayout(layout)
        
        