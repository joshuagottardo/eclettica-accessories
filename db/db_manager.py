import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from models.accessory import Accessory

class DatabaseManager:
    def __init__(self, db_name="app_database.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        
        # Per assicurare la creazione della tabella Accessorio, se non esiste già
        self.create_table()

    def create_table(self):
        """Crea la tabella Accessorio se non esiste già."""
        query = '''
        CREATE TABLE IF NOT EXISTS Accessorio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            immagine BLOB NOT NULL
        )
        '''
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def insert_accessory(self, nome, tipo, immagine):
        """Inserisce un nuovo accessorio nel database.

        Args:
            nome (str): Nome dell'accessorio.
            tipo (str): Tipo dell'accessorio.
            immagine (bytes): Immagine dell'accessorio come oggetto binario.

        Raises:
            ValueError: Se uno dei campi obbligatori non è fornito.
        """
        if not nome or not tipo or not immagine:
            raise ValueError("I campi 'nome', 'tipo' e 'immagine' sono obbligatori.")

        query = '''
        INSERT INTO Accessorio (nome, tipo, immagine) 
        VALUES (?, ?, ?)
        '''
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (nome, tipo, immagine))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Errore durante l'inserimento: {e}")

    def get_all_names_and_types(self):
        """Recupera tutti i nomi e i tipi dal database."""
        query = "SELECT id, nome, tipo, immagine FROM Accessorio ORDER BY nome"
        cursor = self.connection.cursor()
        results = cursor.execute(query)
        accessories = [Accessory(id, nome, tipo, immagine) for id, nome, tipo, immagine in results]
        return accessories
    
    def get_tags(self):
        """Recupera tutti i tag dal database."""
        query = "SELECT nome FROM tag ORDER BY nome"
        cursor = self.connection.cursor()
        cursor.execute(query)
        tags = [row[0] for row in cursor.fetchall()]
        return tags

    def close_connection(self):
        """Chiude la connessione al database."""
        if self.connection:
            self.connection.close()
