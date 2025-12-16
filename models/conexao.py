import sqlite3
'''Cria a conexão com o banco e cria as três tabelas no sqlite3'''
class Conexao:
    def __init__(self):
        with sqlite3.connect('biblioteca.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS obra (
                    id_obra INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    ano INTEGER,
                    autor TEXT NOT NULL,
                    tipo TEXT,
                    genero TEXT,
                    numero_paginas INTEGER,
                    avaliacao FLOAT,
                    status TEXT DEFAULT 'NAO_LIDO' CHECK(status IN ('NAO_LIDO', 'LENDO', 'LIDO')),
                    data_inicio TEXT,
                    data_termino TEXT,
                    UNIQUE(titulo)                   
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anotacao (
                    id_anotacao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_obra INTEGER NOT NULL,
                    texto TEXT NOT NULL,
                    trecho TEXT,
                    data DATE,
                    FOREIGN KEY(id_obra) REFERENCES obra(id_obra)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS colecao (
                    id_colecao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_obra INTEGER NOT NULL,
                    titulo TEXT,
                    FOREIGN KEY(id_obra) REFERENCES obra(id_obra),
                    FOREIGN KEY(titulo) REFERENCES obra(titulo)
                    UNIQUE(id_obra)
                )
            """)

import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE obra ADD COLUMN data_inicio TEXT")
except sqlite3.OperationalError:
    pass

try:
    cursor.execute("ALTER TABLE obra ADD COLUMN data_termino TEXT")
except sqlite3.OperationalError:
    pass

conn.commit()
conn.close()
print("Colunas adicionadas com sucesso (ou já existiam).")

Conexao()