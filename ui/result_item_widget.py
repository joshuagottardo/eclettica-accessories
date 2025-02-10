from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

class ResultItemWidget(QWidget):
    def __init__(self, name, type_):
        super().__init__()

        layout = QHBoxLayout()

        # Nome accessorio
        name_label = QLabel(name)
        name_label.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")

        # Tipo accessorio
        type_label = QLabel(f"({type_})")
        type_label.setStyleSheet("color: gray; font-size: 12px; font-style: italic;")

        layout.addWidget(name_label)
        layout.addWidget(type_label)
        layout.addStretch()
        self.setLayout(layout)
        self.setStyleSheet(
            """
            background-color: #3a3a3a;
            border-radius: 6px;
            padding: 8px;
        """
        )
