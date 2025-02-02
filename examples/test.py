from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout

app = QApplication([])

# Layout principale verticale
main_layout = QVBoxLayout()

# Primo layout orizzontale
top_layout = QHBoxLayout()
top_layout.addWidget(QPushButton("Sinistra"))
top_layout.addWidget(QPushButton("Destra"))

# Secondo layout orizzontale
bottom_layout = QHBoxLayout()
bottom_layout.addWidget(QPushButton("In basso a sinistra"))
bottom_layout.addWidget(QPushButton("In basso a destra"))

# Terzo layout griglia
grid_layout = QGridLayout()
grid_layout.addWidget(QPushButton("Widget 1"), 0, 0)
grid_layout.addWidget(QPushButton("Widget 2"), 0, 1)
grid_layout.addWidget(QPushButton("Widget 3"), 1, 0, 1, 2)  # Occupa due colonne

# Quarto layout stack
stack_layout = QStackedLayout()
stack_layout.addWidget(QPushButton("Vista 1"))
stack_layout.addWidget(QPushButton("Vista 2"))
stack_layout.addWidget(QPushButton("Vista 3"))
stack_layout.setCurrentIndex(1) # Cambia vista manualmente (mostra la seconda vista)

# Quinto layout con spazi flessibili
stretch = QHBoxLayout()
stretch.addWidget(QPushButton("Widget 1"))
stretch.addStretch()  # Spazio flessibile
stretch.addWidget(QPushButton("Widget 2"))
stretch.setStretch(0, 1)  # Il primo widget si espande meno
stretch.setStretch(2, 3)  # Il secondo widget si espande di più

# Aggiungi i layout orizzontali al layout principale
main_layout.addLayout(top_layout)
main_layout.addLayout(bottom_layout)
main_layout.addLayout(grid_layout)
main_layout.addLayout(stack_layout)
main_layout.addLayout(stretch)

# Configurazione finestra
window = QWidget()
window.setWindowTitle("Layout")
window.setLayout(main_layout)
window.show()

app.exec()