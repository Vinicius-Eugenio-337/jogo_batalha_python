from atk import Atk
from efeito import Efeito
from slayer import Slayer
from oni import Oni
from personagens import PERSONAGENS
from bancodedados import criar_tabela_jogadores, adicionar_jogador, obter_jogador, adicionar_xp

import time
from datetime import datetime

# ---------- CONFIGURAÇÃO DO BANCO ----------
criar_tabela_jogadores()

# ---------- FUNÇÕES DE INTERAÇÃO ----------
def listar_personagens(personagens=PERSONAGENS):
    print("\n" + "="*40)
    print("🌸  LISTA DE PERSONAGENS DISPONÍVEIS  🌸")
    print("="*40)
    for num, p in personagens.items():
        print(f"\n[{num}] 🧍 {p['nome'].upper()} ({p['tipo']})")
        print("-"*40)
        print(f"  🧠 Idade: {p.get('idade','??')} anos")
        print(f"  ❤️ Vida: {p.get('vida','??')}")
        print(f"  💨 Esquiva: {p.get('esquiva',0)*100:.0f}%")
        print(f"  🌬️ Respiração: {p.get('tipo_resp','Nenhuma')}")
        print(f"  ⚔️ Ataque Base: {p['atk'].dano if 'atk' in p else 'N/A'}")
        print(f"  ☠️ Efeito: {p['atk'].efeito.tipo if 'atk' in p else 'N/A'}")
        print("-"*40)
    print()

def mostrar_info_jogador(jogador_db):
    xp_para_proximo = 10 - jogador_db['xp'] % 10
    print(f"\n👤 {jogador_db['nome']} - Nível {jogador_db['nivel']} | XP: {jogador_db['xp']} | Próximo nível em {xp_para_proximo} XP\n")

def selecionar_usuario(num_jogador):
    while True:
        nome = input(f"Digite o nome do Jogador {num_jogador}: ").strip()
        if not nome:
            print("❌ Nome inválido.")
            continue
        # adiciona jogador no banco se não existir
        adicionar_jogador(nome)
        jogador_db = obter_jogador(nome)
        # mostrar info do jogador imediatamente após o login
        mostrar_info_jogador(jogador_db)
        return jogador_db

def escolher_personagem_interativo(jogador, personagens_disponiveis):
    while True:
        try:
            listar_personagens()
            escolha = input(f"\n{jogador['nome']}, digite o número do personagem: ").strip()
            if escolha.lower() == "exit":
                return None
            escolha_num = int(escolha)
            if escolha_num not in personagens_disponiveis:
                print("❌ Número inválido.")
                continue

            pinfo = personagens_disponiveis[escolha_num]
            if pinfo["tipo"] == "Slayer":
                return Slayer(
                    pinfo["nome"],
                    pinfo["idade"],
                    pinfo["vida"],
                    pinfo["esquiva"],
                    pinfo["tipo_resp"],
                    pinfo["hashira"],
                    pinfo["atk"]
                )
            elif pinfo["tipo"] == "Oni":
                return Oni(
                    pinfo["nome"],
                    pinfo["idade"],
                    pinfo["vida"],
                    pinfo["esquiva"],
                    pinfo["tipo_resp"],
                    pinfo.get("regen",0),
                    pinfo["atk"]
                )
            else:
                print("❌ Tipo de personagem desconhecido.")
        except ValueError:
            print("❌ Entrada inválida.")

