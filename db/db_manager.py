import sqlite3

class DatabaseManager:
    def __init__(self, db_name="app_database.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
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
        query = "SELECT nome, tipo FROM Accessorio"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def search_by_name(self, partial_name):
        """Cerca i nomi nel database che corrispondono parzialmente."""
        query = "SELECT nome FROM Accessorio WHERE nome LIKE ?"
        cursor = self.connection.cursor()
        cursor.execute(query, (f"%{partial_name}%",))
        return [row[0] for row in cursor.fetchall()]

    def close_connection(self):
        """Chiude la connessione al database."""
        if self.connection:
            self.connection.close()
