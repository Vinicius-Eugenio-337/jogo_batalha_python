from person import Person

class Slayer(Person):
    def __init__(self, nome:str, idade: int, vida: int, esquiva: float, tipo_resp: str, hashira: bool, atk: object):
        super().__init__(nome, idade, vida, esquiva, tipo_resp, atk)
        self.hashira = hashira