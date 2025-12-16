import sqlite3
'''A classe Coleção é o agrupamento de obras. Possui a função de adicionar e mostrar as obras na coleção'''
class Colecao:
    def __init__(self, id_obra):
        self.id_obra = id_obra  

    def adicionar_obra_colecao(self, id_obra):
        self.id_obra = id_obra
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("SELECT titulo FROM obra WHERE id_obra = ?", (id_obra,))
        obra = cursor.fetchone()
        if not obra:
            conn.close()
            raise ValueError(f"Obra com id {id_obra} não existe no banco.")

        try:
            cursor.execute("INSERT INTO colecao (id_obra) VALUES (?)", (id_obra,))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise ValueError(f"A obra '{obra[0]}' já está na coleção.")
        conn.close()
        print("Obra adicionada à coleção.")

    def listar_obras_colecao(self):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.id_obra, o.titulo, o.autor, o.status
            FROM obra o
            JOIN colecao c ON o.id_obra = c.id_obra
        """)
        obras = cursor.fetchall()
        conn.close()
        print(obras)
