# testbench.py
from person import Person
from slayer import Slayer
from oni import Oni
from atk import Atk
from efeito import Efeito

print("=== TESTBENCH COMPLETO ===\n")

# ------------------------------
# Criar efeitos
# ------------------------------
efeito_nenhum = Efeito("Nenhum", 0)
efeito_veneno = Efeito("Veneno", 5)

print("Efeitos criados:")
print(f"Efeito 1: {efeito_nenhum}")
print(f"Efeito 2: {efeito_veneno}\n")

# ------------------------------
# Criar ataques
# ------------------------------
atk1 = Atk(7, efeito_nenhum)
atk2 = Atk(5, efeito_veneno)

print("Ataques criados:")
print(f"Atk 1: {atk1}")
print(f"Atk 2: {atk2}\n")

# ------------------------------
# Teste 1: Person genérico
# ------------------------------
p = Person("TestePerson", 20, 15, 0.2, "Sol", atk1)
print("Person instanciado:")
print(p)
p.mostrar_vida()
p.esquivar()
print()

# ------------------------------
# Teste 2: Slayer
# ------------------------------
slayer = Slayer("Tanjiro", 15, 20, 0.3, "Sol", False, atk1)
print("Slayer instanciado:")
print(slayer)
slayer.mostrar_vida()
slayer.esquivar()
print()

# ------------------------------
# Teste 3: Oni
# ------------------------------
oni = Oni("Kokushibo", 480, 50, 0.1, "Lua", 5, atk2)
print("Oni instanciado:")
print(oni)
oni.mostrar_vida()
oni.esquivar()
oni.regenerar()
oni.mostrar_vida()
print()

# ------------------------------
# Teste de ataques
# ------------------------------
print("Simulação de ataques:")
print(f"{slayer.nome} ataca {oni.nome}")
dano_total = slayer.atk.dano + oni.envenenado
oni.vida -= dano_total
oni.ajustar_vida()
oni.mostrar_vida()
print()

print(f"{oni.nome} ataca {slayer.nome}")
dano_total = oni.atk.dano + slayer.envenenado
slayer.vida -= dano_total
slayer.ajustar_vida()
slayer.mostrar_vida()
print()

print("=== FIM DO TESTBENCH ===")
