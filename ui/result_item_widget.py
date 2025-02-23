from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

class ResultItemWidget(QWidget):
    def __init__(self, nome, tipo):
        super().__init__()

        # Layout principale
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)  # Nessuna separazione extra

        nomeUpper = nome.upper()
        # Creazione della QLabel con entrambi i testi
        label = QLabel(f"<b>{nomeUpper}</b>  <i style=\"color: grey; margin-right:auto;\">[{tipo}]</i>")  # HTML per formattazione
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Aggiungi la QLabel al layout
        layout.addWidget(label)

        # Imposta il layout al widget
        self.setLayout(layout)

        # Stile generale del widget
        self.setStyleSheet("""
            QWidget {
                background-color: #323232;
                border-radius: 10px;
                padding: 15px;
            }
            QLabel {
                color: white;
                font-size: 17px;
            }
        """)

        # Dimensioni minime
        self.setMinimumHeight(50)
