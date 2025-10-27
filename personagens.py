from atk import Atk
from efeito import Efeito

PERSONAGENS = {
    1: {
        "tipo": "Slayer",
        "nome": "Tanjiro",
        "idade": 15,
        "vida": 20,
        "esquiva": 0.3,
        "tipo_resp": "Sol",
        "hashira": False,
        "atk": Atk(8, Efeito("Nenhum", 0))
    },
    2: {
        "tipo": "Oni",
        "nome": "Kokushibo",
        "idade": 480,
        "vida": 20,
        "esquiva": 0.2,
        "tipo_resp": "Lua",
        "regen": 3,
        "hashira": False,
        "atk": Atk(5, Efeito("Nenhum", 0))
    },
    3: {
        "tipo": "Slayer",
        "nome": "Shinobu",
        "idade": 18,
        "vida": 12,
        "esquiva": 0.1,
        "tipo_resp": "Inseto",
        "hashira": True,
        "atk": Atk(3, Efeito("Veneno", 5))
    },
    4: {
        "tipo": "Oni",
        "nome": "Muzan",
        "idade": 1000,
        "vida": 50,
        "esquiva": 0.15,
        "tipo_resp": "Nenhuma",
        "regen": 5,
        "hashira": False,
        "atk": Atk(5, Efeito("Veneno", 5)) #dano_poison pode ser maior
    }
}
