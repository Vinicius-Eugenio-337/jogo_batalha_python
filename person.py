class Person:
    def __init__(self, nome, idade, vida, esquiva, tipo_resp, atk):
        self.nome = nome
        self.idade = idade
        self.vida_max = vida
        self.vida = vida
        self.esquiva = esquiva
        self.tipo_resp = tipo_resp
        self.atk = atk

        # --- Veneno ---
        self.veneno_dano = 0      # quanto dano por turno
        self.veneno_turnos = 0    # quantos turnos restantes
        # --- Esquiva ---
        self.conseguiu_esquivar = 0

    def mostrar_vida(self):
        print(f"{self.nome}: {self.vida}/{self.vida_max} HP")

    def ajustar_vida(self):
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        if self.vida < 0:
            self.vida = 0

    def esquivar(self):
        from random import random
        chance = random()
        if chance < self.esquiva:
            self.conseguiu_esquivar = 1
            print(f"{self.nome} conseguiu esquivar!")
        else:
            self.conseguiu_esquivar = 0
            print(f"{self.nome} não conseguiu esquivar.")

    # --- NOVO: Veneno ---
    def aplicar_veneno(self, dano):
        self.veneno_dano = dano
        self.veneno_turnos = 3
        print(f"☠️ {self.nome} foi envenenado! Sofrerá {dano} de dano por 3 turnos.")

    def processar_veneno(self):
        if self.veneno_turnos > 0:
            self.vida -= self.veneno_dano
            self.ajustar_vida()
            self.veneno_turnos -= 1
            print(f"☠️ {self.nome} sofre {self.veneno_dano} de dano de veneno! Turnos restantes: {self.veneno_turnos}")
class Person:
    def __init__(self, nome: str, idade: int, vida: int, esquiva: float, tipo_resp: str, atk: object):
        self.nome = nome
        self.idade = idade
        self.vida_max = vida
        self.vida = vida
        self.esquiva = esquiva
        self.tipo_resp = tipo_resp
        self.atk = atk
        self.conseguiu_esquivar = 0
        self.envenenado = 0
        self.turnos_veneno = 0

    def lista_acoes(self):
        print("1 - Atacar")
        print("2 - Esquivar")

    def esquivar(self):
        import random
        chance = random.random()
        if chance < self.esquiva:
            self.conseguiu_esquivar = 1
            print(f"😎 {self.nome} conseguiu esquivar!")
        else:
            print(f"😔 {self.nome} falhou na esquiva.")

    def ajustar_vida(self):
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        elif self.vida < 0:
            self.vida = 0

    def mostrar_vida(self):
        print(f"💖 {self.nome}: {self.vida}/{self.vida_max} HP")

    def processar_veneno(self):
        if self.turnos_veneno > 0:
            print(f"☠️ {self.nome} sofre dano do veneno! (-{self.envenenado} HP)")
            self.vida -= self.envenenado
            self.ajustar_vida()
            self.turnos_veneno -= 1
            self.mostrar_vida()
            if self.vida <= 0:
                print(f"💀 {self.nome} morreu por veneno!")
                return True  # morreu
        return False