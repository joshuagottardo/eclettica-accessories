class Accessory:
    def __init__(self, id: int = None, nome: str = None, tipo: str = None, immagine: str = None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.immagine = immagine

    def __repr__(self):
        return f"Accessory(id={self.id}, nome={self.nome}, tipo={self.tipo}, immagine={self.immagine})"

    def to_dict(self):
        """Converte l'oggetto Accessory in un dizionario."""
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "immagine": self.immagine
        }