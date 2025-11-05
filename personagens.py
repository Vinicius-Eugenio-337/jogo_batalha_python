from atk import Atk
from efeito import Efeito

PERSONAGENS = {
    1: {
        "tipo": "Slayer",
        "nome": "Tanjiro",
        "idade": 15,
        "vida": 20,
        "esquiva": 0.25,
        "tipo_resp": "Sol",
        "hashira": False,
        "atk": Atk(9, Efeito("Nenhum", 0))
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
        "atk": Atk(7, Efeito("Nenhum", 0))
    },
    3: {
        "tipo": "Slayer",
        "nome": "Shinobu",
        "idade": 18,
        "vida": 12,
        "esquiva": 0.1,
        "tipo_resp": "Inseto",
        "hashira": True,
        "atk": Atk(2, Efeito("Veneno", 4))
    },
    4: {
        "tipo": "Oni",
        "nome": "Muzan",
        "idade": 1000,
        "vida": 35,
        "esquiva": 0.15,
        "tipo_resp": "Nenhuma",
        "regen": 4,
        "hashira": False,
        "atk": Atk(3, Efeito("Veneno", 4))
    },
    5: {
        "tipo": "Slayer",
        "nome": "Yoriichi",
        "idade": 25,
        "vida": 30,
        "esquiva": 0.95,
        "tipo_resp": "Sol",
        "hashira": False,
        "atk": Atk(17, Efeito("Nenhum", 0))
    },
    6: {
        "tipo": "Oni",
        "nome": "Akaza",
        "idade": 200,
        "vida": 17,
        "esquiva": 0.17,
        "tipo_resp": "Nenhuma",
        "regen": 2,
        "hashira": False,
        "atk": Atk(6, Efeito("Nenhum", 0))
    }
}
