import random

class Person:
    def __init__(self, nome: str, idade: int, vida: int, esquiva: float, tipo_resp: str, atk: object):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.esquiva = esquiva
        self.tipo_resp = tipo_resp
        self.atk = atk
        self.envenenado = 0
        self.conseguiu_esquivar = 0
        self.vida_max = vida

    def ajustar_vida(self):
        """Garante 0 <= vida <= vida_max."""
        if self.vida < 0:
            self.vida = 0
        elif self.vida > self.vida_max:
            self.vida = self.vida_max

    def lista_acoes(self):
        print("\natk:", self.atk, "\nesq:", self.esquiva)

    def atacar(self):
        print(self.atk)

    def esquivar(self):
        chance = random.random()
        if chance <= self.esquiva:
            self.conseguiu_esquivar = 1
            print(f"{self.nome} conseguiu esquivar! ({chance:.2f} ≤ {self.esquiva:.2f})")
        else:
            self.conseguiu_esquivar = 0
            print(f"{self.nome} não conseguiu esquivar... ({chance:.2f} > {self.esquiva:.2f})")

    def ajustar_vida(self):
        if self.vida < 0:
            self.vida = 0
        elif self.vida > self.vida_max:
            self.vida = self.vida_max

    def mostrar_vida(self):
        print(f"❤️ {self.nome}: {self.vida}/{self.vida_max} de vida")

    def __str__(self):
        return f'Nome:{self.nome} | Idade:{self.idade} | Vida:{self.vida} | Esquiva:{self.esquiva * 100:.0f}% | Respiração:{self.tipo_resp}'