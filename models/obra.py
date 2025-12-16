from abc import ABC, abstractmethod
import sqlite3
from typing import Optional
from models.status import Status

'''A classe Obra é uma classe superclasse Abstrata, servindo como um molde e permitindo que Livro e Revistas herdem seus métodos e atributos. 
Contém as opereções de CRUD e os métodos especiais. '''
class Obra(ABC):
    def __init__(self, titulo, ano, autor, tipo, genero, numero_paginas, avaliacao = None, db_path ="biblioteca.db"):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.tipo = tipo
        self.genero = genero
        self.numero_paginas = numero_paginas
        self.avaliacao = avaliacao
        self.db_path = db_path

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo_valido: str):
        if titulo_valido.strip() == "":
            raise ValueError("Título inválido! O campo não pode ser vazio.")
        else:
            self._titulo = titulo_valido

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano_valido):
        if ano_valido < 1500:
            raise ValueError("Ano inálido! O ano deve ser maior que 1500!")
        else:
            self._ano = ano_valido

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor_valido):
        if autor_valido == "":
            raise ValueError("Autor inválido! O campo não pode ser vazio!")
        else: 
            self._autor = autor_valido
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter 
    def tipo(self, tipo_valido):
        if tipo_valido not in ("revista", "livro"):
            raise ValueError("Tipo inválido! O tipo deve ser livro ou revista!")
        else:
            self._tipo = tipo_valido
        
    @property
    @abstractmethod
    def genero(self):
        pass

    @genero.setter 
    @abstractmethod
    def genero(self, genero_valido):
        pass
        
    @property
    def numero_paginas(self):
        return self._numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, numero_paginas_valido):
        if not isinstance(numero_paginas_valido, int):
            raise ValueError("Erro. O número de páginas deve ser um valor inteiro.")
        else:
            self._numero_paginas = numero_paginas_valido

    @property
    def avaliacao(self):
        return self._avaliacao
    
    @avaliacao.setter
    def avaliacao(self, avaliacao_valido):
        if avaliacao_valido != None:   
            if not isinstance(avaliacao_valido, float) or avaliacao_valido > 10 or avaliacao_valido < 0:
                raise ValueError("Nota inválida! Deve ser entre 0-10!")
            else:
                self._avaliacao = avaliacao_valido 
        self._avaliacao = avaliacao_valido
    
    # CRUD de Obra

    def _conectar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        return conn, cursor
    
    def adicionar_obra(self, titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status = 'NAO_LIDO'):
        conn, cursor = self._conectar()
        cursor.execute("""
        INSERT INTO obra (titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (titulo, ano, autor, tipo, genero, numero_paginas, avaliacao, status))
        conn.commit()
        conn.close()

    @classmethod
    def listar_obras(cls, titulo):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM obra WHERE titulo=?", (titulo,))
        obras = cursor.fetchall()
        conn.close()
        return obras

    @classmethod
    def atualizar_obra(self, id_obra, titulo=None, ano=None, autor=None, genero=None, numero_paginas=None, avaliacao=None, status=None):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
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

    @classmethod
    def deletar_obra(self, id_obra):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM obra WHERE id_obra=?", (id_obra,))
        conn.commit()
        conn.close()

    def salvar_no_banco(self, status='NAO_LIDO'):
        self.adicionar_obra(
            self.titulo,
            self.ano,
            self.autor,
            self.tipo,
            self.genero,
            self.numero_paginas,
            self.avaliacao,
            status
        )
        print("Obra salva com sucesso!")

    # Métodos especiais
    def __str__(self):
        return f"{self.titulo}, {self.tipo} por {self.autor}, publicado em {self.ano}"
    
    def __repr__(self):
        return (f"tipo={self.tipo} titulo='{self.titulo}' autor='{self.autor}' "
                f"ano={self.ano} genero={self.genero} paginas={self.numero_paginas} "
                f"avaliacao={self.avaliacao}>")

    def __eq__(self, other):
        if not isinstance(other, Obra):
            return False
        return self.titulo == other.titulo and self.autor == other.autor
    
    def __lt__(self, other):
        if not isinstance(other, Obra):
            return NotImplemented
        return self.ano < other.ano 
