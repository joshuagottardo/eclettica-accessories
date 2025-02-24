from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

class ResultItemWidget(QWidget):
    def __init__(self, nome, tipo):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)

        nomeUpper = nome.upper()
        label = QLabel(f"{nomeUpper} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i style=\"color: grey; margin-right:auto;\">({tipo})</i>")  # HTML per formattazione
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #202020;
                padding: 15px;
            }
            QLabel {
                color: white;
                font-size: 17px;
            }
            QWidget:hover {
                background-color: #333333;
            }
        """)

        self.setMinimumHeight(50)
