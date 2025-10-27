from person import Person

class Oni(Person):
    def __init__(self, nome: str, idade: int, vida: int, esquiva: float, tipo_resp: str, regen: int, atk: object):
        super().__init__(nome, idade, vida, esquiva, tipo_resp, atk)
        self.regen = regen

    def regenerar(self):
        self.vida += self.regen
        self.ajustar_vida()
        print(f"🩸 {self.nome} regenerou {self.regen} (vida: {self.vida}/{self.vida_max})")