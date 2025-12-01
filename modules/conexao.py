import sqlite3

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
                    status TEXT
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

# Instanciando para criar o banco
Conexao()