# ---------- FUNÇÃO DA BATALHA ----------
def iniciar_batalha(jogador1_db, jogador2_db):
    print("\n=== SELEÇÃO DE PERSONAGENS ===")

    personagens_disponiveis = PERSONAGENS.copy()
    p1 = escolher_personagem_interativo(jogador1_db, personagens_disponiveis)
    if not p1:
        return
    del personagens_disponiveis[next(k for k,v in PERSONAGENS.items() if v["nome"]==p1.nome)]

    p2 = escolher_personagem_interativo(jogador2_db, personagens_disponiveis)
    if not p2:
        return

    print(f"\n✅ {p1.nome} e {p2.nome} prontos para a batalha!\n")
    time.sleep(1)

    turno = 1
    veneno_p1 = []
    veneno_p2 = []

    def aplicar_veneno(personagem, veneno_lista):
        if veneno_lista:
            dano_total = 0
            for i in range(len(veneno_lista)):
                dano, turnos = veneno_lista[i]
                personagem.vida -= dano
                dano_total += dano
                veneno_lista[i] = (dano, turnos-1)
            veneno_lista[:] = [v for v in veneno_lista if v[1] > 0]
            if dano_total > 0:
                print(f"☠️ {personagem.nome} sofreu {dano_total} de dano de veneno!")
                personagem.ajustar_vida()
                if personagem.vida <= 0:
                    return True
        return False

    while p1.vida > 0 and p2.vida > 0:
        print(f"\n========== 🌀 TURNO {turno} 🌀 ==========")
        print(f"{p1.nome}: {p1.vida}/{p1.vida_max} HP  |  {p2.nome}: {p2.vida}/{p2.vida_max} HP\n")

        if aplicar_veneno(p1, veneno_p1):
            print(f"💀 {p1.nome} morreu por veneno! {p2.nome} vence!")
            adicionar_xp(jogador2_db['nome'],5)
            break
        if aplicar_veneno(p2, veneno_p2):
            print(f"💀 {p2.nome} morreu por veneno! {p1.nome} vence!")
            adicionar_xp(jogador1_db['nome'],5)
            break

        # --- TURNO P1 ---
        print(f"\n🎴 {p1.nome}, é sua vez!")
        p1.lista_acoes()
        acao = input("Escolha uma ação (1 = atacar, 2 = esquivar, exit = sair): ").strip().lower()
        if acao=="exit":
            print("Batalha encerrada pelo jogador.")
            return
        if acao=="1":
            if p2.conseguiu_esquivar==0:
                if getattr(p1.atk.efeito,"dano_poison",0)!=0:
                    veneno_p2.append((p1.atk.efeito.dano_poison,3))
                dano_total = p1.atk.dano
                p2.vida -= dano_total
                p2.ajustar_vida()
                print(f"💥 {p1.nome} atacou {p2.nome}! Dano: {dano_total}")
            else:
                print(f"😎 {p2.nome} esquivou!")
                p2.conseguiu_esquivar=0
        elif acao=="2":
            p1.esquivar()
        else:
            print("Opção inválida.")
        if p2.vida<=0:
            print(f"\n💀 {p2.nome} foi derrotado! {p1.nome} vence!")
            adicionar_xp(jogador1_db['nome'],5)
            break
        if isinstance(p1, Oni):
            p1.regenerar()

        # --- TURNO P2 ---
        print(f"\n🔥 {p2.nome}, é sua vez!")
        p2.lista_acoes()
        acao = input("Escolha uma ação (1 = atacar, 2 = esquivar, exit = sair): ").strip().lower()
        if acao=="exit":
            print("Batalha encerrada pelo jogador.")
            return
        if acao=="1":
            if p1.conseguiu_esquivar==0:
                if getattr(p2.atk.efeito,"dano_poison",0)!=0:
                    veneno_p1.append((p2.atk.efeito.dano_poison,3))
                dano_total = p2.atk.dano
                p1.vida -= dano_total
                p1.ajustar_vida()
                print(f"💥 {p2.nome} atacou {p1.nome}! Dano: {dano_total}")
            else:
                print(f"😏 {p1.nome} esquivou!")
                p1.conseguiu_esquivar=0
        elif acao=="2":
            p2.esquivar()
        else:
            print("Opção inválida.")
        if p1.vida<=0:
            print(f"\n💀 {p1.nome} foi derrotado! {p2.nome} vence!")
            adicionar_xp(jogador2_db['nome'],5)
            break
        if isinstance(p2, Oni):
            p2.regenerar()

        turno +=1
        time.sleep(0.6)

    print("\n🏁 Fim da batalha!\n")

# ---------- SOBRE ----------
def sobre_projeto():
    print("\n📘 SOBRE O PROJETO")
    print("=" * 30)
    print("Projeto: Demon Slayer RPG")
    print("Autor: Vinícius Eugênio")
    print("Descrição: Simulação de batalhas entre Slayers e Onis,")
    print("com sistema de ataques, esquivas, efeitos de veneno,")
    print("e banco de jogadores com XP e níveis.")
    print("=" * 30)
    input("\nPressione Enter para voltar ao menu...")

# ---------- MENU ----------
def menu_principal():
    while True:
        print("\n🌸 MENU PRINCIPAL 🌸")
        print("1 - Iniciar Batalha")
        print("2 - Listar Personagens")
        print("3 - Sobre o Projeto")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip().lower()
        if opcao in ("1","iniciar","iniciar batalha"):
            jogador1_db = selecionar_usuario(1)
            jogador2_db = selecionar_usuario(2)
            iniciar_batalha(jogador1_db,jogador2_db)
        elif opcao in ("2","listar","listar personagens"):
            listar_personagens()
            input("Pressione Enter para voltar ao menu...")
        elif opcao in ("3","sobre"):
            sobre_projeto()
        elif opcao in ("4","sair","exit"):
            print("Saindo do jogo... 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# ---------- EXECUÇÃO ----------
if __name__=="__main__":
    menu_principal()
