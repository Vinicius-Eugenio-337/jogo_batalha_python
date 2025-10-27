class Efeito:
    def __init__(self, tipo: str, dano_poison: int):
        self.tipo = tipo
        self.dano_poison = dano_poison

    def __str__(self):
        return f'{self.tipo} {self.dano_poison}'