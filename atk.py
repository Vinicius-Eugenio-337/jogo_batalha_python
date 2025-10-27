class Atk:
    def __init__(self, dano: int, efeito: object):
        self.dano = dano
        self.efeito = efeito

    def __str__(self):
        return f'{self.dano} {self.efeito}'

