from atk import Atk
from efeito import Efeito
from slayer import Slayer
from oni import Oni
from personagens import PERSONAGENS  # dicionário com os personagens

import time  # só pra dar ritmo nos prints (mais imersão)


def listar_personagens(personagens=PERSONAGENS):
    """Lista personagens. Aceita ser chamada sem argumentos."""
    print("\n" + "=" * 40)
    print("🌸  LISTA DE PERSONAGENS DISPONÍVEIS  🌸")
    print("=" * 40)

    for num, p in personagens.items():
        print(f"\n[{num}] 🧍 {p['nome'].upper()} ({p['tipo']})")
        print("-" * 40)
        print(f"  🧠 Idade: {p.get('idade', '??')} anos")
        print(f"  ❤️ Vida: {p.get('vida', '??')}")
        print(f"  💨 Esquiva: {p.get('esquiva', 0) * 100:.0f}%")
        print(f"  🌬️ Respiração: {p.get('tipo_resp', 'Nenhuma')}")
        print(f"  ⚔️ Ataque Base: {p['atk'].dano if 'atk' in p else 'N/A'}")
        print(f"  ☠️ Efeito: {p['atk'].efeito.tipo if 'atk' in p else 'N/A'}")
        print("-" * 40)
    print()


def escolher_personagem_interativo(jogador):
    """Loop seguro para escolher personagem (retorna instância de Person)."""
    while True:
        try:
            listar_personagens()
            escolha = input(f"\n{jogador}, digite o número do personagem: ").strip()
            if escolha.lower() == "exit":
                return None
            escolha_num = int(escolha)
            if escolha_num not in PERSONAGENS:
                print("❌ Número inválido. Tente novamente.")
                continue

            pinfo = PERSONAGENS[escolha_num]
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
                    pinfo.get("regen", 0),
                    pinfo["atk"]
                )
            else:
                print("❌ Tipo de personagem desconhecido.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número ou 'exit' para cancelar.")


def iniciar_batalha():
    """Função que engloba a seleção e o loop de batalha."""
    print("=== SELEÇÃO DE PERSONAGEM ===")

    p1 = escolher_personagem_interativo("Jogador 1")
    if p1 is None:
        print("Seleção do jogador 1 cancelada. Voltando ao menu.")
        return

    print(f"\n✅ {p1.nome} escolhido(a)!\n")

    # Jogador 2 — impede escolher o mesmo personagem
    while True:
        p2 = escolher_personagem_interativo("Jogador 2")
        if p2 is None:
            print("Seleção do jogador 2 cancelada. Voltando ao menu.")
            return
        if p2.nome == p1.nome:
            print("❌ Esse personagem já foi escolhido pelo Jogador 1. Escolha outro.")
            continue
        break

    print(f"\n✅ {p2.nome} escolhido(a)!\n")

    # -------------------------
    # 🎯 COMEÇA A BATALHA
    # -------------------------
    print("\n⚔️  COMEÇA A BATALHA! ⚔️\n")
    time.sleep(0.8)

    turno = 1
    while p1.vida > 0 and p2.vida > 0:
        print(f"\n========== 🌀 TURNO {turno} 🌀 ==========")
        print(f"{p1.nome}: {p1.vida}/{p1.vida_max} HP  |  {p2.nome}: {p2.vida}/{p2.vida_max} HP\n")

        # -------------------------------
        # TURNO P1
        # -------------------------------
        print(f"\n🎴 {p1.nome}, é sua vez!")
        p1.lista_acoes()
        acao = input("Escolha uma ação (1 = atacar, 2 = esquivar, exit = sair): ").strip().lower()
        if acao == "exit":
            print("Batalha encerrada pelo jogador.")
            return

        if acao == "1":  # atacar
            if p2.conseguiu_esquivar == 0:
                if getattr(p1.atk.efeito, "dano_poison", 0) != 0:
                    p2.envenenado += p1.atk.efeito.dano_poison
                dano_total = p1.atk.dano + p2.envenenado
                p2.vida -= dano_total
                p2.ajustar_vida()
                print(f"💥 {p1.nome} atacou {p2.nome}! Dano total: {dano_total}")
                p1.mostrar_vida()
                p2.mostrar_vida()
            else:
                print(f"😎 {p2.nome} esquivou do ataque!")
                p2.conseguiu_esquivar = 0
        elif acao == "2":
            p1.esquivar()
        else:
            print("Opção inválida — turno perdido.")

        time.sleep(0.5)

        # Verifica se p2 morreu
        if p2.vida <= 0:
            print(f"\n💀 {p2.nome} foi derrotado(a)! {p1.nome} venceu!")
            break

        # Regeneração do p1 (após sua ação)
        if isinstance(p1, Oni):
            p1.regenerar()

        # -------------------------------
        # TURNO P2
        # -------------------------------
        print(f"\n🔥 {p2.nome}, é sua vez!")
        p2.lista_acoes()
        acao = input("Escolha uma ação (1 = atacar, 2 = esquivar, exit = sair): ").strip().lower()
        if acao == "exit":
            print("Batalha encerrada pelo jogador.")
            return

        if acao == "1":  # atacar
            if p1.conseguiu_esquivar == 0:
                if getattr(p2.atk.efeito, "dano_poison", 0) != 0:
                    p1.envenenado += p2.atk.efeito.dano_poison
                dano_total = p2.atk.dano + p1.envenenado
                p1.vida -= dano_total
                p1.ajustar_vida()
                print(f"💥 {p2.nome} atacou {p1.nome}! Dano total: {dano_total}")
                p1.mostrar_vida()
                p2.mostrar_vida()
            else:
                print(f"😏 {p1.nome} desviou com estilo!")
                p1.conseguiu_esquivar = 0
        elif acao == "2":
            p2.esquivar()
        else:
            print("Opção inválida — turno perdido.")

        # Verifica se p1 morreu
        if p1.vida <= 0:
            print(f"\n💀 {p1.nome} foi derrotado! {p2.nome} venceu!")
            break

        if isinstance(p2, Oni):
            p2.regenerar()

        turno += 1
        time.sleep(0.6)

    print("\n🏁 Fim da batalha!\n")


def sobre_projeto():
    print("\n📘 SOBRE O PROJETO")
    print("=" * 30)
    print("Projeto: Demon Slayer RPG")
    print("Autor: Vinícius Eugênio")
    print("Descrição: Simulação de batalhas entre Slayers e Onis,")
    print("com sistema de ataques, esquivas e efeitos de veneno.")
    print("Menu funcional com acesso a todas as funcionalidades.")
    print("=" * 30)
    input("\nPressione Enter para voltar ao menu...")


def menu_principal():
    """Loop principal com tratamento robusto de entrada."""
    while True:
        print("\n🌸 MENU PRINCIPAL 🌸")
        print("1 - Iniciar Batalha")
        print("2 - Listar Personagens")
        print("3 - Sobre o Projeto")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip().lower()

        # aceitar números e palavras (ex: '1' ou 'iniciar')
        if opcao in ("1", "iniciar", "iniciar batalha"):
            iniciar_batalha()
        elif opcao in ("2", "listar", "listar personagens"):
            listar_personagens()
            input("Pressione Enter para voltar ao menu...")
        elif opcao in ("3", "sobre"):
            sobre_projeto()
        elif opcao in ("4", "sair", "exit"):
            print("Saindo do jogo... 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
