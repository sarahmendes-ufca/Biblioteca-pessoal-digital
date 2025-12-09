from obra import Obra

class Revista(Obra):
    def __init__ (self, titulo, ano, editora, tipo, genero, numero_paginas, avaliacao):
        super().__init__(titulo, ano, tipo, numero_paginas, avaliacao)
        self.editora = editora
        self.genero = genero

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
    def editora(self):
        print("Editora da Revista: ")
        return self._editora
    
    @editora.setter
    def editora(self, editora_valida):
        if editora_valida == "":
            raise ValueError("Editora inválida! O campo não pode ser vazio!")
        else: 
            self._editora = editora_valida

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
    def genero(self):
        print("Gênero do livro: ")
        return self._genero
    
    @genero.setter
    def genero(self, genero_valido):
        if genero_valido not in ('noticia', 'reportagem', 'entrevista', 'editorial', 'cronica', 'resenha', 'opiniao'):
            raise ValueError("Gênero inválido")
        else:
            self._genero = genero_valido

    @property
    def numero_paginas(self):
        print("Número de páginas")
        return self._numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, numero_paginas_valido):
        if not isinstance(numero_paginas_valido, int):
            raise ValueError("Erro. O número de páginas deve ser um valor inteiro.")
        else:
            self._numero_paginas = numero_paginas_valido

    @property
    def avaliacao(self):
        print("Avaliação da Obra: ")
        return self._avaliacao
    
    @avaliacao.setter
    def avaliacao(self, avaliacao_valido):
        if not avaliacao_valido == None:
            if not isinstance(avaliacao_valido, float) or avaliacao_valido > 10 or avaliacao_valido < 0:
                raise ValueError("Nota inválida! Deve ser entre 0-10!")
            else:
                self._avaliacao = avaliacao_valido 
        else:
            self._avaliacao = "Campo vazio"
