from atk import Atk
from efeito import Efeito
from slayer import Slayer
from oni import Oni

print("=== TESTBENCH COMPLETO ===\n")

# -----------------------------
# Criar efeitos e ataques
# -----------------------------
efeito_nenhum = Efeito("Nenhum", 0)
efeito_veneno = Efeito("Veneno", 5)

atk_forte = Atk(10, efeito_nenhum)
atk_veneno = Atk(5, efeito_veneno)

print("✅ Ataques e efeitos criados:")
print(atk_forte)
print(atk_veneno)
print()

# -----------------------------
# Criar personagens
# -----------------------------
tanjiro = Slayer("Tanjiro", 15, 20, 0.3, "Sol", False, atk_forte)
shinobu = Slayer("Shinobu", 18, 12, 0.1, "Inseto", True, atk_veneno)
kokushibo = Oni("Kokushibo", 480, 20, 0.2, "Lua", 3, atk_forte)
muzan = Oni("Muzan", 1000, 50, 0.15, "Nenhuma", 5, atk_veneno)

personagens = [tanjiro, shinobu, kokushibo, muzan]

# -----------------------------
# Teste de atributos iniciais
# -----------------------------
print("✅ Testando atributos iniciais:\n")
for p in personagens:
    print(p)
    p.mostrar_vida()
print()

# -----------------------------
# Teste de esquiva
# -----------------------------
print("✅ Testando esquiva:\n")
for p in personagens:
    print(f"{p.nome} tentando esquivar...")
    p.esquivar()
print()

# -----------------------------
# Teste de ataque e envenenamento
# -----------------------------
print("✅ Testando ataques e veneno:\n")
# Tanjiro ataca Kokushibo
print("Tanjiro ataca Kokushibo")
kokushibo.vida -= tanjiro.atk.dano
if tanjiro.atk.efeito.dano_poison != 0:
    kokushibo.envenenado += tanjiro.atk.efeito.dano_poison
kokushibo.ajustar_vida()
kokushibo.mostrar_vida()
print(f"Envenenado: {kokushibo.envenenado}\n")

# Shinobu ataca Muzan
print("Shinobu ataca Muzan")
muzan.vida -= shinobu.atk.dano
if shinobu.atk.efeito.dano_poison != 0:
    muzan.envenenado += shinobu.atk.efeito.dano_poison
muzan.ajustar_vida()
muzan.mostrar_vida()
print(f"Envenenado: {muzan.envenenado}\n")

# -----------------------------
# Teste de regeneração (Oni)
# -----------------------------
print("✅ Testando regeneração dos Oni:\n")
for o in [kokushibo, muzan]:
    print(f"{o.nome} regenera...")
    o.regenerar()
print()

# -----------------------------
# Teste de ajustar_vida
# -----------------------------
print("✅ Testando ajustar_vida (vida não pode ultrapassar o máximo ou ser negativa):\n")
kokushibo.vida = 100  # ultrapassa o máximo
kokushibo.ajustar_vida()
kokushibo.mostrar_vida()

tanjiro.vida = -5  # valor negativo
tanjiro.ajustar_vida()
tanjiro.mostrar_vida()
print()

print("✅ TESTBENCH FINALIZADO")
