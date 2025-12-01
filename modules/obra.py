class Obra:
    def __init__(self, titulo, ano, autor, tipo, numero_paginas, avaliacao):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.tipo = tipo
        self.numero_paginas = numero_paginas
        self.avaliacao = avaliacao

    @property
    def titulo(self):
        print("Título da obra: ")
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo_valido: str):
        if titulo_valido.strip() == "":
            raise ValueError("Título inválido! O campo não pode ser vazio.")
        else:
            self._titulo = titulo_valido     

    @property
    def ano(self):
        print("Ano de publicação da obra: ")
        return self._ano
    
    @ano.setter
    def ano(self, ano_valido):
        if ano_valido < 1500:
            raise ValueError("Ano inálido! O ano deve ser maior que 1500!")
        else:
            self._ano = ano_valido
    @property
    def autor(self):
        print("Autor da Obra: ")
        return self._autor
    
    @autor.setter
    def autor(self, autor_valido):
        if autor_valido == "":
            raise ValueError("Autor inválido! O campo não pode ser vazio!")
        else: 
            self._autor = autor_valido
        
    @property
    def tipo(self):
        print("Tipo da obra")
        return self._tipo
    
    @tipo.setter 
    def tipo(self, tipo_valido):
        if tipo_valido not in ("livro", "revista"):
            raise ValueError("Tipo inválido! O tipo deve ser livro ou revista!")
        else:
            self._tipo = tipo_valido
        
    @property
    def numero_paginas(self):
        print("Número de páginas")
        return self._numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, numero_paginas_valido):
        if isinstance(numero_paginas_valido, int):
            self._numero_paginas = numero_paginas_valido
        else:
            return("Número de páginas inválido!")

    @property
    def avaliacao(self):
        print("Avaliação da Obra: ")
        return self._avaliacao
    
    @avaliacao.setter
    def avaliacao(self, avaliacao_valido):
        if isinstance(avaliacao_valido, float):
            self._avaliacao = avaliacao_valido
        else:
            return("Avaliação inválida!") 
        
    # Testes: Criação de instâncias de classe

pub = Obra("Dom Casmurro", 1500, "Machado_de_Assis", "livro", 280, 8.9)
print(pub.titulo)
print(pub.ano)
print(pub.autor)
print(pub.tipo)
print(pub.numero_paginas)
print(pub.avaliacao)