import sqlite3

class Dados:
    def __init__(self, db_path="biblioteca.db"):
        self.db_path = db_path

    def _conectar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        return conn, cursor

#CRUD de Obras
    def adicionar_obra(self, titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status):
        conn, cursor = self._conectar()
        cursor.execute("""
        INSERT INTO obra (titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status))
        conn.commit()
        conn.close()

    def listar_obras(self):
        conn, cursor = self._conectar()
        cursor.execute("SELECT * FROM obra")
        obras = cursor.fetchall()
        conn.close()
        return obras

    def atualizar_obra(self, id_obra, titulo=None, ano=None, autor=None, tipo=None, genero=None, numero_paginas=None, avaliacao=None, status=None):
        conn, cursor = self._conectar()
        campos = []
        valores = []
        if titulo is not None:
            campos.append("titulo=?")
            valores.append(titulo)
        if ano is not None:
            campos.append("ano=?")
            valores.append(ano)
        if autor is not None:
            campos.append("autor=?")
            valores.append(autor)
        if tipo is not None:
            campos.append("tipo=?")
            valores.append(tipo)
        if genero is not None:
            campos.append("genero=?")
            valores.append(genero)
        if numero_paginas is not None:
            campos.append("numero_paginas=?")
            valores.append(numero_paginas)
        if avaliacao is not None:
            campos.append("avaliacao=?")
            valores.append(avaliacao)
        if status is not None:
            campos.append("status=?")
            valores.append(status)
        
        valores.append(id_obra) 
        sql = f"UPDATE obra SET {', '.join(campos)} WHERE id_obra=?"
        cursor.execute(sql, valores)
        conn.commit()
        conn.close()

    def deletar_obra(self, id_obra):
        conn, cursor = self._conectar()
        cursor.execute("DELETE FROM obra WHERE id_obra=?", (id_obra,))
        conn.commit()
        conn.close()

# CRUD de Anotações

    def adicionar_anotacao(self, id_obra, texto, trecho=None, data=None):
        conn, cursor = self._conectar()
        cursor.execute("""
            INSERT INTO anotacao (id_obra, texto, trecho, data)
            VALUES (?, ?, ?, ?)
        """, (id_obra, texto, trecho, data))
        conn.commit()
        conn.close()
        

    def atualizar_anotacao(self, id_obra, texto, trecho, data):
        conn, cursor = self._conectar()
        campos = []
        valores = []
        if texto is not None:
            campos.append("texto=?")
            valores.append(texto)
        if trecho is not None:
            campos.append("trecho=?")
            valores.append(trecho)
        if data is not None:
            campos.append("data=?")
            valores.append(data)

        valores.append(id_obra) 
        sql = f"UPDATE obra SET {', '.join(campos)} WHERE id_obra=?"
        cursor.execute(sql, valores)
        conn.commit()
        conn.close()

    def listar_anotacoes(self, id_obra=None):
        conn, cursor = self._conectar()
        if id_obra is not None:
            cursor.execute("SELECT * FROM anotacao WHERE id_obra=?", (id_obra,))
        else:
            cursor.execute("SELECT * FROM anotacao")
        anotacoes = cursor.fetchall()
        conn.close()
        return anotacoes

    def deletar_anotacao(self, id_anotacao):
        conn, cursor = self._conectar()
        cursor.execute("DELETE FROM anotacao WHERE id_anotacao=?", (id_anotacao,))
        conn.commit()
        conn.close()
