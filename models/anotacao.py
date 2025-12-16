import sqlite3
from datetime import datetime
from typing import Optional
'''A classe Anotacao permite escrever um texto  relacionado a uma obra, podendo selecionar um trecho ou nao.'''
class Anotacao:
    def __init__(self, id_obra, texto = None, trecho = None, data = None):
        self.id_obra = id_obra
        self.texto = texto
        self.trecho = trecho
        self.data = data

    def _conectar(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        return conn, cursor

    def adicionar_anotacao(self, id_obra, texto, trecho=None, data = datetime.now().strftime("%d-%m-%Y")):
        conn, cursor = self._conectar()
        cursor.execute("""
            INSERT INTO anotacao (id_obra, texto, trecho, data)
            VALUES (?, ?, ?, ?)
        """, (id_obra, texto, trecho, data))
        conn.commit()
        conn.close()
        print("Anotação adicionada com sucesso!")
        
    
    def atualizar_anotacao(self, id_obra, texto, trecho, data):
        conn, cursor = self._conectar()
        campos = []
        valores = []
        if texto is not None:
            campos.append("texto=?")
            valores.append(texto)
        if data is not None:
            campos.append("trecho=?")
            valores.append(trecho)
        if trecho is not None:
            campos.append("data=?")
            valores.append(data)

        valores.append(id_obra) 
        sql = f"UPDATE anotacao SET {', '.join(campos)} WHERE id_obra=?"
        print("SQL EXECUTADO:", sql)
        cursor.execute(sql, valores)
        conn.commit()
        conn.close()
        print("Anotação atualizada com sucesso!")

    def listar_anotacoes(self, id_obra=None):
        conn, cursor = self._conectar()
        if id_obra is not None:
            cursor.execute("SELECT * FROM anotacao WHERE id_obra=?", (id_obra,))
        else:
            cursor.execute("SELECT * FROM anotacao")
        anotacoes = cursor.fetchall()
        conn.close()
        print("Mostrar anotação")
        return anotacoes

    @classmethod
    def deletar_anotacao(cls, id_anotacao):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM anotacao WHERE id_anotacao=?", (id_anotacao,))
        conn.commit()
        conn.close()
        print("Anotação deletada com sucesso!")