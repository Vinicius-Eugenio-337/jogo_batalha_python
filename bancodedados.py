import sqlite3
from datetime import datetime

DB_NAME = "jogadores.db"

def criar_tabela_jogadores():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            nivel INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0,
            data_criacao TEXT
        )
    """)
    conn.commit()
    conn.close()

def adicionar_jogador(nome):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT OR IGNORE INTO jogadores (nome, nivel, xp, data_criacao)
        VALUES (?, 1, 0, ?)
    """, (nome, data_criacao))
    conn.commit()
    conn.close()

def obter_jogador(nome):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jogadores WHERE nome=?", (nome,))
    jogador = cursor.fetchone()
    conn.close()
    if jogador:
        return {
            "id": jogador[0],
            "nome": jogador[1],
            "nivel": jogador[2],
            "xp": jogador[3],
            "data_criacao": jogador[4]
        }
    return None

def adicionar_xp(nome, quantidade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nivel, xp FROM jogadores WHERE nome=?", (nome,))
    res = cursor.fetchone()
    if res is None:
        conn.close()
        return
    nivel, xp_atual = res
    xp_novo = xp_atual + quantidade
    # definir XP necessário para subir de nível
    xp_necessario = 5 * nivel  # exemplo: níveis iniciais sobem rápido
    while xp_novo >= xp_necessario:
        nivel += 1
        xp_novo -= xp_necessario
        xp_necessario = 5 * nivel
    cursor.execute("UPDATE jogadores SET xp=?, nivel=? WHERE nome=?", (xp_novo, nivel, nome))
    conn.commit()
    conn.close()
