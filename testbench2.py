# testbench_completo.py
from person import Person
from slayer import Slayer
from oni import Oni
from atk import Atk
from efeito import Efeito

print("=== TESTBENCH COMPLETO COM ASSERTS ===\n")

# ------------------------------
# Criar efeitos
# ------------------------------
efeito_nenhum = Efeito("Nenhum", 0)
efeito_veneno = Efeito("Veneno", 5)

# Verificação automática
assert efeito_nenhum.tipo == "Nenhum"
assert efeito_veneno.dano_poison == 5

print("Efeitos criados e verificados com sucesso.\n")

# ------------------------------
# Criar ataques
# ------------------------------
atk1 = Atk(7, efeito_nenhum)
atk2 = Atk(5, efeito_veneno)

# Verificação automática
assert atk1.dano == 7
assert atk1.efeito.tipo == "Nenhum"
assert atk2.efeito.dano_poison == 5

print("Ataques criados e verificados com sucesso.\n")

# ------------------------------
# Instanciar Person
# ------------------------------
p = Person("TestePerson", 20, 15, 0.2, "Sol", atk1)
assert p.nome == "TestePerson"
assert p.vida == 15
assert p.esquiva == 0.2

print("Person instanciado corretamente:")
print(p)
p.mostrar_vida()
p.esquivar()
print()

# ------------------------------
# Instanciar Slayer
# ------------------------------
slayer = Slayer("Tanjiro", 15, 20, 0.3, "Sol", False, atk1)
assert isinstance(slayer, Slayer)
assert slayer.hashira == False

print("Slayer instanciado corretamente:")
print(slayer)
slayer.mostrar_vida()
slayer.esquivar()
print()

# ------------------------------
# Instanciar Oni
# ------------------------------
oni = Oni("Kokushibo", 480, 50, 0.1, "Lua", 5, atk2)
assert isinstance(oni, Oni)
assert oni.regen == 5

print("Oni instanciado corretamente:")
print(oni)
oni.mostrar_vida()
oni.esquivar()
oni.regenerar()
assert oni.vida <= oni.vida_max  # verifica que vida não passou do máximo
oni.mostrar_vida()
print()

# ------------------------------
# Teste de ataques simples
# ------------------------------
print("Simulação de ataques:\n")

# Slayer ataca Oni
dano_total = slayer.atk.dano + oni.envenenado
oni.vida -= dano_total
oni.ajustar_vida()
oni.mostrar_vida()
assert 0 <= oni.vida <= oni.vida_max

# Oni ataca Slayer
dano_total = oni.atk.dano + slayer.envenenado
slayer.vida -= dano_total
slayer.ajustar_vida()
slayer.mostrar_vida()
assert 0 <= slayer.vida <= slayer.vida_max

print("\n=== FIM DOS TESTES ===")
